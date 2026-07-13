---
version: alpha
name: Forge Capital Cyber Operations
description: Cockpit financier public de supervision et d’opérations, dense, cyan sur noir pétrole, où toute activité reste liée à sa provenance et à son niveau de preuve.
colors:
  primary: "#35E7FF"
  primaryStrong: "#8CF3FF"
  primaryDim: "#0A6674"
  background: "#02080D"
  backgroundRaised: "#05121A"
  surface: "#071821"
  surfaceRaised: "#0A202B"
  surfaceSunken: "#030D13"
  border: "#163746"
  borderStrong: "#23627A"
  text: "#EAFBFF"
  textMuted: "#8DAEBA"
  textFaint: "#5E7A85"
  warning: "#FF9B42"
  danger: "#FF667A"
  paper: "#B6A3FF"
  success: "#57E6A5"
  grid: "#0C2A36"
typography:
  display:
    fontFamily: Arial Narrow, Bahnschrift Condensed, Roboto Condensed, Arial, sans-serif
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 0.96
    letterSpacing: "-0.04em"
  h1:
    fontFamily: Arial Narrow, Bahnschrift Condensed, Roboto Condensed, Arial, sans-serif
    fontSize: 2.25rem
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.03em"
  h2:
    fontFamily: Arial Narrow, Bahnschrift Condensed, Roboto Condensed, Arial, sans-serif
    fontSize: 1.25rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.01em"
  body:
    fontFamily: Arial, Helvetica, sans-serif
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: "0em"
  label:
    fontFamily: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace
    fontSize: 0.6875rem
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0.1em"
  data:
    fontFamily: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace
    fontSize: 0.8125rem
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: "0em"
rounded:
  xs: 2px
  sm: 4px
  md: 6px
  pill: 999px
spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 40px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.background}"
    rounded: "{rounded.xs}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.primaryStrong}"
    textColor: "{colors.background}"
    rounded: "{rounded.xs}"
    padding: 12px
  button-secondary:
    backgroundColor: "{colors.surfaceRaised}"
    textColor: "{colors.text}"
    rounded: "{rounded.xs}"
    padding: 12px
  panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: 16px
  panel-sunken:
    backgroundColor: "{colors.surfaceSunken}"
    textColor: "{colors.text}"
    rounded: "{rounded.xs}"
    padding: 12px
  badge-live:
    backgroundColor: "{colors.primaryDim}"
    textColor: "{colors.text}"
    rounded: "{rounded.xs}"
    padding: 4px
  badge-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.background}"
    rounded: "{rounded.xs}"
    padding: 4px
---

## Overview

Forge Capital Cyber Operations est d’abord une surface **Monitor / Operate**, jamais une landing SaaS maquillée en dashboard. L’écran présente un système financier expérimental comme un poste de supervision : état global en tête, noyau radar original au centre, rails de risque et de provenance, topologie de flux, mini carnets, agents et journal. La densité est assumée, mais chaque groupe possède un intitulé, une provenance et une hiérarchie de lecture.

La direction transforme deux vocabulaires sans les reproduire : la densité produit et les micro-données d’un terminal de marché ; la précision industrielle, les angles courts et l’accent-signal d’une interface de calcul. La référence visuelle fournie inspire la profondeur, les couches HUD et le noyau géospatial, mais aucun écran, contenu, globe, watermark ou composition propriétaire n’est repris.

Marque de release : `cyber-ops-v1`.

## Colors

