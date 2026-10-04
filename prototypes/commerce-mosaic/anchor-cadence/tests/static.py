"""Behavioral rendering/planning checks, independently of visual acceptance."""
from html.parser import HTMLParser
from pathlib import Path
from copy import deepcopy
import ast
import json
import re
import subprocess
import sys
BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE))
from planner import plan
from render import DATA, FIXTURES, PRODUCTS, image_html, money, render_card, render_collection, render_page, result_sequence, truth
count=0

def check(condition,name):
    global count
    assert condition,name
    count+=1

class Document(HTMLParser):
    def __init__(self,html):
        super().__init__();self.nodes=[];self.stack=[];self.feed(html)
    def handle_starttag(self,tag,attrs):
        n={'tag':tag,'attrs':dict(attrs),'text':'','ancestors':self.stack.copy()};self.nodes.append(n)
        if tag not in ('img','meta','link','input','br','hr'):self.stack.append(n)
    def handle_endtag(self,tag):
        if self.stack and self.stack[-1]['tag']==tag:self.stack.pop()
    def handle_data(self,s):
        for n in self.stack:n['text']+=s
    def cls(self,name):return [n for n in self.nodes if name in n['attrs'].get('class','').split()]
    def tags(self,name):return [n for n in self.nodes if n['tag']==name]

def inside(node,parent):return parent in node['ancestors']
def field(doc,card,cls):return [n['text'] for n in doc.cls(cls) if inside(n,card)]
def card_truths(doc):
    return [([n['attrs']['href'] for n in doc.cls('product-link') if inside(n,c)],*[field(doc,c,x) for x in ('price','status','compare','unit','badge','options','vendor')],[n['text'] for n in doc.tags('h3') if inside(n,c)]) for c in doc.cls('product-card')]

check(len(PRODUCTS)>=24 and len(set(p['id'] for p in PRODUCTS.values()))==len(PRODUCTS),'distinct fixture products')
check(len(DATA['fixtures'])==len(FIXTURES)==43,'unique collection fixture inventory')
allowed={'id','label','products','title','description','preset','rhythm','feature_source','density','editorial','filter','sort','page','page_size','instances'}
for f in DATA['fixtures']:
    check(set(f)<=allowed,'semantic inputs only; no arbitrary placement controls')
    html=render_page(f['id']);doc=Document(html);result=result_sequence(f);instances=f.get('instances',1)
    check(len(doc.cls('product-card'))==len(result['items'])*instances,'truthful rendered result count')
    check([n['attrs']['data-product'] for n in doc.cls('product-card')]==[i['key'] for i in result['items']]*instances,'source order exactly follows collection result sequence')
    ids=[n['attrs']['id'] for n in doc.nodes if 'id' in n['attrs']]
    check(len(ids)==len(set(ids)),'scoped unique IDs across instances')
    check(len(doc.tags('h1'))==1 and len(doc.tags('h2'))==instances,'logical document/collection headings')
    check(not doc.tags('script'),'no runtime script or layout engine')
    check(all(not any(a['tag']=='a' for a in n['ancestors']) for n in doc.tags('a')),'no nested interactive links')
    for section in doc.cls('collection'):
        cards=[n for n in doc.cls('product-card') if inside(n,section)]
        feature=[i for i,c in enumerate(cards) if 'feature' in c['attrs']['class'].split()]
        _,_,p=render_collection(f)
        check(feature==([p['feature_index']] if p['feature_index'] is not None else []),'one deterministic nonduplicated anchor')
        editorials=[n for n in doc.cls('editorial') if inside(n,section)]
        check(len(editorials)==int(p['editorial_after'] is not None),'editorial only with restoration space')
        check(all('data-product' not in n['attrs'] for n in editorials),'editorial not marked as product')
        if editorials:
            children=[n for n in doc.nodes if n['tag']=='li' and inside(n,section)]
            check(children.index(editorials[0])==9,'story follows nine products, with at least three restoring products')
        check(len(cards)-int(p['editorial_after'] or len(cards))>=0,'no orphan story')
    fallback=deepcopy(f);fallback['rhythm']='standard';ordinary=Document(render_collection(fallback)[0])
    check(not ordinary.cls('feature') and not ordinary.cls('editorial'),'first-class Standard Grid omits interruptions')
    primary=Document(render_collection(f)[0])
    check(card_truths(primary)==card_truths(ordinary),'feature/standard preserve price/state/compare/unit/destination/title/order truth')
    for img in doc.tags('img'):
        check((BASE/img['attrs']['src'].lstrip('/')).is_file(),'existing local media')
        check(bool(img['attrs'].get('alt')) and int(img['attrs']['width'])>0 and int(img['attrs']['height'])>0,'meaningful media alt/intrinsic size')
    for card in doc.cls('product-card'):
        check(card['tag']=='li' and card['ancestors'][-1]['tag']=='ul','native list/list-item relation')

