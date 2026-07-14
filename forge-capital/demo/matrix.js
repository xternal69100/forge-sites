(()=>{'use strict';
const SNAPSHOT='../data/public-snapshot.json';
const HYPERLIQUID='https://api.hyperliquid.xyz/info';
const COINS=['BTC','ETH','SOL'];
const CLASS_LABELS=['TRACE D’APPRENTISSAGE','PAPER','RESEARCH','VETO','NOOP'];
const state={snapshot:null,events:[],paused:false};
const $=selector=>document.querySelector(selector);
const esc=value=>window.ForgeCapitalMatrix.escapeHTML(value);
const unique=(rows,key)=>[...new Set(rows.map(row=>String(row[key]||'')).filter(Boolean))].sort((a,b)=>a.localeCompare(b,'fr'));
const formatPrice=value=>{const number=Number(value);return Number.isFinite(number)?number.toLocaleString('fr-CH',{minimumFractionDigits:number<100?2:1,maximumFractionDigits:number<100?4:1}):'—'};
function setOptions(selector,values){const select=$(selector),first=select.options[0].outerHTML;select.innerHTML=first+values.map(value=>`<option value="${esc(value)}">${esc(value)}</option>`).join('');}
function marketFallback(reason){
  $('#market-status').className='tag delayed';$('#market-status').innerHTML='<span class="dot"></span>DIFFÉRÉ · LIVE INDISPONIBLE';
  $('#market-time').textContent=`Fallback différé honnête · ${reason}`;$('#hl-health').className='tag delayed';$('#hl-health').textContent='INDISPONIBLE';
  COINS.forEach(coin=>{const ticker=document.querySelector(`[data-coin="${coin}"]`),book=document.querySelector(`[data-book="${coin}"]`);ticker.querySelector('[data-mid]').textContent='—';ticker.querySelector('[data-freshness]').textContent='DIFFÉRÉ';book.querySelector('[data-bid]').textContent='—';book.querySelector('[data-ask]').textContent='—';});
}
async function loadMarket(){
  const post=body=>fetch(HYPERLIQUID,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}).then(response=>{if(!response.ok)throw new Error(`HTTP ${response.status}`);return response.json();});
  try{
    const [mids,...books]=await Promise.all([post({type:'allMids'}),...COINS.map(coin=>post({type:'l2Book',coin}))]);
    const observedAt=new Date();
    COINS.forEach((coin,index)=>{const levels=books[index]?.levels,ticker=document.querySelector(`[data-coin="${coin}"]`),book=document.querySelector(`[data-book="${coin}"]`);if(!mids[coin]||!levels?.[0]?.[0]?.px||!levels?.[1]?.[0]?.px)throw new Error(`book ${coin} incomplet`);ticker.querySelector('[data-mid]').textContent=formatPrice(mids[coin]);ticker.querySelector('[data-freshness]').textContent='ON-CHAIN LIVE';book.querySelector('[data-bid]').textContent=formatPrice(levels[0][0].px);book.querySelector('[data-ask]').textContent=formatPrice(levels[1][0].px);});
    $('#market-status').className='tag live';$('#market-status').innerHTML='<span class="dot"></span>ON-CHAIN LIVE';$('#market-time').textContent=`${observedAt.toLocaleString('fr-CH')} · ${observedAt.toISOString()}`;$('#hl-health').className='tag live';$('#hl-health').textContent='HTTP SUCCESS';
  }catch(error){marketFallback(error.message);}
}
function traceMarkup(item){return `<article class="trace-row trace-${esc(item.classification.toLowerCase().replace(/[^a-z]+/g,'-'))}"><span class="trace-seq">${String(item.sequence).padStart(2,'0')}</span><span class="trace-class">${esc(item.displayLabel)}</span><span class="trace-role">${esc(item.role)}</span><span class="trace-method">${esc(item.method)}</span><span class="trace-status">${esc(item.status)}</span><span class="trace-message">${esc(item.message)}</span><span class="trace-source">${esc(item.sourceAlias)} · ${esc(item.proofLevel)} · ${esc(item.freshnessState)}</span></article>`;}
function filteredTape(){const role=$('#tape-role').value,method=$('#tape-method').value,status=$('#tape-status').value;return state.events.filter(item=>(!role||item.role===role)&&(!method||item.method===method)&&(!status||item.status===status));}
function renderTape(){
  const rows=filteredTape(),track=$('#tape-track');$('#tape-count').textContent=`${rows.length} / ${state.events.length} ARTEFACTS`;
  if(!rows.length){track.innerHTML='<p class="muted">Aucune trace dans ce filtre.</p>';track.classList.remove('is-scrolling');return;}
  const group=`<div class="tape-group">${rows.map(traceMarkup).join('')}</div>`;
  track.innerHTML=group+`<div class="tape-group tape-clone" aria-hidden="true">${rows.map(traceMarkup).join('')}</div>`;
  track.classList.toggle('is-scrolling',rows.length>4);track.classList.toggle('tape-paused',state.paused);
}
function renderReports(reports){
  $('#report-grid').innerHTML=reports.map(report=>`<article class="report-card"><div class="report-top"><span class="tag ${report.classification==='VETO'?'veto':'noop'}">${esc(report.classification)}</span><span>${esc(report.source)}</span></div><h3>${esc(report.title)}</h3><p>${esc(report.conclusion)}</p><dl><div><dt>MÉTHODE</dt><dd>${esc(report.method)}</dd></div><div><dt>TRADES</dt><dd>${report.trades===null?'NON DISPONIBLE':esc(report.trades)}</dd></div></dl><button class="secondary compact-button" type="button" data-report="${esc(report.id)}">OUVRIR LA PREUVE</button></article>`).join('');
  document.querySelectorAll('[data-report]').forEach(button=>button.addEventListener('click',()=>openReport(reports.find(report=>report.id===button.dataset.report))));
}
function openReport(report){if(!report)return;const gates=report.gates.map(gate=>`<li><span>${esc(gate.name)}</span><strong class="${gate.outcome==='PASS'?'ok':'bad'}">${esc(gate.outcome)}</strong></li>`).join('');$('#drawer-content').innerHTML=`<h2 id="drawer-title">${esc(report.title)}</h2><p class="drawer-lead">${esc(report.conclusion)}</p><dl class="evidence-grid"><div><dt>SOURCE</dt><dd>${esc(report.source)}</dd></div><div><dt>CLASSIFICATION</dt><dd>${esc(report.classification)}</dd></div><div><dt>DATASET</dt><dd>${esc(report.dataset)}</dd></div><div><dt>FENÊTRE</dt><dd>${esc(report.window)}</dd></div><div><dt>COÛTS / STRESS</dt><dd>${esc(report.costs)}</dd></div><div><dt>BENCHMARK</dt><dd>${esc(report.benchmark)}</dd></div><div><dt>TRADES</dt><dd>${report.trades===null?'Non disponible dans la source':esc(report.trades)}</dd></div><div><dt>PREUVE GÉNÉRIQUE</dt><dd>${esc(report.proof)}</dd></div></dl><h3>GATES</h3><ul class="gate-list">${gates}</ul>`;$('#report-drawer').showModal();}
function renderMethods(methods){$('#method-lab').innerHTML=methods.map(item=>`<article class="method-step"><span>${esc(item.step)}</span><div><h3>${esc(item.name)}</h3><p>${esc(item.human)}</p><small>${esc(item.source)}</small></div></article>`).join('');}
function renderAgents(activity){$('#agent-mesh').innerHTML=activity.map((item,index)=>`<article class="mesh-row"><span class="mesh-index">${String(index+1).padStart(2,'0')}</span><div><strong>${esc(item.role)}</strong><small>${esc(item.latestArtifact)} · ${esc(item.source)}</small></div><span class="mesh-state state-${esc(item.state.toLowerCase().replace(/[^a-z]+/g,'-'))}">${esc(item.state)}</span></article>`).join('');}
function renderDecision(decision){const fill=(selector,rows)=>{$(selector).innerHTML=rows.map(row=>`<li>${esc(row)}</li>`).join('');};fill('#learned-list',decision.learned);fill('#failed-list',decision.failed);fill('#next-list',decision.next);}
function renderRuntime(runtime){$('#runtime-gate').innerHTML=`<div><dt>MODE</dt><dd>${esc(runtime.mode)}</dd></div><div><dt>STATUT</dt><dd>${esc(runtime.status)}</dd></div><div><dt>Experiment Runner</dt><dd>${esc(runtime.experimentRunner)}</dd></div><div><dt>Tokens scheduler</dt><dd>${esc(runtime.schedulerTokenUsage)}</dd></div>${runtime.missingProofs.map(item=>`<div><dt>PREUVE MANQUANTE</dt><dd>${esc(item)}</dd></div>`).join('')}`;}
async function loadSnapshot(){
  try{
    const response=await fetch(SNAPSHOT,{cache:'no-store'});if(!response.ok)throw new Error(`HTTP ${response.status}`);const snapshot=await response.json();if(snapshot.release!=='matrix-learning-v1')throw new Error('release inattendue');
    state.snapshot=snapshot;state.events=snapshot.strategyTape;setOptions('#tape-role',unique(state.events,'role'));setOptions('#tape-method',unique(state.events,'method'));setOptions('#tape-status',unique(state.events,'status'));
    renderTape();renderReports(snapshot.learningReports);renderMethods(snapshot.methodology);renderAgents(snapshot.agentActivity);renderDecision(snapshot.decisionSynthesis);renderRuntime(snapshot.runtimeGate);
    $('#snapshot-health').className='tag live';$('#snapshot-health').textContent='SNAPSHOT OK';$('#snapshot-provenance').textContent=`${snapshot.release} · ${snapshot.generatedAt} · ${snapshot.provenance}`;
    $('#agent-source-health').textContent=`Roster documenté par les rapports 44–45, pas un flux terminal. Collecte différée ${snapshot.agentCell.sourceSummary.httpSuccess}/${snapshot.agentCell.sourceSummary.expected} HTTP ; elle n’implique ni edge ni performance.`;
  }catch(error){$('#snapshot-health').className='tag delayed';$('#snapshot-health').textContent='INDISPONIBLE';$('#snapshot-provenance').textContent=`Snapshot public indisponible · ${error.message}`;}
}
function bindControls(){['#tape-role','#tape-method','#tape-status'].forEach(selector=>$(selector).addEventListener('change',renderTape));$('#tape-pause').addEventListener('click',event=>{state.paused=!state.paused;event.currentTarget.textContent=state.paused?'REPRENDRE':'PAUSE';event.currentTarget.setAttribute('aria-pressed',String(state.paused));renderTape();});const reduced=window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;if(reduced){state.paused=true;$('#tape-pause').textContent='REPRENDRE';$('#tape-pause').setAttribute('aria-pressed','true');}}
document.addEventListener('DOMContentLoaded',()=>{bindControls();void Promise.all([loadSnapshot(),loadMarket()]);});
void CLASS_LABELS;
})();
