---
version: alpha
name: Atelier Confiance
description: Une identité premium, claire et rassurante pour une offre d'assistant administratif agentique destinée aux artisans et petites structures suisses.
colors:
  primary: "#1E3A5F"
  primarySoft: "#D8E4F0"
  secondary: "#667085"
  tertiary: "#8C4F22"
  neutral: "#F6F3EE"
  surface: "#FFFFFF"
  ink: "#0F172A"
  muted: "#E8E1D7"
  success: "#22543D"
typography:
  h1:
    fontFamily: Manrope
    fontSize: 3.75rem
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.035em"
  h2:
    fontFamily: Manrope
    fontSize: 2.4rem
    fontWeight: 800
    lineHeight: 1.08
    letterSpacing: "-0.025em"
  h3:
    fontFamily: Manrope
    fontSize: 1.5rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  body-lg:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0em"
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.68
    letterSpacing: "0em"
  label:
    fontFamily: Inter
    fontSize: 0.78rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.08em"
rounded:
  sm: 12px
  md: 18px
  lg: 30px
  xl: 40px
spacing:
  xs: 8px
  sm: 12px
  md: 20px
  lg: 32px
  xl: 56px
  2xl: 80px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#FFFFFF"
    rounded: "{rounded.md}"
    padding: 14px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "#FFFFFF"
    rounded: "{rounded.md}"
    padding: 14px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 14px
  badge-trust:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  panel-emphasis:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 32px
  notice-soft:
    backgroundColor: "{colors.primarySoft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: 24px
  status-success:
    backgroundColor: "{colors.success}"
    textColor: "#FFFFFF"
    rounded: "{rounded.sm}"
    padding: 8px
  section-soft:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 32px
  divider-soft:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 8px
---

## Overview
Atelier Confiance mélange sérieux suisse, lisibilité SaaS moderne et chaleur artisanale. Le site doit inspirer confiance immédiatement : pas de noir agressif, pas de gimmick futuriste, pas de promesse magique. L'impression recherchée est celle d'un back-office calme, fiable et premium qui travaille pour le client sans lui enlever la main.

## Colors
- **Primary (`#1E3A5F`)** : bleu nuit professionnel, rassurant et stable.
- **Primary Soft (`#D8E4F0`)** : contrepoint clair pour fonds techniques, surlignages doux et repères d'interface.
- **Secondary (`#667085`)** : gris ardoise pour les textes secondaires et les explications.
- **Tertiary (`#8C4F22`)** : cuivre sombre pour les accents d'attention et les micro-signaux de chaleur.
- **Neutral (`#F6F3EE`)** : fond chaud, non clinique, qui rappelle la matière et l'atelier.
- **Surface (`#FFFFFF`)** : cartes et zones de lecture.
- **Ink (`#0F172A`)** : texte fort et structurant.
- **Muted (`#E8E1D7`)** : séparateurs doux, aplats secondaires et badges calmes.
- **Success (`#22543D`)** : validation, stabilité et garde-fous tenus.

## Typography
- **Manrope** pour les titres : compacte, nette, contemporaine, avec un vrai impact premium sans agressivité.
- **Inter** pour le texte : lisibilité maximale sur mobile comme sur desktop.
- Les titres sont francs, les paragraphes respirent, les labels sont en capitales espacées.
- Les grands titres doivent porter la promesse opératoire ; le corps de texte doit toujours rester concret, jamais marketing pour le marketing.

## Layout
- Très grande respiration au-dessus de la ligne de flottaison.
- Hero en deux colonnes sur desktop, une colonne mobile.
- Alternance entre grandes zones ouvertes et cartes densément utiles.
- Largeur de lecture contrôlée pour garder un ton premium.
- Une idée claire par section : douleur, cas d'usage, méthode, garde-fous, offre, conversion.

## Elevation & Depth
- Ombres douces, jamais dramatiques.
- Utiliser la profondeur pour distinguer les cartes utiles, pas pour décorer.
- Les panneaux de méthode et les preuves opératoires peuvent monter légèrement en relief ; le reste doit rester calme.

## Shapes
- Arrondis généreux et cohérents.
- Pas d'angles trop techniques.
- Les blocs importants doivent sembler solides et accueillants, comme un comptoir bien fini plutôt qu'un dashboard gadget.

## Components
- `button-primary` est réservé au CTA principal vers le pilote.
- `button-secondary` doit rester calme et lisible.
- `badge-trust` sert aux statuts, labels et garde-fous visibles.
- Les cartes doivent privilégier la clarté, les puces courtes et les chiffres visibles.
- Les panneaux d'offre et de méthode peuvent utiliser `panel-emphasis` pour porter l'information sans bruit visuel.

## Do's and Don'ts
### Do
- Montrer des cas d'usage concrets d'artisans et de petites structures.
- Parler de temps rendu, relances, messages, suivi et cadence terrain.
- Rester humain, crédible, opérationnel.
- Garder des contrastes AA et des focus visibles.
- Mettre en avant les garde-fous human-in-the-loop aussi clairement que la promesse commerciale.

### Don'ts
- Ne pas promettre un remplacement total de l'humain.
- Ne pas adopter un langage “IA magique”.
- Ne pas surcharger le site d'effets visuels, d'icônes gadget ou de jargon technique.
- Ne pas introduire de couleurs non définies par les tokens.
- Ne pas faire croire que le pilote remplace bexio, KLARA, Swiss21 ou un ERP existant.