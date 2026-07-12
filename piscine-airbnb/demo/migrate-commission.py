#!/usr/bin/env python3
import json,re
from decimal import Decimal,ROUND_HALF_UP
from pathlib import Path
ROOT=Path(__file__).resolve().parent; SITE=ROOT.parent

def q(x): return x.quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
def enrich(obj):
 for o in obj['offers']:
  hb=Decimal(str(o.pop('hostBase'))); ext=Decimal(str(o['extensionHourly'])); extra=Decimal(str(o['extraGuest']))
  vals={}
  for party in (2,4,6,8):
   for hours in (0,1,2):
    for weekend in (0,1):
     h=q((hb+ext*hours+extra*max(0,party-4))*(Decimal('1.15') if weekend else Decimal('1')))
     fee=max(Decimal('6'),min(Decimal('18'),q(h*Decimal('.08'))))
     vals[f'{party}-{hours}-{weekend}']=float(q(h+fee))
  o['rentalValueG']=o.pop('guestTotal2h');o['standardRentalValues']=vals
 return obj

def pricing(path):
 s=path.read_text(); m=re.search(r'(<script id="pricing-data" type="application/json">\s*)(\{.*?\})(\s*</script>)',s,re.S)
 if not m:return s
 data=enrich(json.loads(m.group(2)))
 return s[:m.start()]+m.group(1)+json.dumps(data,ensure_ascii=False,separators=(',',':'))+m.group(3)+s[m.end():]

