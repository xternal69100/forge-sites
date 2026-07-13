# Démonstrateur coach — Studio Office (`coach-office-v2`)

## Surfaces

- `../index.html` — landing commerciale Telegram-first. Elle présente l’**offre fondatrice** CHF 300 d’installation + CHF 150/mois et précise qu’il ne s’agit pas du tarif standard.
- `index.html` — parcours client fictif : offre → exactement 2 rendez-vous d’onboarding d’1 h → activation des 8 domaines → checkout simulé → confirmation.
- `admin.html` — cockpit de la coach : agenda, CRM, prospects, inbox, marketing, devis/factures, pré-compta, tâches, approbations, journal, KPIs, filtres, détail et reset vide.
- `../demo.html` — console de preuve **interne**, accessible depuis l’admin seulement et non promue comme démonstration client.
- `transaction.html` — route de compatibilité vers le nouveau parcours.

## Contrat de données

Le client et l’admin partagent exclusivement le store local versionné :

```text
forge:coach-office:demo:v2
```

Le store vide est valide. Le checkout simulé génère un jeu déterministe de fixtures synthétiques : identités marquées `Démo`, adresses réservées `.test`, aucune donnée de santé, aucune carte et aucun appel réseau. Le reset supprime toute souscription et remet tous les tableaux à zéro.

## Approvals & Telegram

La simulation Telegram est visuelle et locale. Les commandes `/aujourdhui`, `/clients`, `/factures`, `/contenu` et `/priorites` lisent le store. Les boutons **Valider / Modifier / Refuser** modifient une approbation locale et ajoutent une entrée au journal. Aucun message n’est envoyé.

## Validation statique

Depuis `site/demo/` :

```bash
python3 validate.py
```

Le validateur :

1. parse toutes les surfaces HTML ;
2. extrait les scripts inline et lance `node --check` ;
3. vérifie `app.js` avec `node --check` ;
4. contrôle le store v2 partagé, les 8 domaines, les 2 rendez-vous et les mentions de simulation ;
5. interdit les appels réseau applicatifs et les coordonnées hors `.test` dans les fixtures ;
6. interdit l’ancienne mention tarifaire canonique sur landing, client et admin ;
7. vérifie que la console interne existe mais n’est pas promue depuis landing/client.

## Replay navigateur attendu

1. Effacer `forge:coach-office:demo:v2`.
2. Ouvrir `index.html` et suivre les 5 étapes.
3. Choisir exactement 2 rendez-vous, activer les 8 domaines, cocher la confirmation et activer.
4. Ouvrir `admin.html` ; contrôler les 10 domaines et les 4 KPIs.
5. Lancer `/contenu`, prendre une décision et vérifier le journal.
6. Recharger ; vérifier la persistance.
7. Filtrer, rechercher et ouvrir un détail.
8. Confirmer **Reset vide** et vérifier l’état vide.
9. Mesurer à 390 px : `document.documentElement.scrollWidth === document.documentElement.clientWidth` sur landing, client et admin.
10. Vérifier console et ressources : zéro erreur, aucune requête applicative hors fichiers statiques locaux.

Tout le contenu sous `site/` est public : ne jamais y ajouter d’identité réelle, de secret, de donnée de santé ou de coordonnées actives.
