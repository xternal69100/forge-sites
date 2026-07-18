# Vérification locale — rappel qualité total `studio-quality-recall-20260718`

**Exécutée :** 18 juillet 2026  
**Périmètre :** copie locale `site/` ; aucune publication externe.

## État attendu

- 0 famille disponible ;
- 7 éditions rappelées ;
- 0 ZIP et 0 binaire de police sous `site/` ;
- parcours CHF 0 bloqué par inventaire vide ;
- store local version 1 vide, allowlist vide, paquets vides ;
- admin à zéro ;
- aucun provider de paiement.

## Gates déterministes

```text
STORE PASS — allowlist et paquets vides, création refusée, récupération et reset fail-closed.
EDITORIAL GATE GREEN — aucune famille FAIL exposée dans catalogue/client/admin/store.
PUBLIC SITE PASS — 3 pages HTML, 27 liens locaux, 15 fichiers publics, 0 binaire distribué.
BASELINE PASS — catalogue, allowlist, paquets et store vides.
```

## Quarantaine

Les deux ZIP et les deux WOFF2 précédemment présents dans la copie publique locale ont été déplacés vers :

`../quarantine/public-site-recall-2026-07-18/`

`MANIFEST.sha256` a été vérifié à 4/4 avec `sha256sum -c`.

## Frontière distante

Cette vérification ne vaut pas publication. Le runner n’a pas pu résoudre `typoforge.alwaysdata.net` lors du contrôle final. La purge/synchronisation hôte reste décrite dans `../operations/HOST-PURGE-AND-PUBLIC-SYNC-2026-07-18.md`.
