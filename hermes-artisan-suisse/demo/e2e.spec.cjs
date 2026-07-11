const { test, expect } = require('@playwright/test');

const origin = process.env.DEMO_ORIGIN || 'http://127.0.0.1:8765';
const key = 'forge:hermes-artisan-suisse:demo:v1';
const empty = {version:1,subscriptions:[],workflows:[],tasks:[],approvals:[],journal:[]};

test.use({ viewport: { width: 390, height: 844 } });

test('parcours client/admin complet à 390 px', async ({ page }) => {
  const errors = [];
  const paymentRequests = [];
  page.on('pageerror', error => errors.push(`pageerror: ${error.message}`));
  page.on('console', message => { if (message.type() === 'error') errors.push(`console: ${message.text()}`); });
  page.on('request', request => { if (/stripe|paypal|twint|adyen/i.test(request.url())) paymentRequests.push(request.url()); });

  await page.goto(`${origin}/demo/admin.html`);
  await page.evaluate(({key, empty}) => localStorage.setItem(key, JSON.stringify(empty)), {key, empty});
  await page.reload();
  await expect(page.locator('#resultCount')).toHaveText('0 pilotes affichés sur 0');

  await page.goto(`${origin}/demo/`);
  await page.getByRole('button', {name:'Configurer ce pilote'}).click();
  await page.locator('#email').fill('client@example.com');
  await page.getByRole('button', {name:'Vérifier le récapitulatif'}).click();
  await expect(page.locator('#email')).toHaveAttribute('aria-invalid', 'true');
  await expect(page.locator('[data-error="email"]')).toContainText('.test');

  await page.locator('#email').fill('client@atelier.test');
  await page.getByRole('button', {name:'Vérifier le récapitulatif'}).click();
  await expect(page.getByText('SIMULATION DE CHECKOUT — PAS DE CARTE, PAS DE DÉBIT, PAS DE FACTURE')).toBeVisible();
  await page.locator('#demoConsent').check();
  await page.locator('#confirmButton').click();
  await expect(page.getByRole('heading', {name:'Votre espace de pilotage est prêt.'})).toBeVisible();
  await expect(page.locator('#activationCard')).toContainText('CHF 3’700 · paiement simulé');

  await page.getByRole('link', {name:'Voir le pilote dans l’espace équipe'}).click();
  await expect(page.locator('#resultCount')).toHaveText('1 pilote affiché sur 1');
  await expect(page.locator('#detail')).toContainText('SIMULÉ — AUCUN DÉBIT');
  await expect(page.locator('#journal')).toContainText('paiement simulé, aucun débit');
  await page.reload();
  await expect(page.locator('#resultCount')).toHaveText('1 pilote affiché sur 1');

  await page.locator('#detailStatus').selectOption('EN_PAUSE_SIMULÉE');
  await page.reload();
  await expect(page.locator('#detailStatus')).toHaveValue('EN_PAUSE_SIMULÉE');
  await expect(page.locator('#journal')).toContainText('Statut du pilote changé vers En pause simulée');

  await page.locator('#search').fill('introuvable');
  await expect(page.locator('#resultCount')).toHaveText('0 pilotes affichés sur 1');
  await page.locator('#search').fill('Atelier');
  await page.locator('#statusFilter').selectOption('ACTIF_SIMULÉ');
  await expect(page.locator('#resultCount')).toHaveText('0 pilotes affichés sur 1');
  await page.locator('#statusFilter').selectOption('EN_PAUSE_SIMULÉE');
  await page.locator('#offerFilter').selectOption('Atelier Intervention');
  await expect(page.locator('#resultCount')).toHaveText('1 pilote affiché sur 1');

  const adminOverflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
  expect(adminOverflow).toBeFalsy();
  await page.goto(`${origin}/demo/`);
  const clientOverflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
  expect(clientOverflow).toBeFalsy();

  await page.goto(`${origin}/demo/admin.html`);
  await page.locator('#reset').click();
  await page.locator('#confirmReset').click();
  await expect(page.locator('#resultCount')).toHaveText('0 pilotes affichés sur 0');
  const stored = await page.evaluate(key => JSON.parse(localStorage.getItem(key)), key);
  expect(stored).toEqual(empty);
  expect(errors).toEqual([]);
  expect(paymentRequests).toEqual([]);
  console.log('E2E PASS empty→invalid→.test→checkout→confirmation→admin→persistence→status→filters→reset');
  console.log('MOBILE PASS viewport=390 client_overflow=false admin_overflow=false');
  console.log('CONSOLE PASS errors=0 payment_provider_requests=0');
  console.log('STORE PASS key=' + key + ' reset=' + JSON.stringify(stored));
});
