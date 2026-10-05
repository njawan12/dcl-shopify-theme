"""Synthetic content, never genuine product evidence. One schema across verticals."""
from copy import deepcopy

def note(kind='fact', **fields):
    return dict(kind=kind, value='', label='', body='', attribution='', source_title='', source_url='', qualification='', **fields) if not fields else {**note(kind), **fields}

SUBJECTS = {
    'beauty':dict(title='Every ingredient. In context.', product='Daily care pump', media='care-pump.jpg', alt='Ordinary white-background pump-bottle test packshot', price='CAD 24.00', material='Container material', value='Glass', body='The fixture container uses glass; the pump is a separate material.', quote='I prefer having the container and care details beside the product.', intro='A closer look at what is supplied, how it is described, and how to care for it.'),
    'neutral':dict(title='Know the object. Follow the detail.', product='Utility storage case', media='utility-case.jpg', alt='Ordinary rectangular utility case test packshot', price='CAD 24.00', material='Outer material', value='Woven canvas', body='The fixture describes the outer shell; hardware is listed separately.', quote='The dimensions and care instructions helped me understand the case.', intro='Plain product information, connected to its context rather than dressed up as a promise.'),
    'jewelry':dict(title='The material. The making.', product='Plain metal ring', media='metal-ring.svg', alt='Ordinary ring schematic on a white background', price='CAD 38.00', material='Ring material', value='Steel', body='Schematic fixture material, not a real product specification or hallmark.', quote='I want the material and care notes to remain easy to find.', intro='Material, dimensions and care are part of the same product story.'),
    'food':dict(title='What is inside. How it is served.', product='Pantry jar', media='pantry-jar.svg', alt='Ordinary pantry jar schematic on white', price='CAD 12.00', material='Ingredient record', value='Oats', body='Synthetic one-ingredient fixture, not a real nutrition or allergen declaration.', quote='Serving and storage information belong next to the ingredient record.', intro='Ingredient context, portion detail and storage instructions in one reading journey.')}

def base(preset='beauty',host='pdp'):
    s=deepcopy(SUBJECTS[preset]); generic=preset!='beauty'
    notes=[note('fact',value=s['value'],label=s['material'],body=s['body'],qualification='Synthetic fixture content; no real product specification is certified.'),
           note('metric',value='240 g',label='Fixture object mass',body='Mass includes its outer container in this authored test record.',source_title='Fixture measurement context',source_url='#subject',qualification='Example only; not a measured merchant result.'),
           note('quote',body=s['quote'],attribution='Example editorial author',qualification='Synthetic merchant-authored quotation; not a review or verified buyer.')]
    steps=[dict(heading='Inspect',instruction='Read the supplied material record before use.',media='',alt='',qualification='Test instruction, not product efficacy evidence.'),dict(heading='Use',instruction='Keep the object within the described use context.',media='',alt='',qualification=''),dict(heading='Care',instruction='Follow the specific care information supplied with a real product.',media='',alt='',qualification='')]
    return dict(preset=preset,host=host,subject=s,notes=notes[:2],pair=dict(mode='comparison',heading='Compare the supplied details',introduction='Two explicit fixture subjects; no automatic recommendation.',subjects=['This object','Reference object'],rows=[dict(criterion='Material record',left=s['value'],right='Not supplied',qualification='Missing reference information is explicit.'),dict(criterion='Care record',left='Supplied',right='Not supplied',qualification='')],qualification='Illustrative authored comparison, not competitor claims.',source_title='',source_url=''),process=dict(heading='A clear care sequence',introduction='Instructions are distinct from factual claims.',steps=steps,source_title='Fixture instructions',source_url='#subject'),order=['notes','pair','process'],guest='',guest_position='after',instances=1,dir='ltr',density='balanced',emphasis='normal')