market=pricing(ROOT/'index.html')
repls=[
("<a href=\"admin.html\">Admin</a>","<a href=\"admin.html\">Admin</a><a href=\"guide-membre.html\">Guide membre</a><a href=\"guide-loueur.html\">Guide loueur</a>"),
("total du créneau inclut déjà les frais obligatoires.","total du créneau inclut déjà la commission Poolbnb 25 % incluse."),
("frais obligatoires inclus</small>","commission Poolbnb 25 % incluse</small>"),
("<span>Prix hôte</span><strong id=\"hostPrice\">—</strong>","<span>Valeur de location G</span><strong id=\"rentalValueG\">—</strong>"),
("<span>Frais invité inclus</span><strong id=\"guestFee\">—</strong>","<span>dont commission Poolbnb 25 % incluse</span><strong id=\"commissionGross\">—</strong>"),
("<span>Total avant promo</span><strong id=\"subtotal\">—</strong>","<span>Net hôte 75 %</span><strong id=\"hostNet\">—</strong>"),
("<span>Revenu hôte inchangé</span><strong id=\"hostPayout\">—</strong>","<span>Contribution avant coûts</span><strong id=\"contributionBeforeCosts\">—</strong>"),
("price:p.hostBase","price:p.rentalValueG"),
("q=PoolbnbPricing.quote({hostBase:l.hostBase,extensionHourly:l.extensionHourly,extraGuest:l.extraGuest,partySize:4,extensionHours:0,weekend:false,promo:false})","q=PoolbnbPricing.quote({rentalValueG:l.standardRentalValues['4-0-0'],promo:false})"),
("amount:q.finalTotal,subtotal:q.guestTotalBeforePromo,hostPrice:q.hostPrice,guestFee:q.guestFee,guestTotalBeforePromo:q.guestTotalBeforePromo,discountAmount:0,creditUsed:0,finalTotal:q.finalTotal,hostPayout:q.hostPayout,packApplied:false,status","amount:q.finalTotal,rentalValueG:q.rentalValueG,commissionGross:q.commissionGross,hostNet:q.hostNet,promoTotal:0,discountAmount:0,creditUsed:0,finalTotal:q.finalTotal,contributionBeforeCosts:q.contributionBeforeCosts,contributionNet:null,costMeasurementStatus:'UNMEASURED',commissionPolicyVersion:q.commissionPolicyVersion,packApplied:false,status"),
("version:1,pricingVersion:'17-pilote'","version:2,pricingVersion:'17-pilote',commissionPolicyVersion:'gross_25_included_v1'"),
("eventJournal:[{id:'EVT-DEMO-001'","legacySnapshots:[{bookingId:'BKG-LEGACY-SNAPSHOT',commissionPolicyVersion:'legacy_10_host_8_guest',rentalValueG:99.36,hostPayout:82.80,immutable:true}],financialLedger:[{ledgerEntryId:'FIN-DEMO-001',entryGroupId:'GRP-RESET-001',sequenceNo:1,bookingId:null,accountCode:'POOLBNB_COMMISSION_REVENUE',entryType:'MIGRATION_SNAPSHOT_CREATED',amountMinorSigned:0,currency:'CHF',eventType:'RESET_BASELINE_CREATED',commissionPolicyVersion:'gross_25_included_v1',pricingVersion:'17-pilote',reversesEntryId:null,idempotencyKey:'reset-v2-001'}],eventJournal:[{id:'EVT-DEMO-001'"),
("return s&&s.version===1&&Array.isArray(s.bookings)&&Array.isArray(s.partnerOrders)&&Array.isArray(s.hostApplications)&&Array.isArray(s.referrals)&&Array.isArray(s.creditLedger)","return s&&s.version===2&&Array.isArray(s.bookings)&&Array.isArray(s.partnerOrders)&&Array.isArray(s.hostApplications)&&Array.isArray(s.referrals)&&Array.isArray(s.creditLedger)&&Array.isArray(s.financialLedger)"),
("q=PoolbnbPricing.quote({hostBase:l.hostBase,extensionHourly:l.extensionHourly,extraGuest:l.extraGuest,partySize:b.partySize||4,extensionHours:b.extensionHours||0,weekend:Boolean(b.weekend),promo:false})","q=PoolbnbPricing.quote({rentalValueG:l.standardRentalValues[`${b.partySize||4}-${b.extensionHours||0}-${b.weekend?1:0}`],promo:false})"),
("amount:q.finalTotal,subtotal:q.guestTotalBeforePromo,hostPrice:q.hostPrice,guestFee:q.guestFee,guestTotalBeforePromo:q.guestTotalBeforePromo,discountAmount:b.packApplied?b.discountAmount:0,creditUsed:b.packApplied?b.creditUsed:0,finalTotal:b.packApplied?b.finalTotal:q.finalTotal,hostPayout:q.hostPayout","amount:b.packApplied?b.finalTotal:q.finalTotal,rentalValueG:q.rentalValueG,commissionGross:q.commissionGross,hostNet:q.hostNet,promoTotal:b.packApplied?(b.discountAmount+b.creditUsed):0,discountAmount:b.packApplied?b.discountAmount:0,creditUsed:b.packApplied?b.creditUsed:0,finalTotal:b.packApplied?b.finalTotal:q.finalTotal,contributionBeforeCosts:b.packApplied?q.commissionGross-b.discountAmount-b.creditUsed:q.contributionBeforeCosts,contributionNet:null,costMeasurementStatus:'UNMEASURED',commissionPolicyVersion:'gross_25_included_v1'"),
("return PoolbnbPricing.quote({hostBase:listing.hostBase,extensionHourly:listing.extensionHourly,extraGuest:listing.extraGuest,partySize,extensionHours,weekend,promo:Boolean(store.discoveryPack.eligible&&!store.discoveryPack.used)})","return PoolbnbPricing.quote({rentalValueG:listing.standardRentalValues[`${partySize}-${extensionHours}-${weekend?1:0}`],promo:Boolean(store.discoveryPack.eligible&&!store.discoveryPack.used)})"),
("x.guestTotal2h<=maxTotal","x.rentalValueG<=maxTotal"),
("money(x.guestTotal2h)","money(x.rentalValueG)"),
("q.guestTotalBeforePromo<90","q.rentalValueG<90"),
("$('#hostPrice').textContent=money(q.hostPrice);$('#guestFee').textContent=money(q.guestFee);$('#subtotal').textContent=money(q.guestTotalBeforePromo)","$('#rentalValueG').textContent=money(q.rentalValueG);$('#commissionGross').textContent=money(q.commissionGross);$('#hostNet').textContent=money(q.hostNet)"),
("$('#hostPayout').textContent=money(q.hostPayout)","$('#contributionBeforeCosts').textContent=money(q.contributionBeforeCosts)"),
("subtotal:q.guestTotalBeforePromo,hostPrice:q.hostPrice,guestFee:q.guestFee,guestTotalBeforePromo:q.guestTotalBeforePromo,discountAmount:q.discountAmount,creditUsed:q.creditUsed,finalTotal:q.finalTotal,hostPayout:q.hostPayout","rentalValueG:q.rentalValueG,commissionGross:q.commissionGross,hostNet:q.hostNet,promoTotal:q.promoTotal,discountAmount:q.discountAmount,creditUsed:q.creditUsed,finalTotal:q.finalTotal,contributionBeforeCosts:q.contributionBeforeCosts,contributionNet:null,costMeasurementStatus:'UNMEASURED',commissionPolicyVersion:q.commissionPolicyVersion"),
("s.eventJournal.push({id:'EVT-'+Date.now(),at:new Date().toISOString(),type:'BOOKING_CREATED',message:b.id});","s.financialLedger.push({ledgerEntryId:'FIN-'+Date.now(),entryGroupId:'GRP-'+b.id,sequenceNo:1,bookingId:b.id,accountCode:'POOLBNB_COMMISSION_REVENUE',entryType:'BOOKING_CONTRACTED',amountMinorSigned:q.commissionGrossMinor,currency:'CHF',eventType:'BOOKING_CONTRACTED',commissionPolicyVersion:q.commissionPolicyVersion,pricingVersion:'17-pilote',reversesEntryId:null,idempotencyKey:'booking-'+b.id});s.eventJournal.push({id:'EVT-'+Date.now(),at:new Date().toISOString(),type:'BOOKING_CREATED',message:b.id});"),
("guestFee:PoolbnbPricing.guestFee,","policy:PoolbnbPricing.POLICY,"),
]
for a,b in repls:
 if a not in market: print('WARN market missing',a[:80])
 market=market.replace(a,b)
