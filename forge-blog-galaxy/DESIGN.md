# DESIGN.md — Stack PME, projection G6

Source canonique : `../../../blogs/stack-pme/DESIGN.md`.

Cette projection associe le DESIGN.md revu aux fichiers exécutables du canari :

- `design-tokens.css` porte les couleurs, espacements, rayons, polices système et cible tactile de 44 px ;
- `tokens.json` expose le sous-ensemble contractuel contrôlé par les validateurs ;
- `styles.css` applique une composition mobile-first à 390 px, puis 8 colonnes à 768 px et 12 colonnes à 1440 px ;
- `assets/decision-ledger.svg` est une illustration locale originale du registre de décision ;
- les statuts `sourcé`, `jugement éditorial` et `à vérifier` utilisent un libellé en plus de la couleur ;
- `citron` est réservé au repère méthodique, jamais à une preuve produit inexistante ;
- la réduction de mouvement, le focus visible, la navigation clavier et l'absence de CDN sont obligatoires.

Le build reste dans `site.pending-gates/` et n'est pas publiable avant revue G7.
