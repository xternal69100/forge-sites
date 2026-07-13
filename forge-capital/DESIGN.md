---
version: alpha
name: Forge Capital Cyber Operations — ON-CHAIN ONLY
description: Cockpit financier dense pétrole/cyan, orienté Monitor / Operate, séparant observation on-chain, différé, PAPER et exécution prouvée.
colors:
  primary: "#02080D"
  panel: "#07131B"
  panelStrong: "#0B1C26"
  line: "#173746"
  cyan: "#35E7FF"
  cyanSoft: "#99F4FF"
  text: "#D9F3F7"
  muted: "#7799A4"
  warning: "#FF9B42"
  danger: "#FF5D62"
  success: "#43F0A1"
typography:
  display:
    fontFamily: Arial Narrow, Impact, Arial, sans-serif
    fontSize: 5rem
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: "0.025em"
  h1:
    fontFamily: Arial Narrow, Impact, Arial, sans-serif
    fontSize: 3rem
    fontWeight: 900
    lineHeight: 0.95
    letterSpacing: "0.025em"
  body:
    fontFamily: Arial, Helvetica, sans-serif
    fontSize: 0.9375rem
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0em"
  data:
    fontFamily: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace
    fontSize: 0.75rem
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: "0.04em"
rounded:
  sm: 2px
  md: 4px
  lg: 6px
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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.cyan}"
    rounded: "{rounded.sm}"
    padding: 12px
  panel:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    padding: 20px
  status-live:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.success}"
    rounded: "{rounded.sm}"
    padding: 4px
  status-warning:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.warning}"
    rounded: "{rounded.sm}"
    padding: 4px
---

## Overview

`cyber-ops-v1` est un cockpit **Monitor / Operate** public pour Forge Capital. Il expose quatre surfaces : manifeste, cockpit, Transaction Lab et administration. La doctrine produit est **ON-CHAIN ONLY** : Hyperliquid public est la source live primaire et la venue cible ; aucune plateforme centralisée ne peut servir à l’activité, la custody ou au hedge. Une donnée CEX éventuelle ne peut apparaître que sous le libellé secondaire **DATA-ONLY EXOGÈNE**.

Deux axes restent orthogonaux : fraîcheur/provenance (`ON-CHAIN LIVE`, `DIFFÉRÉ`) et cycle transactionnel (`OBSERVÉ`, `ÉTUDIÉ`, `PAPER`, `TICKET À VALIDER`, `EXÉCUTÉ AVEC PREUVE`). Le badge live exige une lecture Hyperliquid actuelle réussie avec source et timestamp. En cas d’échec, toutes les valeurs live sont effacées.

## Colors

- **Primary (#02080D)** : fond pétrole presque noir, sans voile transparent.
- **Panel (#07131B)** et **Panel Strong (#0B1C26)** : profondeur par matières opaques imbriquées.
- **Cyan (#35E7FF)** : signal, focus et source on-chain active ; jamais une grande nappe décorative.
- **Warning (#FF9B42)** : risques, gates et dégradation différée.
- **Success (#43F0A1)** : lecture live réussie ou absence confirmée d’un chemin dangereux.
- Les statuts sont toujours écrits ; la couleur ne porte jamais seule la vérité.

## Typography

Les titres utilisent une pile condensée industrielle native. Les prix, timestamps, IDs, sources et statuts utilisent une monospace native. Aucun asset typographique externe n’est chargé.

## Layout

Le cockpit assemble une barre système, une truth strip et une grille dense : ticker, radar abstrait, top of book, risque, topologie, santé, cellule d’agents et provenance. La landing sert de manifeste de routes. Le Transaction Lab conserve un faux parcours complet relié au store canonique `forge:forge-capital:demo:v1`. À 390 px, chaque surface passe en une colonne ; les rangées denses défilent dans leur propre cadre sans overflow du document.

## Elevation & Depth

Toutes les surfaces sont opaques. La profondeur vient de traits, contrastes de matière et rares décalages. Aucun glassmorphism, blur, halo géant ou gradient violet générique.

## Shapes

Angles de 2 à 6 px, panneaux rectangulaires, tags compacts et radar circulaire uniquement comme instrument focal abstrait non géographique. Les cibles interactives gardent 44 px minimum.

## Components

- **Truth strip** : `ON-CHAIN LIVE`, `DIFFÉRÉ`, `PAPER`, `EXÉCUTÉ AVEC PREUVE`, et `DATA-ONLY EXOGÈNE` secondaire.
- **Market ticker** : BTC/ETH/SOL issus de l’Info API publique officielle Hyperliquid, lecture seule sans compte ni clé.
- **Top of book** : meilleur bid/ask `l2Book` uniquement ; aucune profondeur inventée.
- **Honest fallback** : retire les prix live et affiche `DIFFÉRÉ · LIVE INDISPONIBLE` si une lecture échoue.
- **Transaction Lab** : signal DÉMO → étude → PAPER/REJETÉ → ticket non signé/non transmis.
- **Proof gate** : `EXÉCUTÉ AVEC PREUVE` exige `proofId`, `proofSource` et `proofTimestamp`.
- **Admin** : filtres, journal, preuve DÉMO et reset exact de la baseline.

## Do's and Don'ts

### Do

- Afficher la source et le timestamp de toute donnée `ON-CHAIN LIVE`.
- Répéter `ON-CHAIN ONLY` et `AUCUN COMPTE CEX` sur les quatre surfaces.
- Garder capital réel, PAPER et preuve d’exécution séparés.
- Effacer les valeurs live au moindre échec du batch BTC/ETH/SOL.
- Conserver le faux parcours et le reset exact pour démontrer le contrat sans agir.

### Don't

- Ne jamais demander ni stocker de secret, clé, signature, compte ou identité.
- Ne jamais proposer de contrôle Signer / Acheter / Vendre / Exécuter / Transmettre.
- Ne jamais présenter une CEX comme source primaire ou venue d’activité.
- Ne jamais appeler une donnée différée « live » ni déduire une position d’un prix public.
- Ne jamais prétendre qu’une preuve DÉMO locale atteste une transaction réelle.
