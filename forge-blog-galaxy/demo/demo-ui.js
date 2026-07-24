(() => {
  'use strict';

  const byId = id => document.getElementById(id);
  const escapeHtml = value => String(value).replace(/[&<>"']/g, character => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[character]));
  const labels = { choisir: 'Choisir', deployer: 'Déployer', quitter: 'Quitter', 'a-revoir': 'À revoir', archive: 'Archivé' };

  function customer() {
    const form = byId('scenario-form');
    const checkout = byId('checkout');
    const confirmation = byId('confirmation');
    form.addEventListener('submit', event => {
      event.preventDefault();
      const data = new FormData(form);
      checkout.hidden = false;
      checkout.dataset.team = data.get('team');
      byId('checkout-details').textContent = `Équipe de ${data.get('team')} personnes · priorité : ${labels[data.get('decision')]}.`;
    });
    byId('confirm-order').addEventListener('click', () => {
      const data = new FormData(form);
      const request = window.StackPMEDemo.createRequest({ scenario: data.get('scenario'), team: data.get('team'), decision: data.get('decision') });
      byId('reference').textContent = request.id;
      checkout.hidden = true;
      confirmation.hidden = false;
      form.querySelectorAll('button, input, select').forEach(control => { control.disabled = true; });
    });
  }

  function admin() {
    const list = byId('admin-requests');
    const statusFilter = byId('status-filter');
    const search = byId('search');
    const empty = byId('empty-state');
    function render() {
      const state = window.StackPMEDemo.read();
      const filter = statusFilter.value;
      const query = search.value.trim().toLocaleLowerCase('fr');
      const requests = state.requests.filter(request => (filter === 'all' || request.status === filter) && request.scenario.toLocaleLowerCase('fr').includes(query));
      byId('request-count').textContent = String(state.requests.length);
      byId('archived-count').textContent = String(state.requests.filter(request => request.status === 'archive').length);
      empty.hidden = requests.length !== 0;
      list.innerHTML = requests.map(request => `<article class="request-row"><div><strong>${escapeHtml(request.scenario)}</strong><br><span>${escapeHtml(request.id)} · ${escapeHtml(request.team)} personnes · ${escapeHtml(labels[request.decision])}</span></div><div><span class="chip ${request.status === 'archive' ? 'chip-sourced' : 'chip-review'}">${escapeHtml(labels[request.status])}</span>${request.status === 'a-revoir' ? ` <button type="button" class="button button-secondary" data-archive="${escapeHtml(request.id)}">Archiver</button>` : ''}</div></article>`).join('');
      list.querySelectorAll('[data-archive]').forEach(button => button.addEventListener('click', () => { window.StackPMEDemo.updateStatus(button.dataset.archive, 'archive'); statusFilter.value = 'all'; render(); }));
    }
    statusFilter.addEventListener('change', render);
    search.addEventListener('input', render);
    byId('reset-demo').addEventListener('click', () => byId('reset-dialog').showModal());
    byId('cancel-reset').addEventListener('click', () => byId('reset-dialog').close());
    byId('confirm-reset').addEventListener('click', () => { window.StackPMEDemo.reset(); byId('reset-dialog').close(); search.value = ''; statusFilter.value = 'all'; render(); });
    render();
  }

  if (document.body.dataset.page === 'customer') customer();
  if (document.body.dataset.page === 'admin') admin();
})();
