(() => {
  'use strict';
  const store = ForgeStore.create(localStorage);
  const body = document.querySelector('#ordersBody'); const detail = document.querySelector('#orderDetail');
  const search = document.querySelector('#searchOrders'); const statusFilter = document.querySelector('#statusFilter'); const familyFilter = document.querySelector('#familyFilter');
  let selectedId = null;
  function esc(value) { const span = document.createElement('span'); span.textContent = String(value); return span.innerHTML; }
  function filtered(orders) { const query = search.value.trim().toLocaleLowerCase('fr'); return orders.filter(order => (!query || `${order.id} ${order.name} ${order.email}`.toLocaleLowerCase('fr').includes(query)) && (statusFilter.value === 'all' || order.status === statusFilter.value) && (familyFilter.value === 'all' || order.family === familyFilter.value)); }
  function badge(status) { return `<span class="pill ${status === 'Vérifiée' ? 'success' : ''}">${esc(status)}</span>`; }
  function renderDetail(order) {
    if (!order) { detail.innerHTML = '<div class="eyebrow">Détail</div><h2>Sélectionnez une référence</h2><p class="muted">Son statut et son paquet apparaîtront ici.</p>'; return; }
    detail.innerHTML = `<div class="eyebrow">Référence fictive</div><h2>${esc(order.id)}</h2><dl><dt>Famille</dt><dd>${esc(order.family)}</dd><dt>Contact</dt><dd>${esc(order.name)}</dd><dt>Courriel</dt><dd>${esc(order.email)}</dd><dt>Montant</dt><dd>CHF 0</dd><dt>Créée</dt><dd>${esc(new Date(order.createdAt).toLocaleString('fr-CH'))}</dd></dl><div class="field" style="margin-top:18px"><label for="detailStatus">Statut</label><select id="detailStatus">${ForgeStore.STATUSES.map(status => `<option ${status === order.status ? 'selected' : ''}>${esc(status)}</option>`).join('')}</select></div><p>${badge(order.status)}</p><a class="button" href="${esc(order.pack)}" download>Télécharger le ZIP</a>`;
    detail.querySelector('#detailStatus').addEventListener('change', event => { store.updateStatus(order.id, event.target.value); render(); });
  }
  function render() {
    const state = store.read(); const orders = filtered(state.orders);
    document.querySelector('#kpiOrders').textContent = state.orders.length; document.querySelector('#kpiValue').textContent = 'CHF 0';
    document.querySelector('#kpiNew').textContent = state.orders.filter(order => order.status === 'Nouvelle').length;
    document.querySelector('#kpiFamilies').textContent = new Set(state.orders.map(order => order.family)).size;
    document.querySelector('#visibleCount').textContent = `${orders.length} résultat${orders.length > 1 ? 's' : ''}`; body.textContent = '';
    orders.forEach(order => { const row = document.createElement('tr'); row.tabIndex = 0; row.classList.toggle('selected', order.id === selectedId); row.innerHTML = `<td><strong>${esc(order.id)}</strong></td><td>${esc(order.name)}<br><small class="muted">${esc(order.email)}</small></td><td>${esc(order.family)}</td><td>CHF 0</td><td>${badge(order.status)}</td>`; const select = () => { selectedId = order.id; render(); }; row.addEventListener('click', select); row.addEventListener('keydown', event => { if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); select(); } }); body.append(row); });
    document.querySelector('#emptyOrders').hidden = orders.length > 0; const selected = state.orders.find(order => order.id === selectedId); if (!selected) selectedId = null; renderDetail(selected || null);
  }
  [search,statusFilter,familyFilter].forEach(control => control.addEventListener(control === search ? 'input' : 'change', render));
  const dialog = document.querySelector('#resetDialog'); const resetBtn = document.querySelector('#resetBtn');
  resetBtn.addEventListener('click', () => dialog.showModal()); dialog.querySelector('.close').addEventListener('click', () => dialog.close()); dialog.querySelector('.cancel-reset').addEventListener('click', () => dialog.close());
  dialog.querySelector('.confirm-reset').addEventListener('click', () => { store.reset(); selectedId = null; search.value = ''; statusFilter.value = 'all'; familyFilter.value = 'all'; dialog.close(); render(); const status = document.querySelector('#resetStatus'); status.textContent = 'Démonstration réinitialisée : 0 référence, CHF 0.'; status.focus(); });
  dialog.addEventListener('close', () => { if (!document.querySelector('#resetStatus').textContent) resetBtn.focus(); }); window.addEventListener('storage', event => { if (event.key === ForgeStore.KEY) render(); }); render();
})();
