(function(root,factory){const api=factory();if(typeof module==='object'&&module.exports)module.exports=api;root.PoolbnbPricing=api})(typeof globalThis!=='undefined'?globalThis:this,function(){'use strict';
const POLICY='gross_25_included_v1',RATE_BPS=2500,MIN_PROMO_MINOR=9000;
const asMinor=value=>Number.isInteger(value)?value:Math.floor(Number(value)*100+0.5);
const asCHF=minor=>minor/100;
const roundCHF=value=>asCHF(asMinor(value));
function quote25({rentalValueGMinor,promoEligible=false,promoAvailable=false}){
 const g=Math.max(0,Math.trunc(Number(rentalValueGMinor)||0));
 const commission=Math.floor((g*25+50)/100),hostNet=g-commission;
 const eligible=Boolean(promoEligible&&promoAvailable&&g>=MIN_PROMO_MINOR);
 const discount=eligible?Math.floor((g*20+50)/100):0;
 const credit=eligible?Math.min(2000,g-discount):0;
 const promo=discount+credit;
 return{rentalValueGMinor:g,commissionRateBps:RATE_BPS,commissionGrossMinor:commission,hostNetMinor:hostNet,promoEligible:eligible,promoDiscount20Minor:discount,promoCreditUsedMinor:credit,promoTotalMinor:promo,clientPayableMinor:g-promo,contributionBeforeCostsMinor:commission-promo,pspCostMinor:null,insuranceCostMinor:null,supportCostMinor:null,fraudCostMinor:null,refundCostMinor:null,platformTaxCostMinor:null,otherMeasuredCostMinor:null,costMeasurementStatus:'UNMEASURED',contributionNetMinor:null,commissionPolicyVersion:POLICY}
}
function quoteCHF({rentalValueGCHF,promo=false}){const q=quote25({rentalValueGMinor:Math.floor(Number(rentalValueGCHF)*100+0.5),promoEligible:promo,promoAvailable:promo});return{...q,rentalValueG:asCHF(q.rentalValueGMinor),commissionGross:asCHF(q.commissionGrossMinor),hostNet:asCHF(q.hostNetMinor),discountAmount:asCHF(q.promoDiscount20Minor),creditUsed:asCHF(q.promoCreditUsedMinor),promoTotal:asCHF(q.promoTotalMinor),finalTotal:asCHF(q.clientPayableMinor),contributionBeforeCosts:asCHF(q.contributionBeforeCostsMinor)}}
return{POLICY,RATE_BPS,MIN_PROMO_MINOR,asMinor,asCHF,roundCHF,quote25,quoteCHF}});
