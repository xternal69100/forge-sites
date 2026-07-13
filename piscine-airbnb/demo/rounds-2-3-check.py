#!/usr/bin/env python3
"""Validateur stdlib zéro dépendance — Poolbnb démo rounds 2 et 3."""
from __future__ import annotations
import re, subprocess, tempfile
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SITE=ROOT.parent
PAGES={name:ROOT/name for name in ("index.html","account.html","member.html","host.html","admin.html")}
KEY="forge:piscine-airbnb:demo:v1"
DISCLOSURE="Mode démonstration — aucune donnée envoyée, aucun débit réel"
STATES=("BROUILLON","DOSSIER_COMPLET","VISITE_PLANIFIÉE","VALIDÉ","CONDITIONNEL","REFUSÉ")
FORBIDDEN_INPUTS=("type=\"file\"","type='file'","passport","numéro de police","carte d’identité")

class Parser(HTMLParser):
    def error(self, message: str) -> None: raise AssertionError(message)

def require(source:str,*needles:str)->None:
    for needle in needles: assert needle in source, f"élément absent: {needle}"

def main()->int:
    sources={}
    for name,path in PAGES.items():
        assert path.exists(), f"page absente: {name}"
        source=path.read_text(encoding="utf-8"); Parser().feed(source); sources[name]=source
        print(f"HTML OK {name}")
    combined="\n".join(sources.values())
    for name in ("index.html","account.html","admin.html"): require(sources[name],KEY,DISCLOSURE)
    require(sources["index.html"],"Devenir loueur","account.html","admin.html")
    require(sources["account.html"],"HOST_ROLE_REQUESTED","hostRoleRequest","eventJournal","example.test","Réservations","Parrainage","Devenir loueur")
    require(sources["admin.html"],*STATES,"hostApplications","eventJournal","VISITE_PLANIFIÉE","CONDITIONNEL","REFUSÉ","VALIDÉ")
    assert "published:app.status==='VALIDÉ'" in combined or "published = app.status === 'VALIDÉ'" in combined, "gate de publication absent"
    assert all(term.lower() not in combined.lower() for term in FORBIDDEN_INPUTS), "collecte réelle ou upload interdit"
    require(combined,"−20 % + CHF 20","Piscines partenaires","location.replace")
    scripts=[]
    for name,source in sources.items():
        scripts += [(name+f"-{i}",body) for i,(attrs,body) in enumerate(re.findall(r"<script([^>]*)>(.*?)</script>",source,re.S),1) if body.strip() and 'type="application/json"' not in attrs]
    with tempfile.TemporaryDirectory() as tmp:
        for name,body in scripts:
            path=Path(tmp)/(name+".js"); path.write_text(body,encoding="utf-8")
            done=subprocess.run(["node","--check",str(path)],capture_output=True,text=True)
            assert done.returncode==0, done.stderr
    print(f"PASS rounds 2–3: {len(PAGES)} pages, {len(scripts)} scripts")
    return 0
if __name__=="__main__": raise SystemExit(main())
