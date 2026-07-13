(()=>{'use strict';
const STORE_KEY='forge:forge-capital:demo:v1';
const STATES=['OBSERVÉ','ÉTUDIÉ','PAPER','TICKET À VALIDER','EXÉCUTÉ AVEC PREUVE','REJETÉ'];
const experts=[
 {name:'Market Validator',mission:'Surveille les données publiques Kraken et la qualité des signaux.',status:'COLLECTE'},
 {name:'Legal Expert',mission:'Vérifie les restrictions Suisse, ToS et zones grises avant toute action.',status:'GARDE-FOU'},
 {name:'Fiscal Optimizer',mission:'Sépare P&L paper, valeur nette réelle et implications fiscales probables.',status:'VEILLE'},
 {name:'Business Planner',mission:'Compare la stratégie aux benchmarks et aux seuils du mandat.',status:'ANALYSE'},
 {name:'Funding Specialist',mission:'Contrôle le capital reçu, la réserve et les engagements.',status:'0 USDT REÇU'},
 {name:'Web Builder',mission:'Maintient le cockpit public sanitizé et le pipeline privé local.',status:'LIVRÉ'},
 {name:'Synergy Finder',mission:'Relie données, décisions, risques et apprentissages de Forge Capital.',status:'INDEXATION'},
 {name:'Quality Guardian',mission:'Bloque EXÉCUTÉ AVEC PREUVE sans identifiant, source et timestamp.',status:'GATE ACTIF'}
];
const projects=[
 {slug:'market-data',name:'Collecte publique Kraken',phase:3,status:'DIFFÉRÉ',score:null},
 {slug:'paper-learning',name:'Centre d’apprentissage long / short',phase:3,status:'PAPER',score:null},
 {slug:'risk-governance',name:'Capital, risques et conformité',phase:3,status:'GARDE-FOU',score:null},
 {slug:'execution',name:'Tickets spot long-only à signature humaine',phase:3,status:'BLOQUÉ — 0 USDT REÇU',score:null,capital:{authorized_usdt:100,received_usdt:0,liquid_usdt:0,invested_usdt:0,committed_usdt:0,net_value_usdt:0}}
];
function clone(value){return JSON.parse(JSON.stringify(value));}
function baseline(){return {version:3,mode:'DÉMO',experts:experts.map((expert,i)=>({id:`EXP-${String(i+1).padStart(2,'0')}`,...expert})),projects:clone(projects),learnings:[{id:'LRN-001',domain:'marché',text:'Une donnée publique n’est LIVE PUBLIC que si sa source et son horodatage sont visibles ; sinon elle reste DIFFÉRÉ.',provenance:'FORGE CAPITAL'},{id:'LRN-002',domain:'preuve',text:'EXÉCUTÉ AVEC PREUVE exige proofId, proofSource et proofTimestamp.',provenance:'FORGE CAPITAL'},{id:'LRN-003',domain:'risque',text:'Le P&L PAPER ne modifie jamais la valeur nette réelle.',provenance:'FORGE CAPITAL'}],transactions:[{id:'TX-DEMO-BASE',title:'Capital non reçu — aucune exécution',asset:'USDT',status:'REJETÉ',proofId:'PRF-DEMO-BASE',proofSource:'Fixture DÉMO locale',proofTimestamp:'2026-07-13T00:00:00Z',study:'100 USDT autorisés mais 0 USDT reçus : ordre réel interdit.',createdAt:'2026-07-13T00:00:00Z',updatedAt:'2026-07-13T00:00:00Z',provenance:'DÉMO'}],journal:[{id:'EVT-DEMO-BASE',at:'2026-07-13T00:00:00Z',type:'RESET_BASELINE',message:'Baseline Forge Capital synthétique chargée',provenance:'DÉMO'}]};}
function valid(store){return store&&store.version===3&&Array.isArray(store.experts)&&Array.isArray(store.projects)&&Array.isArray(store.learnings)&&Array.isArray(store.transactions)&&Array.isArray(store.journal);}
function saveStore(store){localStorage.setItem(STORE_KEY,JSON.stringify(store));window.dispatchEvent(new CustomEvent('forge-capital-change',{detail:store}));return store;}
function loadStore(){try{const parsed=JSON.parse(localStorage.getItem(STORE_KEY));if(valid(parsed))return parsed;}catch(_error){}return saveStore(baseline());}
function resetStore(){return saveStore(baseline());}
function uid(prefix){return `${prefix}-DEMO-${Date.now().toString(36).toUpperCase()}`;}
function appendEvent(store,type,message,refId=''){store.journal.push({id:uid('EVT'),at:new Date().toISOString(),type,message,refId,provenance:'DÉMO'});return store;}
function getTransaction(store,id){const item=store.transactions.find(row=>row.id===id);if(!item)throw new Error('Signal introuvable');return item;}
function createSignal({title,asset}){const store=loadStore();const now=new Date().toISOString();const item={id:uid('TX'),title:String(title||'Signal synthétique').trim(),asset:String(asset||'Aucun actif').trim(),status:'OBSERVÉ',proofId:'',proofSource:'',proofTimestamp:'',study:'',ticket:null,createdAt:now,updatedAt:now,provenance:'DÉMO'};store.transactions.unshift(item);appendEvent(store,'SIGNAL_OBSERVÉ','Signal fixture DÉMO créé',item.id);saveStore(store);return item;}
function studySignal(id,note){const store=loadStore(),item=getTransaction(store,id);item.status='ÉTUDIÉ';item.study=String(note||'Étude synthétique terminée.').trim();item.updatedAt=new Date().toISOString();appendEvent(store,'SIGNAL_ÉTUDIÉ','Étude fixture DÉMO ajoutée',id);saveStore(store);return item;}
function decideSignal(id,status){if(!['PAPER','REJETÉ'].includes(status))throw new Error('Décision autorisée : PAPER ou REJETÉ');const store=loadStore(),item=getTransaction(store,id);item.status=status;item.updatedAt=new Date().toISOString();appendEvent(store,`DÉCISION_${status}`,`Décision ${status} enregistrée`,id);saveStore(store);return item;}
function createUnsignedTicket(id){const store=loadStore(),item=getTransaction(store,id);item.status='TICKET À VALIDER';item.ticket={kind:'SPOT LONG-ONLY',signed:false,execution:false,humanSignatureRequired:true,expiresMinutes:30};item.updatedAt=new Date().toISOString();appendEvent(store,'TICKET_NON_SIGNÉ','Ticket fixture DÉMO créé — signature humaine par ordre requise',id);saveStore(store);return item;}
function addProof(id,label='Preuve de démonstration',source='Fixture DÉMO locale'){const store=loadStore(),item=getTransaction(store,id),stamp=new Date().toISOString();item.proofId=uid('PRF');item.proofLabel=String(label).trim();item.proofSource=String(source).trim();item.proofTimestamp=stamp;item.updatedAt=stamp;appendEvent(store,'PREUVE_AJOUTÉE','Référence de preuve DÉMO complète ajoutée',id);saveStore(store);return item;}
function hasCompleteProof(item){return ['proofId','proofSource','proofTimestamp'].every(field=>String(item[field]||'').trim());}
function updateStatus(id,status){if(!STATES.includes(status))throw new Error('Statut invalide');const store=loadStore(),item=getTransaction(store,id);if(status==='EXÉCUTÉ AVEC PREUVE'&&!hasCompleteProof(item))throw new Error('EXÉCUTÉ AVEC PREUVE exige proofId, proofSource et proofTimestamp');item.status=status;item.updatedAt=new Date().toISOString();appendEvent(store,'STATUT_MODIFIÉ',`Statut passé à ${status}`,id);saveStore(store);return item;}
function assertBaseline(){const store=loadStore();return {ok:store.transactions.length===1&&store.transactions[0].id==='TX-DEMO-BASE'&&store.journal.length===1,transactions:store.transactions.length,journal:store.journal.length};}
function escapeHTML(value){return String(value??'').replace(/[&<>"']/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));}
function badge(status){return `<span class="badge ${escapeHTML(status)}">${escapeHTML(status)}</span>`;}
window.ForgeCapitalMatrix={STORE_KEY,STATES,baseline,loadStore,saveStore,resetStore,appendEvent,createSignal,studySignal,decideSignal,createUnsignedTicket,addProof,hasCompleteProof,updateStatus,assertBaseline,escapeHTML,badge};
})();
