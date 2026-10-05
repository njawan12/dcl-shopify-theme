from pathlib import Path
import sys,copy,json
B=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(B/'extensions'))
from purchase import with_support
from story import product_note
from model import PRODUCTS,truth
from render import purchase
results=[]
def check(name,value):
 results.append({'test':name,'pass':bool(value)})
for pid,choices in [('daily-cleanser',[]),('balancing-formula',[]),('balancing-formula',['60 ml','Rich']),('balancing-formula',['30 ml','Rich']),('balancing-formula',['30 ml','Light'])]:
 p=PRODUCTS[pid];before=copy.deepcopy(p)
 h,t=with_support(p,choices,'balanced',{'body':'Read <merchant> context','label':'Details'})
 check(pid+str(choices)+' shared truth',t==truth(p,choices))
 check(pid+str(choices)+' preserved purchase',h.startswith(purchase(p,choices,'balanced')))
 check(pid+str(choices)+' immutable',p==before)
 check(pid+str(choices)+' native disclosure',h.count('<details class="purchase-support">')==1 and '&lt;merchant&gt;' in h)
check('support omission',with_support(PRODUCTS['daily-cleanser'],[],'balanced')[0]==purchase(PRODUCTS['daily-cleanser'],[],'balanced'))
check('story canonical identity','Daily cleansing milk' in product_note('daily-cleanser','Ordinary context'))
check('story canonical destination','href="/products/daily-cleanser"' in product_note('daily-cleanser','Context'))
check('story escape','&lt;script&gt;' in product_note('daily-cleanser','<script>'))
check('story missing reference omitted',product_note('missing','Context')=='')
check('story empty omitted',product_note('daily-cleanser','')=='')
check('story vertical reuse','href="/products/jewelry-1"' in product_note('jewelry-1','Materials'))
(B/'tests/evidence/extensions-results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'pass':sum(x['pass'] for x in results),'fail':sum(not x['pass'] for x in results)}))
assert all(x['pass'] for x in results)
