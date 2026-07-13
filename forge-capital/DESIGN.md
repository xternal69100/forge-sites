---
version: alpha
name: Studio Office — Telegram-first
description: Un office manager numérique chaleureux et précis pour coach indépendante, piloté par conversation et gardé sous contrôle humain.
colors:
  ink: "#16231F"
  inkSoft: "#344A42"
  canvas: "#F4F1E8"
  paper: "#FFFCF5"
  paperStrong: "#FFFFFF"
  line: "#D7D0C1"
  accent: "#E95435"
  accentDark: "#A82E1A"
  sage: "#CBE4D7"
  sageDark: "#1E684D"
  telegram: "#2389C7"
  warning: "#A96500"
  danger: "#A12C2C"
typography:
  display:
    fontFamily: Georgia, Times New Roman, serif
    fontSize: 4rem
    fontWeight: 700
    lineHeight: 0.98
    letterSpacing: "-0.04em"
  h1:
    fontFamily: Georgia, Times New Roman, serif
    fontSize: 2.75rem
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: "-0.03em"
  h2:
    fontFamily: Arial, Helvetica, sans-serif
    fontSize: 1.5rem
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  body:
    fontFamily: Arial, Helvetica, sans-serif
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.55
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
  lg: 22px
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
    backgroundColor: "{colors.accent}"
    textColor: "{colors.paperStrong}"
    rounded: "{rounded.pill}"
    padding: 14px
  button-primary-hover:
    backgroundColor: "{colors.accentDark}"
    textColor: "{colors.paperStrong}"
    rounded: "{rounded.pill}"
    padding: 14px
  button-secondary:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: 14px
  panel:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  telegram-panel:
    backgroundColor: "{colors.telegram}"
    textColor: "{colors.paperStrong}"
    rounded: "{rounded.lg}"
    padding: 24px
---

## Overview

Studio Office matérialise un office manager numérique complet pour une coach sportive indépendante fictive. Le produit se pilote d’abord dans Telegram, mais montre une profondeur opérationnelle réelle : agenda, relation client, contenus, facturation, pré-comptabilité, tâches et décisions à approuver. L’esthétique associe papier de planning, encre profonde, corail énergique et vert calme. Elle doit ressembler à un studio bien tenu, jamais à un chatbot gadget ni à un SaaS violet générique.

Marque de release : `coach-office-v2`.

## Colors

- **Ink (#16231F)** porte la confiance, les titres et le cockpit.
- **Canvas (#F4F1E8)** évoque un carnet de travail sans paraître rétro.
- **Paper (#FFFCF5)** sépare les modules et les fiches opérationnelles.
- **Accent (#E95435)** signale les actions commerciales importantes, jamais les métriques décoratives.
- **Sage (#CBE4D7)** distingue les éléments validés, planifiés ou sous contrôle.
- **Telegram (#2389C7)** n’apparaît que dans la simulation conversationnelle.
- Tous les statuts ont un libellé ; la couleur seule ne porte aucune décision.

## Typography

Les grandes promesses utilisent Georgia pour une présence éditoriale humaine. Le produit et les données utilisent une pile sans-serif native. Les micro-libellés et commandes Telegram utilisent une monospace native. Aucun chargement de police externe n’est nécessaire.

## Layout

La landing alterne blocs éditoriaux généreux et preuves opérationnelles compactes. Le parcours client conserve une colonne principale lisible avec un rail de résumé. L’admin adopte une grille cockpit : navigation latérale, espace de travail central et téléphone Telegram. À 390 px, tout passe en une colonne, les tableaux défilent uniquement dans leur cadre et le document ne déborde jamais.

## Elevation & Depth

Les surfaces sont opaques. La profondeur vient d’une ombre courte, d’un trait brun-gris et de décalages éditoriaux. Aucun glassmorphism, aucun flou, aucun halo décoratif.

## Shapes

Les panneaux principaux ont des angles de 12 à 22 px. Les boutons sont des pilules pour rester confortables au pouce. Les fiches opérationnelles utilisent une bande latérale ou un index plutôt que des icônes génériques répétées.

## Components

- **Offer card** : prix fondateur explicitement distinct d’un tarif standard, installation et abonnement séparés.
- **Journey stepper** : cinq étapes, état courant lisible et navigation arrière possible.
- **Domain selector** : huit responsabilités activables, toutes requises pour cette démonstration complète.
- **Cockpit navigation** : agenda, CRM, inbox, marketing, factures, pré-compta, tâches, approbations et journal.
- **Telegram phone** : commandes réalistes, réponses synthétiques et décisions Valider / Modifier / Refuser, sans réseau.
- **Approval card** : contexte, niveau de contrôle et décision persistée dans le journal.
- **Empty state** : reset réellement vide et chemin explicite vers le parcours fictif.

## Do's and Don'ts

### Do

- Répéter que la démonstration est fictive, locale, sans débit ni transmission.
- Utiliser exclusivement des emails `.test` et des identités manifestement synthétiques.
- Montrer l’autonomie graduée : préparer, proposer, puis faire approuver les actions sensibles.
- Séparer l’offre fondatrice du futur tarif standard, qui n’est pas annoncé.
- Conserver des cibles tactiles de 44 px et un focus visible.

### Don't

- Ne prétendre ni client réel, ni traction, ni résultat réel.
- Ne demander aucune carte bancaire et ne déclencher aucun appel réseau applicatif.
- Ne stocker aucune donnée de santé, performance physique, blessure ou diagnostic.
- Ne présenter aucune ancienne offre comme canonique.
- Ne promouvoir la console de preuve interne comme parcours client.
