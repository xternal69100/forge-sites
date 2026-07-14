---
version: matrix-learning-v1
name: Forge Capital Matrix Learning — ON-CHAIN ONLY
description: Cockpit Matrix dense pétrole/cyan/vert, orienté Monitor / Operate, qui rejoue des artefacts PAPER bornés et sépare observation live, recherche, veto et exécution prouvée.
colors:
  primary: "#020908"
  petrol: "#051311"
  panel: "#071A17"
  panelStrong: "#0A231E"
  line: "#17483E"
  matrix: "#65FF9A"
  cyan: "#35E7FF"
  cyanSoft: "#A8F7FF"
  text: "#E4FFF3"
  muted: "#7FA99B"
  warning: "#FFB347"
  danger: "#FF6574"
typography:
  display:
    fontFamily: Arial Narrow, Impact, Arial, sans-serif
    fontSize: 4.8rem
    fontWeight: 900
    lineHeight: 0.88
    letterSpacing: "0.045em"
  h1:
    fontFamily: Arial Narrow, Impact, Arial, sans-serif
    fontSize: 3rem
    fontWeight: 900
    lineHeight: 0.92
    letterSpacing: "0.045em"
  body:
    fontFamily: Arial, Helvetica, sans-serif
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: "0em"
  data:
    fontFamily: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace
    fontSize: 0.75rem
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: "0.04em"
rounded:
  sm: 1px
  md: 2px
  lg: 4px
spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 20px
  xl: 32px
components:
  button-primary:
    backgroundColor: "{colors.cyan}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px
  button-secondary:
    backgroundColor: "{colors.petrol}"
    textColor: "{colors.cyan}"
    rounded: "{rounded.sm}"
    padding: 12px
  panel:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: 12px
  status-replay:
    backgroundColor: "{colors.panelStrong}"
    textColor: "{colors.matrix}"
    rounded: "{rounded.sm}"
    padding: 4px
  status-veto:
    backgroundColor: "{colors.panelStrong}"
    textColor: "{colors.danger}"
    rounded: "{rounded.sm}"
    padding: 4px
---

## Overview

`matrix-learning-v1` est la surface primaire **Monitor / Operate** de Forge Capital. Ce n’est pas une landing SaaS : la route cockpit affiche immédiatement l’état de décision, le marché public read-only, les traces de recherche, les méthodes, les gates et les agents.

Le modèle mental est une salle d’observabilité financière : dense, asymétrique, opaque et lisible. Le vert Matrix signale une chaîne d’apprentissage/provenance, le cyan les données et actions de lecture, le rouge un veto ou une preuve manquante. Aucun grand slogan marketing, chiffre décoratif, glassmorphism ou violet.

## Contrat de vérité

Quatre axes ne doivent jamais se confondre :

1. **Marché** : `ON-CHAIN LIVE` uniquement après succès actuel de l’Info API Hyperliquid. Le fallback efface les valeurs et dit `DIFFÉRÉ`.
2. **Recherche** : `TRACE D’APPRENTISSAGE`, `PAPER`, `RESEARCH`, `VETO` ou `NOOP` ; jamais ordre, fill ou transaction réelle.
3. **Capital** : 0 reçu, 0 liquide, 0 investi, 0 engagé, valeur nette réelle 0.
4. **Exécution** : absente du navigateur. `EXÉCUTÉ AVEC PREUVE` reste le gate du store DÉMO, avec `proofId`, `proofSource`, `proofTimestamp`.

Hyperliquid public est la source live primaire et read-only. Toute référence CEX éventuelle est **DATA-ONLY EXOGÈNE**, secondaire, sans compte, clé, custody, dépôt, ordre, signature, provider ou hedge.

## Layout

La composition desktop plein écran est volontairement asymétrique :

- barre système et truth strip compactes ;
- ticker Hyperliquid horizontal ;
- colonne gauche : top-of-book puis synthèse décisionnelle ;
- centre : Learning Reports et Method Lab ;
- colonne focale haute : Strategy Tape vertical ;
- rail droit : runtime gate et Agent Mesh ;
- provenance en fermeture de grille.

