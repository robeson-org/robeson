"""Verify source fidelity and every built local link/fragment before publication."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib,json,re
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'migration/routes.json').read_text())
for entry in manifest:
 source=root/'migration/github-pages'/entry['source']; raw=source.read_text()
 assert hashlib.sha256(source.read_bytes()).hexdigest()==entry['sourceSha256'],entry['source']
 body=re.sub(r'^---\n.*?\n---\n','',raw,count=1,flags=re.S).lstrip('\n') if raw.startswith('---\n') else raw
 migrated=(root/entry['target']).read_text().split('---\n',2)[2].lstrip('\n')
 # Only the explicitly recorded link destinations may differ.
 changes={c['from']:c['to'] for c in entry['linkChanges']}
 expected=re.sub(r'\]\(([^)]+)\)',lambda m:']('+changes.get(m.group(1),m.group(1))+')',body)
 assert migrated==expected, 'Substantive or whitespace change: '+entry['source']
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=set();self.links=[];self.h1=0
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  if 'id' in attrs:self.ids.add(attrs['id'])
  if tag=='h1':self.h1+=1
  for key in ['href','src']:
   if key in attrs:self.links.append(attrs[key])
dist=root/'dist'; pages={}
for file in dist.rglob('*.html'):
 page=Page();page.feed(file.read_text());pages[file]=page
 if file.name!='404.html':assert page.h1==1, str(file)+' has '+str(page.h1)+' H1s'
count=0
for file,page in pages.items():
 for href in page.links:
  url=urlsplit(href)
  if url.scheme or url.netloc:continue
  path=unquote(url.path)
  target=(dist/path.lstrip('/')) if path.startswith('/') else file.parent/path if path else file
  if target.is_dir():target=target/'index.html'
  assert target.exists(),f'{file}: broken link {href}'
  if url.fragment and target in pages:assert unquote(url.fragment) in pages[target].ids,f'{file}: missing anchor {href}'
  count+=1
print(f'PASS: {len(manifest)} source bodies preserved; {len(pages)} pages; {count} local links/assets/fragments resolve; one H1 per page.')
