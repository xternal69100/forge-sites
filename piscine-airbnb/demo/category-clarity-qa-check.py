#!/usr/bin/env python3
"""QA renforcée : clarté 3 secondes, métadonnées et libellés pool-first."""
from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path

DEMO = Path(__file__).resolve().parent
SITE = DEMO.parent
PAGES = [SITE / "index.html", *sorted(DEMO.glob("*.html"))]
LANDING = SITE / "index.html"
CLIENT = DEMO / "index.html"
OLD_REAL_ESTATE_NAMES = ("Villa Panorama", "Maison des Vignes")


class MetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.title = ""
        self.description = ""
        self.images: list[dict[str, str | None]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "meta" and values.get("name", "").lower() == "description":
            self.description = values.get("content") or ""
        elif tag == "img":
            self.images.append(values)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data


def normalized(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().casefold()


def main() -> int:
    sources = {path: path.read_text(encoding="utf-8") for path in PAGES}
    combined = "\n".join(sources.values())

    for page in (LANDING, CLIENT):
        source = sources[page]
        badge = source.index("LOCATION DE PISCINE PRIVÉE")
        hour = source.index("à l’heure ou à la journée", badge)
        lodging = source.index("jamais un hébergement", hour)
        assert badge < hour < lodging, f"{page.name}: ordre du message 3 secondes incorrect"
        assert "text-sm" in source or "font-size:13px" in source, f"{page.name}: badge catégorie trop petit/non spécifié"
        assert "bg-ink" in source or "background:var(--ink)" in source, f"{page.name}: contraste du badge non garanti"

    landing = sources[LANDING]
    client = sources[CLIENT]
    assert 'class="flex flex-col justify-start"' in landing, "landing: message 3 secondes repoussé sous le viewport desktop"
    assert "image-fallback::after" in landing and "Piscine privée" in landing.split("image-fallback::after", 1)[1].split("}", 1)[0], "landing: fallback hero ne nomme pas la piscine privée"
    assert re.search(r'id="heroImage"[\s\S]*?alt="[^"]*Piscine privée', landing), "landing: alt hero non pool-first"
    assert "<figure class=\"photo pool-fallback\"" in client, "demo: fallback sémantique du hero absent"
    assert "LOCATION DE PISCINE PRIVÉE" in client.split('<figure class="photo pool-fallback">', 1)[1].split("</figure>", 1)[0], "demo: overlay catégorie absent du hero"

    assert all(name not in combined for name in OLD_REAL_ESTATE_NAMES), "anciens noms immobiliers encore présents"
    for forbidden in (
        ">Voir le lieu<",
        ">Pré-réserver ce lieu<",
        ">Voir la vitrine<",
        "lieux correspondent à vos filtres",
        "Choisir un lieu, comprendre les règles",
        "Comment un lieu devient publiable",
        "avant de proposer un lieu",
    ):
        assert forbidden not in landing, f"landing: libellé non pool-first: {forbidden}"

    for path, source in sources.items():
        parser = MetadataParser()
        parser.feed(source)
        title = normalized(parser.title)
        description = normalized(parser.description)
        assert "piscine" in title, f"{path.name}: title ne nomme pas la piscine"
        assert "piscine" in description, f"{path.name}: meta description ne nomme pas la piscine"
        assert "sans hébergement" in description, f"{path.name}: meta description n’exclut pas l’hébergement"
        for image in parser.images:
            assert normalized(image.get("alt") or ""), f"{path.name}: image sans alt utile"

    assert 'role="dialog"' in landing and 'aria-modal="true"' in landing and 'aria-labelledby="modalTitle"' in landing, "landing: modale catalogue non annoncée comme dialogue"
    print(f"PASS category clarity QA: {len(PAGES)} surfaces, message 3 secondes, metadata, fallback, labels et dialogue")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
