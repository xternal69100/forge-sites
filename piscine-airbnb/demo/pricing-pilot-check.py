#!/usr/bin/env python3
"""Contrat TDD du pricing pilote Poolbnb, sans dépendance Python tierce."""
from __future__ import annotations

import json
import re
import subprocess
from html.parser import HTMLParser
from pathlib import Path

DEMO = Path(__file__).resolve().parent
SITE = DEMO.parent
ENGINE = DEMO / "pricing-engine.js"
PAGES = {
    "landing": SITE / "index.html",
    "market": DEMO / "index.html",
    "member": DEMO / "account.html",
    "host": DEMO / "account.html",
    "admin": DEMO / "admin.html",
    "partners": DEMO / "partners.html",
}
OLD_TOTALS = (160, 175, 185, 190, 210, 230, 245, 265, 280, 320, 340, 355)
OLD_FILTERS = (180, 260, 350)
STORE_KEY = "forge:piscine-airbnb:demo:v1"
HYPOTHESIS = "Hypothèses de démonstration — aucun vrai tarif ni traction"


class Parser(HTMLParser):
    pass


def require(source: str, *needles: str) -> None:
    for needle in needles:
        assert needle in source, f"élément absent: {needle}"


def pricing_data(source: str) -> dict:
    match = re.search(r'<script id="pricing-data" type="application/json">\s*(\{.*?\})\s*</script>', source, re.S)
    assert match, "pricing-data JSON absent"
    return json.loads(match.group(1))


def main() -> int:
    sources = {}
    for name, path in PAGES.items():
        source = path.read_text(encoding="utf-8")
        Parser().feed(source)
        sources[name] = source
        print(f"HTML OK {name}")

    landing, market, member, host, admin = (sources[x] for x in ("landing", "market", "member", "host", "admin"))
    require(landing, "price-total", "total groupe", "commission Poolbnb 25 % incluse", "soit CHF", HYPOTHESIS)
    require(market, "price-total", "Valeur de location G", "commission Poolbnb 25 % incluse", "Net hôte 75 %", "Extension 1 h", HYPOTHESIS)
    require(member, "commission Poolbnb 25 % incluse", "net hôte", "promo", "politique")
    require(admin, "Commission brute", "Net hôte", "Contribution avant coûts", "Politique")
    require(landing, 'value="75"', 'value="100"', 'value="150"')
    require(market, 'data-total="75"', 'data-total="100"', 'data-total="150"')

    # Écarter les dimensions CSS (p. ex. 210px) : ce contrat vise les prix/données visibles.
    def without_styles(text: str) -> str:
        text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.I | re.S)
        return re.sub(r'\sclass="[^"]*"', "", text, flags=re.I)

    combined_pricing = "\n".join(without_styles(x) for x in (landing, market, member, admin))
    for amount in OLD_TOTALS:
        visible_old_price = rf"(?:CHF\s*{amount}(?:\.00)?|(?<![\d.]){amount}(?:\.00)?\s*CHF)"
        legacy_data_price = rf"(?:price|rentalValueG)\s*:\s*{amount}(?![\d.])"
        assert not re.search(visible_old_price, combined_pricing), f"ancien montant public présent: {amount}"
        assert not re.search(legacy_data_price, combined_pricing), f"ancienne fixture tarifaire présente: {amount}"
    for amount in OLD_FILTERS:
        assert f'value="{amount}"' not in combined_pricing, f"ancien filtre présent: {amount}"
    for phrase in ("CHF / 4h", "/ 4 h", "base 4h", "créneau de 4 h", "Math.round(base * 0.08)", "chosen.price*1.08"):
        assert phrase not in combined_pricing, f"ancien pricing présent: {phrase}"

    landing_data = pricing_data(landing)
    market_data = pricing_data(market)
    assert landing_data == market_data, "catalogues pricing landing/démo divergents"
    offers = landing_data["offers"]
    assert len(offers) == 12, "12 offres attendues"
    assert any(o["rentalValueG"] == 69 and o["includedGuests"] == 4 and o["bookable"] for o in offers), "offre CHF 69 réservable absente"
    assert sum(o["rentalValueG"] < 150 for o in offers) >= 9, "la majorité des offres standard doit être sous CHF 150/2 h"
    premium = [o for o in offers if o["level"] == "Exception"]
    assert 1 <= len(premium) <= 2 and all(o.get("premiumReason") for o in premium), "premium rare et justifié attendu"
    assert all(o["durationHours"] == 2 for o in offers), "durée carte par défaut différente de 2 h"
    assert all(abs(o["perPersonAt4"] - round(o["rentalValueG"] / 4, 2)) < 0.001 for o in offers), "ventilation /personne incorrecte"

    assert ENGINE.exists(), "pricing-engine.js absent"
    node_test = r"""
const assert = require('node:assert/strict');
const p = require(process.argv[1]);
assert.equal(p.quote,undefined,'API quote ambiguë interdite');
let minor=p.quote25({rentalValueGMinor:6900,promoEligible:false,promoAvailable:false});
assert.equal(minor.commissionGrossMinor,1725);assert.equal(minor.hostNetMinor,5175);
let q=p.quoteCHF({rentalValueGCHF:69,promo:false});
assert.equal(q.commissionGross,17.25);assert.equal(q.hostNet,51.75);assert.equal(q.finalTotal,69);
q=p.quoteCHF({rentalValueGCHF:99.36,promo:true});
assert.equal(q.commissionGross,24.84);assert.equal(q.hostNet,74.52);assert.equal(q.discountAmount,19.87);assert.equal(q.creditUsed,20);assert.equal(q.finalTotal,59.49);assert.equal(q.contributionBeforeCosts,-15.03);
assert.equal(p.quoteCHF({rentalValueGCHF:129.17,promo:false}).commissionGross,32.29);
assert.equal(p.quoteCHF({rentalValueGCHF:99.36,promo:false}).finalTotal,99.36);
console.log('ENGINE OK commission incluse 25%; groupes/durée/week-end pré-calculés; pack; second booking; net hôte 75%');
"""
    done = subprocess.run(["node", "-e", node_test, str(ENGINE)], text=True, capture_output=True, check=False)
    assert done.returncode == 0, done.stderr
    print(done.stdout.strip())

    require(market, "PoolbnbPricing.quoteCHF", "rentalValueGCHF", "commissionGross", "extensionHours", "weekend", "partySize", "discountAmount", "creditUsed", "hostNet")
    assert "PoolbnbPricing.quote(" not in market, "appel runtime ambigu quote() encore présent"
    require(market, "partnerOrders", "hostApplications", "referrals", "creditLedger")
    require(market, "BKG-DEMO-260711-001", "rentalValueG", "commissionGross", "commissionPolicyVersion", "hostNet")
    require(market, "status:i===2?'CONDITIONNEL':([0,1,3].includes(i)?'VALIDÉ':'BROUILLON')", "published:[0,1,3].includes(i)")
    require(admin, "Baseline exacte restaurée", "3 réservations", "0 commande partenaire")
    assert STORE_KEY in "\n".join(sources.values())
    assert "surgeMultiplier" not in combined_pricing and "surgePrice" not in combined_pricing, "mécanique surge interdite"
    print("PASS pricing pilot: CHF69 réservable, 12 offres 2h, commission 25% incluse, groupes/durée/week-end, pack, net hôte, historique et baseline")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
