# Démo publique Forge Capital — cyber-ops-v1

Quatre surfaces :

1. `../index.html` — manifeste ON-CHAIN ONLY ;
2. `index.html` — cockpit Hyperliquid public BTC/ETH/SOL ;
3. `transaction.html` — faux parcours signal → étude → PAPER / REJETÉ → ticket non signé ;
4. `admin.html` — filtres, journal, gate de preuve et reset exact.

Store canonique : `forge:forge-capital:demo:v1`.

## Contrat de vérité

- `ON-CHAIN LIVE` uniquement après lecture actuelle réussie sur l’Info API publique Hyperliquid, avec source et timestamp.
- En échec : valeurs live supprimées et état `DIFFÉRÉ` explicite.
- CEX éventuelle : `DATA-ONLY EXOGÈNE` secondaire uniquement ; **AUCUN COMPTE CEX**.
- `EXÉCUTÉ AVEC PREUVE` exige `proofId`, `proofSource`, `proofTimestamp`.
- Aucun secret, ordre, signature, wallet, dépôt ou provider réel.

## Vérifications locales

```bash
python3 -m unittest tests.test_cyber_ops_contract tests.test_matrix_contract -v
node tests/test_demo_store.js
```

Servir depuis `site/`, puis vérifier les quatre routes en desktop et 390 px, l’overflow document, les erreurs console/ressource, le parcours complet, l’administration et le reset final.
