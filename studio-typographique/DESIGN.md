---
version: alpha
name: Forge Open Editions — Catalogue public
description: Un index typographique public, précis et tactile, construit comme un établi éditorial contemporain.
colors:
  primary: "#C4432C"
  ink: "#151512"
  paper: "#F2EFE5"
  surface: "#FFFCF5"
  muted: "#5C5B54"
  line: "#C7C1B3"
  ember: "#C4432C"
  emberDark: "#772617"
  acid: "#D9E35D"
  success: "#1D6440"
  danger: "#8E2E24"
typography:
  display:
    fontFamily: Georgia, serif
    fontSize: 4rem
    fontWeight: 400
    lineHeight: 1.02
    letterSpacing: "-0.02em"
  secondary:
    fontFamily: Georgia, serif
    fontSize: 4rem
    fontWeight: 400
    lineHeight: 0.94
    letterSpacing: "-0.015em"
  h1:
    fontFamily: Georgia, serif
    fontSize: 3rem
    fontWeight: 600
    lineHeight: 1.04
    letterSpacing: "-0.025em"
  h2:
    fontFamily: Georgia, serif
    fontSize: 1.5rem
    fontWeight: 600
    lineHeight: 1.15
  body:
    fontFamily: Arial, sans-serif
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: Arial, sans-serif
    fontSize: 0.75rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.08em"
rounded:
  sm: 2px
  md: 6px
  lg: 14px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface}"
    rounded: "{rounded.sm}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.emberDark}"
    textColor: "{colors.surface}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 12px
  status-open:
    backgroundColor: "{colors.acid}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 8px
  specimen-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px
  site-canvas:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
  muted-copy:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.muted}"
  divider:
    backgroundColor: "{colors.line}"
  focus-ring:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
  accent-marker:
    backgroundColor: "{colors.ember}"
    textColor: "{colors.surface}"
  status-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.surface}"
  status-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.surface}"
---

## Overview

Forge Open Editions est un catalogue public de fontes réelles, téléchargeables et gratuites. La page emprunte au catalogue de caractères son efficacité — recherche, catégories et aperçu immédiat — sans reprendre l’identité d’un site tiers. La personnalité vient d’un établi graphique suisse contemporain : papier chaud, filets précis, index numéroté et deux voix typographiques très distinctes.

## Colors

- **Ink** assure le contraste structurel et les actions principales.
- **Paper** donne au catalogue une matière chaude sans effet nostalgique.
- **Surface** isole les spécimens et formulaires.
- **Ember** signale le geste et la sélection ; il reste réservé aux petits accents.
- **Acid** identifie les Open Editions gratuites et publiques.
- **Success** et **Danger** servent uniquement aux états de la démonstration.

## Typography

Les familles rappelées ne sont plus chargées par le site. Georgia structure les titres éditoriaux ; Arial garde les commandes sobres, robustes et locales. Toute réintroduction d’une fonte de spécimen exige une nouvelle contre-revue indépendante et un allowlist explicite.

## Layout

Le catalogue associe une tête éditoriale courte, un établi de contrôle et une pile de grandes fiches. La largeur maximale est de 1480 px. Les fiches utilisent un index latéral et une grille asymétrique, qui devient une seule colonne sous 900 px. À 390 px, chaque commande reste visible, les boutons atteignent 44 px et aucun contenu ne déborde du document.

## Elevation & Depth

La profondeur repose sur les bordures et l’alternance paper/surface. Une ombre courte est réservée aux dialogues. Aucun verre, dégradé technologique ou empilement gratuit de cartes.

## Shapes

Les angles sont presque droits : 2 px pour les boutons, 6 px pour les blocs, 14 px uniquement pour les dialogues. Les pastilles sont des marqueurs de statut, jamais une décoration répétitive.

## Components

- **Bande Open Edition :** statut public, gratuité et lien vers le parcours CHF 0.
- **Établi d’essai :** recherche, catégorie, texte direct, taille et modes titre/paragraphe/glyphes.
- **Fiche de famille :** vrai rendu WOFF2, version, couverture, limites, fiche détaillée et ZIP.
- **Parcours gratuit :** choix de la famille, coordonnées fictives, récapitulatif CHF 0, référence et téléchargement.
- **Admin :** indicateurs calculés, recherche, statut, détail et remise à zéro exacte.

## Do's and Don'ts

**À faire**
- Présenter uniquement les deux familles réellement publiées.
- Afficher SIL Open Font License 1.1, CHF 0 et l’absence de carte sans ambiguïté.
- Dire que les noms sont des labels d’édition et que la licence porte sur les fichiers.
- Maintenir focus visible, navigation clavier et réduction de mouvement.
- Conserver un état initial et final vide dans la démonstration.

**À éviter**
- Revendiquer une clearance de marque, un droit enregistré ou une titularité vérifiée.
- Inventer des styles, clients, volumes de téléchargement, notes ou traction.
- Employer les fontes display comme texte courant de l’interface.
- Copier l’esthétique distinctive d’un catalogue tiers.
- Demander une carte, appeler un service de paiement ou suggérer un débit réel.
