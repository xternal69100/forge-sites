#!/usr/bin/env python3
"""Contrat stdlib — Poolbnb rounds 6–7, parcours Piscines partenaires."""
from __future__ import annotations
import re, subprocess, tempfile
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NAMES = ("index.html", "account.html", "partners.html", "admin.html")
KEY = "forge:piscine-airbnb:demo:v1"
DISCLOSURE = "Mode démonstration — aucune donnée envoyée, aucun débit réel"
BAD_CTA = (">Acheter<", ">Souscrire maintenant<")
PROHIBITED = ("tarif négocié", "partenaire officiel")

class Parser(HTMLParser):
    pass

def require(source: str, *needles: str) -> None:
    for needle in needles:
        assert needle in source, f"élément absent: {needle}"

def main() -> int:
    pages = {}
    for name in NAMES:
        path = ROOT / name
        assert path.exists(), f"page absente: {name}"
        source = path.read_text(encoding="utf-8")
        Parser().feed(source)
        require(source, KEY, DISCLOSURE)
        pages[name] = source
        print("HTML OK", name)

    for name in ("index.html", "account.html", "admin.html"):
        require(pages[name], 'partners.html')

    market, partner, admin = pages["index.html"], pages["partners.html"], pages["admin.html"]
    require(market, "Piscines partenaires", "Alternative accessible")
    require(partner,
        "Offre illustrative — aucun partenariat conclu", "Simuler cette offre",
        "partnerOffers", "partnerOrders", "calculatePartnerQuote", "referencePrice",
        "scenarioPrice", "unitSaving", "commissionHypothesis", "sourceLabel", "sourceDate",
        "Affiliation", "Apporteur d’affaires", "Revente", "aucune redirection",
        "aucun lead", "Vendeur / modèle hypothétique", "Quantité", "Total CHF",
        "Confirmer la simulation", "aucune commande, aucun paiement, aucun abonnement et aucune transmission au partenaire",
        "PARTNER_ORDER_CREATED", "eventJournal")
    require(admin,
        "Commandes partenaires", "partnerOrders", "partnerOrderSearch", "partnerOrderStatus",
        "SIMULÉE", "ANNULÉE", "KPI synthétiques — démonstration, pas traction",
        "Commandes partenaires simulées", "0 commande partenaire", "PARTNER_ORDER_STATUS_CHANGED")
    require(market, "partnerOffers:partnerOfferSeed()", "partnerOrders:[]")

    combined = "\n".join(pages.values()).lower()
    for phrase in PROHIBITED:
        assert phrase not in combined, f"allégation interdite: {phrase}"
    assert all(x.lower() not in combined for x in BAD_CTA), "CTA transactionnel interdit"
    assert "logo" not in partner.lower(), "logo réel/mention logo dans les offres"
    assert "type=\"card\"" not in partner.lower() and "cvv" not in partner.lower(), "collecte carte interdite"
    assert partner.count("Simuler cette offre") >= 1 and "document.querySelectorAll('.simulate')" in partner, "CTA offre absent"
    assert partner.count("Offre illustrative — aucun partenariat conclu") >= 2, "badge absent par offre"

    # Les anciens parcours doivent rester contractuellement présents.
    all_source = "\n".join(pages.values())
    require(all_source, "discoveryPack", "creditLedger", "referrals", "hostApplications", "bookings")

    scripts = []
    for name, source in pages.items():
        scripts += [(f"{name}-{i}", body) for i, (attrs, body) in enumerate(
            re.findall(r"<script([^>]*)>(.*?)</script>", source, re.S), 1)
            if body.strip() and 'type="application/json"' not in attrs]
    with tempfile.TemporaryDirectory() as tmp:
        for name, body in scripts:
            path = Path(tmp) / f"{name}.js"
            path.write_text(body, encoding="utf-8")
            done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)
            assert done.returncode == 0, done.stderr
    print(f"PASS rounds 6–7: {len(pages)} pages, {len(scripts)} scripts")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
