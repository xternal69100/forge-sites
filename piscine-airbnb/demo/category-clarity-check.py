#!/usr/bin/env python3
"""Contrat de clarté catégorie Poolbnb : piscine privée, jamais hébergement."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path

DEMO = Path(__file__).resolve().parent
SITE = DEMO.parent
PUBLIC_PAGES = [SITE / "index.html", *sorted(DEMO.glob("*.html"))]
HERO = "Louez une piscine privée à l’heure ou à la journée"
SCOPE = "Vous louez la piscine et ses espaces autorisés — jamais la villa, jamais un hébergement"
BAD_NAMES = ("Villa Panorama", "Maison des Vignes")
DISCLOSURE = "Mode démonstration — aucune donnée envoyée, aucun débit réel"


class Parser(HTMLParser):
    pass


def main() -> int:
    sources: dict[Path, str] = {}
    for path in PUBLIC_PAGES:
        source = path.read_text(encoding="utf-8")
        Parser().feed(source)
        sources[path] = source
        print(f"HTML OK {path.relative_to(SITE)}")

    landing = sources[SITE / "index.html"]
    demo = sources[DEMO / "index.html"]
    combined = "\n".join(sources.values())

    for name, source in (("landing", landing), ("demo", demo)):
        assert HERO in source, f"{name}: H1 explicite absent"
        assert SCOPE in source, f"{name}: périmètre sans hébergement absent"
        assert "LOCATION DE PISCINE PRIVÉE" in source, f"{name}: badge catégorie absent"
        assert "🏊" in source, f"{name}: pictogramme piscine absent"
        assert "Voir les piscines à louer" in source, f"{name}: CTA explicite absent"
        assert "Ce que vous réservez" in source, f"{name}: section pédagogique absente"
        for item in ("Piscine privée", "Plage ou terrasse autorisée", "Créneau", "villa, nuitée, logement"):
            assert item in source, f"{name}: détail de périmètre absent: {item}"

    assert "Piscine privée · créneau de ${" in landing and " h · sans hébergement" in landing, "landing: ligne constante des cartes absente"
    assert "Piscine privée · créneau de 4 h · sans hébergement" in demo, "demo: ligne constante des cartes absente"
    assert all(name not in combined for name in BAD_NAMES), "ancien nom immobilier présent dans une surface publique/store seed"
    assert "Pas l’“Airbnb des piscines”" not in landing and "Pas l’Airbnb des piscines" not in landing, "formulation contradictoire présente"
    assert DISCLOSURE in demo, "disclaimer de démonstration absent"
    assert "Aucun moyen de paiement n’est demandé" in demo, "disclaimer checkout absent"

    print(f"PASS category clarity: {len(PUBLIC_PAGES)} surfaces, héros explicites, cartes pool-first, zéro ancien nom")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
