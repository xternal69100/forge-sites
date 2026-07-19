(()=>{'use strict';
const SNAPSHOT='../data/public-snapshot.json';
const HYPERLIQUID='https://api.hyperliquid.xyz/info';
const esc=value=>window.ForgeCapitalMatrix?.escapeHTML(value)??String(value??'').replace(/[&<>"']/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
const money=value=>new Intl.NumberFormat('fr-CH',{maximumFractionDigits:2}).format(Number(value||0));
const number=value=>new Intl.NumberFormat('fr-CH',{maximumFractionDigits:2}).format(Number(value||0));
const statusClass=status=>status==='ARRÊTÉE'||status==='ÉCHEC'||status==='BLOQUÉ'?'danger':status==='CORRIGÉ'?'success':status==='EN CONSTRUCTION'||status==='SPÉCIFIÉE'?'info':'warning';
let tactics=[];

function renderSummary(human,payload){
  document.querySelector('#activation-reason').textContent=human.activation.reason;
  document.querySelector('#activation-verdict').textContent=human.activation.verdict;
  document.querySelector('#activation-champion').textContent=human.activation.champion;
  document.querySelector('#capital-autorise').innerHTML=`${money(human.money.authorizedUsdt)} <small>USDT</small>`;
  document.querySelector('#capital-reel').innerHTML=`${money(human.money.observedOnConfiguredAccountUsdt)} <small>USDT</small>`;
  document.querySelector('#project-quality').innerHTML=`${number(human.scores.projectQuality)} <small>/ 10</small>`;
  document.querySelector('#trading-readiness').innerHTML=`${number(human.scores.tradingReadiness)} <small>/ 10</small>`;
  document.querySelector('#snapshot-date').textContent=`Actualisé le ${new Date(payload.generatedAt).toLocaleString('fr-CH',{dateStyle:'medium',timeStyle:'short'})}`;
  document.querySelector('#source-refs').textContent=`Sources : ${human.sourceRefs.join(' · ')}`;
}

function renderTactics(filter='all'){
  const visible=tactics.filter(item=>filter==='all'||(filter==='stopped'?item.status==='ARRÊTÉE':item.status!=='ARRÊTÉE'));
  document.querySelector('#tactics-count').textContent=`${visible.length} tactique${visible.length>1?'s':''}`;
  document.querySelector('#tactics-list').innerHTML=visible.map(item=>`
    <article class="tactic-row">
      <span class="tactic-id">${esc(item.id)}</span>
      <div class="tactic-name"><strong>${esc(item.name)}</strong><small>${esc(item.category)}</small></div>
      <span class="status ${statusClass(item.status)}">${esc(item.status)}</span>
      <div class="tactic-summary">${esc(item.result)}</div>
      <button class="detail-button" type="button" data-tactic="${esc(item.id)}" aria-label="Voir le détail de ${esc(item.name)}">→</button>
    </article>`).join('')||'<p class="truth-note">Aucune tactique dans ce filtre.</p>';
  document.querySelectorAll('[data-tactic]').forEach(button=>button.addEventListener('click',()=>openTactic(button.dataset.tactic)));
}

function openTactic(id){
  const item=tactics.find(row=>row.id===id); if(!item)return;
  document.querySelector('#tactic-dialog-title').textContent=item.name;
  document.querySelector('#tactic-dialog-body').innerHTML=`
    <div class="detail-grid">
      <div class="detail-block"><span>Statut</span><strong>${esc(item.status)}</strong></div>
      <div class="detail-block"><span>Catégorie</span><strong>${esc(item.category)}</strong></div>
      <div class="detail-block"><span>Preuve actuelle</span><strong>${esc(item.evidence)}</strong></div>
      <div class="detail-block"><span>Conclusion</span><strong>${esc(item.result)}</strong></div>
    </div>
    <div class="detail-next"><strong>Étape suivante :</strong> ${esc(item.next)}</div>
    <p class="kpi-note">Éligible au live : non. Ce détail ne constitue ni un signal ni un conseil d’investissement.</p>`;
  document.querySelector('#tactic-dialog').showModal();
}

function renderGates(rows){
  document.querySelector('#activation-gates').innerHTML=rows.map((gate,index)=>`
    <article class="gate-row">
      <span class="gate-number">${index+1}</span>
      <div class="gate-label">${esc(gate.label)}</div>
      <span class="status ${statusClass(gate.state)}">${esc(gate.state)}</span>
      <div class="gate-reason">${esc(gate.reason)}<span class="gate-proof">Preuve : ${esc(gate.evidence)}</span></div>
    </article>`).join('');
}

function renderRemediations(rows){
  document.querySelector('#remediations').innerHTML=rows.map(row=>`
    <div class="remediation"><span class="remediation-id">${esc(row.id)}</span><strong>${esc(row.label)}</strong><span class="status ${statusClass(row.state)}">${esc(row.state)}</span><p>${esc(row.proof)}</p></div>`).join('');
}

function renderLearnings(reports){
  const selected=reports.filter(row=>['LR-25','LR-26','LR-27','LR-28'].includes(row.id));
  document.querySelector('#learning-reports').innerHTML=selected.map(row=>`
    <article class="card learning-card">
      <span class="status ${row.classification==='VETO'?'danger':'warning'}">${esc(row.classification)}</span>
      <h3>${esc(row.title)}</h3>
      <p>${esc(row.conclusion)}</p>
      <div class="proof">${esc(row.costs)} · ${esc(row.proof)}</div>
    </article>`).join('');
}

function renderActions(rows){
  document.querySelector('#next-actions').innerHTML=rows.map(row=>`
    <article class="action-row"><span class="action-number">${String(row.order).padStart(2,'0')}</span><strong>${esc(row.label)}</strong><p>${esc(row.why)}</p></article>`).join('');
}

async function loadSnapshot(){
  const response=await fetch(SNAPSHOT,{cache:'no-store'}); if(!response.ok)throw new Error(`snapshot ${response.status}`);
  const payload=await response.json();
  if(payload.release!=='clair-capital-v2'||!payload.humanDashboard)throw new Error('Snapshot incompatible');
  const human=payload.humanDashboard; tactics=human.tactics;
  renderSummary(human,payload); renderTactics(); renderGates(human.activationGates); renderRemediations(human.remediations); renderLearnings(payload.learningReports); renderActions(human.nextActions);
  document.querySelector('#snapshot-freshness').innerHTML='<span class="pill-dot"></span>Snapshot vérifié';
}

async function loadMarket(){
  try{
    const response=await fetch(HYPERLIQUID,{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({type:'allMids'}),cache:'no-store'});
    if(!response.ok)throw new Error(`HTTP ${response.status}`);
    const mids=await response.json();
    for(const coin of ['BTC','ETH','SOL']){
      const card=document.querySelector(`[data-coin="${coin}"]`),value=Number(mids[coin]);
      if(!card||!Number.isFinite(value)||value<=0)throw new Error(`Prix ${coin} absent`);
      card.querySelector('[data-mid]').textContent=new Intl.NumberFormat('fr-CH',{style:'currency',currency:'USD',maximumFractionDigits:value>1000?0:2}).format(value);
      card.querySelector('[data-freshness]').textContent='PRIX PUBLIC HYPERLIQUID · LECTURE SEULE';
    }
  }catch(error){
    document.querySelectorAll('[data-coin]').forEach(card=>{card.querySelector('[data-mid]').textContent='Indisponible';card.querySelector('[data-freshness]').textContent='DIFFÉRÉ · aucune valeur conservée';});
    console.warn('Observation Hyperliquid indisponible',error);
  }
}

document.addEventListener('DOMContentLoaded',()=>{
  document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('[data-filter]').forEach(item=>item.setAttribute('aria-pressed','false'));button.setAttribute('aria-pressed','true');renderTactics(button.dataset.filter);}));
  document.querySelector('[data-close-dialog]').addEventListener('click',()=>document.querySelector('#tactic-dialog').close());
  loadSnapshot().catch(error=>{document.querySelector('#snapshot-freshness').textContent='Snapshot indisponible';console.error(error);});
  loadMarket();
});
})();
