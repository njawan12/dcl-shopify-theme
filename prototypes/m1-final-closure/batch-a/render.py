"""Non-production integrated surfaces; explicit variants share purchase/data truth."""
import sys,importlib.util,json,copy
from pathlib import Path
from html import escape
from urllib.parse import urlencode
from model import BASE,DATA,PRODUCTS,truth,money,resolve,totals,fixture,FIXTURES

def load(name,path):
 sys.path.insert(0,str(path.parent));spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);sys.path.pop(0);return module
rail=load('accepted_rail',BASE/'reuse/rail/render.py');mosaic=load('accepted_mosaic',BASE/'reuse/mosaic/render.py')
def e(v):return escape(str(v),quote=True)
def adapted(p):
 a=copy.deepcopy(p);a['image']=next((m for m in p['media'] if m['type']=='image'),None);a['options']=[o['name']+': '+', '.join(o['values']) for o in p['options']];return a
mosaic.BASE=BASE # Bind copied renderer asset resolution to the shared canonical media root.
mosaic.PRODUCTS={k:adapted(p) for k,p in PRODUCTS.items()}
def card_truth(a):
 p=PRODUCTS[a['id']];selected=next((v for v in p['variants'] if v['id']==a.get('represented_variant')),None);t=truth(p,selected['options'] if selected else None);available=selected['available'] if selected else any(v['available'] for v in p['variants']);return {'price':t['display_price'],'status':t['status'] if t['variant'] else ('Choose options on product page' if available else 'Sold out'),'available':available,'compare':money(t['compare']) if t['compare'] else None,'unit':money(t['unit']['amount'])+' / '+t['unit']['reference'] if t['unit'] else None,'url':p['url'],'title':p['title']}
mosaic.truth=card_truth

def media(p,family):
 records=p['media'];parts=[]
 for i,m in enumerate(records):
  src=m.get('src') or m.get('poster');alt=m['alt'];inner=f'<img src="/{e(src)}" width="{m.get("width",800)}" height="{m.get("height",800)}" alt="{e(alt)}" loading="{"eager" if i==0 else "lazy"}" decoding="async">' if src else ''
  parts.append(f'<figure id="media-{e(m["id"])}" data-media="{e(m["id"])}" class="media-item type-{m["type"]}">{inner}<figcaption>{e(alt) if m["type"]!="image" else "Product view "+str(i+1)}</figcaption></figure>')
 if not parts:return '<section class="pdp-media empty-media" aria-label="Product media"><p>No product media supplied. Product details and purchase choices remain available.</p></section>'
 nav='<nav class="media-nav" aria-label="Product media views">'+''.join(f'<a href="#media-{e(m["id"])}">View {i+1} · {e(m["type"])}</a>' for i,m in enumerate(records))+'</nav>'
 return f'<section class="pdp-media media-{family}" aria-label="Product media">{nav}<div class="media-encounters">'+''.join(parts)+'</div></section>'

def facts(p,t):
 return f'<header class="product-facts" data-product="{e(p["id"])}" data-variant="{e(t["variant"] or "unresolved")}"><p class="eyebrow">{e(p["vendor"])}</p><h1>{e(p["title"])}</h1><p class="price">{e(t["display_price"])}</p>'+ (f'<p>Previously <s>{money(t["compare"])}</s></p>' if t['compare'] else '')+(f'<p class="unit">{money(t["unit"]["amount"])} / {e(t["unit"]["reference"])}</p>' if t['unit'] else '')+f'<p class="availability">{e(t["status"])}</p></header>'

