"""Single canonical fixture truth and transactional simulated cart. No Shopify APIs."""
from pathlib import Path
import json,copy,hashlib
BASE=Path(__file__).parent;DATA=json.loads((BASE/'dataset.json').read_text());PRODUCTS=DATA['products'];WIDTHS=[320,375,390,430,768,1024,1280,1440]
FIXTURES=['balanced','compact','editorial','balanced-neutral','compact-neutral','editorial-neutral','simple','sold-out','nonexistent','long','short','missing','many-media','rich-media','manual','structured','disconnected','rtl','plan','properties','pickup','app','collection12','collection24','collection100','cart-empty','cart-populated','cart-error','story','story-neutral']
def money(value):
 if type(value)!=int or value<0:raise ValueError('Nonnegative integer money required')
 return f'CAD {value//100:,}.{value%100:02d}'
def resolve(product,choices=None):
 choices=choices or [];v=next((v for v in product['variants'] if v['options']==choices),None)
 if product['options'] and len(choices)!=len(product['options']):v=None
 return v

def truth(p,choices=None):
 v=resolve(p,choices);prices=[x['price'] for x in p['variants']]
 return {'product':p['id'],'variant':v['id'] if v else None,'tuple':v['options'] if v else [],'price':v['price'] if v else None,'display_price':money(v['price']) if v else 'From '+money(min(prices)),'compare':v.get('compare_at') if v and (v.get('compare_at') or 0)>v['price'] else None,'unit':v.get('unit_price') if v else None,'available':v['available'] if v else False,'status':('Available' if v['available'] else 'Sold out') if v else 'Choose every option; this combination is not purchasable yet.','url':p['url']}

def line(p,variant,quantity=1,plan='',properties=None):
 v=next((v for v in p['variants'] if v['id']==variant),None);rules=p['quantity'];properties=properties or {}
 if not v or not v['available']:raise ValueError('Choose an available real variant.')
 if type(quantity)!=int or quantity<rules['min'] or quantity>rules['max'] or (quantity-rules['min'])%rules['increment']:raise ValueError('Quantity does not meet fixture bounds/increments.')
 if plan and plan not in [s['id'] for s in p['plans']]:raise ValueError('This plan does not belong to this product.')
 if any(not properties.get(k,'').strip() for k in p['required_properties']):raise ValueError('Complete the required line information.')
 if any(k not in p['required_properties'] for k in properties):raise ValueError('Unsupported line property.')
 identity=json.dumps([p['id'],v['id'],plan,sorted(properties.items())],ensure_ascii=False)
 return {'key':hashlib.sha256(identity.encode()).hexdigest()[:16],'product':p['id'],'variant':v['id'],'quantity':quantity,'plan':plan,'properties':properties,'discount':0}

def new_cart():return {'lines':[],'note':'','order_discount':0,'message':''}
def mutate(cart,action,**fields):
 nextcart=copy.deepcopy(cart)
 if fields.get('fail'):raise ValueError('Simulated update failure. Previous cart is unchanged; retry is available.')
 if action=='add':
  p=PRODUCTS[fields['product']];incoming=line(p,fields['variant'],int(fields['quantity']),fields.get('plan',''),fields.get('properties',{}));old=next((l for l in nextcart['lines'] if l['key']==incoming['key']),None)
  if old:
   incoming=line(p,incoming['variant'],old['quantity']+incoming['quantity'],incoming['plan'],incoming['properties']);incoming['discount']=old['discount'];nextcart['lines'][nextcart['lines'].index(old)]=incoming
  else:nextcart['lines'].append(incoming)
 elif action in ('update','remove'):
  old=next((l for l in nextcart['lines'] if l['key']==fields['key']),None)
  if not old:raise ValueError('Line is no longer present. Review the cart.')
  q=0 if action=='remove' else int(fields['quantity'])
  if q==0:nextcart['lines'].remove(old)
  else:
   replacement=line(PRODUCTS[old['product']],old['variant'],q,old['plan'],old['properties']);replacement['discount']=old['discount'];nextcart['lines'][nextcart['lines'].index(old)]=replacement
 elif action=='note':nextcart['note']=str(fields.get('note',''))[:1000]
 else:raise ValueError('Unknown simulated action.')
 nextcart['message']='Simulated cart updated.';return nextcart

def totals(cart):
 gross=net=0
 for l in cart['lines']:
  p=PRODUCTS[l['product']];v=next(v for v in p['variants'] if v['id']==l['variant']);amount=v['price']*l['quantity'];gross+=amount;net+=max(0,amount-min(amount,max(0,l['discount'])))
 order=min(net,max(0,cart['order_discount']));return {'gross':gross,'line_discount':gross-net,'order_discount':order,'total':net-order}

def seeded_cart():
 c=new_cart();c['lines']=[line(PRODUCTS['balancing-formula'],'balancing-formula-30-light',2),line(PRODUCTS['care-08'],'care-08-v1',1,'monthly-care'),line(PRODUCTS['care-09'],'care-09-v1',1,properties={'Recipient note':'For Alex · synthetic'})];c['lines'][0]['discount']=300;c['order_discount']=500;c['note']='Please keep the fictional recipient note with this order.';return c

def fixture(name):
 name=name if name in FIXTURES else 'balanced';p=copy.deepcopy(PRODUCTS['balancing-formula']);layout=name.split('-')[0] if name.split('-')[0] in ('balanced','compact','editorial') else 'balanced';f={'name':name,'layout':layout,'preset':'neutral' if 'neutral' in name else 'beauty','product':p,'choices':['30 ml','Light'],'dir':'rtl' if name=='rtl' else 'ltr','binding':'connected' if name=='structured' else 'disconnected' if name=='disconnected' else 'manual','scale':1}
 switches={'simple':'daily-cleanser','sold-out':'care-12','missing':'care-16','plan':'care-08','properties':'care-09','pickup':'care-11','app':'care-13'}
 if name in switches:f['product']=copy.deepcopy(PRODUCTS[switches[name]]);f['choices']=[]
 if name=='nonexistent':f['choices']=['60 ml','Rich']
 if name=='long':p['title']+=' — '+('Detailed product and source information for unfamiliar care routines '*3);p['description']*=6;p['evidence'][0]['source_title']='Long synthetic source context '*18
 if name=='rtl':p['title']='صيغة العناية اليومية';p['description']='معلومات واضحة عن المنتج وطريقة الاستخدام. هذا محتوى تجريبي خيالي، وليس دليلاً على الفعالية.'
 if name=='short':p['title']='Care';p['description']='';p['faq']=[];p['recommendations']=[]
 if name not in ('many-media','rich-media'):f['product']['media']=f['product']['media'][:4]
 if name=='manual':f['product']['evidence']=[]
 if name=='disconnected':f['product']['evidence']=[]
 return f
