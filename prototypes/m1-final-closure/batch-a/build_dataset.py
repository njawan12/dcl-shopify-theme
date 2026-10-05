"""Author one explicitly synthetic canonical catalog; no runtime data fetching."""
import json, pathlib, shutil, hashlib, xml.etree.ElementTree as ET
B=pathlib.Path(__file__).parent; R=B.parents[2]; sources={}
def copy(src,dst):
 dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(R/src,dst);sources[str(dst.relative_to(B))]={'source':src,'sha256':hashlib.sha256(dst.read_bytes()).hexdigest()}
for group,root,files in [('rail','prototypes/evidence-layer/evidence-rail',['render.py','content.py','fixtures.py','evidence.css']),('mosaic','prototypes/commerce-mosaic/anchor-cadence',['render.py','planner.py','fixtures.json','mosaic.css']),('guided','prototypes/living-canvas/split-tension',['split-tension.js','split-tension.css'])]:
 for f in files:copy(root+'/'+f,B/'reuse'/group/f)
 for p in (R/root/'media').iterdir():
  if p.is_file():
   copy(str(p.relative_to(R)),B/'reuse'/group/'media'/p.name)
   if not (B/'media'/p.name).exists():copy(str(p.relative_to(R)),B/'media'/p.name)
# Ordinary white-background schematic assets are data fixtures, not new composition IP.
for name,object_markup in {'cloth-square':'<rect x="145" y="160" width="510" height="480" rx="8" fill="#ddd9ce" stroke="#777"/><path d="M165 180h470v440H165z" fill="none" stroke="#aaa" stroke-dasharray="5 4"/>','care-pouch':'<rect x="130" y="220" width="540" height="360" rx="20" fill="#ccc" stroke="#666"/><path d="M150 245h490" stroke="#555" stroke-width="8"/><rect x="615" y="237" width="25" height="24" fill="#888"/>','gift-card':'<rect x="130" y="240" width="540" height="320" rx="16" fill="#eee" stroke="#777"/><text x="400" y="405" text-anchor="middle" font-family="sans-serif" font-size="32" fill="#444">Fixture gift card</text>'}.items():
 (B/'media'/(name+'.svg')).write_text('<svg xmlns="http://www.w3.org/2000/svg" width="800" height="800" viewBox="0 0 800 800"><rect width="800" height="800" fill="white"/>'+object_markup+'</svg>')