def purchase(p,choices,name):
 t=truth(p,choices);options=''
 for i,o in enumerate(p['options']):
  options+=f'<label for="option-{i}">{e(o["name"])}</label><select name="option-{i}" id="option-{i}"><option value="">Choose {e(o["name"])}</option>'+''.join(f'<option value="{e(v)}"'+(' selected' if i<len(choices) and choices[i]==v else '')+'>'+e(v)+'</option>' for v in o['values'])+'</select>'
 chooser=(f'<form method="get" class="option-form"><input type="hidden" name="fixture" value="{e(name)}"><input type="hidden" name="product" value="{e(p["id"])}">{options}<button>Resolve options</button></form>' if options else '')
 quantity=p['quantity'];plans='<label for="plan">Purchase terms</label><select id="plan" name="plan"><option value="">One-time purchase</option>'+''.join(f'<option value="{e(s["id"])}">{e(s["label"])}</option>' for s in p['plans'])+'</select>' if p['plans'] else ''
 properties=''.join(f'<label for="property-{i}">{e(k)}</label><input required id="property-{i}" name="property-{i}" maxlength="120" autocomplete="off">' for i,k in enumerate(p['required_properties']))
 action=f'<form method="post" action="/action" class="purchase-form"><input type="hidden" name="action" value="add"><input type="hidden" name="product" value="{e(p["id"])}"><input type="hidden" name="variant" value="{e(t["variant"] or "")}"><label for="quantity">Quantity</label><input id="quantity" name="quantity" type="number" value="{quantity["min"]}" min="{quantity["min"]}" max="{quantity["max"]}" step="{quantity["increment"]}" required>{plans}{properties}<button class="primary"'+(' disabled' if not t['available'] else '')+'>Add to simulated cart</button><p>No inventory promise. This is a local fixture action.</p></form>'
 seams='<section class="platform-seams" aria-label="Platform host feasibility"><p>Accelerated payment / installments host: reserved normal flow; no payment service connected.</p>'+(f'<p>{e(p["pickup"]["location"])} — {e(p["pickup"]["message"])}</p>' if p['pickup'] else '')+(f'<aside class="app-guest"><h2>{e(p["app"]["heading"])}</h2><p>{e(p["app"]["body"])}</p></aside>' if p['app'] else '')+'</section>'
 return '<section class="purchase" aria-label="Purchase information">'+facts(p,t)+chooser+action+seams+'</section>'

def education(p,binding='manual',prefix='proof',include_notes=True):
 notes=p['evidence'];notes=[{'binding':{'state':'connected','value':n}} for n in notes] if binding=='connected' else notes
 if binding=='disconnected' or not include_notes:notes=[]
 process={'heading':'A practical care sequence','introduction':'Instructions are distinct from product efficacy.','steps':p['usage'],'source_title':'Synthetic catalog instructions','source_url':'/sources/catalog'}
 pair={'mode':'comparison','heading':'Read the supplied product context','introduction':'Named fixture contexts, not an inferred winner.','subjects':[p['title'],'Unspecified reference'],'rows':[{'criterion':'Information','left':'Supplied below','right':'Not supplied','qualification':'No competitor claim.'}],'qualification':'Synthetic authored comparison only.'}
 specs='<section class="education-data"><h2>Ingredients & specifications</h2><ul>'+''.join('<li>'+e(i)+'</li>' for i in p['ingredients'])+'</ul><dl>'+''.join('<dt>'+e(k)+'</dt><dd>'+e(v)+'</dd>' for k,v in p['specifications'].items())+'</dl></section>'
 faq='<section><h2>Questions & details</h2>'+''.join('<details><summary>'+e(q['question'])+'</summary><p>'+e(q['answer'])+'</p></details>' for q in p['faq'])+'</section>' if p['faq'] else ''
 return '<div class="evidence-host preset-beauty education" data-binding="'+binding+'">'+rail.render_notes(notes,prefix)+specs+rail.render_pair(pair,prefix)+rail.render_process(process,prefix)+faq+'</div>'

def related(p):
 refs=[r for r in p['recommendations'] if r in PRODUCTS];return '<section class="related"><h2>Related product context</h2><ul>'+''.join('<li><a href="'+PRODUCTS[r]['url']+'">'+e(PRODUCTS[r]['title'])+'</a></li>' for r in refs)+'</ul><p>Complementary: '+(', '.join(e(PRODUCTS[r]['title']) for r in p['complementary'] if r in PRODUCTS) or 'None supplied')+'</p></section>' if refs or p['complementary'] else ''

def pdp(f):
 p=f['product'];comp=f['layout'];buy=purchase(p,f['choices'],f['name']);edu=education(p,f['binding'],include_notes=comp!='editorial');copy='<section class="product-story"><p class="eyebrow">Product context</p><h2>Care, with its details in view.</h2><p>'+e(p['description'])+'</p></section>' if p['description'] else ''
 if comp=='balanced':body='<div class="pdp-two-zone">'+media(p,'gallery')+buy+'</div>'+copy+edu
 elif comp=='compact':body=media(p,'stack')+'<div class="purchase-band">'+buy+'</div>'+copy+edu
 else:body=media(p,'focused')+'<div class="editorial-purchase"><div class="narrative-zone">'+copy+rail.render_notes(p['evidence'],'opening')+'</div>'+buy+'</div>'+edu
 return '<article class="pdp layout-'+comp+'" data-layout="'+comp+'">'+body+related(p)+'</article>'

