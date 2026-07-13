#!/usr/bin/env python3
"""Contrat TDD stdlib : compte unifié, onboarding guidé et identité légale fictive."""
from __future__ import annotations
import re, subprocess, tempfile
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT.parent
KEY = "forge:piscine-airbnb:demo:v1"
LEGAL_ID = "Poolbnb Démo SA — société fictive, non constituée et non inscrite au registre du commerce"
PAGES = {
    "landing": SITE / "index.html", "market": ROOT / "index.html", "account": ROOT / "account.html",
    "member": ROOT / "member.html", "host": ROOT / "host.html", "admin": ROOT / "admin.html",
    "partners": ROOT / "partners.html", "guides": ROOT / "guides.html",
    "memberGuide": ROOT / "guide-membre.html", "hostGuide": ROOT / "guide-loueur.html", "legal": ROOT / "legal.html",
}

class Parser(HTMLParser): pass

def require(text: str, *needles: str) -> None:
    for needle in needles: assert needle in text, f"élément absent: {needle}"

def main() -> int:
    pages = {}
    for name, path in PAGES.items():
        assert path.exists(), f"page absente: {path.name}"
        text = path.read_text(encoding="utf-8"); Parser().feed(text); pages[name] = text
        print("HTML OK", name)
    demos = [pages[x] for x in ("market","account","admin","partners","guides","memberGuide","hostGuide","legal")]
    assert all(KEY in p for p in (pages["market"], pages["account"], pages["admin"])), "store canonique absent"
    require(pages["account"], "Créer mon profil membre", "Lire le guide essentiel", "checklist membre obligatoire",
            "acceptanceVersion", "member-guide-essential-v1", "PROFILE_ACTIVATED", "Devenir loueur",
            "checklist loueur obligatoire", "host-guide-essential-v1", "HOST_ROLE_REQUESTED",
            "hostRoleRequest", "disabled", "@example.test")
    require(pages["admin"], "Demandes de rôle loueur", "hostRoleRequest", "HOST_ROLE_REQUESTED")
    for name in ("market","account","partners"):
        nav = re.search(r"<nav.*?</nav>", pages[name], re.S)
        assert nav, f"navigation absente: {name}"
        assert nav.group(0).count('href="guides.html"') == 1, f"entrée Guides non unique: {name}"
        assert "guide-membre.html" not in nav.group(0) and "guide-loueur.html" not in nav.group(0), f"guides séparés dans nav: {name}"
        assert 'href="account.html"' in nav.group(0), f"compte canonique absent: {name}"
    require(pages["guides"], "Guides Poolbnb", "Parcours membre", "Parcours loueur", "guide-membre.html", "guide-loueur.html")
    for compat in ("member","host"):
        require(pages[compat], "account.html", "location.replace")
    for name, page in pages.items():
        require(page, LEGAL_ID, 'legal.html', "legal@poolbnb.example.test")
    require(pages["legal"], "Adresse de démonstration — non réelle", "RC : NON CONSTITUÉ — PLACEHOLDER NON VALABLE",
            "IDE : CHE-XXX.XXX.XXX — PLACEHOLDER NON VALABLE", 'id="cgu"', 'id="confidentialite"', "Statut démo")
    combined = "\n".join(pages.values())
    assert not re.search(r"CHE-\d{3}\.\d{3}\.\d{3}", combined), "IDE apparemment valable interdit"
    assert "capital-actions" not in combined.casefold() and "capital social" not in combined.casefold(), "capital inventé"
    assert "type=\"file\"" not in pages["account"].casefold(), "upload interdit"
    scripts=[]
    for name, source in pages.items():
        for i,(attrs,body) in enumerate(re.findall(r"<script([^>]*)>(.*?)</script>",source,re.S),1):
            if body.strip() and 'type="application/json"' not in attrs:
                scripts.append((f"{name}-{i}",body))
    with tempfile.TemporaryDirectory() as tmp:
        for name,body in scripts:
            path=Path(tmp)/(name+".js"); path.write_text(body,encoding="utf-8")
            done=subprocess.run(["node","--check",str(path)],capture_output=True,text=True)
            assert done.returncode==0, done.stderr
    print(f"PASS compte unifié: {len(PAGES)} pages, onboarding/checklists, demande loueur, footer légal")
    return 0
if __name__ == "__main__": raise SystemExit(main())