names=['Daily cleansing milk','Everyday barrier cream','Daily concentrate','Soft finishing oil','Reusable cleansing cloth','Balancing formula','Unscented hand wash','Everyday body lotion','Cleansing balm','Hand cream refill','Daily body wash','Body butter','Gentle face wash','Hand cleansing gel','Everyday face lotion','Cream refill','Body oil','Care pouch','Soft cotton cloth','Travel cleansing milk','Daily care pump','Everyday cream jar','Care gift card','Hand wash refill pouch']
handles=['daily-cleanser','barrier-cream','concentrate','finishing-oil','woven-cloth','balancing-formula']+[f'care-{i:02}' for i in range(7,25)]
products={}
for i,(title,pid) in enumerate(zip(names,handles)):
 image='bottle-portrait.svg' if i==0 else 'jar.svg' if i==1 else ['care-pump.jpg','care-jar.jpg','bottle-portrait.svg','case-landscape.svg'][i%4]
 media=[{'id':pid+'-media-1','type':'image','src':'media/'+image,'width':800,'height':1000 if i%4==2 else 800,'alt':title+' — synthetic ordinary product media'}]
 price=[2400,3800,4200,3100,1200,2900][i] if i<6 else 1600+i*150
 p={'id':pid,'handle':pid,'title':title,'vendor':'Fieldwork Care · fictional brand','url':'/products/'+pid,'published':True,'options':[],'variants':[{'id':pid+'-v1','options':[],'price':price,'available':i!=11,'compare_at':price+600 if i==1 else None,'unit_price':{'amount':price*2,'reference':'100 ml'} if i in (0,1,5) else None,'media_id':media[0]['id']}],'media':media,'description':'A straightforward care product for everyday use. This fictional catalog tests presentation, not efficacy.','ingredients':['Water','Glycerin'] if i%3 else ['Cotton (cloth fixture)'] if i==4 else ['Water','Glycerin','Container: glass'],'specifications':{'Container':'Glass or refill packaging, as described','Size':'250 ml fixture'},'usage':[{'heading':'Prepare','instruction':'Read the supplied product information.','media':'','alt':'','qualification':'Synthetic instructions; no efficacy claim.'},{'heading':'Use','instruction':'Follow the product-specific directions supplied with real merchandise.','media':'','alt':'','qualification':''}],'evidence':[{'kind':'fact','value':'250 ml','label':'Nominal fixture capacity','body':'A fictional product specification, not a measured merchant result.','source_title':'Synthetic catalog record','source_url':'/sources/catalog','qualification':'All content is authored synthetic test data.'}],'faq':[{'question':'Where is the product information?','answer':'Ingredients, specifications and instructions are provided alongside this fictional product.'}],'recommendations':[],'complementary':[],'plans':[],'quantity':{'min':1,'max':8,'increment':1},'required_properties':[],'pickup':None,'app':None,'gift_card':i==22}
 if i==5:
  p['options']=[{'name':'Size','values':['30 ml','60 ml']},{'name':'Finish','values':['Light','Rich']}]
  p['variants']=[{'id':pid+'-'+s+'-'+f,'options':[s+' ml',f.title()],'price':a,'available':ok,'compare_at':3400 if a==2900 else None,'unit_price':{'amount':round(a*100/int(s)),'reference':'100 ml'},'media_id':media[0]['id']} for s,f,a,ok in [('30','light',2900,True),('30','rich',3100,False),('60','light',4700,True)]]
 if i==2:
  p['options']=[{'name':'Volume','values':['10 ml','20 ml','30 ml','40 ml','50 ml','60 ml']},{'name':'Texture','values':['Light','Smooth','Rich','Fluid']}]
  p['variants']=[{'id':pid+f'-v{j+1}','options':[a,b],'price':4200+j*100,'available':j!=3,'compare_at':None,'unit_price':None,'media_id':media[0]['id']} for j,(a,b) in enumerate((a,b) for a in p['options'][0]['values'] for b in p['options'][1]['values'])]
 if i in (3,4):
  p['options']=[{'name':'Format','values':['Small','Large'] if i==4 else ['Light','Silky','Soft','Rich','Fluid','Smooth']}]
  p['variants']=[{'id':pid+f'-v{j+1}','options':[s],'price':price+j*100,'available':True,'compare_at':None,'unit_price':None,'media_id':media[0]['id']} for j,s in enumerate(p['options'][0]['values'])]
 if i==7:p['plans']=[{'id':'monthly-care','label':'Monthly delivery · fixture','price_adjustment':0,'terms':'Recurring purchase-shaped data; no subscription service.'}]
 if i==8:p['required_properties']=['Recipient note']
 if i==9:p['quantity']={'min':2,'max':10,'increment':2}
 if i==10:p['pickup']={'location':'Example studio','message':'Fixture pickup context; no live availability.'}
 if i==12:p['app']={'heading':'External product information seam','body':'Independent synthetic guest. No review, rating or vendor integration.'}
 if i==13:p['description']='';p['faq']=[];p['evidence']=[]
 if i==14:p['title']='Everyday face lotion with detailed packaging and care information for a considered daily routine and unfamiliar long product names'
 if i==15:p['media']=[]
 if i==5:
  p['media'] += [{'id':pid+f'-media-{j+2}','type':'image','src':'media/'+a,'width':800,'height':800,'alt':title+' — supplementary synthetic packshot'} for j,a in enumerate(['care-jar.jpg','bottle-portrait.svg','case-landscape.svg','care-pump.jpg','jar.svg','box.svg','bottle.svg','care-jar.jpg','bottle-portrait.svg'])]
  p['media'] += [{'id':pid+'-video','type':'video','poster':'media/care-pump.jpg','alt':'Video-shaped fixture: handling demonstration text alternative. No playable video source supplied.','source':None},{'id':pid+'-model','type':'model','poster':'media/care-jar.jpg','alt':'3D-shaped fixture: cylindrical container with separate pump. No interactive model supplied.','source':None}]
 # Synthetic physical facts follow the product category/options, never a universal capacity.
 capacity='50 ml' if i in (0,1) else '30 / 60 ml' if i==5 else '10–60 ml by selected option' if i==2 else '250 ml'
 p['specifications']={'Packaging':'Fixture container; no sustainability certification','Nominal volume':capacity}
 if p['evidence']:p['evidence'][0]['value']=capacity
 if i in (3,16):p['ingredients']=['Sunflower seed oil','Squalane (fictional ingredient list)']
 if i in (4,18):p['ingredients']=[];p['specifications']={'Material':'Cotton fixture','Format':'Small / Large' if i==4 else 'Single cloth'};p['evidence'][0].update(value='Cotton',label='Fixture material')
 if i==17:p['ingredients']=[];p['specifications']={'Material':'Woven textile fixture','Purpose':'Storage pouch'};p['evidence'][0].update(value='Textile',label='Fixture material')
 if i==22:p['ingredients']=[];p['specifications']={'Type':'Gift card shaped product','Delivery':'Not integrated in this proof'};p['evidence'][0].update(value='Gift card',label='Fixture product type');p['description']='Digital gift-card-shaped identity and price only. Issuance, recipient form and redemption are outside this proof.'
 products[pid]=p