def collection(count=24,preset='beauty',instance=1):
 refs=(DATA['beauty']*((count+23)//24))[:count];f={'id':'canonical','products':refs,'title':'Everyday care. Considered choices.','description':f'{min(count,24)} distinct Beauty products'+(f' repeated into {count} density encounters; not unique SKUs.' if count>24 else ' from one canonical fictional catalog.'),'rhythm':'anchor','feature_source':'automatic','density':'balanced','preset':preset,'editorial':{'enabled':True,'title':'Know what belongs in your day.','body':'Ingredients, packaging and use context stay attached to their subject.','link':{'label':'Read the field notes','url':'/pages/story'},'image':adapted(PRODUCTS['barrier-cream'])['image']}}
 return mosaic.render_collection(f,instance)[0]

def story(preset):
 p=PRODUCTS['daily-cleanser'];hero=f'<section class="story-opening"><div><p class="eyebrow">Field notes / fictional care business</p><h1>Less guessing.<br>More context.</h1><p>Simple products, clear details, and space to decide what belongs in your routine.</p><a class="action" href="/products/daily-cleanser">Meet the daily cleanser</a></div><figure><img src="/{p["media"][0]["src"]}" width="{p["media"][0]["width"]}" height="{p["media"][0]["height"]}" alt="{e(p["media"][0]["alt"])}"><figcaption>Fictional catalog packshot. No efficacy or provenance claim.</figcaption></figure></section>'
 return '<article class="story-page">'+hero+'<section class="story-copy"><h2>Information follows the object.</h2><p>Read the supplied ingredients and packaging context before choosing. These notes are authored fixture content, never verified reviews.</p></section>'+education(p,prefix='story-proof')+collection(12,preset)+'<section class="closing"><h2>Build your own daily rhythm.</h2><p>Guided merchandising keeps each product independent. No bundle or discount is invented.</p><a class="action" href="/guided?fixture=beauty">Explore the guided collection</a></section></article>'

def cart_html(cart,error=''):
 t=totals(cart);parts=['<article class="cart"><header><p class="eyebrow">Your selection / local simulation</p><h1>Your cart</h1></header>']
 if error:parts.append('<div role="alert" class="error">'+e(error)+'</div>')
 if cart['message']:parts.append('<p role="status">'+e(cart['message'])+'</p>')
 if not cart['lines']:return ''.join(parts)+'<p>Your simulated cart is empty.</p><a class="action" href="/collection">Explore the collection</a></article>'
 parts.append('<div class="cart-layout"><ol class="cart-lines">')
 for l in cart['lines']:
  p=PRODUCTS[l['product']];v=next(v for v in p['variants'] if v['id']==l['variant']);unit=truth(p,v['options']);img=next((m for m in p['media'] if m['type']=='image'),None)
  parts.append('<li class="cart-line" data-line="'+l['key']+'">'+(f'<img src="/{img["src"]}" width="160" height="160" alt="{e(img["alt"])}">' if img else '')+'<div><h2><a href="'+p['url']+'">'+e(p['title'])+'</a></h2><p>Variant: '+e(' / '.join(v['options']) or 'Single variant')+'</p><p>'+money(v['price'])+' per item</p>'+(f'<p>{money(unit["unit"]["amount"])} / {e(unit["unit"]["reference"])}</p>' if unit['unit'] else '')+'<p>Purchase plan: '+e(l['plan'] or 'One-time')+'</p>'+''.join('<p>'+e(k)+': '+e(value)+'</p>' for k,value in l['properties'].items())+(f'<p>Explicit fixture line discount: {money(l["discount"])}</p>' if l['discount'] else '')+f'<form method="post" action="/action"><input type="hidden" name="action" value="update"><input type="hidden" name="key" value="{l["key"]}"><label for="q-{l["key"]}">Quantity for {e(p["title"])}</label><input type="number" id="q-{l["key"]}" name="quantity" value="{l["quantity"]}" min="0" max="{p["quantity"]["max"]}" step="{p["quantity"]["increment"]}"><button>Update quantity</button><button name="fail" value="1">Simulate failed update</button></form><form method="post" action="/action"><input type="hidden" name="action" value="remove"><input type="hidden" name="key" value="{l["key"]}"><button>Remove {e(p["title"])}</button></form></div><strong>{money(max(0,v["price"]*l["quantity"]-l["discount"]))}</strong></li>')
 parts.append('</ol><aside class="cart-summary"><h2>Selection summary</h2><dl>'+''.join('<dt>'+label+'</dt><dd>'+money(t[key])+'</dd>' for key,label in [('gross','Items'),('line_discount','Fixture line discounts'),('order_discount','Fixture order discount'),('total','Selected items total')])+'</dl><p>Taxes, shipping and duties are not calculated. No actual discount or checkout integration.</p><a class="primary action" href="/checkout-preview">Continue to checkout explanation</a><p>Accelerated checkout host: no provider connected.</p><form method="post" action="/action"><input type="hidden" name="action" value="note"><label for="note">Order note</label><textarea id="note" name="note" maxlength="1000">'+e(cart['note'])+'</textarea><button>Save note</button></form></aside></div></article>');return ''.join(parts)

def normalized(f):
 p=f['product'];return {'truth':truth(p,f['choices']),'media':p['media'],'quantity':p['quantity'],'plans':p['plans'],'properties':p['required_properties'],'evidence':p['evidence'],'usage':p['usage'],'ingredients':p['ingredients'],'specifications':p['specifications'],'recommendations':p['recommendations'],'complementary':p['complementary']}

def page(name='balanced',cart=None,error='',product=None,choices=None,scale=1,preset=None):
 f=fixture(name)
 if product in PRODUCTS:f['product']=copy.deepcopy(PRODUCTS[product]);f['choices']=[]
 if choices is not None:f['choices']=choices
 if preset in ('beauty','neutral'):f['preset']=preset
 if name.startswith('collection'):body='<h1 class="surface-title">Your care collection</h1>'+collection(int(name[10:]),f['preset'])
 elif name.startswith('story'):body=story(f['preset'])
 elif name.startswith('cart'):body=cart_html(cart or {'lines':[],'message':'','note':'','order_discount':0},error)
 elif name=='checkout-preview':body='<article class="closing"><h1>Checkout is outside this proof.</h1><p>No payment, inventory reservation or Shopify checkout occurred.</p><a href="/cart">Review simulated cart</a></article>'
 else:body=pdp(f)
 opts=''.join('<option'+(' selected' if n==name else '')+'>'+n+'</option>' for n in FIXTURES)
 return '<!doctype html><html lang="'+('ar' if f['dir']=='rtl' else 'en')+'" dir="'+f['dir']+'" data-fixture="'+e(name)+'" data-preset="'+f['preset']+'" style="--text-scale:'+str(scale)+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>Batch A · '+e(name)+'</title><link rel="stylesheet" href="/reuse/mosaic/mosaic.css"><link rel="stylesheet" href="/reuse/rail/evidence.css"><link rel="stylesheet" href="/tokens.css"><link rel="stylesheet" href="/system.css"></head><body class="integrated"><a class="skip" href="#main">Skip to content</a><header class="site-header"><a href="/pages/story" class="wordmark">FIELDWORK / CARE</a><nav aria-label="Main navigation"><a href="/collection">Collection</a><a href="/products/balancing-formula">Product</a><a href="/pages/story">Field notes</a><a href="/cart">Cart · simulation</a></nav></header><aside class="test-harness"><details><summary>Batch A proof controls · synthetic catalog · PENDING HUMAN REVIEW</summary><form method="get"><label for="fixture-a">Fixture</label><select id="fixture-a" name="fixture">'+opts+'</select><label for="preset">Global scheme</label><select id="preset" name="preset"><option value="beauty">Beauty</option><option value="neutral"'+(' selected' if f['preset']=='neutral' else '')+'>Neutral</option></select><label for="scale">Test text enlargement</label><select id="scale" name="scale"><option value="1">100%</option><option value="2">200% text</option><option value="4">400% text</option></select><button>Load proof</button></form></details></aside><main id="main" tabindex="-1">'+body+'</main><footer class="site-footer"><p>Fieldwork fictional business / M1 structural proof.</p><p>One synthetic dataset. No Shopify, app, payment or genuine merchant proof integration.</p><a href="/sources/catalog">Dataset & source qualification</a></footer></body></html>'

def repeated_page():
 html=page('story');start=html.index('<main id="main" tabindex="-1">')+len('<main id="main" tabindex="-1">');end=html.index('</main>',start)
 content='<h1>Repeated integrated hosts / isolation supplement</h1><p>Same catalog repeated into independent scoped instances. Harness only.</p>'+education(PRODUCTS['daily-cleanser'],prefix='repeat-a')+collection(12,instance=1)+education(PRODUCTS['daily-cleanser'],prefix='repeat-b')+collection(12,instance=2)
 return html[:start]+content+html[end:]
