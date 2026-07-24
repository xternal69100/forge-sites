(() => {
  'use strict';

  const KEY = 'forge:stack-pme:demo:v1';
  const VALID_STATUSES = new Set(['a-revoir', 'archive']);

  function baseline() {
    return { version: 1, requests: [], journal: [] };
  }

  function normalize(candidate) {
    if (!candidate || candidate.version !== 1 || !Array.isArray(candidate.requests) || !Array.isArray(candidate.journal)) {
      return baseline();
    }
    const requests = candidate.requests.filter(item => (
      item && typeof item.id === 'string' && typeof item.scenario === 'string' &&
      ['5', '20', '50'].includes(item.team) && ['choisir', 'deployer', 'quitter'].includes(item.decision) &&
      VALID_STATUSES.has(item.status)
    ));
    const journal = candidate.journal.filter(item => item && typeof item.at === 'string' && typeof item.action === 'string');
    return { version: 1, requests, journal };
  }

  function write(state) {
    const safe = normalize(state);
    window.localStorage.setItem(KEY, JSON.stringify(safe));
    return safe;
  }

  function read() {
    try {
      const raw = window.localStorage.getItem(KEY);
      return raw ? write(JSON.parse(raw)) : write(baseline());
    } catch (_error) {
      return write(baseline());
    }
  }

  function reset() {
    return write(baseline());
  }

  function createRequest(input) {
    const state = read();
    const now = new Date().toISOString();
    const id = `SP-DEMO-${Date.now().toString(36).toUpperCase()}`;
    const request = {
      id,
      scenario: input.scenario.trim(),
      team: input.team,
      decision: input.decision,
      status: 'a-revoir',
      createdAt: now,
    };
    state.requests.push(request);
    state.journal.push({ at: now, action: 'request-created', requestId: id });
    write(state);
    return request;
  }

  function updateStatus(id, status) {
    if (!VALID_STATUSES.has(status)) return read();
    const state = read();
    const request = state.requests.find(item => item.id === id);
    if (!request) return state;
    request.status = status;
    state.journal.push({ at: new Date().toISOString(), action: `status-${status}`, requestId: id });
    return write(state);
  }

  window.StackPMEDemo = Object.freeze({ KEY, baseline, read, reset, createRequest, updateStatus });
})();
