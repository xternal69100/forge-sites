(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  root.ForgeStore = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  const KEY = 'forge:studio-typographique:demo:v1';
  const STATUSES = ['Nouvelle', 'Vérifiée', 'Archivée'];
  const FAMILIES = [];
  const PACKS = {};
  function baseline() { return { version: 1, orders: [] }; }
  function validOrder(order) {
    return !!order && typeof order.id === 'string' && FAMILIES.includes(order.family) &&
      typeof order.email === 'string' && order.email.endsWith('.test') && order.amountCHF === 0 &&
      STATUSES.includes(order.status) && typeof order.createdAt === 'string';
  }
  function normalise(value) {
    if (!value || value.version !== 1 || !Array.isArray(value.orders) || !value.orders.every(validOrder)) return baseline();
    return { version: 1, orders: value.orders.map(order => ({ ...order })) };
  }
  function memoryStorage(seed) {
    const data = new Map();
    if (seed !== undefined) data.set(KEY, JSON.stringify(seed));
    return { getItem:key => data.has(key) ? data.get(key) : null, setItem:(key,value) => data.set(key,String(value)), removeItem:key => data.delete(key) };
  }
  function create(storage) {
    function save(state) { const clean = normalise(state); storage.setItem(KEY, JSON.stringify(clean)); return clean; }
    function read() {
      try {
        const raw = storage.getItem(KEY);
        if (!raw) return save(baseline());
        const parsed = JSON.parse(raw); const clean = normalise(parsed);
        if (JSON.stringify(parsed) !== JSON.stringify(clean)) save(clean);
        return clean;
      } catch (_) { return save(baseline()); }
    }
    function addOrder(input) {
      const order = { id:String(input.id), createdAt:String(input.createdAt), family:String(input.family), name:String(input.name), email:String(input.email).toLowerCase(), amountCHF:0, status:'Nouvelle', pack:PACKS[input.family] || '' };
      if (!validOrder(order) || !order.pack) throw new Error('Catalogue fermé : aucune édition autorisée');
      const state = read(); state.orders.unshift(order); save(state); return order;
    }
    function updateStatus(id, status) {
      if (!STATUSES.includes(status)) throw new Error('Statut invalide');
      const state = read(); const order = state.orders.find(item => item.id === id);
      if (!order) return null; order.status = status; save(state); return order;
    }
    function reset() { return save(baseline()); }
    return { read, save, addOrder, updateStatus, reset };
  }
  return { KEY, STATUSES, FAMILIES, PACKS, baseline, normalise, memoryStorage, create };
});
