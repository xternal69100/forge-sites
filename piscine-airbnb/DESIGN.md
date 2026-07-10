---
version: alpha
name: Poolbnb Léman
description: Marketplace premium locale, trust-first et supply-first pour réserver des micro-escapes aquatiques autour du Léman.
colors:
  primary: "#CC3450"
  primary-strong: "#A92A42"
  secondary: "#161A21"
  tertiary: "#0F766E"
  neutral: "#FFF9F6"
  surface: "#FFFFFF"
  surface-muted: "#F3F5FB"
  line: "#E8E1DB"
  text-muted: "#667085"
  info: "#DFF5F1"
  accent-warm: "#FFE7E2"
typography:
  headline-display:
    fontFamily: Cormorant Garamond
    fontSize: 64px
    fontWeight: 600
    lineHeight: 0.95
    letterSpacing: "-0.03em"
  headline-lg:
    fontFamily: DM Sans
    fontSize: 40px
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.04em"
  headline-md:
    fontFamily: DM Sans
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.03em"
  body-lg:
    fontFamily: DM Sans
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.7
  body-md:
    fontFamily: DM Sans
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  label-md:
    fontFamily: DM Sans
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "0.16em"
rounded:
  sm: 12px
  md: 20px
  lg: 32px
  xl: 36px
  full: 9999px
spacing:
  xs: 6px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  gutter: 24px
  container: 1280px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    rounded: "{rounded.full}"
    padding: 14px
  button-primary-hover:
    backgroundColor: "{colors.primary-strong}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.full}"
    padding: 14px
  card-surface:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.lg}"
    padding: 24px
  chip-filter:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.full}"
    padding: 10px
---

# Poolbnb Léman Design System

## Overview

Poolbnb Léman doit ressembler à une **marketplace premium de proximité** : plus chaleureuse qu’un SaaS, plus cadrée qu’une plateforme d’annonces ouverte, plus calme qu’un univers événementiel. L’interface doit évoquer l’idée d’un été beau, privé et maîtrisé autour du Léman : lumière douce, surfaces généreuses, signes de confiance explicites et promesse de simplicité.

Le ton visuel marie un **accent corail énergique** pour l’action, un **vert lac profond** pour la confiance, et des **neutres crème/blanc** pour laisser respirer l’interface. Le site n’essaie pas de vendre une “fête” : il vend une parenthèse premium, filtrée et accompagnée.

## Colors

La palette repose sur un système simple :

- **Primary (#CC3450)** : corail de conversion, réservé aux CTA principaux, aux badges d’attention et aux indicateurs d’action.
- **Primary Strong (#A92A42)** : variante hover/pressed du corail.
- **Secondary (#161A21)** : encre chaude et dense pour les titres, blocs premium et textes structurants.
- **Tertiary (#0F766E)** : vert lac pour tout ce qui exprime la confiance, la sélection, la sérénité et les messages “trust-first”.
- **Neutral (#FFF9F6)** : fond crème lumineux pour éviter le blanc clinique.
- **Surface (#FFFFFF)** : cartes, modales et zones de contenu élevées.
- **Surface Muted (#F3F5FB)** : surfaces secondaires, chips, cartes de support.
- **Line (#E8E1DB)** : bordures douces.
- **Text Muted (#667085)** : textes secondaires, descriptions, aides.
- **Info (#DFF5F1)** : mises en avant calmes autour du sourcing et de l’onboarding.
- **Accent Warm (#FFE7E2)** : halo chaud et arrière-plans de réassurance.

## Typography

La typographie doit créer un équilibre entre **aspiration éditoriale** et **clarté produit**.

- **Headline Display** utilise *Cormorant Garamond* pour les moments de marque les plus émotionnels : hero, intertitres premium, signature finale.
- **Headline LG / MD** utilisent *DM Sans* très gras avec tracking négatif pour l’efficacité produit, les sections et les cartes.
- **Body LG / MD** restent en *DM Sans* pour une lecture web contemporaine et très fluide.
- **Label MD** est en capitales espacées, utilisé pour badges, catégories, micro-titres de section et tokens de confiance.

Ne jamais mélanger plus de deux familles. Les titres serif restent rares et précieux ; toute l’UI, la data et les interactions doivent rester en sans-serif.

## Layout

Le layout suit une logique **mobile-first**, avec conteneur fixe large sur desktop (`1280px`) et un rythme de section généreux. L’espace doit respirer comme une marque premium, mais sans perdre l’efficacité d’une landing de conversion.

- Le hero doit combiner **promesse**, **CTAs**, **preuves de cadrage** et **aperçu produit**.
- Les grandes sections alternent entre fond neutre, surfaces blanches et blocs encre pour installer un tempo.
- Les éléments de filtre, scorecards et mocks doivent rester extrêmement lisibles dès 375px.
- Les chips, toggles et boutons utilisent une rondeur totale (`full`) pour garder un aspect doux et haut de gamme.

## Elevation & Depth

La profondeur doit être douce, jamais clinquante. On privilégie :

- une **fine ligne de contour** sur les cartes claires ;
- des **ombres diffuses** pour les cartes premium et les modales ;
- des **halos colorés subtils** dans les zones hero ou CTA ;
- des fonds dégradés ou “water glow” à très faible intensité pour rappeler l’univers piscine sans photo externe.

La hiérarchie visuelle ne repose pas sur des ombres fortes mais sur la combinaison `surface + line + radius + contraste typographique`.

## Shapes

La forme de Poolbnb Léman est **douce, accueillante et premium**.

- `sm` pour petits champs, chips et micro-composants.
- `md` pour inputs, petits panneaux, badges larges.
- `lg` pour cartes principales, blocs marketplace et grilles vitrines.
- `xl` pour heroes, CTA finaux et grandes zones éditoriales.
- `full` pour boutons, pastilles et toggles.

Ne pas mélanger des angles durs avec ces formes organiques. Tout le système doit sembler cohérent, tactile et calme.

## Components

- **button-primary** : corail, texte blanc, rondeur maximale. Une seule action principale par zone.
- **button-secondary** : surface blanche, texte encre, contour doux. Sert d’action d’exploration ou de bascule d’audience.
- **card-surface** : fond blanc, rayon large, padding généreux, pensée pour contenir des récits courts, des données ou des formulaires.
- **chip-filter** : fond `surface-muted`, texte sombre, rondeur totale. Utilisée pour filtres, statuts, zones pilotes et tags de listing.

Les composants doivent rendre visibles les signaux de confiance : labels “hôte vérifié”, “règles claires”, “créneau calme”, “programme founding host”, etc.

## Do's and Don'ts

- Do réserver `primary` aux actions majeures et aux micro-moments de tension positive.
- Do utiliser `tertiary` pour tout ce qui parle de confiance, qualification, support et exécution.
- Do maintenir un contraste AA minimum sur toutes les zones textuelles et boutons.
- Do garder les sections premium aérées et peu chargées.
- Don’t transformer le site en univers “pool party”.
- Don’t employer plus de deux graisses simultanément dans une même petite carte.
- Don’t utiliser des bleus saturés ou des couleurs additionnelles non définies dans les tokens.
- Don’t publier des preuves sociales inventées ; préférer signaux opératoires, cohortes pilotes et preuves de cadrage réelles.
