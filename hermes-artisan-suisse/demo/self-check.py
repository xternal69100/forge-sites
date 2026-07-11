from html.parser import HTMLParser
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[1]
files = [root / 'index.html', root / 'demo/index.html', root / 'demo/admin.html']

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.scripts = []
        self.in_script = False
    def handle_starttag(self, tag, attrs):
        if tag == 'script' and not dict(attrs).get('src'):
            self.in_script = True
            self.scripts.append('')
    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_script = False
    def handle_data(self, data):
        if self.in_script:
            self.scripts[-1] += data

script_count = 0
for html_file in files:
    parser = Parser()
    parser.feed(html_file.read_text(encoding='utf-8'))
    parser.close()
    for index, script in enumerate(parser.scripts):
        check_file = root / 'demo' / f'.check-{html_file.stem}-{index}.js'
        check_file.write_text(script, encoding='utf-8')
        try:
            subprocess.run(['node', '--check', str(check_file)], check=True, capture_output=True, text=True)
            script_count += 1
        finally:
            check_file.unlink(missing_ok=True)

public = (root / 'demo/index.html').read_text(encoding='utf-8')
admin = (root / 'demo/admin.html').read_text(encoding='utf-8')
landing = (root / 'index.html').read_text(encoding='utf-8')
key = 'forge:hermes-artisan-suisse:demo:v1'
for page in (public, admin):
    assert key in page and 'localStorage' in page
    assert 'Mode démonstration — aucun débit réel' in page
assert public.count('data-step="') >= 4
assert all(term not in public.lower() for term in ['todo', 'reste à faire', 'équipe dev', 'bug connu', 'backlog', 'non branché'])
assert landing.count('href="demo/"') == 3
assert 'href="demo.html">' not in landing
assert 'href="admin.html"' in public and 'href="index.html"' in admin
assert all(word in admin for word in ['Centre d’approbations', 'File de tâches', 'Journal d’activité', 'detailStatus', 'confirmReset'])
assert all(word in public for word in ['tasks', 'approvals', 'ACTIVATION_SIMULÉE'])
assert (root / 'demo.html').exists()
print(f'PASS html_parse=3 node_check={script_count} landing_demo_links=3 shared_store=yes hil_admin=yes legacy_console=yes disclosure=2')
