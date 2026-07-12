#!/usr/bin/env python3
"""Contrat TDD assurance/disclaimers Poolbnb — surfaces et gate synthétique."""
from __future__ import annotations

import re
import subprocess
import tempfile
from html.parser import HTMLParser
from pathlib import Path

DEMO = Path(__file__).resolve().parent
SITE = DEMO.parent
PAGES = {
    "landing": SITE / "index.html",
    "market": DEMO / "index.html",
    "host": DEMO / "host.html",
    "member": DEMO / "member.html",
    "admin": DEMO / "admin.html",
}
KEY = "forge:piscine-airbnb:demo:v1"
DEMO_BANNER = "Mode démonstration — aucune donnée envoyée, aucun débit réel"
CURRENT_INSURANCE = "Aucune assurance Poolbnb par réservation n’est promise à ce stade."
SIMULATE_BUTTON = "Simuler le checkout — aucun débit"
FORBIDDEN_CLAIMS = (
    "assuré par Poolbnb", "assurance incluse", "AirCover des piscines",
    "tout accident est couvert", "tout dommage est couvert", "indemnisation garantie",
    "100 % sûr", "zéro risque", "la protection remplace votre assurance",
    "le dépôt couvre les dommages", "la franchise sera débitée automatiquement",
)


class Parser(HTMLParser):
    pass


def require(source: str, *needles: str) -> None:
    for needle in needles:
        assert needle in source, f"élément absent: {needle}"


def main() -> int:
    pages: dict[str, str] = {}
    for name, path in PAGES.items():
        source = path.read_text(encoding="utf-8")
        Parser().feed(source)
        pages[name] = source
        print(f"HTML OK {name}")

    landing, market, host, member, admin = (pages[x] for x in ("landing", "market", "host", "member", "admin"))
    demos = (market, host, member, admin)
    assert all(KEY in page for page in demos), "store canonique absent"
    assert all(DEMO_BANNER in page for page in demos), "bandeau démo absent"

    require(landing,
        "Réservez l’usage d’une piscine privée proposée par un hôte.",
        "Démonstration uniquement : aucune annonce réelle, aucun paiement, aucune réservation commerciale et aucune assurance Poolbnb par réservation ne sont actifs.",
        CURRENT_INSURANCE, "observation non certifiante", "Informations de démonstration",
        "Poolbnb fournit un service d’intermédiation et de réservation entre hôtes et invités.")
    require(market,
        "Exemple de démonstration — aucun Site réel validé", "Annonce fictive",
        "Aucun hébergement, aucune surveillance de baignade", CURRENT_INSURANCE,
        "Avant de confirmer", SIMULATE_BUTTON, "acceptSafety", "acceptTerms")
    require(host,
        "Acceptations hôte séparées", "acceptRight", "acceptAuthority", "acceptInsurance",
        "acceptEvidence", "acceptVisit", "acceptChanges", "acceptCharter",
        "NO_POOLBNB_BOOKING_PROTECTION", "observation non certifiante",
        "assuranceValidTo", "authorityValidTo", "Aucun document, aucune adresse exacte et aucun identifiant sensible réel")
    require(member,
        "Votre rôle :", "Votre éventuelle déclaration de RC privée ne garantit pas",
        "144/112", "Décrivez les faits observés sans attribuer de faute ni poser de diagnostic",
        "Aucune donnée sensible")
    require(admin,
        "Matrice synthétique des pièces et expirations", "Couche hôte primaire", "Couche Poolbnb corporate",
        "Protection secondaire par réservation", "À VALIDER", "NON SOUSCRITE",
        "insuranceGate", "blockingGateFailures", "GO_CONDITIONNEL", "SIGNATURE_AUTORISÉE",
        "CONDITIONNEL reste non publiable", "journal append-only")

    combined = "\n".join(pages.values())
    lowered = combined.casefold()
    for claim in FORBIDDEN_CLAIMS:
        assert claim.casefold() not in lowered, f"claim interdit: {claim}"
    assert not re.search(r"Poolbnb[^\n<]{0,80}(?:CHF\s*\d[\d’'.,]*|prime\s*(?:de|:)|plafond\s*(?:de|:))", combined, re.I), "plafond/prime Poolbnb inventé"
    assert "type=\"file\"" not in host and "type='file'" not in host, "upload réel interdit"
    assert "type=\"card\"" not in market and "cvv" not in market.casefold(), "paiement réel interdit"

    require(landing, 'href="demo/"')
    require(market, 'href="host.html"', 'href="member.html"', 'href="admin.html"')
    require(host, 'href="admin.html"', 'href="member.html"')
    require(member, 'href="host.html"', 'href="admin.html"')
    require(admin, 'href="index.html"', 'href="host.html"', 'href="member.html"')

    scripts: list[tuple[str, str]] = []
    for name, source in pages.items():
        for number, (attrs, body) in enumerate(re.findall(r"<script([^>]*)>(.*?)</script>", source, re.S), 1):
            if body.strip() and 'type="application/json"' not in attrs:
                scripts.append((f"{name}-{number}", body))
    with tempfile.TemporaryDirectory() as tmp:
        for name, body in scripts:
            path = Path(tmp) / f"{name}.js"
            path.write_text(body, encoding="utf-8")
            done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)
            assert done.returncode == 0, done.stderr
    print(f"PASS assurance integration: {len(PAGES)} surfaces, {len(scripts)} scripts, claims, gates, checkout et liens")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