À 390 px, la grille devient une colonne sans overflow du document. Les zones de données gèrent leur propre scroll. Les champs de la Strategy Tape se simplifient sans perdre classification, rôle, statut, message et source.

## Strategy Tape

La tape n’invente aucun événement. `private/export_snapshot.py` transforme des rapports et états réels en vues `ARTEFACT_REPLAY`, ordonnées et bornées à 32 lignes. La copie DOM qui boucle l’animation est `aria-hidden` et ne modifie pas le compteur de snapshot.

Contrôles obligatoires : filtres par rôle, méthode et statut ; pause/reprise ; compteur `filtré / total`. Avec `prefers-reduced-motion: reduce`, animation et clone sont retirés, le bouton commence en pause et le viewport devient scrollable.

## Learning Reports

Chaque carte donne : classification, source, méthode, conclusion et nombre de trades uniquement si documenté. Le drawer détaille dataset, fenêtre, coûts/stress, benchmark, gates PASS/FAIL et preuve générique. Un nombre absent est affiché `NON DISPONIBLE`, jamais complété par estimation.

## Method Lab

La chaîne en langage humain est fixe et sourcée : walk-forward chronologique → train-only → funding aligné → liquidation intrabar conservatrice → coûts sévères → benchmark BTC → anti-leakage → shadow-forward figé → Council → Factory → audits indépendants → Red-Team. Un veto individuel suffit ; aucun consensus synthétique n’est fabriqué.

## Agent Mesh et décision

Le mesh rend 16 rôles + News Sentinel. Chaque ligne porte uniquement un état, une livraison/latest artifact générique et une source lorsque ces éléments sont dérivables des rapports 44–45. Aucun pourcentage de consensus, score d’agent ou métrique de production n’est inventé.

La synthèse humaine répond toujours à : **Ce qui a été appris**, **Ce qui a échoué**, **Ce qui change ensuite**. `CASH/NOOP` est champion. L’Experiment Runner reste `PAUSED` et le runtime `STOP_FAIL_CLOSED` jusqu’à preuve du runtime budget, du Trial Ledger et du Dataset Registry.

## Colors & Depth

- **Primary / Petrol** : matière de fond, presque noire et légèrement verte.
- **Panel / Panel Strong** : surfaces strictement opaques.
- **Matrix** : apprentissage, provenance positive, chaînes méthodologiques.
- **Cyan** : observation live et interaction read-only.
- **Danger** : veto, pause, fail-closed.
- **Warning** : attente ou NOOP explicite.

La profondeur vient des traits, contrastes, décalages internes et densité. Pas de blur, verre, halo géant, ombre molle ou gradient violet. Les statuts sont écrits : la couleur ne porte jamais seule le sens.

## Surfaces préservées

- `site/index.html` : index opérationnel et routes, sans hero SaaS.
- `site/demo/index.html` : cockpit Matrix primaire.
- `site/demo/transaction.html` : parcours DÉMO local, PAPER et ticket non signé/non transmis.
- `site/demo/admin.html` : filtres, journal, proof gate et reset exact.
- store canonique : `forge:forge-capital:demo:v1`.

## Do

- Sourcer chaque rapport et trace.
- Afficher explicitement snapshot/replay, PAPER et capital réel.
- Conserver la tape bornée et pausée en reduced motion.
- Effacer les prix live si un seul élément du batch Hyperliquid échoue.
- Présenter les méthodes en français humain et les gates sans euphémisme.

## Don’t

- Ne jamais faire passer une trace de recherche pour un ordre, fill ou performance live.
- Ne jamais incrémenter artificiellement un compteur pour créer de l’activité.
- Ne jamais publier titre de news, ID candidat interne, chemin absolu, prompt, token ou thread ID.
- Ne jamais demander ou stocker secret, clé, signature, compte ou identité.
- Ne jamais déduire edge, consensus, position ou santé depuis une simple collecte HTTP.
