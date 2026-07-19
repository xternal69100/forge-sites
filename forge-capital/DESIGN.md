---
version: clair-capital-v2
name: Forge Capital — cockpit humain
reference: Seline Analytics via Refero
theme: Bureau d’analyste calme sur papier chaud
colors:
  paper: "#F7F6F2"
  surface: "#FFFFFF"
  ink: "#202124"
  muted: "#6E706F"
  line: "#DEDDD7"
  cyan: "#00A9C7"
  cyanSoft: "#DFF7FB"
  danger: "#B73A3A"
  dangerSoft: "#FFF0EE"
  warning: "#9B6713"
  warningSoft: "#FFF5DB"
  success: "#24704A"
  successSoft: "#E8F5ED"
fonts:
  sans: "Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, Segoe UI, Arial, sans-serif"
  mono: "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
---

# Direction

Le cockpit **clair-capital-v2** reprend le système Refero de **Seline Analytics** : fond chaud, cartes blanches, encre sombre, bordures fines, typographie sans-serif et cyan réservé aux actions et à la donnée fraîche. L’objectif n’est plus de simuler un terminal, mais de rendre une décision financière difficile compréhensible en moins d’une minute.

## North star

> Un bureau d’analyste calme où l’utilisateur sait immédiatement combien d’argent est réel, quelles tactiques sont encore étudiées et pourquoi le trading live reste autorisé ou interdit.

## Hiérarchie obligatoire

1. **Décision d’activation** — réponse textuelle, jamais seulement une couleur.
2. **Argent** — autorisé, reçu, observé et valeur nette séparés.
3. **Qualité vs préparation** — deux indicateurs qui ne sont jamais moyennés.
4. **Tactiques** — statut, preuve, conclusion et prochaine étape.
5. **Gates live** — sept conditions conjonctives.
6. **Apprentissages** — les échecs restent des résultats utiles.
7. **Actions suivantes** — ordre clair, sans promesse de rendement.

## Règles de vérité

- `ON-CHAIN LIVE` désigne uniquement une observation réussie de l’API publique Hyperliquid.
- `PAPER` ne devient jamais capital, P&L réel, ordre ou fill.
- `DIFFÉRÉ` efface les valeurs live plutôt que de conserver silencieusement un ancien prix.
- `EXÉCUTÉ AVEC PREUVE` appartient au faux parcours local et exige une fixture complète.
- `CASH/NOOP` reste champion tant qu’un gate échoue.
- Le score qualité projet ne mesure ni edge, ni probabilité de gain, ni trading readiness.

## Composition

- Sidebar stable et compacte ; navigation en français.
- Largeur de lecture généreuse, sans mur de widgets.
- Verdict sombre unique comme point focal.
- Quatre KPI essentiels seulement.
- Tactiques en lignes scannables ; détail dans une modale.
- Gates en liste, pas en jauge décorative.
- Mobile : une colonne, aucun débordement horizontal.

## Do

- Utiliser des phrases courtes et concrètes.
- Afficher la preuve et la source à côté de la conclusion.
- Réserver le cyan à la navigation, à la donnée fraîche et aux étapes actives.
- Employer rouge, ambre et vert avec un libellé textuel.
- Garder les surfaces opaques et les séparateurs fins.

## Don’t

- Aucun ticker animé, bande Matrix, faux flux d’activité ou terminal théâtral.
- Aucun gradient, glassmorphism, halo ou violet SaaS.
- Aucun score financier inventé.
- Aucun sigle non expliqué comme titre principal.
- Aucun contrôle navigateur pour signer, transmettre ou trader.

## Surfaces

- `site/index.html` — accueil et verdict synthétique.
- `site/demo/index.html` — dashboard principal.
- `site/demo/transaction.html` — parcours local complet sans provider réel.
- `site/demo/admin.html` — filtres et journal local.
- `site/data/public-snapshot.json` — projection publique allowlistée.
