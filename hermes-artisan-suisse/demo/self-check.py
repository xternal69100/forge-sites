from html.parser import HTMLParser
from pathlib import Path
import subprocess, tempfile
root=Path(__file__).resolve().parents[1]
files=[root/'index.html',root/'demo/index.html',root/'demo/admin.html']
class P(HTMLParser):
    def __init__(self): super().__init__(); self.scripts=[]; self.in_script=False
    def handle_starttag(self,tag,attrs):
        if tag=='script' and not dict(attrs).get('src'): self.in_script=True; self.scripts.append('')
    def handle_endtag(self,tag):
        if tag=='script': self.in_script=False
    def handle_data(self,data):
        if self.in_script: self.scripts[-1]+=data
for f in files:
    p=P(); p.feed(f.read_text()); p.close()
    for i,script in enumerate(p.scripts):
        path=root/'demo'/f'.check-{f.stem}-{i}.js'; path.write_text(script)
        try: subprocess.run(['node','--check',str(path)],check=True,capture_output=True)
        finally: path.unlink(missing_ok=True)
public=(root/'demo/index.html').read_text(); admin=(root/'demo/admin.html').read_text(); landing=(root/'index.html').read_text()
assert public.count('data-step="')==5
assert 'Mode démonstration — aucun débit réel' in public and 'Mode démonstration — aucun débit réel' in admin
assert 'hermes-artisan-suisse.demo.v1' in public and 'hermes-artisan-suisse.demo.v1' in admin
assert landing.count('href="demo/"')==3 and 'href="demo.html">' not in landing
assert (root/'demo.html').exists()
assert all(x not in public.lower() for x in ['todo','travaux restants','équipe dev','bug connu','décision interne'])
print('PASS html_parse=3 node_check=all landing_demo_links=3 shared_store=yes legacy_demo_preserved=yes disclosure=2')
