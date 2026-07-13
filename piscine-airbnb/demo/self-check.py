#!/usr/bin/env python3
"""Contrôles locaux, sans dépendance, des surfaces de démonstration Poolbnb."""
from __future__ import annotations

import re
import subprocess
import tempfile
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT.parent
PAGES = [SITE / "index.html", ROOT / "index.html", ROOT / "account.html", ROOT / "partners.html", ROOT / "guides.html", ROOT / "legal.html", ROOT / "admin.html"]
KEY = "forge:piscine-airbnb:demo:v1"
DISCLOSURE = "Mode démonstration — aucune donnée envoyée, aucun débit réel"
FORBIDDEN = [r"\bTODO\b", r"\bFIXME\b", r"reste à faire", r"équipe dev", r"bug connu"]


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "a" and values.get("href"):
            self.links.append(values["href"] or "")


def main() -> int:
    sources: dict[Path, str] = {}
    for path in PAGES:
        source = path.read_text(encoding="utf-8")
        parser = Parser()
        parser.feed(source)
        parser.close()
        sources[path] = source
        print(f"HTML OK {path.relative_to(SITE)}")

    client = sources[ROOT / "index.html"]
    member = sources[ROOT / "account.html"]
    host = member
    admin = sources[ROOT / "admin.html"]
    landing = sources[SITE / "index.html"]
    demos = [client, member, host, admin]
    assert all(KEY in source for source in (client, member, admin))
    assert all(DISCLOSURE in source for source in (client, member, admin))
    assert all(link in client for link in ('href="account.html"', 'href="guides.html"', 'href="admin.html"'))
    assert 'href="index.html"' in admin
    assert landing.count('href="demo/"') >= 3
    combined = "\n".join(sources.values())
    assert all(item in combined for item in ("LST-DEMO-001", "HST-DEMO-", "BKG-DEMO-260711-001"))
    assert all(not re.search(pattern, combined, re.I) for pattern in FORBIDDEN)
    print(f"CONTRACT OK key={KEY} landing_demo_links={landing.count('href=\"demo/\"')}")

    scripts: list[tuple[str, str]] = []
    for path in PAGES:
        for number, (attrs, script) in enumerate(re.findall(r"<script([^>]*)>(.*?)</script>", sources[path], re.S), 1):
            if script.strip() and 'type="application/json"' not in attrs:
                scripts.append((f"{path.name}-{number}", script))
    with tempfile.TemporaryDirectory() as tmp:
        for name, script in scripts:
            js = Path(tmp) / f"{name}.js"
            js.write_text(script, encoding="utf-8")
            result = subprocess.run(["node", "--check", str(js)], capture_output=True, text=True, check=False)
            if result.returncode:
                raise SystemExit(result.stderr)
            print(f"JS OK {name}")
    print(f"PASS {len(PAGES)} pages, {len(scripts)} scripts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
