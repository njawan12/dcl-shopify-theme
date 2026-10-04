"""Deterministic fixture-authoring source; not a storefront layout engine."""
from pathlib import Path
from copy import deepcopy
import json

BASE = Path(__file__).resolve().parent
products = {}; sets = {}
images = {name: {'src': 'media/'+name, 'width': 1254, 'height': 1254, 'alt': alt} for name, alt in [('care-pump.jpg','Unbranded amber glass pump bottle on a white background.'),('care-jar.jpg','Plain ivory cream jar on a white background.'),('daily-mug.jpg','Ordinary white ceramic mug on a white background.'),('utility-case.jpg','Gray woven utility case on a white background.')]}
for name,w,h,alt in [('case-portrait.svg',500,625,'Entire gray utility case on portrait media.'),('case-landscape.svg',900,600,'Entire gray utility case on landscape media.'),('case-dark.svg',900,600,'Gray utility case on a plain dark background.'),('bag-transparent.svg',600,600,'Whole canvas drawstring bag with transparent background.'),('metal-ring.svg',600,600,'Plain metal ring on white background.'),('pantry-jar.svg',600,600,'Plain pantry jar on white background.')]:
    images[name] = {'src':'media/'+name,'width':w,'height':h,'alt':alt}
names = {
 'beauty':['Gentle hand wash','Daily body wash','Everyday cream','Light daily lotion','Unscented hand wash','Body balm','Daily cleansing oil','Rich hand cream','Evening face cream','Hand wash refill','Body cream, unscented','Everyday hand balm'],
 'neutral':['Utility case','White ceramic mug','Large utility case','Everyday cup','Portrait utility case','Landscape utility case','Everyday travel case','Wide handled mug','Small zipper case','Dark catalog case','Tall ceramic mug','Everyday storage case'],
 'jewelry':['Simple silver band','Wide silver band','Everyday polished ring','Brushed metal ring','Slim silver ring','Rounded silver ring'],
 'food':['Pantry grains','Breakfast oats','Everyday rice','Dried beans','Kitchen lentils','Plain barley']}
for group,titles in names.items():
    sets[group] = []
    for i,title in enumerate(titles):
        key=f'{group}-{i+1}';sets[group].append(key)
        media=('care-jar.jpg' if i in (2,5,7,8,10,11) else 'care-pump.jpg') if group=='beauty' else ('daily-mug.jpg' if i in (1,3,7,10) else 'utility-case.jpg') if group=='neutral' else 'metal-ring.svg' if group=='jewelry' else 'pantry-jar.svg'
        if group=='neutral' and i in (4,5,9): media={4:'case-portrait.svg',5:'case-landscape.svg',9:'case-dark.svg'}[i]
        price=1800+i*200 if group=='beauty' else 1200+i*150 if group=='neutral' else 4200+i*500 if group=='jewelry' else 600+i*100
        variant={'id':key+'-single','price':price,'available':i!=5}
        if i==7: variant['compare_at']=price+600
        if i==2: variant['unit_price']={'amount':price*2,'reference':'100 g' if group in ('beauty','food') else '1 item'}
        p={'id':key,'title':title,'url':'/products/'+key,'vendor':'Everyday care' if group=='beauty' else 'Everyday objects' if group=='neutral' else 'Workshop' if group=='jewelry' else 'Pantry','variants':[variant],'image':deepcopy(images[media])}
        if i==9: p['badge']='Refill format' if group=='beauty' else 'Plain catalog finish'
        if i==10:
            p['options']=['Unscented','Citrus'] if group=='beauty' else ['Small','Large'];p['variants'].append({'id':key+'-large','price':price+500,'available':True})
        products[key]=p

def clone(key, origin, **changes):
    p=deepcopy(products[origin]);p.update(id=key,url='/products/'+key,**changes);products[key]=p

