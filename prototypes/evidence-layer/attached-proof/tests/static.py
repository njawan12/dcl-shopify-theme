"""Independent semantic/data/omission/budget/preservation checks."""
from pathlib import Path
from html.parser import HTMLParser
from copy import deepcopy
import ast,json,re,subprocess,sys
BASE=Path(__file__).resolve().parents[1];sys.path.insert(0,str(BASE))
from content import notes,pair,process,url,media,resolve,NOTE_FIELDS
from render import FIXTURES,DATA,render_page,render_host,render_notes,render_pair,render_process
count=0

def check(value,label):
    global count
    assert value,label;count+=1

class DOM(HTMLParser):
    def __init__(self,html):
        super().__init__();self.nodes=[];self.stack=[];self.feed(html)
    def handle_starttag(self,tag,attrs):
        n={'tag':tag,'attrs':dict(attrs),'text':'','parent':self.stack[-1] if self.stack else None};self.nodes.append(n)
        if tag not in ('img','meta','link','br','input','hr'):self.stack.append(n)
    def handle_endtag(self,tag):
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i]['tag']==tag:self.stack=self.stack[:i];break
    def handle_data(self,data):
        for node in self.stack:node['text']+=data
    def select(self,tag=None,klass=None):
        return [n for n in self.nodes if (tag is None or n['tag']==tag) and (klass is None or klass in n['attrs'].get('class','').split())]

check(len(FIXTURES)==32,'fixture inventory')
check(len(NOTE_FIELDS)==8,'note content cap')
for fid,f in FIXTURES.items():
    html=render_page(fid);d=DOM(html);ns=notes(f.get('notes'));pv=pair(f.get('pair')) if f['host']=='pdp' else None;ps=process(f.get('process'))
    if f['host']=='editorial' and ns:ps=None
    instances=f.get('instances',1)
    check(len(d.select(klass='evidence-note'))==len(ns)*instances,'valid note count '+fid)
    check(len(d.select(klass='pair'))==int(pv is not None)*instances,'pair omission '+fid)
    check(len(d.select(klass='step'))==(len(ps['steps']) if ps else 0)*instances,'valid process count '+fid)
    check(len(d.select(klass='comparison-row'))==(len(pv['rows']) if pv and pv['mode']=='comparison' else 0)*instances,'comparison rows '+fid)
    check(len(d.select(klass='paired-media'))==int(bool(pv and pv['mode']=='before-after'))*instances,'beforeafter '+fid)
    check(len(d.select(klass='app-slot'))==int(bool(f.get('app')))*instances,'app count '+fid)
    ids=[n['attrs']['id'] for n in d.nodes if 'id' in n['attrs']];check(len(ids)==len(set(ids)),'unique IDs '+fid)
    check(len(d.select('h1'))==1 and len(d.select('h2'))==instances,'heading hierarchy '+fid)
    check(not d.select('script'),'no runtime JS '+fid)
    check(DATA['disclaimer'] in html,'synthetic disclosure '+fid)
    check('STALE CONNECTED CONTENT' not in html,'no stale source '+fid)
    for n in d.select('a'):
        check(n['attrs'].get('href','')!='','no empty link')
        parent=n['parent']
        while parent:
            check(parent['tag'] not in ('a','button'),'no nested interactive controls');parent=parent['parent']
        href=n['attrs']['href'];check(not href.startswith('#') or href[1:] in ids,'actual fragment target')
    for n in d.select('img'):
        check(bool(n['attrs'].get('alt')),'meaningful image alt');check(int(n['attrs']['width'])>0 and int(n['attrs']['height'])>0,'reserved dimensions')
        check((BASE/n['attrs']['src'].lstrip('/')).is_file(),'media exists')
    for n in d.select(klass='steps'):
        check(n['tag']=='ol','ordered process');check(all(x['tag']=='li' for x in d.nodes if x['parent'] is n),'ol/li')
    # Each instance has independent source/heading targets and unmodified semantic order.
    for i in range(1,instances+1):
        host=render_host(f,i);check(host.index(f'id="evidence-{i}-subject"')<host.index('data-primitive=') if 'data-primitive=' in host else True,'subject before proof')
        if pv and ps:check(host.index('data-primitive="pair"')<host.index('data-primitive="process"'),'pair before process')
        if f['host']=='editorial':check(host.index('editorial-action')>host.index('subject'),'action after subject')

valid={'metric':{'value':'12 ml','label':'Capacity'},'fact':{'label':'Material','value':'Glass'},'claim':{'body':'Supplied statement'},'certification':{'label':'EXAMPLE','attribution':'Synthetic issuer'},'quote':{'body':'Editorial test quotation','attribution':'Fixture author'}}
required={'metric':['value','label'],'fact':['label','value'],'claim':['body'],'certification':['label','attribution'],'quote':['body','attribution']}
for kind,fields in valid.items():
    check(len(notes([{'kind':kind,**fields}]))==1,'valid '+kind)
    for key in required[kind]:
        n={'kind':kind,**fields};n[key]='';check(notes([n])==[],'missing '+kind+' '+key)
    check(set(notes([{'kind':kind,**fields,'extra':'ignored'}])[0])==set(NOTE_FIELDS),'fixed schema '+kind)