FIXTURES={}
def add(name,f): FIXTURES[name]=deepcopy(f)
add('branded-pdp',base());add('neutral-pdp',base('neutral'))
add('branded-editorial',base(host='editorial'));add('neutral-editorial',base('neutral','editorial'))
add('jewelry',base('jewelry'));add('food',base('food'))
b=base('neutral')
f=deepcopy(b);f.update(notes=[],pair=None,process=None);add('zero',f)
f=deepcopy(b);f.update(notes=b['notes'][:1],pair=None,process=None);add('one',f)
f=deepcopy(b);f['notes']+= [note('certification',label='Example certificate record',attribution='Synthetic issuer',body='Schema test only; no real certification or endorsement.',qualification='Illustrative record scoped to this fixture only.')]; f['pair']['rows'] += [dict(criterion='Size record',left='240 mm',right='Not supplied',qualification='Synthetic dimensions.'),dict(criterion='Finish record',left='Plain',right='Not supplied',qualification='')];f['process']['steps'] += [dict(heading='Store',instruction='Store in the specified context.',media='',alt='',qualification='')];f['density']='spacious';add('dense',f)
f=deepcopy(b);f['notes']=[note('fact',value='Canvas',label='Outer material')];f['pair']['introduction']='';f['process']['source_url']='';f['process']['source_title']='';add('missing-optional',f)
f=deepcopy(b);f['subject']['media']='';add('no-media',f)
for name,media in [('portrait','care-pump.jpg'),('landscape','storage-before.svg')]:
 f=deepcopy(b);f['subject']['media']=media;add(name,f)
f=deepcopy(b);f['notes']=[note('metric',value='240 g',label='Authored fixture mass',qualification='No source supplied; not an independently verified result.')];add('metric-no-source',f)
long='This is deliberately lengthy synthetic authored context with material limitations kept visible in the reading journey. '
for name,kind,field in [('long-claim','claim','body'),('long-source','metric','source_title'),('long-quote','quote','body')]:
 f=deepcopy(b);n=note(kind,value='240 g',label='Fixture mass',body='Test claim only.',attribution='Example author',qualification='Synthetic example; no claim or result is verified.',source_title='Fixture context',source_url='#subject');n[field]=long*9
 if kind in ('claim','quote'): n['value']='';n['label']=''
 f['notes']=[n];add(name,f)
f=deepcopy(b);f['subject']['intro']*=2;f['subject']['title']='情報を読む · Produktinformation ' + 'Materialbeschreibung'*5;f['notes'][0]['body']=long+long[:len(long)//2];add('translation',f)
f=deepcopy(b);f['dir']='rtl';f['subject']['title']='تفاصيل واضحة عن المنتج';f['subject']['intro']='المعلومات المعروضة بيانات اختبار وليست ادعاءات موثقة.';add('rtl',f)
f=deepcopy(b);f['pair']=dict(mode='before-after',heading='Before / after arrangement',introduction='Synthetic storage diagram, not a product-result transformation.',sides=[dict(label='Before',media='storage-before.svg',alt='Schematic storage items before arrangement',caption='Unarranged example.'),dict(label='After',media='storage-after.svg',alt='Same schematic storage items after arrangement',caption='Arranged example.')],qualification='Illustrative schematic only; no customer outcome or efficacy claim.',source_title='Fixture diagram context',source_url='#subject');add('before-after',f)
f['pair']['sides'][1]['media']='';add('before-after-incomplete',f)
add('comparison',b);f=deepcopy(b);f['pair']['rows'][0]['right']='';f['pair']['rows'][1]['left']='';add('comparison-incomplete',f)
f=deepcopy(b);f['order']=['notes','process','pair'];f['notes'].reverse();f['process']['steps'].reverse();add('reorder',f)
f=deepcopy(b);f['instances']=2;f['guest']='plain';add('repeated',f)
add('manual',b)
f=deepcopy(b);f['notes']=[{'binding':{'state':'connected','value':n}} for n in f['notes']];add('dynamic',f)
f=deepcopy(b);f['notes']=[{'binding':{'state':'disconnected','value':note('metric',value='999',label='Stale'), 'fallback':b['notes'][0]}}];add('disconnected-fallback',f)
f=deepcopy(b);f['notes']=[{'binding':{'state':'disconnected','value':note('metric',value='999',label='Stale')}}];add('disconnected-omit',f)
for name,guest,position in [('app-absent','','after'),('app-expected','plain','after'),('app-awkward','plain','between'),('app-tall','tall','between'),('app-wide','wide','between'),('app-removed','','after'),('app-reordered','plain','before')]:
 f=deepcopy(b);f['guest']=guest;f['guest_position']=position;add(name,f)
f=deepcopy(b);f['process']['steps']=[dict(heading='',instruction='Invalid'),b['process']['steps'][2]];add('one-process',f)
f=base('neutral','editorial');f['order']=['process'];add('editorial-process',f)
assert len(FIXTURES)==38
WIDTHS=(320,375,390,430,768,1024,1280,1440)
