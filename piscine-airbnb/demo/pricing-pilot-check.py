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
    "member": DEMO / "member.html",
    "host": DEMO / "host.html",
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
    require(landing, "price-total", "total groupe", "frais obligatoires inclus", "soit CHF", HYPOTHESIS)
    require(market, "price-total", "Prix hôte", "Frais invité inclus", "Total avant promo", "Extension 1 h", HYPOTHESIS)
    require(member, "Prix hôte", "Frais invité inclus", "Total avant promo", "Revenu hôte")
    require(admin, "Prix hôte", "Frais invité inclus", "Total avant promo", "Revenu hôte")
    require(landing, 'value="75"', 'value="100"', 'value="150"')
    require(market, 'data-total="75"', 'data-total="100"', 'data-total="150"')

    combined_pricing = "\n".join((landing, market, member, admin))
    for amount in OLD_TOTALS:
        assert not re.search(rf"(?<![\d.])(?:CHF\s*)?{amount}(?:\.00)?(?![\d.])", combined_pricing), f"ancien montant public présent: {amount}"
    for amount in OLD_FILTERS:
        assert f'value="{amount}"' not in combined_pricing, f"ancien filtre présent: {amount}"
    for phrase in ("CHF / 4h", "/ 4 h", "base 4h", "créneau de 4 h", "Math.round(base * 0.08)", "chosen.price*1.08"):
        assert phrase not in combined_pricing, f"ancien pricing présent: {phrase}"

    landing_data = pricing_data(landing)
    market_data = pricing_data(market)
    assert landing_data == market_data, "catalogues pricing landing/démo divergents"
    offers = landing_data["offers"]
    assert len(offers) == 12, "12 offres attendues"
    assert any(o["guestTotal2h"] == 69 and o["includedGuests"] == 4 and o["bookable"] for o in offers), "offre CHF 69 réservable absente"
    assert sum(o["guestTotal2h"] < 150 for o in offers) >= 9, "la majorité des offres standard doit être sous CHF 150/2 h"
    premium = [o for o in offers if o["level"] == "Exception"]
    assert 1 <= len(premium) <= 2 and all(o.get("premiumReason") for o in premium), "premium rare et justifié attendu"
    assert all(o["durationHours"] == 2 for o in offers), "durée carte par défaut différente de 2 h"
    assert all(abs(o["perPersonAt4"] - round(o["guestTotal2h"] / 4, 2)) < 0.001 for o in offers), "ventilation /personne incorrecte"

    assert ENGINE.exists(), "pricing-engine.js absent"
    node_test = r"""
const assert = require('node:assert/strict');
const p = require(process.argv[1]);
assert.equal(p.guestFee(63), 6);
assert.equal(p.guestFee(92), 7.36);
assert.equal(p.guestFee(300), 18);
assert.deepEqual(p.quote({hostBase:63, extensionHourly:25, extraGuest:8, partySize:4, extensionHours:0, weekend:false, promo:false}), {hostPrice:63, guestFee:6, guestTotalBeforePromo:69, discountAmount:0, creditUsed:0, finalTotal:69, hostPayout:56.7});
assert.deepEqual(p.quote({hostBase:92, extensionHourly:32, extraGuest:10, partySize:4, extensionHours:0, weekend:false, promo:true}), {hostPrice:92, guestFee:7.36, guestTotalBeforePromo:99.36, discountAmount:19.87, creditUsed:20, finalTotal:59.49, hostPayout:82.8});
assert.equal(p.quote({hostBase:63, extensionHourly:25, extraGuest:8, partySize:6, extensionHours:1, weekend:true, promo:false}).hostPrice, 119.6);
assert.equal(p.quote({hostBase:63, extensionHourly:25, extraGuest:8, partySize:6, extensionHours:1, weekend:true, promo:false}).guestTotalBeforePromo, 129.17);
assert.equal(p.quote({hostBase:92, extensionHourly:32, extraGuest:10, partySize:4, extensionHours:0, weekend:false, promo:false}).finalTotal, 99.36);
console.log('ENGINE OK fee=min6/max18; groupes 2/4/6/8; extension; week-end +15%; pack; second booking; payout');
"""
    done = subprocess.run(["node", "-e", node_test, str(ENGINE)], text=True, capture_output=True, check=False)
    assert done.returncode == 0, done.stderr
    print(done.stdout.strip())

    require(market, "guestFee", "extensionHours", "weekend", "partySize", "discountAmount", "creditUsed", "hostPayout")
    require(market, "partnerOrders", "hostApplications", "referrals", "creditLedger")
    require(market, "BKG-DEMO-260711-001", "hostPrice", "guestFee", "guestTotalBeforePromo", "hostPayout")
    require(admin, "Baseline exacte restaurée", "3 réservations", "0 commande partenaire")
    assert STORE_KEY in "\n".join(sources.values())
    assert "surge" not in combined_pricing.lower(), "surge interdit"
    print("PASS pricing pilot: CHF69 réservable, 12 offres 2h, frais, groupes/durée/week-end, pack, payout, historique et baseline")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
