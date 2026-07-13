(() => {
  'use strict';
  const store = ForgeStore.create(localStorage);
  const form = document.querySelector('#openForm');
  let current = 1;
  function showStep(step) {
    current = step;
    document.querySelectorAll('.step').forEach(item => item.classList.toggle('active', Number(item.dataset.step) === step));
    document.querySelectorAll('[data-step-indicator]').forEach(item => item.classList.toggle('active', Number(item.dataset.stepIndicator) <= step));
    const heading = document.querySelector(`[data-step="${step}"] h2`);
    if (heading) { heading.tabIndex = -1; heading.focus(); }
  }
  function chosenFamily() { return form.querySelector('input[name="family"]:checked')?.value || ''; }
  function familyValid() { const ok = Boolean(chosenFamily()); document.querySelector('#familyError').textContent = ok ? '' : 'Choisissez une famille.'; return ok; }
  function contactValid() {
    const name = document.querySelector('#name'); const email = document.querySelector('#email');
    const okName = name.value.trim().length >= 2; const okEmail = /^[^\s@]+@[^\s@]+\.test$/i.test(email.value.trim());
    name.setAttribute('aria-invalid', String(!okName)); email.setAttribute('aria-invalid', String(!okEmail));
    document.querySelector('#emailError').textContent = okEmail ? '' : 'Utilisez une adresse fictive se terminant par .test.';
    if (!okName) name.focus(); else if (!okEmail) email.focus();
    return okName && okEmail;
  }
  function renderSummary() { document.querySelector('#summaryFamily').textContent = `${chosenFamily()} — paquet TTF + OTF + WOFF2`; }
  document.querySelectorAll('.next').forEach(button => button.addEventListener('click', () => {
    if (current === 1 && !familyValid()) return;
    if (current === 2 && !contactValid()) return;
    if (Number(button.dataset.next) === 3) renderSummary();
    showStep(Number(button.dataset.next));
  }));
  document.querySelectorAll('.back').forEach(button => button.addEventListener('click', () => showStep(Number(button.dataset.back))));
  document.querySelector('#email').addEventListener('input', contactValid);
  form.addEventListener('submit', event => {
    event.preventDefault();
    const consent = document.querySelector('#consent');
    if (!consent.checked) { document.querySelector('#consentError').textContent = 'Confirmez la lecture des conditions de démonstration.'; consent.focus(); return; }
    document.querySelector('#consentError').textContent = '';
    const now = new Date(); const ref = `OE-DEMO-${now.getTime().toString(36).toUpperCase()}`; const family = chosenFamily();
    const order = store.addOrder({ id:ref, createdAt:now.toISOString(), family, name:document.querySelector('#name').value.trim(), email:document.querySelector('#email').value.trim() });
    document.querySelector('#confirmationRef').textContent = order.id;
    document.querySelector('#downloadLink').href = order.pack;
    form.hidden = true; showStep(4);
  });
  document.querySelector('#newOrder').addEventListener('click', () => { form.reset(); form.hidden = false; document.querySelector('#name').value = 'Camille Exemple'; document.querySelector('#email').value = 'camille@example.test'; showStep(1); });
  const requested = new URLSearchParams(location.search).get('family');
  if (ForgeStore.FAMILIES.includes(requested)) { const radio = [...form.elements.family].find(item => item.value === requested); if (radio) radio.checked = true; }
  store.read();
})();