(ROOT/'index.html').write_text(market)

# shared nav links and role copy
for fn in ('member.html','host.html','admin.html'):
 p=ROOT/fn;s=p.read_text();s=s.replace('<a href="admin.html">Admin</a>','<a href="admin.html">Admin</a><a href="guide-membre.html">Guide membre</a><a href="guide-loueur.html">Guide loueur</a>')
 s=s.replace('<a class="link" href="host.html">↗ <span>Espace loueur</span></a>','<a class="link" href="host.html">↗ <span>Espace loueur</span></a><a class="link" href="guide-membre.html">? <span>Guide membre</span></a><a class="link" href="guide-loueur.html">? <span>Guide loueur</span></a>')
 p.write_text(s)

member=(ROOT/'member.html').read_text()
member=member.replace('Chaque réservation aligne Prix hôte · Frais invité inclus · Total avant promo · Revenu hôte.','Chaque réservation aligne valeur G · commission Poolbnb 25 % incluse · promotion · total payé · politique versionnée.')
member=member.replace("${b.packApplied?' · pack appliqué':''}</span><small>Prix hôte ${money(b.hostPrice)} · Frais invité inclus ${money(b.guestFee)} · Total avant promo ${money(b.guestTotalBeforePromo??b.subtotal??b.amount)} · Revenu hôte ${money(b.hostPayout)}</small>","${b.packApplied?' · pack appliqué':''}</span><small>G ${money(b.rentalValueG)} · commission Poolbnb 25 % incluse ${money(b.commissionGross)} · net hôte ${money(b.hostNet)} · promo ${money(b.promoTotal||0)} · payé ${money(b.finalTotal)} · politique ${b.commissionPolicyVersion}</small>")
(ROOT/'member.html').write_text(member)

host=(ROOT/'host.html').read_text()
host=host.replace('Revenu hôte fictif après commission 10 %, jamais réduit par le pack','Net hôte fictif 75 % de G, jamais réduit par le pack')
host=host.replace('Prix hôte · Frais invité inclus · Total avant promo · Revenu hôte.','G · commission Poolbnb 25 % incluse · net hôte 75 % · promotion séparée.')
host=host.replace("reduce((a,b)=>a+Number(b.hostPayout||0),0)","reduce((a,b)=>a+Number(b.hostNet||0),0)")
host=host.replace("${b.id} · ${b.date} · ${b.hostPayout?money(b.hostPayout):'Revenu à mesurer'}","${b.id} · ${b.date} · G ${money(b.rentalValueG)} · net 75 % ${money(b.hostNet)}")
host=host.replace('</p><div class="notice"><strong>Gate assurance explicite', '</p><p><strong>Accepter la commission 25 % incluse</strong> est requis avant tout nouveau créneau : le prix G reste inchangé et le net hôte est 75 %.</p><div class="notice"><strong>Gate assurance explicite')
(ROOT/'host.html').write_text(host)

