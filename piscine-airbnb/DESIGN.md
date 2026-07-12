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
  trust-gate:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.lg}"
    padding: 24px
  status-active:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.surface}"
    rounded: "{rounded.full}"
    padding: 10px
  status-planned:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.full}"
    padding: 10px
  qualification-check:
    backgroundColor: "{colors.info}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    padding: 16px
  workspace-nav:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.surface}"
    rounded: "{rounded.full}"
    padding: 12px
  dossier-step:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    padding: 16px
  event-journal:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    padding: 16px
  status-conditional:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.full}"
    padding: 10px
  price-breakdown:
    backgroundColor: "{colors.info}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    padding: 16px
  price-total:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.surface}"
    typography: "{typography.headline-md}"
    rounded: "{rounded.md}"
    padding: 16px
  credit-ledger:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    padding: 16px
  referral-status:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    padding: 16px
  confirmation-dialog:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.lg}"
    padding: 24px
  partner-offer:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.lg}"
    padding: 24px
  partner-model-disclosure:
    backgroundColor: "{colors.info}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    padding: 16px
  partner-checkout:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.lg}"
    padding: 24px
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

### Règle de clarté catégorie — pool-first

La catégorie doit être comprise en moins de trois secondes, y compris en lecture rapide ou à basse acuité visuelle. Chaque surface publique est **pool-first, jamais villa-first** :

- le hero commence par un gros libellé contrasté avec pictogramme `🏊` : **LOCATION DE PISCINE PRIVÉE** ;
- le H1 nomme explicitement la location d’une piscine privée **à l’heure ou à la journée** ;
- la phrase immédiatement visible précise : **« Vous louez la piscine et ses espaces autorisés — jamais la villa, jamais un hébergement »** ;
- le CTA principal dit **« Voir les piscines à louer »** ;
- les cartes portent des noms centrés sur le bassin ou la piscine, jamais sur la villa, maison ou résidence, et répètent une ligne stable : **« Piscine privée · créneau de X h · sans hébergement »** ;
- une section proche du hero résume ce qui est réservé (piscine, plage/terrasse autorisée, créneau) et ce qui est exclu (villa, nuitée, logement) ;
- aucun jargon stratégique comme « supply-first » ou « trust-first » ne doit précéder cette explication de catégorie au-dessus de la ligne de flottaison.

- Le hero doit combiner **promesse**, **CTAs**, **preuves de cadrage** et **aperçu produit**.
- Les grandes sections alternent entre fond neutre, surfaces blanches et blocs encre pour installer un tempo.
- Les éléments de filtre, scorecards et mocks doivent rester extrêmement lisibles dès 375px.
- Les chips, toggles et boutons utilisent une rondeur totale (`full`) pour garder un aspect doux et haut de gamme.

## Elevation & Depth

La profondeur doit être douce, jamais clinquante. On privilégie :

- une **fine ligne de contour** sur les cartes claires ;
- des **ombres diffuses** pour les cartes premium et les modales ;
- des **halos colorés subtils** dans les zones hero ou CTA ;
- des fonds dégradés ou “water glow” à très faible intensité comme solution de repli derrière les photographies.

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
- **trust-gate** : carte blanche calme pour matérialiser une étape de publication ; quatre cartes reliées montrent le passage droit de proposer → confirmation d’assurance écrite → revue sécurité → GO limité.
- **status-active** : pastille vert lac à texte blanc, réservée aux artefacts opérationnels effectivement rédigés et utilisables comme projets pilotes.
- **status-planned** : pastille neutre à texte encre pour les capacités non branchées ou encore soumises à validation humaine.
- **qualification-check** : ligne interactive vert très pâle pour la mini-checklist propriétaire ; la sélection reste strictement locale au navigateur et ne collecte aucune donnée.
- **workspace-nav** : navigation compacte et persistante entre marketplace, espace membre, espace loueur et administration.
- **dossier-step** : carte de progression pour le dossier hôte, les checklists de types/statuts et la visite simulée ; aucun contrôle d’upload.
- **event-journal** : journal chronologique append-only, lisible dans les espaces loueur et admin.
- **status-conditional** : pastille chaude réservée aux décisions conditionnelles, toujours non publiables.
- **price-breakdown** : ventilation calme et ordonnée `sous-total → réduction → crédit → total`, visible avant et après confirmation ; les montants CHF utilisent toujours deux décimales.
- **price-total** : ancrage tarifaire dominant des cartes, du checkout, de la confirmation et des espaces membre/admin. Il affiche en grand le **total du groupe pour le créneau**, avec la durée et la capacité incluse sur la même lecture. La mention **« frais obligatoires inclus »** est immédiatement adjacente. La ventilation **« soit CHF X/personne à 4 »** est calculée et strictement secondaire : le prix par personne n’est jamais le titre, le bouton, le filtre principal ni un « dès ».
- **Règle tarifaire transversale** : toutes les surfaces utilisent `prix hôte + frais invité = total avant promo`, où les frais invité valent `min(CHF 18 ; max(CHF 6 ; 8 % × prix hôte))`. Le total groupe/créneau frais inclus précède toute promotion. Le pack suit exclusivement `total avant promo → −20 % → −CHF 20 → total final`, sans réduire le revenu hôte (`90 % × prix hôte`). La durée par défaut est 2 h, les extensions et suppléments de groupe restent explicites, et la seule modulation temporelle est `week-end +15 %` — jamais de surge.
- Tous les montants Poolbnb sont libellés **« hypothèses de démonstration »** : aucune carte, réservation, ventilation ou KPI ne doit être interprété comme un vrai tarif, une transaction ou de la traction.
- **credit-ledger** : liste append-only des écritures promotionnelles et de parrainage. Le type, le statut, le montant, la date et la référence objet restent lisibles sans faire passer un crédit fictif pour de l'argent.
- **referral-status** : carte d'état agrégé sans identité ni activité du filleul, avec actions locales de copie et de simulation clairement séparées.
- **confirmation-dialog** : dialogue HTML modal accessible, titré, descriptif et testable, utilisé notamment à la place des confirmations natives pour les actions destructrices.
- **partner-offer** : carte d’archétype sans marque ni logo ; le badge d’absence de partenariat, le modèle commercial, les conditions et la provenance du prix de référence restent visibles avant toute action.
- **partner-model-disclosure** : panneau distinguant sans ambiguïté affiliation, apporteur d’affaires et revente ; dans la démo, aucun redirect, lead ou flux réel n’est activé.
- **partner-checkout** : dialogue de simulation sans moyen de paiement, récapitulant quantité, total, comparaison calculée seulement si les deux prix sont sourcés, vendeur/modèle hypothétique et absence de transmission.

