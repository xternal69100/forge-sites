# Vérification — Forge Open Editions publiques

Date de contrôle : 13 juillet 2026. Portée : artefacts de release et site statique local.

## Publication construite

- **Elanovre Regular v1.000** : TTF, OTF CFF et WOFF2 ;
- **KeraVolt Optical Regular v1.100** : TTF, OTF CFF et WOFF2 avec GPOS ;
- deux ZIP publics comprenant chacun exactement les trois binaires, `OFL.txt` et `README-FR.md` ;
- catalogue avec les deux WOFF2 réellement chargées, recherche, catégories, texte éditable, corps et modes titre/paragraphe/glyphes ;
- parcours de démonstration gratuit à **CHF 0**, sans carte ni débit ;
- administration reliée au même store `forge:studio-typographique:demo:v1`, avec filtres, détail, statut et reset vide.

Les copies de release conservent les noms techniques des familles et versions. Leurs métadonnées publiques ont été alignées sur la release : copyright 2026, OFL 1.1 en name IDs 13/14 et `OS/2.fsType = 0`. Aucun Reserved Font Name n’est déclaré.

## Empreintes de release

### Elanovre

- `Elanovre-Regular.ttf` — `6bdbb174249edec2de480ccda3212cf471518f6b301df70bb1ee883d9ee6133f`
- `Elanovre-Regular.otf` — `01433752aaa46806660f35eae4978ee03488c255ba4c96e8dcb103bfb305413d`
- `Elanovre-Regular.woff2` — `b61bd6330074f3d25c7d2d47bd9916d44158984d0fc6a2af6862fe2374ca4a08`
- ZIP — `03d87e486b61be63f497b92e77e3aeabadb3a77cdd9354304c35e5fb5fa36512`

### KeraVolt Optical

- `KeraVoltOptical-Regular.ttf` — `0049c87b5df568a7f3cff992490318e7c3ff9123b4f3ac27c21091a14335e179`
- `KeraVoltOptical-Regular.otf` — `683e6a43149bd589f22a316e8c99e5d9c227ecac2d90f4f215ddd1d725c840b2`
- `KeraVoltOptical-Regular.woff2` — `b649534a3d04f24918474adda690007c0866a6077864d01a79db6d55153ea162`
- ZIP — `6eb5a29f2b6395977d5ca8d6b0a8e764fcd4729ec5361239f47b3cc1a5d9a2ba`

## Sorties exactes décisives

### DESIGN.md

```text
summary: errors 0, warnings 0, infos 1
Design system defines 11 colors, 6 typography scales, 3 rounding levels, 5 spacing tokens, 12 components.
```

Les exports `tokens.json` et `tailwind.theme.json` ont été régénérés après le dernier changement de design.

### Validateur public stdlib

Commande : `python3 site/verify_public_site.py`

```text
PUBLIC SITE PASS — 3 pages HTML, 36 liens locaux, 18 fichiers publics.
PACKAGES PASS — 2 ZIP, 6 binaires hashés, contenu exact 5/5, OFL 1.1 sans RFN déclaré.
STORE PASS — clé exacte, création CHF 0, persistance, statut, récupération et reset vide.
BASELINE PASS — store version 1 laissé vide par le harness.
```

Le comptage ci-dessus précède l’ajout du présent rapport ; le rejeu final couvre 19 fichiers publics.

### fontTools 4.63.0 dans le venv existant

```text
FONT PASS — Elanovre-Regular.otf: family='Elanovre'; version=1.000; outline=CFF; glyphs=143; cmap=142; fsType=0; OFL=yes
FONT PASS — Elanovre-Regular.ttf: family='Elanovre'; version=1.000; outline=glyf; glyphs=143; cmap=142; fsType=0; OFL=yes
FONT PASS — Elanovre-Regular.woff2: family='Elanovre'; version=1.000; outline=glyf; glyphs=143; cmap=142; fsType=0; OFL=yes
FONT PASS — KeraVoltOptical-Regular.otf: family='KeraVolt Optical'; version=1.100; outline=CFF; glyphs=169; cmap=168; fsType=0; OFL=yes
FONT PASS — KeraVoltOptical-Regular.ttf: family='KeraVolt Optical'; version=1.100; outline=glyf; glyphs=169; cmap=168; fsType=0; OFL=yes
FONT PASS — KeraVoltOptical-Regular.woff2: family='KeraVolt Optical'; version=1.100; outline=glyf; glyphs=169; cmap=168; fsType=0; OFL=yes
FONTTOOLS PASS — 6/6 binaires de release chargés lazy=False; noms techniques préservés; OFL embarquée; installation permise.
```

