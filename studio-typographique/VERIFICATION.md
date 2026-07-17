# Vérification publique — release `studio-open-5-20260717`

**Exécutée :** 2026-07-17T18:12:01Z
**Destination :** `xternal69100/forge-sites/studio-typographique/`

## Catalogue

- 7 Open Editions publiques au total ;
- 5 nouvelles éditions dans cette release : Cervalune, Modulune System, Brisacline Display, Hexavox Mono V2 et Riftora Experimental ;
- 7 WOFF2 chargés par Chromium ;
- 7 ZIP, chacun composé exactement de TTF, OTF CFF, WOFF2, `OFL.txt` et `README-FR.md` ;
- SIL Open Font License 1.1, aucun Reserved Font Name déclaré ;
- labels d’édition provisoires, aucune clearance de marque ou titularité vérifiée revendiquée.

## Gates déterministes

```text
PUBLIC SITE PASS — 3 pages HTML, 51 liens locaux, 29 fichiers publics.
PACKAGES PASS — 7 ZIP, 21 binaires hashés, contenu exact 5/5, OFL 1.1 sans RFN déclaré.
STORE PASS — clé exacte, création CHF 0, persistance, statut, récupération et reset vide.
BASELINE PASS — store version 1 laissé vide par le harness.
PROJECT_ISOLATION_OK projects=5 allowlist=0
```

## Runtime Chromium

- mobile 390×844 : `clientWidth=390`, `scrollWidth=390`, aucune barre horizontale ;
- desktop 1440×900 : `clientWidth=1440`, `scrollWidth=1440` ;
- `document.fonts.check(...)` : 7/7 ;
- filtre Hexavox : 1 carte visible ;
- dialogue Hexavox : ouvert et fermé ;
- parcours Hexavox : référence locale, CHF 0, bon ZIP ;
- admin : 1 ligne Hexavox puis reset à 0 ;
- erreurs JavaScript : 0 ;
- requêtes échouées : 0.

## Empreintes ZIP des cinq nouvelles éditions

| ZIP | SHA-256 |
|---|---|
| `Cervalune-Open-Edition-v1.100.zip` | `13ac22852ca8e19edb582db6be1344cf2a25599009d00d27321ced683d5123d7` |
| `Modulune-System-Open-Edition-v1.000.zip` | `5440ebd2049ad7b320e831202f47700f6100221594369aa65041501b003515ef` |
| `Brisacline-Display-Open-Edition-v1.000.zip` | `d6e87180feef895ef343754bb870a8f3205c9727a07fe8eb4bf506b838ffa985` |
| `Hexavox-Mono-V2-Open-Edition-v1.100.zip` | `1f7179f695af9036e0873d49e5c8b2c4432f8c52c3b265c95e8b03b8edf7c5b6` |
| `Riftora-Experimental-Open-Edition-v1.000.zip` | `49887ee97f4434f2789a39514d8f975a3f572ec6a58a5582a96e9a0400a93bd0` |
