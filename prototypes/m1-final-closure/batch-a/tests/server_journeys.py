"""Real loopback GET/POST state proof, independent cookie jars for instance isolation."""
import sys,json,re,urllib.request,urllib.error,http.cookiejar
from pathlib import Path
from urllib.parse import urlencode
B=Path(__file__).parents[1];sys.path.insert(0,str(B))
from model import PRODUCTS,FIXTURES,truth,money
N=0;events=[]
def check(ok,label):
 global N;N+=1
 if not ok:raise AssertionError(label)
def client():return urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
a=client();b=client()
def request(path,data=None,c=a):
 try:
  with c.open('http://127.0.0.1:3005'+path,None if data is None else urlencode(data).encode()) as r:return r.status,r.read().decode()
 except urllib.error.HTTPError as r:return r.code,r.read().decode()
def keys(html):return re.findall('data-line="([^"]+)"',html)
for f in FIXTURES:
 code,html=request('/?fixture='+f);check(code==200,'route '+f);check('data-fixture="'+f+'"' in html,'fixture identity '+f);check('PENDING HUMAN REVIEW' in html,'pending '+f)
for pid,p in PRODUCTS.items():
 code,html=request(p['url']);t=truth(p);check(code==200,'product '+pid);check('data-product="'+pid+'"' in html,'same product');check(t['display_price'] in html,'canonical product price');check(('data-variant="unresolved"' in html)==bool(p['options']),'no silent option default')
 for v in p['variants']:
  q={'product':pid,'fixture':'compact'};q.update({'option-'+str(i):s for i,s in enumerate(v['options'])});code,html=request('/?'+urlencode(q));check(code==200,'native resolve');check('data-variant="'+v['id']+'"' in html,'native tuple');check(money(v['price']) in html,'native price')
code,html=request('/?fixture=cart-empty');check(not keys(html),'empty')
code,html=request('/action',{'action':'add','product':'balancing-formula','variant':'balancing-formula-30-light','quantity':'2'});check(len(keys(html))==1,'add');check('30 ml / Light' in html,'variant identity');key=keys(html)[0]
events.append({'state':'added','lines':keys(html)})
code,html=request('/action',{'action':'update','key':key,'quantity':'3','fail':'1'});check('role="alert"' in html,'failed alert');check('value="2" min="0"' in html,'failure preserved quantity');events.append({'state':'failed unchanged','lines':keys(html)})
code,html=request('/action',{'action':'update','key':key,'quantity':'3'});check('value="3" min="0"' in html,'recovery quantity');check(money(8700) in html,'recovered money');events.append({'state':'recovered','lines':keys(html)})
code,html=request('/action',{'action':'add','product':'care-08','variant':'care-08-v1','quantity':'1','plan':'monthly-care'});check('Purchase plan: monthly-care' in html,'plan identity');check(len(keys(html))==2,'second line')
code,html=request('/action',{'action':'add','product':'care-09','variant':'care-09-v1','quantity':'1','property-0':'For <Alex>'});check('Recipient note: For &lt;Alex&gt;' in html,'escaped property');check(len(keys(html))==3,'third line')
saved=keys(html)
for data in [
 {'action':'add','product':'balancing-formula','variant':'balancing-formula-30-rich','quantity':'1'},
 {'action':'add','product':'balancing-formula','variant':'missing','quantity':'1'},
 {'action':'add','product':'care-10','variant':'care-10-v1','quantity':'3'},
 {'action':'add','product':'care-09','variant':'care-09-v1','quantity':'1'},
 {'action':'add','product':'care-08','variant':'care-08-v1','quantity':'1','plan':'foreign'},
 {'action':'update','key':key,'quantity':'99'},
 {'action':'update','key':'absent','quantity':'1'}]:
 code,html=request('/action',data);check('role="alert"' in html,'ineligible action rejected');check(keys(html)==saved,'no mutation on rejection')
code,html=request('/action',{'action':'note','note':'<script>fixture</script>'});check('&lt;script&gt;fixture&lt;/script&gt;' in html,'escaped note');check('<script>fixture</script>' not in html,'no active note script')
code,html=request('/action',{'action':'remove','key':key});check(key not in keys(html),'remove');check(len(keys(html))==2,'remaining lines');events.append({'state':'removed','lines':keys(html)})
code,html=request('/cart',c=b);check(not keys(html),'independent second browser/session');code,html=request('/cart');check(len(keys(html))==2,'first session unaffected')
code,html=request('/?fixture=cart-populated');check('Fixture line discounts' in html and 'Fixture order discount' in html,'explicit discounts');check('Continue to checkout explanation' in html,'checkout hierarchy')
code,html=request('/checkout-preview');check('No payment, inventory reservation or Shopify checkout occurred.' in html,'truthful checkout end')
for kind in ['beauty','jewelry','neutral']:
 code,html=request('/guided?fixture='+kind);check(code==200,'guided route');check('<noscript>' in html,'literal native fallback');check('/reuse/guided/split-tension.js' in html,'exact existing enhancement')
for path in ['/products/missing','/../dataset.json','/dataset.json','/model.py']:
 check(request(path)[0]==404,'bounded route '+path)
for path in ['/tokens.css','/system.css','/reuse/mosaic/mosaic.css','/reuse/rail/evidence.css','/reuse/guided/split-tension.js']:
 check(request(path)[0]==200,'local asset '+path)
report={'pass':N,'fail':0,'events':events,'scope':'Real local HTTP requests; no Shopify network or checkout.'};(B/'tests/evidence/http-results.json').write_text(json.dumps(report,indent=2)+'\n');print(f'{N} PASS / 0 FAIL')
