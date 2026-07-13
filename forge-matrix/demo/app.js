(()=>{'use strict';
const STORE_KEY='forge:forge-matrix:demo:v1';
const STATES=['OBSERVÉ','ÉTUDIÉ','PAPER','PROPOSÉ','AUTORISÉ','EXÉCUTÉ','REJETÉ'];
const experts=['Market Validator','Legal Expert','Fiscal Optimizer','Business Planner','Funding Specialist','Web Builder','Synergy Finder','Quality Guardian'];
const projects=[
 {slug:'piscine-airbnb',name:'Poolbnb Léman',phase:4,status:'active',score:9.615},
 {slug:'hermes-artisan-suisse',name:'Hermes Artisan Suisse',phase:4,status:'mature',score:8.785},
 {slug:'forge-capital',name:'Forge Capital',phase:3,status:'active',score:null,capital:{authorized_usdt:100,received_usdt:0,liquid_usdt:0,invested_usdt:0,committed_usdt:0,net_value_usdt:0}},
 {slug:'forge-matrix',name:'Forge Matrix',phase:1,status:'active',score:null}
];
function clone(value){return JSON.parse(JSON.stringify(value));}
function baseline(){return {version:1,mode:'DÉMO',experts:experts.map((name,i)=>({id:`EXP-${String(i+1).padStart(2,'0')}`,name,mission:'Mission synthétique de démonstration',status:i<3?'EN REVUE':'DISPONIBLE'})),projects:clone(projects),learnings:[{id:'LRN-001',domain:'web',text:'Séparer vitrine, démonstration et administration.',provenance:'DÉMO'},{id:'LRN-002',domain:'preuve',text:'Une exécution exige une référence de preuve non vide.',provenance:'DÉMO'},{id:'LRN-003',domain:'sécurité',text:'L’absence de donnée reste visible ; elle n’est pas comblée.',provenance:'DÉMO'}],transactions:[{id:'TX-DEMO-BASE',title:'Signal de contrôle sans fonds',asset:'Aucun actif',status:'REJETÉ',proofId:'PRF-DEMO-BASE',study:'Capital reçu nul : exécution interdite.',createdAt:'2026-07-13T00:00:00Z',updatedAt:'2026-07-13T00:00:00Z',provenance:'DÉMO'}],journal:[{id:'EVT-DEMO-BASE',at:'2026-07-13T00:00:00Z',type:'RESET_BASELINE',message:'Baseline synthétique chargée',provenance:'DÉMO'}]};}
function valid(store){return store&&store.version===1&&Array.isArray(store.experts)&&Array.isArray(store.projects)&&Array.isArray(store.learnings)&&Array.isArray(store.transactions)&&Array.isArray(store.journal);}
function saveStore(store){localStorage.setItem(STORE_KEY,JSON.stringify(store));window.dispatchEvent(new CustomEvent('forge-matrix-change',{detail:store}));return store;}
function loadStore(){try{const parsed=JSON.parse(localStorage.getItem(STORE_KEY));if(valid(parsed))return parsed;}catch(_error){}return saveStore(baseline());}
function resetStore(){return saveStore(baseline());}
function uid(prefix){return `${prefix}-DEMO-${Date.now().toString(36).toUpperCase()}`;}
function appendEvent(store,type,message,refId=''){store.journal.push({id:uid('EVT'),at:new Date().toISOString(),type,message,refId,provenance:'DÉMO'});return store;}
function getTransaction(store,id){const item=store.transactions.find(row=>row.id===id);if(!item)throw new Error('Signal introuvable');return item;}
function createSignal({title,asset}){const store=loadStore();const now=new Date().toISOString();const item={id:uid('TX'),title:String(title||'Signal synthétique').trim(),asset:String(asset||'Aucun actif').trim(),status:'OBSERVÉ',proofId:'',study:'',createdAt:now,updatedAt:now,provenance:'DÉMO'};store.transactions.unshift(item);appendEvent(store,'SIGNAL_OBSERVÉ','Signal synthétique créé',item.id);saveStore(store);return item;}
function studySignal(id,note){const store=loadStore(),item=getTransaction(store,id);item.status='ÉTUDIÉ';item.study=String(note||'Étude synthétique terminée.').trim();item.updatedAt=new Date().toISOString();appendEvent(store,'SIGNAL_ÉTUDIÉ','Étude synthétique ajoutée',id);saveStore(store);return item;}
function decideSignal(id,status){if(!['PAPER','REJETÉ'].includes(status))throw new Error('La démo décide uniquement PAPER ou REJETÉ');const store=loadStore(),item=getTransaction(store,id);item.status=status;item.updatedAt=new Date().toISOString();appendEvent(store,`DÉCISION_${status}`,`Décision ${status} enregistrée`,id);saveStore(store);return item;}
function addProof(id,label='Preuve de démonstration'){const store=loadStore(),item=getTransaction(store,id);item.proofId=uid('PRF');item.proofLabel=String(label).trim();item.updatedAt=new Date().toISOString();appendEvent(store,'PREUVE_AJOUTÉE','Référence de preuve synthétique ajoutée',id);saveStore(store);return item;}
function updateStatus(id,status){if(!STATES.includes(status))throw new Error('Statut invalide');const store=loadStore(),item=getTransaction(store,id);if(status==='EXÉCUTÉ'&&!String(item.proofId||'').trim())throw new Error('EXÉCUTÉ exige un proofId non vide');item.status=status;item.updatedAt=new Date().toISOString();appendEvent(store,'STATUT_MODIFIÉ',`Statut passé à ${status}`,id);saveStore(store);return item;}
function assertBaseline(){const store=loadStore();return {ok:store.transactions.length===1&&store.transactions[0].id==='TX-DEMO-BASE'&&store.journal.length===1,transactions:store.transactions.length,journal:store.journal.length};}
function escapeHTML(value){return String(value??'').replace(/[&<>"']/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));}
function badge(status){return `<span class="badge ${escapeHTML(status)}">${escapeHTML(status)}</span>`;}
window.ForgeMatrix={STORE_KEY,STATES,baseline,loadStore,saveStore,resetStore,appendEvent,createSignal,studySignal,decideSignal,addProof,updateStatus,assertBaseline,escapeHTML,badge};
})();