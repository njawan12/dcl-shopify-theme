"""Contract checks; never awards experiential accessibility or visual PASS."""
from pathlib import Path
from html.parser import HTMLParser
from copy import deepcopy
import sys,json,re,subprocess
BASE=Path(__file__).resolve().parents[1];sys.path.insert(0,str(BASE))
from fixtures import FIXTURES,WIDTHS,note
from content import normalize_note,normalize_pair,normalize_process,valid_url,media,NOTE_FIELDS
from render import page,render_notes,render_pair,render_process
checks=0
def check(value,label):
 global checks
 assert value,label
 checks+=1
class Document(HTMLParser):
 def __init__(self,html):super().__init__();self.elements=[];self.feed(html)
 def handle_starttag(self,tag,attrs):self.elements.append((tag,dict(attrs)))
check(len(FIXTURES)==38,'38 fixtures');check(len(WIDTHS)==8,'8 widths');check(len(NOTE_FIELDS)==8,'8 note content fields')
for name,f in FIXTURES.items():
 html=page(name);doc=Document(html);ids=[a['id'] for t,a in doc.elements if 'id' in a]
 check(len(ids)==len(set(ids)),name+' unique IDs')
 check(not any(t=='script' for t,a in doc.elements),name+' no runtime JS')
 check('synthetic test content' in html,name+' disclosed simulation')
 check(len(f['notes'])<=3,name+' note cap')
 check(all(k not in html for k in ['verified buyer','★','star-rating','rating-count']),name+' no fabricated review UI')
 check(sum(t=='article' and 'data-host' in a for t,a in doc.elements)==f['instances'],name+' instances')
 for tag,attrs in doc.elements:
  if tag=='a':check(valid_url(attrs['href'],ids)==attrs['href'],name+' structural link validity')
  if tag=='img':
   check(attrs.get('alt') and attrs.get('width') and attrs.get('height'),name+' image alternative/reservation')
   check(attrs.get('loading') in ('lazy','eager'),name+' image priority')
 check('http://' not in html and 'https://' not in html,name+' no third-party requests')
 check(f['density'] in ('compact','balanced','spacious'),name+' bounded density')
 process=normalize_process(f['process'])
 if process:check(len(process['steps'])<=4,name+' process cap')
 pair=normalize_pair(f['pair'])
 if pair and pair['mode']=='comparison':check(len(pair['rows'])<=4,name+' rows cap')
for kind,fields in [('metric',dict(value='1',label='test')),('fact',dict(label='test',body='test')),('claim',dict(body='test')),('certification',dict(label='test',attribution='issuer')),('quote',dict(body='test',attribution='author'))]:
 check(normalize_note(note(kind,**fields)) is not None,'valid '+kind)
 for required in {'metric':['value','label'],'fact':['label'],'claim':['body'],'certification':['label','attribution'],'quote':['body','attribution']}[kind]:
  n=note(kind,**fields);n[required]='';check(normalize_note(n) is None,'omit invalid '+kind+' '+required)
check(normalize_note({'kind':'unsupported'}) is None,'unknown kind')
check(normalize_note(FIXTURES['dynamic']['notes'][0])==normalize_note(FIXTURES['manual']['notes'][0]),'connected/manual parity')
check(normalize_note(FIXTURES['disconnected-fallback']['notes'][0])==normalize_note(FIXTURES['manual']['notes'][0]),'explicit fallback')
check(normalize_note(FIXTURES['disconnected-omit']['notes'][0]) is None,'disconnected omit')
check('999' not in page('disconnected-omit'),'no stale value')
check(normalize_pair(FIXTURES['before-after-incomplete']['pair']) is None,'missing before-after side')
check(normalize_pair(FIXTURES['comparison-incomplete']['pair']) is None,'no complete comparison rows')
p=deepcopy(FIXTURES['comparison']['pair']);p['rows'][0]['left']='';check(len(normalize_pair(p)['rows'])==1,'incomplete row omitted')
p['subjects'][1]='';check(normalize_pair(p) is None,'missing subject omitted')
check(len(normalize_process(FIXTURES['one-process']['process'])['steps'])==1,'one surviving step')
check('<ol class="rail process-rail" role="list"><li' in page('one-process'),'one-step ordered semantics')
check('<blockquote>' in page('long-quote'),'quote semantics')
check('scope="col"' in page('comparison') and 'scope="row"' in page('comparison'),'comparison semantics')
for value in ['javascript:alert(1)','data:text/html,x','//example.com','https://','https://x:bad','#missing','/x y','https://x/<script>','https://user:pass@x/']:
 check(not valid_url(value,('subject',)),'invalid rendering URL '+value)
for value in ['https://example.com/context','http://example.com/x','/products/object','#subject']:
 check(valid_url(value,('subject',))==value,'supported URL '+value)
check(not media('../media/care-pump.jpg') and not media('missing.jpg'),'invalid optional media')
malicious=note('quote',body='<script>alert("x")</script>',attribution='A & B')
html=render_notes([malicious],'test');check('&lt;script&gt;' in html and '<script>' not in html,'context escaped merchant text')
css=(BASE/'evidence.css').read_text()
for forbidden in ('nth-child','position:fixed','grid-auto-flow:dense','animation:','url(http'):
 check(forbidden not in css,'no forbidden CSS '+forbidden)
check(not re.search(r'(?:^|[;{])\s*order\s*:',css),'no responsive source reordering')
check(css.count('@media(min-width:')==2,'two responsive breakpoints')
liquid=(BASE/'app-host.liquid').read_text();schema=json.loads(liquid.split('{% schema %}')[1].split('{% endschema %}')[0])
check(schema['blocks']==[{'type':'@app'}],'generic @app without forbidden limit')
check("{% when '@app' %}" in liquid and '{% render block %}' in liquid,'real dispatch architecture')
check(schema['settings']==[] and len(schema['presets'])==1,'zero new seam settings')
check(page('app-absent').split('<main')[1].split('</main>')[0]==page('app-removed').split('<main')[1].split('</main>')[0],'removal retains evidence')
check((BASE/'index.html').read_text()==page(),'literal baseline parity')
preservation=json.loads((BASE/'tests/evidence/preservation.json').read_text())
repo=BASE.parents[2]
def git(*args):return subprocess.check_output(['git',*args],cwd=repo,text=True).strip()
for name,sha in preservation['refs'].items():check(git('rev-parse',name)==sha,'preserved ref '+name)
for line in git('ls-tree','-r',preservation['base']).splitlines():
 meta,path=line.split('\t');check(git('hash-object','--',path)==meta.split()[2],'preserved file '+path)
check(git('branch','--show-current')=='m1-evidence-layer-evidence-rail','isolated branch')
print(f'{checks} PASS / 0 FAIL; static/schema/content/preservation checks')
