'use strict';
const assert=require('node:assert/strict');
const p=require('./pricing-engine.js');
const cases=[
 [6900,false,[1725,5175,0,6900,1725]],
 [9936,true,[2484,7452,3987,5949,-1503]],
 [12308,true,[3077,9231,4462,7846,-1385]],
 [14904,true,[3726,11178,4981,9923,-1255]]
];
for(const [g,promo,want] of cases){
 const q=p.quote25({rentalValueGMinor:g,promoEligible:promo,promoAvailable:promo});
 assert.deepEqual([q.commissionGrossMinor,q.hostNetMinor,q.promoTotalMinor,q.clientPayableMinor,q.contributionBeforeCostsMinor],want);
 assert.equal(q.rentalValueGMinor,q.commissionGrossMinor+q.hostNetMinor);
 assert.equal(q.commissionPolicyVersion,'gross_25_included_v1');
 assert.equal(q.contributionNetMinor,null);
}
for(let g=1;g<25000;g+=37){const q=p.quote25({rentalValueGMinor:g});assert.equal(g,q.commissionGrossMinor+q.hostNetMinor)}
console.log('PASS commission engine: 4/4 exacts, seuil promo, invariant centime, coûts null');
