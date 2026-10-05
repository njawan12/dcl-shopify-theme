"""Explicit synthetic test content; not observed clinical/certification/customer evidence."""
from copy import deepcopy
from pathlib import Path
import json

DISCLAIMER='Synthetic test content. No clinical result, real certification, customer review or efficacy claim is represented.'

def note(kind='fact', **fields):
    return {**dict(kind=kind,value='',label='',body='',attribution='',source_title='',source_url='',qualification=''),**fields}


def catalog():
    notes=[note('metric',value='250 ml',label='Container volume',body='A fixture specification, not a study outcome.',source_title='Fixture specification',source_url='#subject',qualification='Nominal fixture volume; test content only.'),note('fact',value='Amber glass',label='Container material',body='A reusable fixture bottle and separate pump.'),note('claim',body='Designed to be stored upright.',qualification='Fixture storage instruction only; no product benefit or performance claim.')]
    pair={'mode':'comparison','heading':'Two formats, one clear comparison','introduction':'Compare supplied specifications rather than inferred superiority.','qualification':'All values are synthetic fixture specifications. Neither format is declared a winner.','source_title':'Comparison context','source_url':'/pages/fixture-source','subjects':['Pump bottle','Refill container'],'rows':[{'criterion':k,'left':l,'right':r,'qualification':q} for k,l,r,q in [('Volume','250 ml','500 ml','Nominal fixture sizes'),('Container','Glass','Pouch','Fixture materials'),('Dispensing','Pump','Pour','Not a performance ranking'),('Storage','Upright','Upright','Follow supplied instructions')]]}
    steps=[{'heading':h,'instruction':t,'media':None,'alt':'','qualification':'Fixture instruction; not an efficacy promise.'} for h,t in [('Prepare','Place the container on a stable surface.'),('Open','Open only when ready to use.'),('Use','Follow the supplied product instructions.'),('Store','Close and store upright away from heat.')]]
    process={'heading':'A practical sequence','introduction':'Simple supplied instructions, kept in their intended order.','source_title':'Fixture instructions','source_url':'/pages/fixture-source','steps':steps}
    base={'id':'branded-pdp','label':'Branded PDP','host':'pdp','preset':'beauty','title':'Everyday care, clearly explained.','introduction':'An ordinary product, with facts attached to what they explain.','product':{'title':'Everyday care bottle','price':'CAD 24.00','status':'Available · fixture only','url':'/products/fixture-product','media':'care-pump.jpg','alt':'Unbranded amber bottle with a pump on a white background'},'notes':notes,'pair':pair,'process':process,'app':None,'density':'balanced','emphasis':'quiet'}
    fixtures=[]
    def add(fid,**changes):
        f=deepcopy(base);f.update(id=fid,label=fid.replace('-',' ').title(),**changes);fixtures.append(f);return f
    add('branded-pdp')
    neutral=add('neutral-pdp',preset='neutral',title='Useful objects. Clear information.',introduction='A collection for everyday use.',product={'title':'Utility storage case','price':'CAD 24.00','status':'Available · fixture only','url':'/products/fixture-product','media':'utility-case.jpg','alt':'Ordinary gray rectangular storage case on white'})
    neutral['notes']=[note('metric',value='24 cm',label='External width',qualification='Synthetic nominal dimension.',source_title='Fixture dimensions',source_url='#subject'),note('fact',value='Zipped case',label='Construction',body='An ordinary rectangular case with a zip closure.'),note('claim',body='Store on a stable surface.',qualification='Supplied fixture instruction only.')]
    neutral['pair']['subjects']=['Small case','Large case'];neutral['pair']['rows'][0].update(criterion='Width',left='24 cm',right='32 cm');neutral['pair']['rows'][1].update(left='Zipped case',right='Zipped case');neutral['pair']['rows'][2].update(criterion='Closure',left='Zip',right='Zip',qualification='Not a performance ranking')
    for fid,preset in [('branded-editorial','beauty'),('neutral-editorial','neutral')]:
        f=add(fid,host='editorial',preset=preset,title='Look closer at the ordinary.',pair=None,process=None)
        if preset=='neutral':f['product']=deepcopy(neutral['product']);f['notes']=deepcopy(neutral['notes'])
    f=add('jewelry-pdp',preset='jewelry',title='Material, measure, care.');f['product'].update(title='Plain metal ring',media='metal-ring.svg',alt='Schematic plain metal ring on white')
    f['notes']=[note('fact',value='Metal',label='Fixture material',source_title='Material record',source_url='#subject'),note('metric',value='18 mm',label='Internal diameter',qualification='Synthetic nominal measurement.'),note('fact',label='Provenance',body='An authored demonstration asset; not a precious-metal certification.')]
    f['pair']['subjects']=['Small ring','Large ring'];f['pair']['rows']=[{'criterion':k,'left':l,'right':r,'qualification':'Synthetic fixture specifications; no superiority claim.'} for k,l,r in [('Diameter','18 mm','20 mm'),('Material','Metal','Metal'),('Profile','Round','Round'),('Care','Soft cloth','Soft cloth')]]
    f['process']['steps']=[{'heading':h,'instruction':t,'media':None,'alt':'','qualification':'Fixture care instruction only.'} for h,t in [('Handle','Place the ring on a stable surface.'),('Inspect','Check the supplied care information.'),('Wipe','Use a soft cloth as instructed.'),('Store','Store safely away from abrasive objects.')]]
    f=add('food-pdp',preset='food',title='Know what you are serving.');f['product'].update(title='Pantry jar',media='pantry-jar.svg',alt='Schematic pantry jar on white')
    f['notes']=[note('fact',label='Ingredients',body='Illustrative fixture content: oats and water; not a real product label.'),note('metric',value='40 g',label='Serving amount',qualification='Synthetic serving example, not nutritional or health advice.'),note('fact',label='Provenance',body='An authored demonstration jar.')];f['process']['steps'][2]['instruction']='Use the supplied serving instructions; check the real label.';f['pair']['subjects']=['Small jar','Large jar'];f['pair']['rows']=[{'criterion':k,'left':l,'right':r,'qualification':'Synthetic fixture specifications; not a real nutritional label.'} for k,l,r in [('Capacity','250 ml','500 ml'),('Container','Jar','Jar'),('Closure','Lid','Lid'),('Serving example','40 g','40 g')]]
    add('editorial-process',host='editorial',notes=[],pair=None)
    ba={'mode':'before-after','heading':'Two labelled storage states','introduction':'Schematic illustrations of the same container in two positions. Not photographic result evidence.','qualification':'Synthetic diagrams; no product performance, efficacy or observed outcome is claimed.','source_title':'Diagram context','source_url':'/pages/fixture-source','items':[{'label':'Before opening','media':'storage-before.svg','alt':'Schematic container with its lid near the container','caption':'Authored storage-state illustration.'},{'label':'After opening','media':'storage-after.svg','alt':'Same schematic container with lid raised away from the container','caption':'Illustration only, not evidence of a product transformation.'}]}
    add('before-after',pair=ba,preset='neutral',title='One container, two labelled states.',product={'title':'Schematic storage container','price':'CAD 24.00','status':'Available · fixture only','url':'/products/fixture-product','media':'storage-before.svg','alt':'Authored schematic container in the before-opening state'},notes=[note('fact',label='Diagram context',body='Two authored storage states of the same schematic object; not photographic or observed result evidence.')])
    f=add('short',density='compact');f['notes']=[note('fact',label='Material',value='Glass')];f['pair']['heading']='Formats';f['pair']['introduction']='';f['pair']['rows']=f['pair']['rows'][:1];f['process']['steps']=f['process']['steps'][:1]
    long='Long synthetic fixture copy explains scope and context without making a claim about outcomes or customer experience. '
    f=add('long',title=long*3,introduction=long*4)
    f['notes']=[note('metric',value='250 millilitres nominal capacity',label=long,body=long*3,source_title=long*2,source_url='#subject',qualification=long*3),note('quote',body=long*4,attribution='DCL fixture editorial author — synthetic quotation',qualification=long),note('certification',label='EXAMPLE ONLY — certification record',attribution='Synthetic test issuer — not a real certification',body=long*3,qualification='No certification is asserted for a real product.')]
    f['pair']['heading']=long*2;f['pair']['rows'][0].update(left=long*3,right=long*2,qualification=long);f['process']['steps'][0].update(heading=long,instruction=long*4)
    add('maximum',density='spacious',emphasis='strong')
    add('zero-evidence',notes=[],pair=None,process=None)
    add('invalid-notes',notes=[note('metric',value='12'),note('fact',label=''),note('claim'),note('certification',label='Missing issuer'),note('quote',body='Missing attribution'),note('fact',label='Valid note',value='Glass')])
    add('optional-empty',notes=[note('fact',label='Material',value='Glass')],pair=None,process=None)
    f=add('missing-media');f['product']['media']='missing.jpg';f['process']['steps'][0].update(media='missing.jpg',alt='Missing optional media')
    bad=deepcopy(ba);bad['items'][1]['media']=None;add('incomplete-before-after',pair=bad)
    f=add('invalid-comparison');f['pair']['subjects'][1]=''
    f=add('partial-comparison');f['pair']['rows'][1]['right']='';f['pair']['rows'][3]['criterion']=''
    f=add('no-comparison-rows');f['pair']['rows']=[{'criterion':'','left':'','right':'','qualification':''}]
    f=add('partial-process');f['process']['steps'][1]['instruction']='';f['process']['steps'][3]['heading']=''
    f=add('one-valid-step');f['process']['steps']=[{'heading':'','instruction':'Invalid'},{'heading':'Store','instruction':'Close the container.'},{'heading':'Missing instruction','instruction':''}]
    f=add('invalid-process');f['process']['steps']=[{'heading':'','instruction':''}]
    manual=[note('fact',label='Manual fallback',value='Explicit supplied value')]
    add('disconnected-fallback',notes={'connected':False,'source':[note('fact',label='STALE CONNECTED CONTENT',value='Must not render')],'manual':manual})
    add('disconnected-omit',notes={'connected':False,'source':[note('fact',label='STALE CONNECTED CONTENT',value='Must not render')]})
    add('connected-source',notes={'connected':True,'source':deepcopy(notes),'manual':manual})
    add('url-valid',notes=[note('fact',label='External source',value='Fixture',source_title='HTTP source',source_url='https://example.org/specification?x=1&y=2'),note('fact',label='Local source',value='Fixture',source_title='Local context',source_url='/pages/fixture-source'),note('fact',label='Same subject',value='Fixture',source_title='Subject',source_url='#subject')])
    add('url-invalid',notes=[note('fact',label='Invalid scheme',value='Text remains',source_title='Source text remains',source_url='javascript:alert(1)'),note('fact',label='Missing target',value='Text remains',source_title='Missing target source text',source_url='#not-rendered'),note('fact',label='Malformed URL',value='Text remains',source_title='Malformed source text',source_url='https://')])
    guest={'heading':'Generic app guest — synthetic test content','body':'This plain app-block stand-in demonstrates an insertion seam only. No reviews, ratings or real app integration are represented.','link':'/pages/fixture-source'}
    add('app-present',app=guest)
    add('app-tall',app={**guest,'body':(guest['body']+' ')*35})
    add('app-removed')
    add('two-instances',instances=2,app=guest)
    f=add('localization',preset='neutral',title='情報と文脈 — معلومات واضحة — Ordinary information',introduction='A product for everyday use. On your terms.')
    f['introduction']=neutral['introduction']+' On your terms.'
    f['notes'][0]['label']='仕様 / مواصفات / '+'LONGUNBROKENLABEL'*10;f['notes'][0]['qualification']='例示用データ。 هذه بيانات تجريبية وليست ادعاءً سريرياً.'
    assert len(fixtures)==32 and len(f['introduction'])==len(neutral['introduction'])*1.5
    return {'disclaimer':DISCLAIMER,'fixtures':fixtures}

if __name__=='__main__':
    Path(__file__).with_name('fixtures.json').write_text(json.dumps(catalog(),ensure_ascii=False,indent=2)+'\n')
