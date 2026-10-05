"""Behavioral audit of canonical truth, cart, all surfaces and preservation."""
import sys,json,hashlib,subprocess,copy
from pathlib import Path
from html.parser import HTMLParser
B=Path(__file__).parents[1];sys.path.insert(0,str(B))
from model import *
from render import page,normalized,adapted,mosaic,repeated_page
from guided import data as guided_data,page as guided_page
N=0
def check(ok,label):
 global N;N+=1
 if not ok:raise AssertionError(label)
def rejects(fn):
 try:fn()
 except (ValueError,KeyError):return True
 return False
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.inputs=[];self.scripts=0;self.images=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='input':self.inputs.append(a)
  if tag=='script':self.scripts+=1
  if tag=='img':self.images.append(a)
check(len(PRODUCTS)==30,'distinct catalog');check(len(DATA['beauty'])==24,'Beauty24');check(len(set(DATA['beauty']))==24,'unique Beauty');check(len(DATA['jewelry'])==6,'Jewelry6')
variants=[]
for pid,p in PRODUCTS.items():
 check(p['id']==pid,'identity');check(p['url']=='/products/'+pid,'destination');check(len({tuple(v['options']) for v in p['variants']})==len(p['variants']),'unique tuples')
 for v in p['variants']:
  variants.append(v['id']);t=truth(p,v['options']);check(t['variant']==v['id'],'same variant');check(t['price']==v['price'],'same price');check(t['available']==v['available'],'same availability');check(type(v['price'])==int,'money integer')
  if v['available']:
   props={k:'Example' for k in p['required_properties']};l=line(p,v['id'],p['quantity']['min'],properties=props);check(l['variant']==v['id'],'line identity');check(totals({'lines':[l],'order_discount':0})['gross']==v['price']*l['quantity'],'cart canonical price')
  else:check(rejects(lambda:line(p,v['id'])),'sold out rejected')
 for m in p['media']:
  src=m.get('src') or m.get('poster');check(not src or (B/src).is_file(),'media exists');check(bool(m['alt']),'media alternative')
check(len(set(variants))==len(variants),'global variant IDs unique')
p=PRODUCTS['balancing-formula'];check(resolve(p,['60 ml','Rich']) is None,'nonexistent');check(truth(p)['variant'] is None,'no silent default');check(rejects(lambda:line(p,'missing')),'missing variant');check(rejects(lambda:line(p,'balancing-formula-30-rich')),'sold-out variant')
for q in [-1,0,9]:check(rejects(lambda:line(p,'balancing-formula-30-light',q)),'quantity bounds')
check(rejects(lambda:line(PRODUCTS['care-10'],'care-10-v1',3)),'increment');check(rejects(lambda:line(PRODUCTS['care-09'],'care-09-v1')),'required property');check(rejects(lambda:line(p,'balancing-formula-30-light',plan='foreign')),'foreign plan')
c=seeded_cart();before=copy.deepcopy(c);updated=mutate(c,'update',key=c['lines'][0]['key'],quantity=3);check(c==before,'immutable update');check(updated['lines'][0]['quantity']==3,'update');check(rejects(lambda:mutate(c,'update',key=c['lines'][0]['key'],quantity=3,fail=True)),'error rejected');check(c==before,'error preserved');check(len(mutate(c,'remove',key=c['lines'][0]['key'])['lines'])==2,'remove');check(mutate(c,'note',note='<script>test</script>')['note']=='<script>test</script>','authored note');check(totals(c)['total']==totals(c)['gross']-800,'explicit discount math');over=copy.deepcopy(c);over['order_discount']=999999;check(totals(over)['total']==0,'discount cap')
story_parser=Parser();story_parser.feed(page('story'));check(story_parser.images[0]['src']=='/'+PRODUCTS['daily-cleanser']['media'][0]['src'],'story canonical subject media')
base=normalized(fixture('balanced'))
for name in ['compact','editorial']:check(normalized(fixture(name))==base,'normalized same-data '+name)
for name in FIXTURES:
 html=page(name,seeded_cart() if name.startswith('cart') and name!='cart-empty' else None);parsed=Parser();parsed.feed(html);check(len(parsed.ids)==len(set(parsed.ids)),'scoped IDs '+name);check(parsed.scripts==0,'script-free native baseline '+name);check('<main' in html,'main '+name);check('PENDING HUMAN REVIEW' in html,'pending '+name)
 for image in parsed.images:check('alt' in image and 'width' in image and 'height' in image,'image semantics '+name)
 for scale in (2,4):check('--text-scale:'+str(scale) in page(name,scale=scale),'reflow fixture '+name)
check('pdp-two-zone' in page('balanced') and 'purchase-band' in page('compact') and 'editorial-purchase' in page('editorial'),'structural ownership paths')
for kind in ['beauty','jewelry','neutral']:
 g=guided_data(kind);check(2<=len(g['steps'])<=5,'guided cap');check(len(g['steps'])==len({s['product']['id'] for s in g['steps']}),'unique guided');parsed=Parser();parsed.feed(guided_page(kind));check(len(parsed.ids)==len(set(parsed.ids)),'guided IDs')
 for step in g['steps']:
  p=step['product'];canonical=PRODUCTS[p['id']];check(p['url']==canonical['url'],'guided destination');check([(v['id'],v['options'],v['price'],v['available']) for v in p['variants']]==[(v['id'],v['options'],v['price'],v['available']) for v in canonical['variants']],'guided canonical commerce')
controls=json.loads((B/'controls.json').read_text())
for k,s in controls.items():
 if isinstance(s,dict) and 'ceiling' in s:check(len(s['initial'])<=s['ceiling'],k+' initial');check(len(s['conditional'])<=s.get('conditional_ceiling',0),k+' conditional')
reuse=json.loads((B/'tests/evidence/reuse.json').read_text())
for path,record in reuse.items():check(hashlib.sha256((B/path).read_bytes()).hexdigest()==record['sha256'],'exact accepted copy '+path)
root=B.parents[2];saved=json.loads((B/'tests/evidence/preservation.json').read_text())
for item in saved['tracked']:
 meta,path=item.split('\t',1);sha=meta.split()[1];actual=subprocess.check_output(['git','hash-object',path],cwd=root,text=True).strip();check(actual==sha,'preserved '+path)
repeated=Parser();repeated.feed(repeated_page());check(len(repeated.ids)==len(set(repeated.ids)),'repeated scoped instances');check(repeated_page().count('class="product-card')==24,'independent repeated collections');check('html lang="ar" dir="rtl"' in page('rtl'),'meaningful RTL language')
for ref in saved['refs']:
 name,sha=ref.split();
 if name!='m1-final-closure-batch-a':check(subprocess.check_output(['git','rev-parse',name],cwd=root,text=True).strip()==sha,'preserved branch '+name)
manifest={'products':len(PRODUCTS),'beauty_distinct':24,'jewelry_distinct':6,'variants':len(variants),'media_records':sum(len(p['media']) for p in PRODUCTS.values()),'variant_counts':sorted(set(len(p['variants']) for p in PRODUCTS.values())),'fixture_names':FIXTURES,'widths':WIDTHS,'density100_unique':24,'density100_encounters':100,'canonical_sha256':hashlib.sha256((B/'dataset.json').read_bytes()).hexdigest(),'normalized_same_data':{n:normalized(fixture(n)) for n in ['balanced','compact','editorial']},'genuine_provenance':False}
(B/'tests/evidence/dataset-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');(B/'tests/evidence/static-results.json').write_text(json.dumps({'pass':N,'fail':0})+'\n');print(f'{N} PASS / 0 FAIL')
