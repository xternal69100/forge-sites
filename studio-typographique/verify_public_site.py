#!/usr/bin/env python3
"""Validateur public, sans dépendance tierce, pour Forge Open Editions."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
COPYRIGHT = "Copyright 2026 The Studio Typographique Forge Project Authors"
STORE_KEY = "forge:studio-typographique:demo:v1"
EXPECTED = {
    "downloads/Elanovre-Open-Edition-v1.000.zip": {
        "Elanovre-Regular.ttf": "c0594a4610c495599a9f5ec4521a64d456e82c6dc5e397c32280032f986896a4",
        "Elanovre-Regular.otf": "f6fa27675792fae738777654fcf109b530946d0bee8d88f0c9ae73e60617d18f",
        "Elanovre-Regular.woff2": "49d49a4dc393f2457ec342a9396091e5913068886017a3a91b0dbd4ad0235f05",
    },
    "downloads/KeraVolt-Optical-Open-Edition-v1.100.zip": {
        "KeraVoltOptical-Regular.ttf": "fa98aa04c353af85bb2addcbd446ae6ecdcdd5d9b278af8ded971ef4b4f6da08",
        "KeraVoltOptical-Regular.otf": "f73628141da8733c4b54b20bc22c758378ef52abacbbff48a88421f6f3b3ddac",
        "KeraVoltOptical-Regular.woff2": "f3b3252b0662e20abfb4c0733584e88ece6ab27fe109fc2472bbe5f7bf1aa4fc",
    },
}
REQUIRED = {
    "index.html", "demo/index.html", "demo/admin.html", "demo/store.js",
    "demo/customer.js", "demo/admin.js", "demo/verify_store.js", "assets/site.css",
    "assets/catalog.js", "DESIGN.md", "tokens.json", "tailwind.theme.json",
}

class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.refs: list[str] = []
        self.text: list[str] = []
        self._hidden_depth = 0
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag in {"script", "style"}:
            self._hidden_depth += 1
        for key in ("href", "src"):
            value = values.get(key)
            if value:
                self.refs.append(value)
    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self._hidden_depth:
            self._hidden_depth -= 1
    def handle_data(self, data: str) -> None:
        if not self._hidden_depth:
            self.text.append(data)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_html() -> tuple[int, int]:
    pages = sorted(ROOT.rglob("*.html"))
    check(len(pages) == 3, f"3 pages HTML attendues, trouvé {len(pages)}")
    refs_checked = 0
    forbidden = ("todo", "à faire", "bug", "équipe interne", "non branché", "reste à")
    for page in pages:
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        parser.close()
        visible = " ".join(parser.text).lower()
        for term in forbidden:
            check(term not in visible, f"vocabulaire interdit visible dans {page.relative_to(ROOT)}: {term}")
        for ref in parser.refs:
            parsed = urlsplit(ref)
            if parsed.scheme or parsed.netloc or not parsed.path or ref.startswith(("#", "data:")):
                continue
            target = (page.parent / unquote(parsed.path)).resolve()
            check(ROOT == target or ROOT in target.parents, f"lien hors site: {ref}")
            check(target.exists(), f"lien local brisé dans {page.relative_to(ROOT)}: {ref}")
            refs_checked += 1
    return len(pages), refs_checked


def validate_public_boundary() -> int:
    files = [p for p in ROOT.rglob("*") if p.is_file()]
    banned_suffixes = {".png", ".pyc", ".log"}
    banned_names = {"provenance.json", "sbom.spdx.json", "manifest.sha256", "fiche.md", "qa-visuelle.md"}
    for path in files:
        lower = path.name.lower()
        check(path.suffix.lower() not in banned_suffixes, f"format privé/interdit dans site: {path.relative_to(ROOT)}")
        check(lower not in banned_names, f"métadonnée interne dans site: {path.relative_to(ROOT)}")
        check("generate_font" not in lower and "specimen-private" not in lower and "prepublication" not in lower, f"artefact privé dans site: {path.relative_to(ROOT)}")
    return len(files)


def validate_copy() -> None:
    landing = (ROOT / "index.html").read_text(encoding="utf-8")
    demo = (ROOT / "demo/index.html").read_text(encoding="utf-8")
    admin = (ROOT / "demo/admin.html").read_text(encoding="utf-8")
    store = (ROOT / "demo/store.js").read_text(encoding="utf-8")
    for needle in ("Elanovre", "KeraVolt Optical", "SIL Open Font License 1.1", "CHF 0", "aucun Reserved Font Name"):
        check(needle in landing, f"mention catalogue absente: {needle}")
    for needle in ("Mode démonstration — aucun débit réel", "aucune carte", "CHF 0"):
        check(needle.lower() in demo.lower(), f"mention démo absente: {needle}")
    check("aucune transmission" in admin.lower(), "divulgation admin absente")
    check(STORE_KEY in store, "clé de store exacte absente")
    check("orders: []" in store, "baseline vide absente")
    check("stripe" not in (demo + store).lower() and "paypal" not in (demo + store).lower(), "provider de paiement détecté")
    check(COPYRIGHT in landing, "notice copyright absente du catalogue")


def validate_zips() -> int:
    verified = 0
    for rel, fonts in EXPECTED.items():
        path = ROOT / rel
        check(path.exists(), f"ZIP absent: {rel}")
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
            expected_names = set(fonts) | {"OFL.txt", "README-FR.md"}
            check(names == expected_names, f"contenu ZIP inattendu {rel}: {sorted(names)}")
            check(archive.testzip() is None, f"entrée ZIP corrompue: {rel}")
            for name, digest in fonts.items():
                check(sha(archive.read(name)) == digest, f"hash binaire incorrect: {rel}/{name}")
                verified += 1
            ofl = archive.read("OFL.txt").decode("utf-8")
            header = ofl.split("-----------------------------------------------------------", 1)[0]
            check(ofl.startswith(COPYRIGHT + "\n\n"), f"notice OFL incorrecte: {rel}")
            check("SIL OPEN FONT LICENSE Version 1.1" in ofl, f"texte OFL 1.1 absent: {rel}")
            check("with Reserved Font Name" not in header, f"Reserved Font Name déclaré: {rel}")
            readme = archive.read("README-FR.md").decode("utf-8")
            for phrase in ("label d’édition", "clearance de marque", "titularité vérifiée", "licence de ce paquet porte sur les fichiers"):
                check(phrase in readme, f"réserve absente de {rel}: {phrase}")
    return verified


def run_commands() -> list[str]:
    commands = [
        ["node", "--check", "assets/catalog.js"],
        ["node", "--check", "demo/store.js"],
        ["node", "--check", "demo/customer.js"],
        ["node", "--check", "demo/admin.js"],
        ["node", "demo/verify_store.js"],
    ]
    outputs = []
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        check(result.returncode == 0, f"commande échouée: {' '.join(command)}\n{result.stderr}")
        if result.stdout.strip():
            outputs.append(result.stdout.strip())
    return outputs


def main() -> int:
    missing = sorted(REQUIRED - {str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file()})
    check(not missing, f"fichiers requis absents: {missing}")
    pages, refs = validate_html()
    file_count = validate_public_boundary()
    validate_copy()
    binaries = validate_zips()
    outputs = run_commands()
    json.loads((ROOT / "tokens.json").read_text(encoding="utf-8"))
    json.loads((ROOT / "tailwind.theme.json").read_text(encoding="utf-8"))
    print(f"PUBLIC SITE PASS — {pages} pages HTML, {refs} liens locaux, {file_count} fichiers publics.")
    print(f"PACKAGES PASS — 2 ZIP, {binaries} binaires hashés, contenu exact 5/5, OFL 1.1 sans RFN déclaré.")
    for output in outputs:
        print(output)
    print("BASELINE PASS — store version 1 laissé vide par le harness.")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"PUBLIC SITE FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
