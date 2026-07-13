(()=>{'use strict';
const STORE_KEY='forge:coach-office:demo:v2';
const RELEASE='coach-office-v2';
const DOMAIN_IDS=['agenda','inbox','crm','prospects','marketing','invoices','accounting','reporting'];
const DOMAIN_LABELS={agenda:'Agenda & rendez-vous',inbox:'Inbox & email',crm:'CRM & base clients',prospects:'Prospects & relances',marketing:'Marketing & contenus',invoices:'Devis & factures',accounting:'Pièces & pré-compta',reporting:'Reporting & approbations'};
const ARRAY_KEYS=['agenda','contacts','inbox','marketing','invoices','accounting','tasks','approvals','journal'];
const clone=value=>JSON.parse(JSON.stringify(value));
function emptyStore(){return {version:2,release:RELEASE,mode:'DÉMO SYNTHÉTIQUE',profile:null,subscription:null,onboarding:{appointments:[],domains:[]},agenda:[],contacts:[],inbox:[],marketing:[],invoices:[],accounting:[],tasks:[],approvals:[],journal:[]};}
function valid(store){return Boolean(store&&store.version===2&&store.release===RELEASE&&store.onboarding&&Array.isArray(store.onboarding.appointments)&&Array.isArray(store.onboarding.domains)&&ARRAY_KEYS.every(key=>Array.isArray(store[key])));}
function emit(store){window.dispatchEvent(new CustomEvent('coach-office-change',{detail:clone(store)}));}
function saveStore(store){if(!valid(store))throw new Error('Store v2 invalide');localStorage.setItem(STORE_KEY,JSON.stringify(store));emit(store);return store;}
function loadStore(){try{const parsed=JSON.parse(localStorage.getItem(STORE_KEY));if(valid(parsed))return parsed;}catch(_error){}return saveStore(emptyStore());}
function resetStore(){return saveStore(emptyStore());}
function isTestEmail(value){return /^[^\s@]+@(?:[a-z0-9-]+\.)*test$/i.test(String(value||'').trim());}
function assertSynthetic(value){if(!isTestEmail(value))throw new Error('Utilisez exclusivement une adresse se terminant par .test.');}
function now(){return new Date().toISOString();}
function event(store,type,message,refId=''){store.journal.unshift({id:`EVT-${Date.now().toString(36).toUpperCase()}`,at:now(),type,message,refId,provenance:'SYNTHÉTIQUE .test'});}
function bootstrapDemo({studio,email,appointments,domains}){
  assertSynthetic(email);
  if(!String(studio||'').trim())throw new Error('Le nom du studio fictif est requis.');
  if(!Array.isArray(appointments)||appointments.length!==2)throw new Error('Sélectionnez exactement deux rendez-vous d’onboarding.');
  if(!Array.isArray(domains)||DOMAIN_IDS.some(id=>!domains.includes(id)))throw new Error('Activez les huit domaines pour la démonstration complète.');
  const createdAt=now(),store=emptyStore();
  store.profile={id:'COACH-DEMO-001',studio:String(studio).trim(),name:'Léa Martin — profil fictif',email:String(email).trim().toLowerCase(),telegram:'@lea_studio_demo',synthetic:true};
  store.subscription={id:'SUB-DEMO-001',offer:'Offre fondatrice',setupCHF:300,monthlyCHF:150,status:'Active — démo',createdAt,realCharge:false};
  store.onboarding={appointments:appointments.map((slot,index)=>({id:`ONB-DEMO-00${index+1}`,slot,durationMinutes:60,status:'Planifié — démo'})),domains:[...DOMAIN_IDS]};
  store.agenda=[
    {id:'RDV-DEMO-101',title:'Bilan de démarrage — Camille Démo',when:'Mardi · 09:00',status:'Confirmé',email:'camille@client-exemple.test',detail:'Rendez-vous fictif, sans note de santé ni donnée physique.'},
    {id:'RDV-DEMO-102',title:'Appel découverte — Noa Démo',when:'Mardi · 14:30',status:'À préparer',email:'noa@prospect-exemple.test',detail:'Échange commercial synthétique de 30 minutes.'},
    {id:'RDV-DEMO-103',title:'Point administratif — Studio',when:'Mercredi · 11:00',status:'Interne',email:'operations@studio-horizon.test',detail:'Créneau fictif de revue des opérations.'}
  ];
  store.contacts=[
    {id:'CRM-DEMO-201',title:'Camille Démo',type:'Cliente',status:'Active',email:'camille@client-exemple.test',detail:'Dossier synthétique : contact et historique administratif uniquement.'},
    {id:'CRM-DEMO-202',title:'Alex Démo',type:'Client',status:'À renouveler',email:'alex@client-exemple.test',detail:'Échéance commerciale fictive dans 12 jours.'},
    {id:'PRO-DEMO-203',title:'Noa Démo',type:'Prospect',status:'Relance prévue',email:'noa@prospect-exemple.test',detail:'A demandé une présentation fictive de l’accompagnement.'},
    {id:'PRO-DEMO-204',title:'Sam Démo',type:'Prospect',status:'Nouveau',email:'sam@prospect-exemple.test',detail:'Contact synthétique issu d’un formulaire local de démonstration.'}
  ];
  store.inbox=[
    {id:'MSG-DEMO-301',title:'Question sur le prochain rendez-vous',from:'camille@client-exemple.test',status:'À répondre',detail:'Message fictif. Réponse proposée, non envoyée.'},
    {id:'MSG-DEMO-302',title:'Demande de devis',from:'noa@prospect-exemple.test',status:'Prioritaire',detail:'Demande commerciale synthétique à traiter aujourd’hui.'},
    {id:'MSG-DEMO-303',title:'Confirmation de réception',from:'alex@client-exemple.test',status:'Classé',detail:'Confirmation fictive sans action requise.'}
  ];
  store.marketing=[
    {id:'MKT-DEMO-401',title:'Carrousel — 3 façons de garder un rythme régulier',channel:'Instagram',status:'À valider',detail:'Brouillon synthétique, sans promesse médicale ni témoignage.'},
    {id:'MKT-DEMO-402',title:'Newsletter — agenda du mois',channel:'Email',status:'Planifié',detail:'Contenu fictif prévu jeudi à 08:30, aucun envoi réel.'}
  ];
  store.invoices=[
    {id:'FAC-DEMO-501',title:'Facture F-2026-014 — Camille Démo',amountCHF:180,status:'Payée — démo',email:'camille@client-exemple.test',detail:'Pièce synthétique, aucun paiement réel.'},
    {id:'DEV-DEMO-502',title:'Devis D-2026-008 — Noa Démo',amountCHF:360,status:'À envoyer',email:'noa@prospect-exemple.test',detail:'Devis fictif en attente d’approbation.'}
  ];
  store.accounting=[
    {id:'PCE-DEMO-601',title:'Reçu matériel — Fournisseur Démo',amountCHF:74.9,status:'À catégoriser',email:'factures@fournisseur-exemple.test',detail:'Justificatif entièrement synthétique.'},
    {id:'PCE-DEMO-602',title:'Abonnement logiciel — Démo',amountCHF:22,status:'Prêt export',email:'billing@outil-exemple.test',detail:'Écriture fictive prête pour export de démonstration.'}
  ];
  store.tasks=[
    {id:'TSK-DEMO-701',title:'Répondre à la demande de devis',owner:'Office manager',status:'Aujourd’hui',detail:'Préparer une réponse et demander validation avant envoi.'},
    {id:'TSK-DEMO-702',title:'Relancer le renouvellement Alex Démo',owner:'Office manager',status:'Planifié',detail:'Relance commerciale fictive planifiée demain.'},
    {id:'TSK-DEMO-703',title:'Catégoriser le reçu matériel',owner:'Coach',status:'À décider',detail:'Choix comptable simulé à confirmer.'}
  ];
  store.approvals=[
    {id:'APR-DEMO-801',title:'Valider le carrousel Instagram',kind:'Contenu',status:'À valider',risk:'Publication externe simulée',detail:'Proposition synthétique : « La régularité commence par un créneau réaliste. »'},
    {id:'APR-DEMO-802',title:'Autoriser l’envoi du devis D-2026-008',kind:'Devis',status:'À valider',risk:'Engagement commercial simulé',detail:'Montant fictif CHF 360. Aucun envoi ni engagement réel.'}
  ];
  event(store,'ACTIVATION_DEMO','Office manager fictif activé : 8 domaines, aucun débit ni transmission.','SUB-DEMO-001');
  event(store,'CHECKOUT_SIMULE','Checkout simulé : CHF 300 installation + CHF 150/mois.','SUB-DEMO-001');
  return saveStore(store);
}
function updateApproval(id,decision){
  const allowed={validate:'Validé — démo',modify:'À modifier',refuse:'Refusé — démo'};
  if(!allowed[decision])throw new Error('Décision invalide.');
  const store=loadStore(),approval=store.approvals.find(item=>item.id===id);
  if(!approval)throw new Error('Approbation introuvable.');
  approval.status=allowed[decision];approval.decidedAt=now();
  event(store,`APPROBATION_${decision.toUpperCase()}`,`${approval.title} : ${allowed[decision]}.`,id);
  return saveStore(store);
}
function allRecords(store=loadStore()){
  const map=(items,domain,domainLabel,subtitle)=>items.map(item=>({domain,domainLabel,id:item.id,title:item.title,subtitle:typeof subtitle==='function'?subtitle(item):item[subtitle]||'',status:item.status||'—',detail:item.detail||'',raw:item}));
  return [
    ...map(store.agenda,'agenda','Agenda',item=>`${item.when} · ${item.email}`),
    ...map(store.contacts,'crm','CRM',item=>`${item.type} · ${item.email}`),
    ...map(store.inbox,'inbox','Inbox',item=>item.from),
    ...map(store.marketing,'marketing','Marketing',item=>item.channel),
    ...map(store.invoices,'invoices','Factures',item=>`CHF ${Number(item.amountCHF).toLocaleString('fr-CH')} · ${item.email}`),
    ...map(store.accounting,'accounting','Pré-compta',item=>`CHF ${Number(item.amountCHF).toLocaleString('fr-CH')} · ${item.email}`),
    ...map(store.tasks,'tasks','Tâches',item=>item.owner),
    ...map(store.approvals,'approvals','Approbations',item=>`${item.kind} · ${item.risk}`),
    ...map(store.journal,'journal','Journal',item=>item.at)
  ];
}
function escapeHTML(value){return String(value??'').replace(/[&<>"']/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));}
window.CoachOffice={STORE_KEY,RELEASE,DOMAIN_IDS,DOMAIN_LABELS,emptyStore,loadStore,saveStore,resetStore,isTestEmail,bootstrapDemo,updateApproval,allRecords,escapeHTML};
})();
