# Démo client + administration locale

Cette maquette fonctionne avec deux pages statiques :

- `index.html` : choix de l'Édition Fondatrice Coach, configuration fictive, faux checkout, activation simulée ;
- `admin.html` : KPIs, souscriptions, workflows, filtres, détail, statuts, journal et reset ;
- `../demo.html` : console de preuve interne historique, conservée séparément du parcours client.

Les pages peuvent être ouvertes directement depuis le système de fichiers. Pour une vérification navigateur reproductible, un serveur statique local peut aussi être utilisé ; il ne constitue pas un backend applicatif.

## Contrat du store

Clé `localStorage` partagée et namespacée :

```text
forge:hermes-artisan-suisse:demo:v1
```

Forme validée à chaque lecture :

```js
{
  version: 1,
  subscriptions: [{
    id, company, contact, email, offer, price, monthlyPrice,
    paymentStatus, status, workflowId, createdAt
  }],
  workflows: [{
    id, subscriptionId, name, channel, cadence, hil, status, createdAt
  }],
  tasks: [{ id, subscriptionId, title, owner, status, due }],
  approvals: [{ id, subscriptionId, level, title, summary, status, createdAt }],
  journal: [{ id, at, type, subscriptionId, message }]
}
```

Un store absent ou malformé est remplacé et persisté par un `emptyStore` valide dont les cinq collections sont des tableaux vides. Aucune baseline ne représente un client et le reload ne réinjecte aucune donnée. Le formulaire refuse les emails qui ne finissent pas par le domaine réservé `.test`.

## États fictifs

- `ACTIF_SIMULÉ` : activation locale visible dans les KPIs ;
- `EN_PAUSE_SIMULÉE` : pause modifiable depuis le détail admin ;
- `CLOS_SIMULÉ` : clôture fictive ;
- `SIMULÉ — AUCUN DÉBIT` : statut de paiement immuable de la maquette.

Chaque création et changement de statut ajoute une entrée au journal local. L'événement navigateur `storage` rafraîchit l'administration lorsqu'une autre fenêtre modifie le store.

## Reset

`Vider le store de démo` ouvre une confirmation, puis remplace le store par des tableaux vides. Il ne supprime ni cookie distant, ni compte, ni paiement : il n'existe aucun système distant dans cette démo.

## Limites intentionnelles

- aucune carte bancaire ni champ assimilé ;
- aucun provider de paiement, backend, API, connecteur ou envoi ;
- aucune souscription, facture, activation ou donnée réelle ;
- persistance limitée au navigateur et à l'origine courante ;
- les données ne sont pas synchronisées entre appareils ou navigateurs ;
- Tailwind CDN et Google Fonts sont les seuls chargements réseau de présentation ; le parcours applicatif reste 100 % local ;
- le stockage `file://` dépend du navigateur : si celui-ci isole chaque fichier, utiliser un serveur statique local pour partager la même origine.

## Tests

Vérification statique locale :

```bash
cd site
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path
class Strictish(HTMLParser):
    def error(self, message): raise AssertionError(message)
for name in ('index.html', 'demo/index.html', 'demo/admin.html'):
    Strictish().feed(Path(name).read_text())
    print('HTML_PARSE PASS', name)
PY
node demo/check-demo.mjs
```

Le contrôle Node extrait chaque script inline des trois pages, exécute `node --check`, puis vérifie la clé partagée, la bannière obligatoire, les liens landing/client/admin/console et la présence de la console historique.

Scénario navigateur attendu depuis un store vide : landing → client → validation invalide → configuration `.test` → faux checkout → activation simulée → admin → persistance après reload → recherche/filtre/détail/statut → console interne → retour landing → reset du store. Contrôler aussi la console JavaScript, la largeur 390 px et les requêtes réseau.