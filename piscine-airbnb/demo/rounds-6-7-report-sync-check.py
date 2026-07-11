#!/usr/bin/env python3
"""Contrat TDD — synchronisation Round 7 avec le rapport partenaire 15."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARTNERS = ROOT / "partners.html"
REPORT = ROOT.parent.parent / "15-validation-marche-piscines-partenaires.md"


def require(source: str, *needles: str) -> None:
    for needle in needles:
        assert needle in source, f"élément absent: {needle}"


def main() -> int:
    page = PARTNERS.read_text(encoding="utf-8")
    assert "referencePrice:null" not in page and "scenarioPrice:null" not in page, "offres encore non chiffrées"
    assert REPORT.exists(), f"rapport source absent: {REPORT.name}"
    report = REPORT.read_text(encoding="utf-8")

    require(page,
        "Carte multi-entrées urbaine", "Pass saison / régional", "Offre wellness",
        "Source officielle", "Référence publique — aucune relation avec Poolbnb",
        "Prix scénario Poolbnb — hypothèse de démonstration",
        "Économie — hypothèse de démonstration",
        "Recommandation : affiliation avec redirection",
        "Aucune redirection, aucun lead et aucune commission réelle")
    assert page.count("Offre illustrative — aucun partenariat conclu") >= 3, "badge requis sur 3 offres"
    assert page.count("Simuler cette offre") == 1, "un seul libellé CTA dans le template dynamique"
    assert "referencePrice:null" not in page and "scenarioPrice:null" not in page, "offres encore non chiffrées"
    assert "Deux archétypes" not in page and "rapport 15 n’était pas disponible" not in page, "fallback obsolète encore public"
    assert page.count("id:'POF-DEMO-") == 3, "catalogue doit contenir exactement 3 archétypes"
    assert "href=\"http" not in page and "src=\"http" not in page, "lien ou ressource externe interdite"
    assert "logo" not in page.lower(), "logo/mention logo interdite"
    assert len(report.strip()) > 100, "rapport 15 vide ou incomplet"
    print("PASS report sync: 3 archétypes génériques, prix/scénarios hypothétiques, aucun flux réel")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