- **Background (#02080D)** : noir bleu pétrole, fond principal non absolu.
- **Surface (#071821)** : modules opératoires ; les variations de surface créent la profondeur, pas le flou.
- **Primary (#35E7FF)** : cyan électrique réservé au signal actif, au focus, aux tracés et aux valeurs actuelles. Ce n’est jamais une grande nappe décorative.
- **Warning (#FF9B42)** : orange rare, réservé aux alertes et gates qui exigent une lecture immédiate.
- **Paper (#B6A3FF)** : différencie les résultats PAPER du capital réel.
- **Text muted (#8DAEBA)** : métadonnées lisibles ; aucun texte essentiel sous ce niveau de contraste.
- Chaque couleur s’accompagne d’un libellé. La couleur seule ne signifie jamais un état financier.

## Typography

Les titres utilisent une pile condensée native et industrielle. Les données, identifiants, timestamps et micro-libellés utilisent une monospace native. Le corps reste sans-serif pour éviter l’effet terminal intégral. Les tailles sont plus petites que sur une vitrine : hiérarchie par contraste, poids, alignement et densité avant la taille monumentale.

## Layout

Desktop : grille d’opérations 12 colonnes, avec noyau radar 6 colonnes, rail marché 3 colonnes et rail risque 3 colonnes. Les modules secondaires composent une topologie asymétrique ; aucune rangée de trois cartes marketing identiques.

Mobile : une colonne stricte à 390 px. Les tickers deviennent un ruban horizontal interne ; les tableaux défilent dans leur propre cadre ; le document conserve `scrollWidth === clientWidth`. Les contrôles tactiles gardent 44 px minimum.

## Elevation & Depth

Trois profondeurs opaques : fond, panneau, panneau creusé. Les bordures de 1 px et les doubles cadres ponctuels évoquent un HUD sans glassmorphism. Un halo cyan extrêmement contenu n’est permis que sur le radar et l’état actif. La grille topographique reste sous 8 % d’opacité et ne traverse jamais du texte long.

## Shapes

Angles courts de 2–6 px. Les panneaux peuvent utiliser des coins coupés via `clip-path` uniquement comme contour décoratif ; la zone interactive reste rectangulaire. Les badges d’état ne sont pas systématiquement des pilules. Les tracés, nœuds et anneaux du radar sont originaux et abstraits : pas de carte mondiale reconnaissable.

## Components

- **System bar** : marque, release, état de provenance, heure locale calculée et accès aux quatre surfaces.
- **Ticker** : données Kraken CORS-safe en lecture seule ; une réponse réussie devient `LIVE PUBLIC` avec source et timestamp. En échec, l’interface efface le faux live et affiche un fallback `DIFFÉRÉ` issu du snapshot.
- **Market radar** : visualisation abstraite de BTC/ETH/SOL, fraîcheur et pipeline ; décor fonctionnel, jamais prétention de géolocalisation ou d’activité transactionnelle.
- **Mini order-books** : bid/ask issus du ticker public courant, sans profondeur inventée. Les trois niveaux sont des repères visuels explicitement nommés `top of book`, pas un carnet complet.
- **Topology** : OBSERVÉ → RESEARCH_QUEUE → PREREGISTERED_PAPER → PAPER → EXÉCUTÉ ; chaque compte vient du snapshot public.
- **Bot health** : santé de collecte et gates, jamais disponibilité d’un moteur live implicite.
- **Provenance ledger** : source, fraîcheur, timestamp et classe de vérité sur un même bloc.
- **Transaction Lab** : crée uniquement des fixtures DÉMO, études, décisions PAPER/REJETÉ ou tickets non signés. Aucun bouton ne signe, transmet ou exécute.
- **Administration** : filtres, preuve complète, journal append-only et reset exact du store `forge:forge-capital:demo:v1`.
- **États publics** : `LIVE PUBLIC`, `DIFFÉRÉ`, `PAPER`, `TICKET À VALIDER`, `EXÉCUTÉ AVEC PREUVE`. Ce dernier exige `proofId`, `proofSource` et `proofTimestamp`.

## Do's and Don'ts

### Do

- Afficher zéro et absence tels quels.
- Répéter provenance, fraîcheur et portée de toute mesure.
- Séparer capital réel, étude PAPER et preuve d’exécution.
- Utiliser l’orange seulement pour une alerte ou un gate.
- Couper animations, balayage radar et transitions avec `prefers-reduced-motion: reduce`.
- Garder la structure et les interactions essentielles sans dépendance externe.

### Don't

- Ne pas copier le contenu, le globe, les panneaux, les libellés ou le watermark de la référence.
- Ne pas utiliser de hero centré, de grille de features ou de métrique décorative.
- Ne jamais conserver une valeur périmée sous un badge `LIVE PUBLIC`.
- Ne publier ni secret, clé, donnée privée, log brut, prompt, URL interne ou chemin local.
- Ne proposer aucun contrôle de signature, transmission, achat, vente ou exécution réelle.
- Ne pas utiliser blur, glassmorphism, dégradés violets ou animation permanente gratuite.
