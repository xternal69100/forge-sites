#!/usr/bin/env python3
"""Validation stdlib du démonstrateur coach public."""
from __future__ import annotations

import re
import subprocess
import tempfile
from html.parser import HTMLParser
from pathlib import Path

DEMO = Path(__file__).resolve().parent
SITE = DEMO.parent
HTMLS = [SITE / "index.html", DEMO / "index.html", DEMO / "admin.html", SITE / "demo.html", DEMO / "transaction.html"]
PROMOTED = [SITE / "index.html", DEMO / "index.html", DEMO / "admin.html"]
STORE_KEY = "forge:coach-office:demo:v2"
DOMAINS = ["agenda", "inbox", "crm", "prospects", "marketing", "invoices", "accounting", "reporting"]


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.inline_scripts: list[str] = []
        self._script: list[str] | None = None
        self.ids: set[str] = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        if tag == "script" and not values.get("src") and values.get("type", "") != "application/json":
            self._script = []

    def handle_data(self, data):
        if self._script is not None:
            self._script.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self._script is not None:
            self.inline_scripts.append("".join(self._script))
            self._script = None


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def node_check(label: str, source: str) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8") as handle:
        handle.write(source)
        handle.flush()
        result = subprocess.run(["node", "--check", handle.name], text=True, capture_output=True)
    check(result.returncode == 0, f"{label}: {result.stderr.strip()}")


def main() -> None:
    for path in HTMLS:
        check(path.is_file(), f"surface absente: {path}")
        text = path.read_text(encoding="utf-8")
        parser = Parser()
        parser.feed(text)
        parser.close()
        check('lang="fr"' in text, f"lang fr absente: {path.name}")
        check('name="viewport"' in text, f"viewport absent: {path.name}")
        for index, script in enumerate(parser.inline_scripts, 1):
            node_check(f"{path.name} inline #{index}", script)

    app = (DEMO / "app.js").read_text(encoding="utf-8")
    node_check("app.js", app)
    combined = "\n".join(path.read_text(encoding="utf-8") for path in PROMOTED)
    all_public = combined + "\n" + app

    check(STORE_KEY in app, "clé store v2 absente")
    check("version:2" in app and "emptyStore" in app and "resetStore" in app, "contrat store/reset incomplet")
    check(all(domain in app for domain in DOMAINS), "un domaine de couverture manque")
    check("appointments.length!==2" in app, "contrainte exacte des 2 rendez-vous absente")
    check("DOMAIN_IDS.some" in app, "activation complète des domaines non contrôlée")
    check(".test" in all_public and "isTestEmail" in app, "frontière .test absente")
    check("realCharge:false" in app, "absence de débit non encodée")
    check("Valider" in combined and "Modifier" in combined and "Refuser" in combined, "actions d’approbation absentes")
    check(all(command in combined for command in ["/aujourdhui", "/clients", "/factures", "/contenu", "/priorites"]), "commandes Telegram incomplètes")

    forbidden_network = [r"\bfetch\s*\(", r"XMLHttpRequest", r"new\s+WebSocket", r"navigator\.sendBeacon", r"https?://(?!www\.w3\.org/2000/svg)"]
    for pattern in forbidden_network:
        check(not re.search(pattern, all_public, re.I), f"appel réseau ou URL externe interdit: {pattern}")

    for pattern in [r"3[’'\s]?700", r"3700"]:
        check(not re.search(pattern, combined, re.I), "ancienne mention tarifaire détectée")
    for health_term in [r"blessure", r"diagnostic", r"pathologie", r"poids\s*:", r"fréquence cardiaque"]:
        check(not re.search(health_term, app, re.I), f"donnée de santé détectée: {health_term}")

    fixture_emails = re.findall(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+", app, re.I)
    check(fixture_emails and all(email.lower().endswith(".test") for email in fixture_emails), "une fixture email ne se termine pas par .test")
    landing = (SITE / "index.html").read_text(encoding="utf-8")
    client = (DEMO / "index.html").read_text(encoding="utf-8")
    admin = (DEMO / "admin.html").read_text(encoding="utf-8")
    check('href="demo/"' in landing, "landing non reliée au parcours client")
    check("demo.html" not in landing and "demo.html" not in client, "console interne promue côté client")
    check('href="../demo.html"' in admin, "console interne non accessible depuis admin")
    check("tarif standard" in landing.lower() and "prix fondateur" in landing.lower(), "distinction tarif fondateur/standard absente")
    check((DEMO / "README.md").is_file(), "README démo absent")

    print(f"VALIDATION_COACH_V2_OK html={len(HTMLS)} inline_js=checked store={STORE_KEY} fixtures={len(fixture_emails)}")


if __name__ == "__main__":
    main()