for product in PRODUCTS.values():
    doc=Document(render_card(product,'same',1,1,False));featured=Document(render_card(product,'same',1,1,True))
    check(card_truths(doc)==card_truths(featured),'same renderer: every product truth invariant under feature treatment')
    for v in product['variants']:
        check(type(v['price']) is int and v['price']>=0,'integer nonnegative product money')
check(truth(PRODUCTS['represented'])['price']=='CAD 36.00' and not truth(PRODUCTS['represented'])['available'],'explicit represented variant, not arbitrary fallback')
check(' – ' in truth(PRODUCTS['complex'])['price'] and 'choose options' in truth(PRODUCTS['complex'])['status'],'unresolved multi-option range and safe navigation')
check(truth(PRODUCTS['beauty-8'])['compare']=='CAD 38.00','valid compare-at only')
check(truth(PRODUCTS['beauty-1'])['compare'] is None,'no empty sale shell')
check(truth(PRODUCTS['beauty-3'])['unit']=='CAD 44.00 / 100 g','unit price exact fixture truth')
check('Image unavailable' in image_html(None) and '<img' not in image_html({'src':'../bad.jpg'}),'missing/unsafe media safe omission')
check(result_sequence(FIXTURES['deleted'])['total']==12,'deleted/unpublished references excluded from count')
check(result_sequence(FIXTURES['filtered-one'])['total']==1,'filter to one result')
check(result_sequence(FIXTURES['empty-filter'])['total']==0,'no-results filter')
check(result_sequence(FIXTURES['page-after'])['start']==0 and result_sequence(FIXTURES['page-two'])['start']==12,'truthful page boundary')
check(render_collection(FIXTURES['page-two'])[2]=={'feature_index':None,'editorial_after':None},'no repeated page-two interruptions')
check(len(FIXTURES['localized']['description'])*2==len(FIXTURES['neutral']['description'])*3,'exact 50 percent copy expansion')
check((BASE/'index.html').read_text()==render_page(),'literal default uses shared renderer')
check(render_page('unknown')==render_page(),'unknown fixture safe default')
f=deepcopy(FIXTURES['branded']);f['title']='<script>x</script>'
check('&lt;script&gt;' in render_collection(f)[0],'escape authored HTML')
for n in range(105):
    for rhythm in ('anchor','standard'):
        for feature in (False,True):
            for editorial in (False,True):
                for start in (0,6,12):
                    p=plan(n,rhythm,feature,editorial,start)
                    check(p==plan(n,rhythm,feature,editorial,start),'planner deterministic')
                    check(p['feature_index'] is None or (p['feature_index']>=3 and p['feature_index']<n),'baseline encounters before anchor')
                    check(p['editorial_after'] is None or n-p['editorial_after']>=3,'rhythm restoration after editorial')
                    check(p['editorial_after'] is None or p['feature_index'] is not None,'no orphan interruption')
# The planner has only bounded scalar inputs and no data/image/fixture dependency.
source=(BASE/'planner.py').read_text();tree=ast.parse(source)
check(not any(isinstance(n,(ast.Import,ast.ImportFrom,ast.Subscript)) for n in ast.walk(tree)),'planner cannot inspect product IDs or aesthetics')
check(set(plan.__code__.co_varnames)<= {'count','rhythm','feature','editorial','page_start','active'},'no hidden planner/fixture inputs')
css=(BASE/'mosaic.css').read_text()
check(not re.search(r'nth-child|nth-of-type|grid-auto-flow\s*:\s*dense|overflow\s*:\s*(hidden|clip)',css),'no index exceptions, visual reordering, or clipping')
check(not any(re.search(r'\.'+re.escape(f['id'])+r'(?:\s|\{|:)',css) for f in DATA['fixtures'] if f['id'] not in ('neutral','jewelry','food','compact','spacious','standard')),'no fixture-specific CSS')
check('object-fit: contain' in css and ':focus-visible' in css and '44px' in css and 'prefers-reduced-motion' in css,'media/focus/target/motion baseline')
check(not re.search(r'https?://|@import|@font-face',css) and not list(BASE.glob('*.js')),'no external font/dependency/browser JS')
for file in BASE.glob('*.py'):
    ast.parse(file.read_text());check(True,'Python source syntax')
status=subprocess.check_output(['git','status','--porcelain','-z','--untracked-files=all'],cwd=BASE,text=True)
check(all(s[3:].startswith('prototypes/commerce-mosaic/anchor-cadence/') for s in status.split('\0') if s),'isolated working-tree scope')
print(f'PASS: {count} static/render/planner assertions; {len(PRODUCTS)} products, {len(FIXTURES)} collection fixtures.')
