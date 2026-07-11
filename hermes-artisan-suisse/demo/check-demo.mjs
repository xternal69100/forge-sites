import { readFileSync, existsSync, mkdtempSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const here = dirname(fileURLToPath(import.meta.url));
const site = resolve(here, '..');
const pages = [resolve(site, 'index.html'), resolve(here, 'index.html'), resolve(here, 'admin.html')];
const banner = 'DÉMO — AUCUNE DONNÉE, SOUSCRIPTION OU PAIEMENT RÉEL';
const key = 'forge:hermes-artisan-suisse:demo:v1';
const temp = mkdtempSync(join(tmpdir(), 'has-demo-check-'));
try {
  for (const page of pages) {
    const html = readFileSync(page, 'utf8');
    const scripts = [...html.matchAll(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/gi)].map(m => m[1]);
    if (!scripts.length) throw new Error(`Aucun script inline: ${page}`);
    scripts.forEach((source, index) => {
      const path = join(temp, `${pages.indexOf(page)}-${index}.js`);
      writeFileSync(path, source);
      const check = spawnSync(process.execPath, ['--check', path], { encoding: 'utf8' });
      if (check.status !== 0) throw new Error(`node --check échoue: ${page} script ${index}\n${check.stderr}`);
    });
    console.log('NODE_CHECK PASS', page);
  }
  const landing = readFileSync(pages[0], 'utf8');
  const client = readFileSync(pages[1], 'utf8');
  const admin = readFileSync(pages[2], 'utf8');
  const regressions = [];
  if ((landing.match(/href="demo\/index\.html"/g) || []).length < 3) regressions.push('Liens landing → client insuffisants');
  if (!client.includes(banner) || !admin.includes(banner)) regressions.push('Bannière obligatoire absente');
  const emptyAdminStore = /const emptyStore=\(\)=>\(\{version:1,subscriptions:\[\],workflows:\[\],tasks:\[\],approvals:\[\],journal:\[\]\}\);/.test(admin);
  if (!emptyAdminStore || /const baseline=/.test(admin) || !/write\(emptyStore\(\)\)/.test(admin)) regressions.push('Reset admin ne vide pas le store');
  if (regressions.length) throw new Error(regressions.join('\n'));
  if (!client.includes(key) || !admin.includes(key)) throw new Error('Clé localStorage non partagée');
  if (!client.includes('admin.html') || !admin.includes('../demo.html') || !admin.includes('index.html')) throw new Error('Chaîne de navigation incomplète');
  if (!existsSync(resolve(site, 'demo.html'))) throw new Error('Console historique absente');
  if (/type=["'](?:text\/["']?card|card)|stripe|paypal|adyen/i.test(client)) throw new Error('Champ/provider de paiement interdit détecté');
  console.log('CONTRACT PASS links, banner, empty reset, key, navigation, legacy console, no payment provider');
} finally { rmSync(temp, { recursive: true, force: true }); }