check(notes([{'kind':'unknown','body':'Text'}])==[],'unknown kind')
check(len(notes([{'kind':'fact','label':'Material','value':'Glass'}]*7))==3,'note cap')
p=deepcopy(FIXTURES['maximum']['pair']);p['rows']*=3;check(len(pair(p)['rows'])==4,'row cap')
s=deepcopy(FIXTURES['maximum']['process']);s['steps']*=3;check(len(process(s)['steps'])==4,'step cap')
for payload,normalize in [(FIXTURES['maximum']['pair'],pair),(FIXTURES['maximum']['process'],process),(FIXTURES['maximum']['notes'],notes)]:
    check(normalize({'connected':True,'source':payload})==normalize(payload),'same connected path')
    check(normalize({'connected':False,'source':payload,'manual':payload})==normalize(payload),'manual fallback')
    check(not normalize({'connected':False,'source':payload}),'disconnected omitted')
    check(not normalize({'connected':True,'source':None}),'missing connected source omitted')
ba=deepcopy(FIXTURES['before-after']['pair'])
for field in ('label','media','alt'):
    broken=deepcopy(ba);broken['items'][1][field]='';check(pair(broken) is None,'beforeafter missing '+field)
for n in (0,1,3):
    broken=deepcopy(ba);broken['items']=(ba['items']*2)[:n];check(pair(broken) is None,'exactly two beforeafter items')
for d in ('compact','balanced','spacious'):
    for emphasis in ('quiet','strong'):
        f=deepcopy(FIXTURES['branded-pdp']);f.update(density=d,emphasis=emphasis)
        h=render_host(f);check(f' {d} {emphasis}' in h,'existing density/emphasis control');check(len(DOM(h).select(klass='evidence-note'))==3,'controls never change data')
for value in ('','javascript:alert(1)','data:text/html,x','ftp://example.org/x','https://','https://example.org:bad','https://bad..host/x','https://-invalid.host/x','https://example.org:99999','https://user:password@example.org','//example.org/x','/pages/unknown','#missing','https://example.org/%0a','https://example.org/a b','https://example.org/%zz','/../pages/fixture-source'):
    check(url(value,{'subject':'evidence-1-subject'}) is None,'invalid URL '+value)
for value in ('https://example.org/a?x=1&y=2','http://example.org:8080/a','https://example.org/a%20b','/pages/fixture-source','/products/fixture-product','#subject'):
    check(url(value,{'subject':'evidence-1-subject'}) is not None,'valid URL '+value)
check(url('#subject',{'subject':'evidence-2-subject'})=='#evidence-2-subject','scoped URL')
html=render_notes(notes([{'kind':'fact','label':'<script>&"','body':'<img onerror=x>','source_title':'"<&','source_url':'https://example.org/?a=1&b=2'}]),'x',{})
check('<script>' not in html and '<img onerror' not in html and '&amp;b=2' in html,'context escaping')
check(media('../care-pump.jpg') is None and media('missing.jpg') is None,'confined media')
check('<ol class="steps"' in render_page('one-valid-step') and len(DOM(render_page('one-valid-step')).select(klass='step'))==1,'one step remains ordered')
check('<blockquote>' in render_page('long'),'quote semantics')
check('<dl>' in render_page('neutral-pdp') and '<dt>' in render_page('neutral-pdp') and '<dd>' in render_page('neutral-pdp'),'comparison semantics')
check(render_host(FIXTURES['app-removed'])==render_host(FIXTURES['branded-pdp']),'app removed no scar')
with_guest=render_host(FIXTURES['app-present'])
without_guest=re.sub(r'<aside class="app-slot".*?</aside>','',with_guest,flags=re.S)
check(re.sub(r'>\s+<','><',without_guest)==re.sub(r'>\s+<','><',render_host(FIXTURES['branded-pdp'])),'guest removal preserves all host content')
check(len(FIXTURES['localization']['introduction'])==len(FIXTURES['neutral-pdp']['introduction'])*1.5,'exact50percent expansion')
check((BASE/'index.html').read_text()==render_page(),'literal default parity')
css=(BASE/'evidence.css').read_text()
for bad in ('nth-child','grid-auto-flow:dense','overflow:hidden','overflow:clip','@import'):
    check(bad not in css,'CSS boundary '+bad)
check(css.count('@media(min-width:')==2,'two breakpoints')
check('focus-visible' in css and 'min-height:44px' in css and 'prefers-reduced-motion' in css,'focus/targets/motion')
check(not list(BASE.glob('*.js')),'zero runtimeJS files')
for path in BASE.glob('*.py'):ast.parse(path.read_text());check(True,'Python syntax '+path.name)
status=subprocess.check_output(['git','status','--porcelain','--untracked-files=all','-z']).decode().split('\0')
changed=subprocess.check_output(['git','diff','c92fc598a9016d75479b811b59c8fcd9275a1ea3','--name-only']).decode().splitlines()
check(all(path.startswith('prototypes/evidence-layer/attached-proof/') for path in changed+[entry[3:] for entry in status if entry]),'isolated Git scope')
for branch,expected in json.loads((BASE/'tests/evidence/preservation.json').read_text())['refs'].items():
    check(subprocess.check_output(['git','rev-parse',branch]).decode().strip()==expected,'preserved branch '+branch)
print(f'{count} PASS / 0 FAIL; 32 fixtures, 3 primitive renderers')
