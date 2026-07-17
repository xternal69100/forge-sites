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
        "Elanovre-Regular.ttf": "6bdbb174249edec2de480ccda3212cf471518f6b301df70bb1ee883d9ee6133f",
        "Elanovre-Regular.otf": "01433752aaa46806660f35eae4978ee03488c255ba4c96e8dcb103bfb305413d",
        "Elanovre-Regular.woff2": "b61bd6330074f3d25c7d2d47bd9916d44158984d0fc6a2af6862fe2374ca4a08",
    },
    "downloads/KeraVolt-Optical-Open-Edition-v1.100.zip": {
        "KeraVoltOptical-Regular.ttf": "0049c87b5df568a7f3cff992490318e7c3ff9123b4f3ac27c21091a14335e179",
        "KeraVoltOptical-Regular.otf": "683e6a43149bd589f22a316e8c99e5d9c227ecac2d90f4f215ddd1d725c840b2",
        "KeraVoltOptical-Regular.woff2": "b649534a3d04f24918474adda690007c0866a6077864d01a79db6d55153ea162",
    },
    "downloads/Cervalune-Open-Edition-v1.100.zip": {
        "Cervalune-Regular.ttf": "78a82099a858f368c7e071888cb0d49f3fa2c65ed829828b3d8f1094b81de329",
        "Cervalune-Regular.otf": "f096d61201cfff8c12fff706a83446c0b2ed708fe065de1b9e3d2406f0cf4648",
        "Cervalune-Regular.woff2": "2a3e52d7079b61ac5a026c8e699b23a393eaff5ef799a84c7f614e88ae8753bd",
    },
    "downloads/Modulune-System-Open-Edition-v1.000.zip": {
        "ModuluneSystem-Regular.ttf": "034f25671b57781fd0f532f09755747b56a468ffcfb8e2a34a7d74db60adaf07",
        "ModuluneSystem-Regular.otf": "1fa7259eccdfe2cf50879469f3471674409a24536a3b3ec08333470999802f61",
        "ModuluneSystem-Regular.woff2": "9ac1b966a1d427f189b4f36bb86e91bdd01f7ef7c606a008339e593cd08ab062",
    },
    "downloads/Brisacline-Display-Open-Edition-v1.000.zip": {
        "BrisaclineDisplay-Regular.ttf": "754947602c16aad8074bc6a54e6326fa1bde3f3db2da878a94fe48c3f4b83a8f",
        "BrisaclineDisplay-Regular.otf": "e326035050bdc91c62c5d65faec5b2a8038b31da39aa4fc55715e1697d771694",
        "BrisaclineDisplay-Regular.woff2": "c4554a69c265956c74b46b5709839ae22edd5bb30f344295041dac2d002c5c57",
    },
    "downloads/Hexavox-Mono-V2-Open-Edition-v1.100.zip": {
        "HexavoxMonoV2-Regular.ttf": "e1aa07fa6ca978de2e0bd250f20141855867ca25523bc4ba67b704b451fd2435",
        "HexavoxMonoV2-Regular.otf": "2bb76cdd39e12197101d45eb261549d9eaac64a11bd35a69e7ab97bed0dd7bc5",
        "HexavoxMonoV2-Regular.woff2": "fff90089b306175cec79e49e575bf72683d6c3d0db42ee72a2232e0c6ba268d7",
    },
    "downloads/Riftora-Experimental-Open-Edition-v1.000.zip": {
        "RiftoraExperimental-Regular.ttf": "402a62beccfc338146ceff0173ef6ea82e15b25e00bcc968a4339ea76952125a",
        "RiftoraExperimental-Regular.otf": "424362ebf6f7d087c22fd11b4ee763a5248c5bbccad26ebe507369abbad03d91",
        "RiftoraExperimental-Regular.woff2": "c2db2c5169ef6f03203c2d3a527bc0e1513bd462e2240c2f14cf49fd9a75c81b",
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
    css = (ROOT / "assets/site.css").read_text(encoding="utf-8").replace(" ", "")
    for needle in ("Elanovre", "KeraVolt Optical", "Cervalune", "Modulune System", "Brisacline Display", "Hexavox Mono V2", "Riftora Experimental", "studio-open-5-20260717", "7 Open Editions publiques", "SIL Open Font License 1.1", "CHF 0", "aucun Reserved Font Name"):
        check(needle in landing, f"mention catalogue absente: {needle}")
    for needle in ("Mode démonstration — aucun débit réel", "aucune carte", "CHF 0"):
        check(needle.lower() in demo.lower(), f"mention démo absente: {needle}")
    check("aucune transmission" in admin.lower(), "divulgation admin absente")
    check(STORE_KEY in store, "clé de store exacte absente")
    check("orders: []" in store, "baseline vide absente")
    check("stripe" not in (demo + store).lower() and "paypal" not in (demo + store).lower(), "provider de paiement détecté")
    check(COPYRIGHT in landing, "notice copyright absente du catalogue")
    check("[hidden]{display:none!important}" in css, "le CSS doit préserver l’attribut hidden des filtres")
    for family, font_file in (("Cervalune", "Cervalune-Regular.woff2"), ("Modulune System", "ModuluneSystem-Regular.woff2"), ("Brisacline Display", "BrisaclineDisplay-Regular.woff2"), ("Hexavox Mono V2", "HexavoxMonoV2-Regular.woff2"), ("Riftora Experimental", "RiftoraExperimental-Regular.woff2")):
        css_family = family.replace(" ", "")
        check(f"font-family:{css_family}" in css or f"font-family:'{css_family}'" in css, f"{family} doit être réellement déclarée dans le CSS")
        check(f"fonts/{font_file}" in css, f"WOFF2 absent du CSS: {font_file}")
        check(family in store, f"famille absente du store: {family}")
    for archive in ("Cervalune-Open-Edition-v1.100.zip", "Modulune-System-Open-Edition-v1.000.zip", "Brisacline-Display-Open-Edition-v1.000.zip", "Hexavox-Mono-V2-Open-Edition-v1.100.zip", "Riftora-Experimental-Open-Edition-v1.000.zip"):
        check(archive in store, f"paquet absent du store: {archive}")


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
    print(f"PACKAGES PASS — {len(EXPECTED)} ZIP, {binaries} binaires hashés, contenu exact 5/5, OFL 1.1 sans RFN déclaré.")
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