### Navigateur local sur `127.0.0.1:8765`

Catalogue desktop mesuré :

```text
clientWidth=1265; scrollWidth=1265; overflow=0
Elanovre loaded=true; KeraVolt Optical loaded=true
search "elanovre" => "1 famille"
mode glyphes => "Glyphes · 42 px"
```

Parcours client → admin :

```text
référence=OE-DEMO-MRJQVF2U; total=CHF 0; ZIP=../downloads/Elanovre-Open-Edition-v1.000.zip
admin: orders=1; value=CHF 0; status=Vérifiée; filtre sans résultat=0 résultat
reset: orders=0; rows=0; value=CHF 0
Démonstration réinitialisée : 0 référence, CHF 0.
```

La première automatisation de clic a seulement accusé réception sans changer l’étape ; le replay déterministe par `element.click()` a été utilisé, puis chaque postcondition a été contrôlée.

Probe responsive par iframe même origine, cadre demandé 390 px :

```text
/index.html       innerWidth=390; clientWidth=375; scrollWidth=375; overflow=0
/demo/index.html  innerWidth=390; clientWidth=375; scrollWidth=375; overflow=0
/demo/admin.html  innerWidth=390; clientWidth=375; scrollWidth=375; overflow=0
```

Les 15 px de différence correspondent à la barre de défilement du contexte mesuré ; aucune page ne déborde horizontalement. Console finale : **0 message, 0 erreur JavaScript**. Le serveur a répondu 200/304 aux pages, scripts, CSS et WOFF2 observés, sans 404.

## Frontière publique

Le scan public refuse les PNG QA, journaux, manifestes, SBOM, provenance, générateurs et spécimens de prépublication. Le site ne contient que les pages, styles/scripts nécessaires, deux WOFF2, deux ZIP, les artefacts de design, le validateur et ce rapport.

## Correction de release — 2026-07-13T21:51:02Z

Le replay indépendant de l’Orchestrateur a détecté puis corrigé une régression de filtrage : la règle auteur `.font-card { display:grid }` neutralisait l’affichage implicite de l’attribut HTML `hidden`. La feuille publique impose désormais `[hidden]{display:none!important}` et le validateur refuse toute suppression de cette règle.

Après rechargement forcé de la CSS :

```text
recherche KeraVolt => compteur 1 famille
Elanovre: hidden=true; display=none; height=0
KeraVolt Optical: hidden=false
mode Glyphes => 42 px; spécimen synchronisé
```

Le parcours a été rejoué après cette correction : référence fictive `OE-DEMO-MRJR9JRA`, total CHF 0, apparition admin 1/CHF 0, statut Nouvelle→Vérifiée, puis reset exact 0/CHF 0/0 ligne. Probe same-origin demandé à 390 px : `innerWidth=390`, `clientWidth=375`, `scrollWidth=375`, `overflow=0` sur catalogue, client et admin. Console finale : 0 message, 0 erreur JavaScript.

Le contrôle ZIP indépendant a ouvert les deux archives, obtenu `bad_member=null`, retrouvé exactement 5 fichiers par paquet et les SHA-256 publiés. Le texte OFL contient les cinq marqueurs structurels contrôlés de la version 1.1 ; l’endpoint SIL officiel a opposé Cloudflare aux téléchargements automatisés de cette session, donc aucune égalité octet-par-octet distante n’est revendiquée.

## Réserves

- Les noms sont des **labels d’édition**. Cette publication ne revendique ni clearance de marque, ni droit enregistré, ni titularité vérifiée.
- La SIL Open Font License 1.1 porte sur les fichiers distribués ; elle ne constitue pas un avis juridique ou une garantie d’absence de droits de tiers.
- La validation navigateur est locale. Aucune URL publique de production n’a été fournie pour contrôler une éventuelle propagation CDN après auto-publication.
- Le store a été laissé à sa baseline exacte : `{ "version": 1, "orders": [] }`.
