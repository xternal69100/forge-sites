#!/usr/bin/env python3
"""Contrat TDD — commission 25 % incluse et guides publics Poolbnb."""
from __future__ import annotations
import re, subprocess
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SITE=ROOT.parent
ENGINE=ROOT/'pricing-engine.js'
SURFACES={
 'landing':SITE/'index.html','market':ROOT/'index.html','member':ROOT/'account.html',
 'host':ROOT/'account.html','admin':ROOT/'admin.html','memberGuide':ROOT/'guide-membre.html',
 'hostGuide':ROOT/'guide-loueur.html'}
POLICY='gross_25_included_v1'
KEY='forge:piscine-airbnb:demo:v1'

class Parser(HTMLParser): pass

def require(text,*needles):
    for needle in needles: assert needle in text, f'élément absent: {needle}'

def main():
    pages={}
    for name,path in SURFACES.items():
        assert path.exists(),f'page absente: {path.name}'
        text=path.read_text(encoding='utf-8'); Parser().feed(text); pages[name]=text
        print('HTML OK',name)
    engine=ENGINE.read_text(encoding='utf-8')
    node=r"""
const assert=require('node:assert/strict'),p=require(process.argv[1]);
const cases=[
 [6900,false,[1725,5175,0,6900,1725]],
 [9936,true,[2484,7452,3987,5949,-1503]],
 [12308,true,[3077,9231,4462,7846,-1385]],
 [14904,true,[3726,11178,4981,9923,-1255]]];
for(const [g,promo,want] of cases){const q=p.quote25({rentalValueGMinor:g,promoEligible:promo,promoAvailable:promo});assert.deepEqual([q.commissionGrossMinor,q.hostNetMinor,q.promoTotalMinor,q.clientPayableMinor,q.contributionBeforeCostsMinor],want);assert.equal(q.rentalValueGMinor,q.commissionGrossMinor+q.hostNetMinor);assert.equal(q.commissionPolicyVersion,'gross_25_included_v1');assert.equal(q.commissionRateBps,2500);assert.equal(q.contributionNetMinor,null)}
for(let g=1;g<25000;g+=37){const q=p.quote25({rentalValueGMinor:g});assert.equal(q.rentalValueGMinor,q.commissionGrossMinor+q.hostNetMinor)}
assert.equal(p.quote25({rentalValueGMinor:8999,promoEligible:true,promoAvailable:true}).promoTotalMinor,0);
assert.equal(p.quote25({rentalValueGMinor:9000,promoEligible:true,promoAvailable:true}).promoTotalMinor,3800);
console.log('ENGINE 25/75 OK: 4 exemples, seuil, null costs, invariants');
"""
    done=subprocess.run(['node','-e',node,str(ENGINE)],text=True,capture_output=True)
    assert done.returncode==0,done.stderr
    print(done.stdout.strip())
    assert not re.search(r'guestFee|hostPrice|0\.08|0\.10|min\s*6|max\s*18',engine,re.I),'logique legacy dans le runtime'
    for name in ('landing','market','member','host','admin'):
        require(pages[name],'commission Poolbnb 25 % incluse')
    require(pages['market'],POLICY,'commissionGrossMinor','hostNetMinor','contributionBeforeCostsMinor','costMeasurementStatus','UNMEASURED','contributionNetMinor','MIGRATION_SNAPSHOT_CREATED','reversesEntryId')
    require(pages['admin'],'Contribution avant coûts','À mesurer','Politique','25,00 %','Contribution négative')
    require(pages['host'],'75 %','commission Poolbnb 25 % incluse')
    combined='\n'.join(pages.values())
    assert KEY in combined
    assert 'commission 10 %' not in combined and 'Frais invité inclus' not in combined
    for name in ('member','host'):
        require(pages[name],'guide-membre.html','guide-loueur.html')
    for name in ('landing','market','admin'):
        require(pages[name],'guides.html')
    for name,title,other in [('memberGuide','Guide membre Poolbnb','guide-loueur.html'),('hostGuide','Guide loueur Poolbnb','guide-membre.html')]:
        page=pages[name]; require(page,title,other,'Démarrage rapide','FAQ','checklist','@media print','@media (max-width:')
        assert page.count('href="#')>=6,'sommaire ancré insuffisant'
        assert page.count('type="checkbox"')>=5,'checklist insuffisante'
        assert not re.search(r'\bTODO\b|localStorage|équipe dev|@(?![a-z0-9.-]*example\.test\b)[a-z0-9.-]+\.[a-z]{2,}',page,re.I),'jargon ou contact réel dans guide'
    print('PASS commission 25 % + guides: 7 surfaces, liens, ancres, checklists, impression')
if __name__=='__main__': main()