admin=(ROOT/'admin.html').read_text()
admin=admin.replace('<p><strong>KPI synthétiques — démonstration, pas traction</strong></p>','<p><strong>KPI synthétiques — démonstration, pas traction</strong> · Politique gross_25_included_v1 · take rate 25,00 % · coûts et contribution nette : À mesurer.</p>')
admin=admin.replace('<th>Prix hôte</th><th>Frais invité inclus</th><th>Total avant promo</th><th>−20 %</th><th>Crédit</th><th>Total final</th><th>Revenu hôte</th><th>Statut</th>','<th>G</th><th>Commission brute</th><th>Net hôte</th><th>Promo</th><th>Client payé</th><th>Contribution avant coûts</th><th>Contribution nette</th><th>Politique</th><th>Statut</th>')
old="<td>${money(b.hostPrice)}</td><td>${money(b.guestFee)}</td><td>${money(b.guestTotalBeforePromo??b.subtotal??b.amount)}</td><td>− ${money(b.discountAmount)}</td><td>− ${money(b.creditUsed)}</td><td><strong>${money(b.finalTotal??b.amount)}</strong></td><td>${money(b.hostPayout)}</td><td><span class=\"status\">${b.status}</span></td>"
new="<td>${money(b.rentalValueG)}</td><td>${money(b.commissionGross)}<br><small>commission Poolbnb 25 % incluse</small></td><td>${money(b.hostNet)}</td><td>− ${money(b.promoTotal||0)}</td><td><strong>${money(b.finalTotal)}</strong></td><td class=\"${b.contributionBeforeCosts<0?'negative':''}\">${money(b.contributionBeforeCosts)}${b.contributionBeforeCosts<0?'<br><small>Contribution négative · CAC pack</small>':''}</td><td>À mesurer</td><td>${b.commissionPolicyVersion}</td><td><span class=\"status\">${b.status}</span></td>"
admin=admin.replace(old,new)
admin=admin.replace('.status{display:inline-flex', '.negative{color:#A92A42;font-weight:850}.status{display:inline-flex')
(ROOT/'admin.html').write_text(admin)

landing=pricing(SITE/'index.html')
landing=landing.replace('frais obligatoires inclus','commission Poolbnb 25 % incluse')
landing=landing.replace('<span>Prix hôte</span><span id="lineBase">0 CHF</span>','<span>Valeur de location G</span><span id="lineBase">0 CHF</span>')
landing=landing.replace('<span>Frais invité inclus</span><span id="lineService">0 CHF</span>','<span>dont commission Poolbnb 25 % incluse</span><span id="lineService">0 CHF</span>')
landing=landing.replace("PoolbnbPricing.quote({hostBase:currentListing.hostBase,extensionHourly:currentListing.extensionHourly,extraGuest:currentListing.extraGuest,partySize:guestCount,extensionHours:Math.max(0,duration-2),weekend:Boolean(selectedDate&&[0,6].includes(selectedDate.getDay())),promo:false})","PoolbnbPricing.quote({rentalValueG:currentListing.standardRentalValues[`${guestCount}-${Math.max(0,duration-2)}-${selectedDate&&[0,6].includes(selectedDate.getDay())?1:0}`],promo:false})")
landing=landing.replace('const base = pricing.hostPrice;','const base = pricing.rentalValueG;').replace('const service = pricing.guestFee;','const service = pricing.commissionGross;').replace('const total = pricing.guestTotalBeforePromo + extras;','const total = pricing.rentalValueG + extras;')
# add guide links to desktop/mobile footer by inserting before body end (visible compact)
landing=landing.replace('</footer>','<div class="mx-auto mt-8 flex max-w-[1280px] flex-wrap gap-4 px-6"><a href="demo/guide-membre.html" class="font-extrabold underline">Guide membre</a><a href="demo/guide-loueur.html" class="font-extrabold underline">Guide loueur</a></div></footer>')
(SITE/'index.html').write_text(landing)