Les espaces membre et loueur sont des surfaces distinctes. Ils réutilisent les cartes, chips et statuts mais n’exposent que des alias et adresses `example.test`. Les montants de portefeuille, crédits, réservations et revenus sont explicitement simulés.

Les composants doivent rendre visibles les signaux de confiance : labels “hôte vérifié”, “règles claires”, “créneau calme”, “programme founding host”, etc.

Toute architecture trust/safety doit distinguer visuellement et textuellement :

- ce qui existe comme **document ou processus pilote** (charte, questionnaire/screening, matrice incident) ;
- ce qui n’est **pas encore actif dans le produit public** (paiement, protection secondaire, annonces réelles) ;
- une revue Poolbnb d’une certification, d’une garantie de sécurité ou d’une confirmation de couverture.

### Direction photographique

Les images installent un luxe calme, local et crédible : architecture soignée, eau naturelle, lumière matinale ou dorée, végétation mature et horizons lémaniques. Les cadrages évitent toute énergie “pool party”, toute foule et toute mise en scène ostentatoire. Puisque le catalogue est une démo, les photographies sont toujours présentées comme des **visuels d’ambiance** et jamais comme la preuve de lieux réellement disponibles.

- Le hero utilise un cadrage cinématographique `16:9`, lisible sans texte directement posé sur les zones détaillées de la photo.
- Les annonces et la modale utilisent un ratio stable `4:3` avec `object-cover` ; le sujet principal doit rester visible au centre sur mobile comme sur desktop.
- Chaque image porte un alt text descriptif utile, des dimensions intrinsèques et un décodage asynchrone ; les vignettes hors écran sont chargées en lazy-loading.
- Un dégradé tokenisé reste sous chaque image. En cas d’asset absent ou illisible, il devient le fallback visuel et conserve la lisibilité des informations de l’annonce.
- Ne jamais intégrer de texte, logo, donnée personnelle ou preuve sociale inventée dans une photographie.

## Do's and Don'ts

- Do réserver `primary` aux actions majeures et aux micro-moments de tension positive.
- Do utiliser `tertiary` pour tout ce qui parle de confiance, qualification, support et exécution.
- Do maintenir un contraste AA minimum sur toutes les zones textuelles et boutons.
- Do garder les sections premium aérées et peu chargées.
- Do signaler explicitement le statut de visuel d’ambiance pour cette démo.
- Do qualifier chaque GO comme limité aux paramètres et à la version du dossier examinés.
- Do préciser que les interactions de qualification sont locales, sans envoi ni conservation de données.
- Don’t transformer le site en univers “pool party”.
- Don’t employer plus de deux graisses simultanément dans une même petite carte.
- Don’t utiliser des bleus saturés ou des couleurs additionnelles non définies dans les tokens.
- Don’t publier des preuves sociales inventées ; préférer signaux opératoires, cohortes pilotes et preuves de cadrage réelles.
- Don’t employer « assuré », « certifié » ou « sécurité garantie » sans préciser exactement l’auteur, le périmètre, les conditions et le statut réel de la validation.
