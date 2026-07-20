/* Hack Sentinel — Surveillance Panel */
(function () {
  'use strict';

  const SURVEILLANCE_URL = '../data/surveillance-snapshot.json';
  let currentFilter = 'all';

  function init() {
    document.querySelectorAll('[data-surv-filter]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        document.querySelectorAll('[data-surv-filter]').forEach(function (b) { b.setAttribute('aria-pressed', 'false'); });
        btn.setAttribute('aria-pressed', 'true');
        currentFilter = btn.dataset.survFilter;
        loadSurveillance();
      });
    });
    loadSurveillance();
  }

  function loadSurveillance() {
    var status = document.getElementById('surveillance-status');
    fetch(SURVEILLANCE_URL + '?qa=' + Date.now())
      .then(function (r) { return r.json(); })
      .then(function (data) {
        renderWatchlist(data.watchlist || []);
        renderEvents(data.active_events || []);
        renderTrails(data.recent_trails || []);
        if (status) {
          status.textContent = (data.summary ? data.summary.tokens_under_surveillance : 0) + ' tokens surveillés';
        }
      })
      .catch(function () {
        var tb = document.getElementById('surveillance-body');
        if (tb) tb.innerHTML = '<tr><td colspan="6">Données de surveillance indisponibles (PAPER uniquement)</td></tr>';
      });
  }

  function severityClass(sev) {
    if (sev === 'critical') return 'danger';
    if (sev === 'high') return 'warning';
    return '';
  }

  function statusBadge(status) {
    if (status === 'short_simulated') return '<span class="status warning">SHORT SIMULÉ</span>';
    if (status === 'alert') return '<span class="status danger">ALERTE</span>';
    return '<span class="pill">surveillance</span>';
  }

  function renderWatchlist(tokens) {
    var tbody = document.getElementById('surveillance-body');
    if (!tbody) return;
    var filtered = tokens;
    if (currentFilter === 'alert') filtered = tokens.filter(function (t) { return t.status === 'alert' || t.status === 'short_simulated'; });
    if (currentFilter === 'monitoring') filtered = tokens.filter(function (t) { return t.status === 'monitoring'; });

    if (filtered.length === 0) {
      tbody.innerHTML = '<tr><td colspan="6">Aucun token correspondant au filtre</td></tr>';
      return;
    }

    var html = '';
    filtered.forEach(function (t) {
      var flags = (t.vulnerability_flags || []).map(function (f) { return '<span class="flag-tag">' + f + '</span>'; }).join(' ');
      var scoreClass = t.risk_score >= 80 ? 'danger' : t.risk_score >= 60 ? 'warning' : '';
      html += '<tr class="' + (t.active_events > 0 ? 'row-alert' : '') + '">' +
        '<td><strong>' + t.token + '</strong><br><small>' + t.name + '</small></td>' +
        '<td><span class="' + scoreClass + '">' + t.risk_score + '/100</span></td>' +
        '<td>$' + (t.tvl_billion || 0).toFixed(1) + 'B</td>' +
        '<td>' + (flags || '—') + '</td>' +
        '<td>' + t.active_events + '</td>' +
        '<td>' + statusBadge(t.status) + '</td>' +
        '</tr>';
    });
    tbody.innerHTML = html;
  }

  function renderEvents(events) {
    var tbody = document.getElementById('events-body');
    if (!tbody) return;
    if (events.length === 0) {
      tbody.innerHTML = '<tr><td colspan="6">Aucun événement actif — <em>injecter des simulations via hack_sentinel/event_injector.py</em></td></tr>';
      return;
    }
    var html = '';
    events.forEach(function (e) {
      html += '<tr>' +
        '<td><code>' + (e.event_id || '').substring(0, 8) + '</code></td>' +
        '<td>' + (e.scenario || '') + '</td>' +
        '<td><span class="' + severityClass(e.severity) + '">' + (e.severity || '').toUpperCase() + '</span></td>' +
        '<td><strong>' + (e.token || '') + '</strong></td>' +
        '<td><small>' + (e.injected_at || '').substring(11, 19) + '</small></td>' +
        '<td>' + (e.recommended_action || '') + '</td>' +
        '</tr>';
    });
    tbody.innerHTML = html;
  }

  function renderTrails(trails) {
    var tbody = document.getElementById('trails-body');
    if (!tbody) return;
    if (trails.length === 0) {
      tbody.innerHTML = '<tr><td colspan="6">Aucune piste de décision — <em>exécuter hack_sentinel/decision_engine.py après avoir injecté des événements</em></td></tr>';
      return;
    }
    var html = '';
    trails.forEach(function (t) {
      var pnl = t.estimated_pnl_usdc;
      var pnlStr = pnl !== null && pnl !== undefined ? (pnl > 0 ? '+' : '') + pnl.toFixed(2) + ' USDC' : 'N/A';
      var pnlClass = pnl !== null && pnl !== undefined ? (pnl > 0 ? 'positive' : 'negative') : '';
      html += '<tr>' +
        '<td><code>' + (t.trail_id || '').substring(0, 10) + '</code></td>' +
        '<td><strong>' + (t.token || '') + '</strong></td>' +
        '<td>' + (t.action || '') + '</td>' +
        '<td>' + (t.total_latency_ms || 0) + ' ms</td>' +
        '<td class="' + pnlClass + '">' + pnlStr + '</td>' +
        '<td><span class="pill">' + (t.status || '') + '</span></td>' +
        '</tr>';
    });
    tbody.innerHTML = html;
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
