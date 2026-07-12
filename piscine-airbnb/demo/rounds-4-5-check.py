#!/usr/bin/env python3
"""Contrat stdlib — Poolbnb rounds 4 (pack découverte) et 5 (parrainage)."""
from __future__ import annotations
import re, subprocess, tempfile
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PAGES={n:(ROOT/n).read_text(encoding="utf-8") for n in ("index.html","member.html","host.html","admin.html")}
KEY="forge:piscine-airbnb:demo:v1"

class Parser(HTMLParser):
    pass

def require(source:str,*needles:str)->None:
    for needle in needles:
        assert needle in source, f"élément absent: {needle}"

def main()->int:
    for name,source in PAGES.items(): Parser().feed(source); require(source,KEY); print("HTML OK",name)
    market=PAGES["index.html"]; member=PAGES["member.html"]; admin=PAGES["admin.html"]
    require(market,"discoveryPack","creditLedger","calculateDiscoveryQuote","subtotal","discountAmount","creditUsed","finalTotal","PoolbnbPricing.quote","PACK_DISCOUNT","PACK_CREDIT_REDEEMED","bookingId","Ventilation avant confirmation")
    require(member,"Solde disponible","Pack découverte","Écritures du ledger","Parrainage","INVITATION_COPIÉE","ÉLIGIBILITÉ_EN_REVUE","CRÉDIT_ACQUIS","REFUS_ANTI_ABUS","EXPIRÉ","simulateEligibleReferral","simulateAntiAbuse","Hypothèse de démonstration : CHF 10","PENDING","AVAILABLE","REFUSED","s.discoveryPack.creditBalance+")
    require(admin,"Réservations et ventilation","Parrainages agrégés","Ledger append-only","KPI synthétiques — démonstration, pas traction","resetDialog","showModal","Baseline exacte restaurée")
    combined="\n".join(PAGES.values())
    require(combined,"REFERRAL_CREDIT_SPONSOR","REFERRAL_CREDIT_GUEST","non remboursable en cash","non transférable","CREDIT_REVERSED","CREDIT_EXPIRED")
    assert "confirm(" not in admin and "window.confirm" not in admin, "reset natif encore présent"
    assert "friendEmail" not in member and "filleulEmail" not in combined, "identité filleul exposée"
    scripts=[]
    for name,source in PAGES.items():
        scripts += [(f"{name}-{i}",body) for i,body in enumerate(re.findall(r"<script(?:\\s[^>]*)?>(.*?)</script>",source,re.S),1) if body.strip()]
    with tempfile.TemporaryDirectory() as tmp:
        for name,body in scripts:
            path=Path(tmp)/(name+".js"); path.write_text(body,encoding="utf-8")
            done=subprocess.run(["node","--check",str(path)],capture_output=True,text=True)
            assert done.returncode==0, done.stderr
    print(f"PASS rounds 4–5: {len(PAGES)} pages, {len(scripts)} scripts")
    return 0
if __name__=="__main__": raise SystemExit(main())