# A coherent, deliberately fictional manual-content baseline rather than 24 renamed placeholders.
for i,pid in enumerate(handles):
 p=products[pid]
 if i in (4,18):kind='cloth';material='Cotton';volume='15 × 15 / 25 × 25 cm' if i==4 else '25 × 25 cm';asset='cloth-square.svg';ingredients=[];directions=[('Dampen','Wet the cloth with water before use.'),('Care','Rinse after use and allow the cloth to dry fully.')]
 elif i==17:kind='storage pouch';material='Woven textile';volume='22 × 14 cm';asset='care-pouch.svg';ingredients=[];directions=[('Arrange','Place closed care containers inside the pouch.'),('Care','Empty the pouch before spot cleaning and leave it open to dry.')]
 elif i==22:kind='gift card';material='Digital product-shaped record';volume='Value shown in the purchase information';asset='gift-card.svg';ingredients=[];directions=[('Review','Gift-card issuance, recipient handling and redemption require production integration; this proof only represents the product identity and value.')]
 elif i in (3,16):kind='finishing oil';material='Glass bottle fixture';volume='30 ml';asset='bottle-portrait.svg';ingredients=['Sunflower seed oil','Squalane'];directions=[('Dispense','Place a small amount of the fictional oil in your palm.'),('Use','Apply according to the final merchant-authored directions; efficacy is not represented by this fixture.')]
 elif i in (1,5,7,8,9,11,14,15,21):kind='cream or balm';material='Jar or refill container fixture';volume='50 ml' if i==1 else '30 / 60 ml by selected option' if i==5 else '100 ml';asset='jar.svg' if i==1 else 'care-pump.jpg' if i==7 else 'box.svg' if i in (9,15) else 'care-jar.jpg';ingredients=['Water','Glycerin','Squalane','Cetearyl alcohol'];directions=[('Prepare','Use clean hands and check the supplied ingredient list.'),('Apply','Dispense a small amount and follow the merchant-authored product directions; no outcome is promised.')]
 elif i==2:kind='concentrate';material='Glass bottle fixture';volume='10–60 ml by selected option';asset='bottle-portrait.svg';ingredients=['Water','Glycerin','Panthenol'];directions=[('Dispense','Use the supplied dispenser for the selected bottle size.'),('Use','Follow the concentration-specific instructions provided with real merchandise; this fictional formula makes no result claim.')]
 else:kind='wash or cleansing milk';material='Pump bottle or refill container fixture';volume='50 ml' if i==0 else '100 ml' if i==19 else '250 ml';asset='bottle-portrait.svg' if i in (0,12,19) else 'box.svg' if i==23 else 'care-pump.jpg';ingredients=['Water','Glycerin','Decyl glucoside'];directions=[('Wash','Dispense a small amount onto wet hands or a damp cloth.'),('Finish','Rinse with water, close the container and follow the product-specific merchant directions.')]
 p['description']=p['title']+' is a fictional '+kind+' record with packaging, ingredient or material information and practical usage context. No clinical outcome, genuine inventory or certification is asserted.'
 if i==13:p['description']=''
 p['ingredients']=ingredients;p['specifications']={'Material / packaging':material,'Nominal size / format':volume}
 if p['evidence']:p['evidence'][0].update(value=material if kind in ('cloth','storage pouch') else 'Gift card' if kind=='gift card' else volume,label='Fixture material' if kind in ('cloth','storage pouch') else 'Product type' if kind=='gift card' else 'Nominal format / volume',body='Authored product context for this fictional '+kind+'. The source is a synthetic catalog record, not a measured result.')
 p['usage']=[{'heading':head,'instruction':text,'media':'','alt':'','qualification':'Synthetic instructions; final directions require merchant content.' if j==0 else ''} for j,(head,text) in enumerate(directions)]
 if p['media']:p['media'][0]['src']='media/'+asset
 if p['faq']:p['faq']=[{'question':'What information should I review?','answer':'Check the '+('material and dimensions' if not ingredients else 'ingredient list and selected size')+' above and the supplied usage sequence. These records are fictional and do not validate product claims.'}]