clone('no-media','neutral-1',image=None)
clone('transparent','neutral-1',title='Canvas drawstring bag',image=images['bag-transparent.svg'])
clone('long-title','neutral-1',title='Everyday utility case with a full-length zipper and room for small things you carry from one place to another',vendor='An intentionally long fixture vendor name representing independent everyday object makers')
clone('long-money','neutral-2',variants=[{'id':'long-money-single','price':123456789,'available':True,'unit_price':{'amount':98765432,'reference':'one deliberately long reference measure for localized shopping contexts'}}])
clone('selling-plan','beauty-1',commerce_context='Selling-plan details on product page')
clone('app-owned','beauty-3',commerce_context='App-managed purchase details on product page',app_note='Fixture app seam: product information from an app. No rating or review claim.')
clone('complex','neutral-3',options=['Small','Medium','Large','Cotton','Canvas'],variants=[{'id':f'complex-{i}','price':2400+i*200,'available':i!=0} for i in range(20)],commerce_context='Complex options on product page')
clone('represented','neutral-3',options=['Small','Large'],variants=[{'id':'represented-a','price':2400,'available':True},{'id':'represented-b','price':3600,'available':False}],represented_variant='represented-b')
clone('unpublished','neutral-1',published=False)
clone('all-sold','neutral-1',variants=[{'id':'all-sold-one','price':1800,'available':False}])
story={'enabled':True,'title':'A little more room for the everyday.','body':'Simple objects, familiar uses. Read the notes behind this collection.','image':deepcopy(images['daily-mug.jpg']),'link':{'label':'Read the collection notes','url':'/pages/field-notes'}}
fixtures=[]
def add(id,label,group='neutral',count=12,**changes):
    refs=(sets[group]*((count+len(sets[group])-1)//len(sets[group])))[:count]
    f={'id':id,'label':label,'products':refs,'title':'Everyday essentials' if group=='beauty' else 'Objects for daily use' if group=='neutral' else 'Everyday metal' if group=='jewelry' else 'The pantry shelf','description':'A collection of simple products for ordinary days.','preset':group,'rhythm':'anchor','feature_source':'automatic','density':'balanced','editorial':deepcopy(story)}
    if group=='beauty': f['editorial'].update(title='Start with a simpler daily ritual.',body='A few everyday essentials, with room to choose what works for you.',image=deepcopy(images['care-jar.jpg']))
    f.update(changes);fixtures.append(f);return f
add('branded','Branded Beauty / Wellness',group='beauty')
add('neutral','Neutral originality torture')
for count in [0,1,2,3,5,24,30,100,104]: add('count-'+str(count),'Result count '+str(count),count=count)
add('standard','Standard Grid fallback',rhythm='standard')
add('branded-standard','Branded Standard Grid',group='beauty',rhythm='standard')
add('editorial-absent','Editorial absent',editorial=None)
f=add('editorial-no-image','Editorial without image');f['editorial']['image']=None
f=add('editorial-no-link','Editorial without link');f['editorial']['link']=None
f=add('editorial-long','Very long editorial heading');f['editorial']['title']='The everyday objects that accompany you through changing places and routines deserve a thoughtful place in the way you shop and choose.'
add('feature-missing','Missing selected feature reference',feature_source='missing')
add('no-eligible-feature','No eligible feature treatment',feature_source='none')
for id,product in [('feature-no-media','no-media'),('feature-sold-out','all-sold'),('feature-complex','complex'),('feature-app','app-owned'),('feature-represented','represented')]:
    f=add(id,id.replace('-',' ').title());f['products'][6]=product
f=add('mixed-media','Mixed-ratio media and missing image');f['products']=['transparent','no-media','neutral-5','neutral-6','neutral-2','neutral-10',*sets['neutral'][6:]]
f=add('truth-stress','Long title, sale, sold out, unit price, app/options');f['products']=['long-title','beauty-8','all-sold','long-money','selling-plan','complex','represented','app-owned',*sets['neutral'][8:]]
add('long-titles','All product titles two or three lines',products=['long-title']*12)
add('all-white','All white-background catalog media',products=['neutral-2','neutral-4']*6)
add('deleted','Deleted and unpublished references omitted',products=['deleted-ref','unpublished',*sets['neutral']])
add('empty-filter','No results after filtering',products=['all-sold']*12,filter='available')
add('filtered-one','Only one result after filtering',products=['neutral-1']+['all-sold']*11,filter='available')
add('filtered-five','Filtering below interruption',products=sets['neutral'][:5]+['all-sold']*7,filter='available')
add('sorted','Price-sorted collection',sort='price-low')
add('page-before','Pagination boundary before editorial',count=24,page_size=6,page=1)
add('page-after','Pagination boundary after editorial',count=24,page_size=12,page=1)
add('page-two','Second page: no repeated interruptions',count=24,page_size=12,page=2)
add('adjacent','Two adjacent collection instances',instances=2)
add('all-disabled','All optional treatments disabled',feature_source='none',editorial=None)
add('compact','Compact density',density='compact')
add('spacious','Spacious density',density='spacious')
add('jewelry','Jewelry / Accessories',group='jewelry')
add('food','Food / Drink',group='food')
f=add('localized','Long collection heading and +50% copy');f['title']='Alltägliche Gegenstände, die Sie auf Ihren Wegen begleiten und Raum für bewusste Entscheidungen lassen'
fixtures[1]['description']='A collection for everyday use.'
f['description']=fixtures[1]['description']+' On your terms.'
assert len(f['description'])*2==len(fixtures[1]['description'])*3
if __name__ == '__main__':
    (BASE/'fixtures.json').write_text(json.dumps({'products':products,'fixtures':fixtures},indent=2,ensure_ascii=False)+'\n')
    print(f'{len(products)} distinct product fixtures; {len(fixtures)} collection fixtures')
