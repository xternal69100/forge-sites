---
version: alpha
name: Forge Matrix
description: Cockpit de preuve noir et vert, dense mais lisible, inspiré des terminaux Matrix sans théâtraliser l’activité.
colors:
  primary: "#6CFF8F"
  primaryStrong: "#32E875"
  primaryDim: "#173D27"
  background: "#050806"
  surface: "#0A100C"
  surfaceRaised: "#101A13"
  surfaceGlass: "#0D1711"
  border: "#284B33"
  text: "#F1FFF4"
  textMuted: "#A7C9AF"
  info: "#75D7FF"
  warning: "#FFD166"
  danger: "#FF7B89"
  paper: "#C5A3FF"
typography:
  display:
    fontFamily: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace
    fontSize: 4rem
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: "-0.05em"
  h1:
    fontFamily: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-0.04em"
  h2:
    fontFamily: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace
    fontSize: 2rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.03em"
  body:
    fontFamily: Inter, ui-sans-serif, system-ui, sans-serif
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: "0em"
  label:
    fontFamily: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace
    fontSize: 0.75rem
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0.08em"
rounded:
  sm: 6px
  md: 12px
  lg: 20px
  pill: 999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 72px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.background}"
    rounded: "{rounded.sm}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.primaryStrong}"
    textColor: "{colors.background}"
    rounded: "{rounded.sm}"
    padding: 12px
  button-secondary:
    backgroundColor: "{colors.surfaceRaised}"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: 12px
  card:
    backgroundColor: "{colors.surfaceGlass}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    padding: 24px
  terminal:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: 24px
  badge-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.background}"
    rounded: "{rounded.pill}"
    padding: 8px
  badge-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.background}"
    rounded: "{rounded.pill}"
    padding: 8px
---

## Overview

Forge Matrix est un cockpit de preuve, pas un théâtre d’agents. L’identité transpose le noir et vert Matrix dans une interface premium, sobre et opérationnelle : grille fine, lueur contenue, pluie numérique décorative rare et terminal structuré. Toute animation doit représenter un état de démonstration clairement étiqueté, jamais une activité réelle implicite.

## Colors

- **Background (#050806)** : noir légèrement vert, plus confortable qu’un noir absolu.
- **Primary (#6CFF8F)** : vert principal pour actions, focus et preuves positives ; contraste supérieur à AA sur le fond.
- **Text (#F1FFF4)** : blanc vert pour la lecture longue.
- **Text muted (#A7C9AF)** : texte secondaire, réservé aux métadonnées et descriptions.
- **Info / Warning / Danger / Paper** : codent la nature d’un état avec un libellé textuel systématique ; la couleur ne porte jamais seule l’information.

## Typography

Les titres, métriques, identifiants et commandes utilisent une pile monospace native. Le corps utilise Inter si disponible, puis la pile système. Deux familles et trois graisses au maximum. Les titres restent courts ; les preuves et garde-fous privilégient la lisibilité plutôt que l’effet terminal.

## Layout

Grille mobile-first en une colonne, puis 12 colonnes à partir de 900 px. Largeur maximale 1200 px, gouttières de 20 px sur mobile et 32 px sur desktop. Les tableaux défilent dans leur propre conteneur ; le document ne déborde jamais horizontalement. La densité des dashboards repose sur des cartes compactes, avec espace respirant entre groupes fonctionnels.

## Elevation & Depth

Les cartes translucides utilisent un fond opaque à 94 % compatible avec les contrastes et une bordure verte grisée. Une seule ombre diffuse verte est autorisée sur le focus actif ou l’élément hero. Pas de glassmorphism illisible ni de halos derrière du texte long.

## Shapes

Angles techniques mais non agressifs : rayon 6 px pour commandes, 12 px pour cartes, 20 px pour panneaux hero. Les badges sont en pilule. Les lignes de circuit et coins coupés sont décoratifs et ne modifient jamais la zone de clic.

## Components

- **Navigation** : sticky, fond opaque, lien actif explicite et focus visible de 3 px.
- **Bannière DÉMO** : persistante sur toutes les surfaces transactionnelles ; elle rappelle qu’aucun ordre, débit, provider ou transmission réelle n’est possible.
- **Cartes de preuve** : titre, état textuel, source publique autorisée et fraîcheur. Une preuve absente reste affichée comme absente.
- **Terminal** : journal synthétique append-only, horodatage et identifiant ; jamais de prompts ou logs privés.
- **Transaction Lab** : étapes OBSERVÉ → ÉTUDIÉ → PAPER ou REJETÉ → preuve. Les états PROPOSÉ, AUTORISÉ et EXÉCUTÉ sont visibles comme vocabulaire de gouvernance ; EXÉCUTÉ exige un `proofId` non vide.
- **Boutons** : libellés verbaux, états disabled explicites, aucune action financière réelle.

## Do's and Don'ts

### Do

- Répéter les badges `DÉMO` ou `DIFFÉRÉ` avec timestamp selon la provenance.
- Associer icône ou couleur à un libellé lisible.
- Maintenir WCAG AA, navigation clavier et focus visible.
- Désactiver pluie, scintillement, transitions et smooth scroll avec `prefers-reduced-motion: reduce`.
- Afficher les zéros réellement lus du registre Forge Capital, sans extrapoler un rendement.

### Don't

- Ne jamais publier prompt, log privé, secret, donnée personnelle, coordonnée, montant confidentiel ou chemin interne.
- Ne pas présenter une animation comme du temps réel.
- Ne pas utiliser de vert néon sur de longues zones de texte.
- Ne jamais permettre `EXÉCUTÉ` sans preuve ni suggérer qu’un bouton passe un ordre réel.
- Ne pas dépendre d’une ressource externe pour la structure, l’interaction ou la lisibilité essentielles.