for i,title in enumerate(['Plain steel band','Wide steel ring','Rounded everyday ring','Brushed metal ring','Slim metal ring','Polished metal band']):
 pid=f'jewelry-{i+1}';p=json.loads(json.dumps(products['daily-cleanser']));p.update(id=pid,handle=pid,title=title,vendor='Fieldwork Objects · fictional brand',url='/products/'+pid,options=[],variants=[{'id':pid+'-v1','options':[],'price':3800+i*400,'available':True,'compare_at':None,'unit_price':None,'media_id':pid+'-media-1'}],media=[{'id':pid+'-media-1','type':'image','src':'media/metal-ring.svg','width':600,'height':600,'alt':title+' synthetic schematic'}],ingredients=[],specifications={'Material':'Steel fixture','Dimensions':'18 mm nominal fixture'},description='Ordinary metal object with material and care context. No hallmark or real provenance claim.',usage=[{'heading':'Wipe','instruction':'Use a soft dry cloth on the ordinary metal surface.','media':'','alt':'','qualification':'Synthetic care content; real merchandise requires merchant instructions.'},{'heading':'Store','instruction':'Keep the ring separated from other objects when storing it.','media':'','alt':'','qualification':''}],evidence=[{'kind':'fact','value':'Steel','label':'Fixture material','body':'Synthetic specification, not a verified hallmark.','source_title':'Synthetic catalog','source_url':'/sources/catalog','qualification':'Fictional jewelry test content.'}]);products[pid]=p
for i,p in enumerate(list(products.values())[:24]):
 p['recommendations']=[] if i%4==0 else [handles[(i+1)%24],handles[(i+2)%24]];p['complementary']=[] if i%5==0 else [handles[4]]
for product in products.values():
 for item in product['media']:
  source=item.get('src') or item.get('poster')
  if source and source.endswith('.svg'):
   svg=ET.parse(B/source).getroot();item['width']=int(float(svg.attrib.get('width','800')));item['height']=int(float(svg.attrib.get('height','800')))
  elif source and source.endswith('.jpg'):item['width']=1254;item['height']=1254
D={'disclaimer':'Synthetic non-production catalog. No genuine merchant provenance, inventory, efficacy, review or certification claim.','currency':'CAD','products':products,'beauty':handles,'jewelry':[f'jewelry-{i}' for i in range(1,7)]}
(B/'dataset.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n');(B/'tests/evidence/reuse.json').write_text(json.dumps(sources,indent=2)+'\n')
print('30 distinct products:24 Beauty +6 Jewelry')
