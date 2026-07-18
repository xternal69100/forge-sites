#!/usr/bin/env python3
"""Validateur fail-closed de la copie publique locale après rappel qualité."""
from __future__ import annotations

import json
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
STORE_KEY = "forge:studio-typographique:demo:v1"
REQUIRED = {
    "index.html", "demo/index.html", "demo/admin.html", "demo/store.js",
    "demo/customer.js", "demo/admin.js", "demo/verify_store.js", "assets/site.css",
    "assets/catalog.js", "DESIGN.md", "tokens.json", "tailwind.theme.json",
}
RECALLED_ARTIFACTS = {
    "downloads/Elanovre-Open-Edition-v1.000.zip",
    "downloads/KeraVolt-Optical-Open-Edition-v1.100.zip",
    "assets/fonts/Elanovre-Regular.woff2",
    "assets/fonts/KeraVoltOptical-Regular.woff2",
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


def validate_boundary() -> int:
    files = [path for path in ROOT.rglob("*") if path.is_file()]
    banned_suffixes = {".png", ".pyc", ".log", ".zip", ".woff", ".woff2", ".ttf", ".otf"}
    for path in files:
        check(path.suffix.lower() not in banned_suffixes, f"binaire rappelé ou format privé dans site: {path.relative_to(ROOT)}")
    for rel in RECALLED_ARTIFACTS:
        check(not (ROOT / rel).exists(), f"artefact rappelé encore présent: {rel}")
    return len(files)


def validate_copy() -> None:
    landing = (ROOT / "index.html").read_text(encoding="utf-8")
    demo = (ROOT / "demo/index.html").read_text(encoding="utf-8")
    admin = (ROOT / "demo/admin.html").read_text(encoding="utf-8")
    store = (ROOT / "demo/store.js").read_text(encoding="utf-8")
    css = (ROOT / "assets/site.css").read_text(encoding="utf-8")
    for needle in ("studio-quality-recall-20260718", "Catalogue momentanément vide", "7 éditions retirées", "0 famille disponible", "aucun binaire distribué"):
        check(needle.lower() in landing.lower(), f"mention de rappel absente: {needle}")
    for needle in ("Mode démonstration — aucun débit réel", "aucune carte", "aucune distribution", "Inventaire vide"):
        check(needle.lower() in demo.lower(), f"mention démo absente: {needle}")
    check("aucune transmission" in admin.lower(), "divulgation admin absente")
    check(STORE_KEY in store, "clé de store exacte absente")
    check("const FAMILIES = [];" in store and "const PACKS = {};" in store, "allowlist ou paquets non vides")
    check("@font-face" not in css and "fonts/" not in css, "police rappelée encore chargée par le CSS")
    check("stripe" not in (demo + store).lower() and "paypal" not in (demo + store).lower(), "provider de paiement détecté")
    exposed = landing + demo + admin + store
    for family in ("Elanovre", "KeraVolt Optical", "Cervalune", "Modulune System", "Brisacline Display", "Hexavox Mono V2", "Riftora Experimental"):
        check(family not in exposed, f"famille rappelée encore exposée: {family}")


def run_commands() -> list[str]:
    commands = [
        ["node", "--check", "assets/catalog.js"],
        ["node", "--check", "demo/store.js"],
        ["node", "--check", "demo/customer.js"],
        ["node", "--check", "demo/admin.js"],
        ["node", "demo/verify_store.js"],
        [sys.executable, "../bin/check_editorial_publication.py"],
    ]
    outputs = []
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        check(result.returncode == 0, f"commande échouée: {' '.join(command)}\n{result.stderr}")
        if result.stdout.strip():
            outputs.append(result.stdout.strip())
    return outputs


def main() -> int:
    missing = sorted(REQUIRED - {str(path.relative_to(ROOT)) for path in ROOT.rglob("*") if path.is_file()})
    check(not missing, f"fichiers requis absents: {missing}")
    pages, refs = validate_html()
    file_count = validate_boundary()
    validate_copy()
    outputs = run_commands()
    json.loads((ROOT / "tokens.json").read_text(encoding="utf-8"))
    json.loads((ROOT / "tailwind.theme.json").read_text(encoding="utf-8"))
    print(f"PUBLIC SITE PASS — {pages} pages HTML, {refs} liens locaux, {file_count} fichiers publics, 0 binaire distribué.")
    for output in outputs:
        print(output)
    print("BASELINE PASS — catalogue, allowlist, paquets et store vides.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, OSError, ValueError) as exc:
        print(f"PUBLIC SITE FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
