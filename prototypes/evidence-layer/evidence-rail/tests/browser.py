"""Validate actual browser observations and image/source parity; never manufacture them."""
from pathlib import Path
import sys,json,hashlib,struct
BASE=Path(__file__).resolve().parents[1];sys.path.insert(0,str(BASE))
from fixtures import FIXTURES,WIDTHS
from content import normalize_note,normalize_pair,normalize_process
E=BASE/'tests/evidence';checks=0
def check(v,label):
 global checks
 assert v,label
 checks+=1
matrix=json.loads((E/'browser-matrix.json').read_text())
check(len(matrix)==304,'304 observations')
check({(r['fixture'],r['width']) for r in matrix}=={(f,w) for f in FIXTURES for w in WIDTHS},'complete38x8 matrix')
for r in matrix:
 f=FIXTURES[r['fixture']]
 check(r['overflow']==0,r['fixture']+' page overflow')
 for key in ['duplicateIds','textOverflow','collisions','targets','unloaded']:check(r[key]==[],r['fixture']+' '+key)
 check(r['scripts']==0,'zero runtime JS')
 check(len(r['hosts'])==f['instances'],'isolated instance count')
 for h in r['hosts']:
  allowed=f['order'] if f['host']=='pdp' else (['process'] if f['order']==['process'] else ['notes'])
  kinds=[n['kind'] for raw in f['notes'] if (n:=normalize_note(raw))] if 'notes' in allowed else []
  pair=normalize_pair(f['pair']) if 'pair' in allowed else None
  process=normalize_process(f['process']) if 'process' in allowed else None
  check(h['kinds']==kinds,'note kind/input order')
  check(h['notes']==len(kinds),'note omissions/count')
  check(h['pairs']==int(pair is not None),'pair omissions')
  check(h['rows']==(len(pair['rows']) if pair and pair['mode']=='comparison' else 0),'complete comparison rows')
  check(h['sides']==(2 if pair and pair['mode']=='before-after' else 0),'explicit before-after sides')
  check(h['steps']==(len(process['steps']) if process else 0),'step omissions/count')
  check(h['ordered']==('OL' if process else ''),'ordered process including one step')
  check(h['dir']==f['dir'],'RTL source direction')
  check(h['host']==f['host'],'semantic host type')
  check(h['apps']==int(bool(f['guest'])),'app omission/insertion')
  present={'notes':bool(kinds),'pair':bool(pair),'process':bool(process)}
  order=['subject']
  if f['guest'] and f['guest_position']=='before':order.append('app')
  for i,key in enumerate(allowed):
   if present[key]:order.append(key)
   if f['guest'] and f['guest_position']=='between' and i==0:order.append('app')
  if f['guest'] and f['guest_position']=='after':order.append('app')
  check(h['order']==order,'one deterministic semantic source order')
  check('999' not in h['text'],'no disconnected stale content')
  check('CAD' in h['text'] if f['host']=='pdp' else '/editorial-destination' in h['links'],'host commerce/editorial destination')
  for g in h['guests']:
   check(g['tabindex']=='0','focusable guest region')
   check(g['rect']['x']>=0 and g['rect']['right']<=r['width']+1,'guest confined without page overflow')
   if f['guest']=='wide' and r['width']<1280:check(g['scrollWidth']>g['width'],'wide guest remains locally accessible')
journey=json.loads((E/'interactions.json').read_text());cases={r['case']:r for r in journey}
check(cases['keyboard-source-focus']['observed']['tag']=='A','native source keyboard focus')
check('3px' in cases['keyboard-source-focus']['observed']['outline'],'visible source outline')
check(cases['source-target']['observed']['focus']=='rail-1-subject','source target focus')
check(cases['skip-target']['observed']['focus']=='content','skip target focus')
check(cases['product-destination']['url'].endswith('/products/fixture-object'),'native product destination')
check(cases['guest-destination']['url'].endswith('/guest-destination'),'native guest destination')
check(cases['wide-guest-keyboard']['observed']['scrollLeft']>0,'native keyboard scroll reaches wide guest')
check(cases['wide-guest-keyboard']['observed']['overflow']==0,'guest keyboard no page overflow')
check('list' in cases['one-step-semantics']['snapshot'] and 'Care' in cases['one-step-semantics']['snapshot'],'one-step browser semantic observation')
def dimensions(path):
 data=path.read_bytes();check(data[:2]==b'\xff\xd8','real JPEG '+path.name);i=2
 while i<len(data):
  if data[i]!=255:i+=1;continue
  marker=data[i+1];i+=2
  if marker in (0xd8,0xd9):continue
  size=struct.unpack('>H',data[i:i+2])[0]
  if marker in (0xc0,0xc1,0xc2):h,w=struct.unpack('>HH',data[i+3:i+7]);return w,h
  i+=size
 raise AssertionError('missing JPEG dimensions')
frames=json.loads((E/'frames.json').read_text());check(len(frames)==43,'43 full-page review frames')
for f in frames:
 w,h=dimensions(E/f['file']);check(w==f['width'] and h>=f['height'],'full-size frame '+f['file'])
loading=json.loads((E/'media-loading.json').read_text());check({r['file'] for r in loading}=={f['file'] for f in frames},'all frames media observed')
check(all(r['unloaded']==0 for r in loading),'no unloaded screenshot media')
check(dimensions(E/'keyboard-focus-390.jpg')==(390,1000),'keyboard frame')
supp=json.loads((E/'supplemental.json').read_text());check(len(supp)==3,'three supplemental proofs')
for row in supp:
 check(dimensions(E/row['file'])[0]==row['width'],'supplemental dimensions')
 if row['file']=='reduced-motion-invariant-390.jpg':check(row['observed']['animations']==0,'zero required motion')
 else:
  check(row['observed']['overflow']==0,'supplemental reflow')
  check(row['observed']['scripts']==0,'script-free supplemental')
  check(row['observed']['collisions']==[] and row['observed']['targets']==[],'supplemental geometry')
 if row['file']=='reflow-320.jpg':check(row['rootFont']=='24px','150% text enlargement')
for name,digest in json.loads((E/'capture.json').read_text())['source_sha256'].items():check(hashlib.sha256((BASE/name).read_bytes()).hexdigest()==digest,'source parity '+name)
for name,digest in json.loads((E/'capture.json').read_text())['image_sha256'].items():check(hashlib.sha256((E/name).read_bytes()).hexdigest()==digest,'captured image parity '+name)
print(f'{checks} PASS / 0 FAIL;304 actual browser views;43 full-page +4 supplemental JPEGs')
