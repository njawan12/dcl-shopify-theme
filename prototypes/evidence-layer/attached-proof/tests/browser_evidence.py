"""Validate actual native-browser observations; never create substitute evidence."""
from pathlib import Path
import hashlib,json,struct,sys
BASE=Path(__file__).resolve().parents[1];sys.path.insert(0,str(BASE))
from render import FIXTURES
from content import notes,pair,process
E=BASE/'tests/evidence';count=0

def check(value,label):
    global count
    assert value,label;count+=1


def audit(row,f):
    for field in ('duplicateIds','collisions','overflows','badTargets','badImages','unloadedEager'):check(row[field]==[],field+' '+f['id'])
    check(row['overflow']<=0,'no page overflow');check(row['scripts']==0,'zero runtime scripts')
    check(len(row['hosts'])==f.get('instances',1),'independent host count')
    ns=notes(f.get('notes'));pv=pair(f.get('pair')) if f['host']=='pdp' else None;ps=process(f.get('process'))
    if f['host']=='editorial' and ns:ps=None
    primitives=(['notes'] if ns else [])+(['pair'] if pv else [])+(['process'] if ps else [])
    sequence=['subject']+(['note-group'] if ns else [])+(['commerce'] if f['host']=='pdp' else [])+(['education pair'] if pv else [])+(['education process'] if ps else [])+(['app-slot'] if f['host']=='pdp' and f.get('app') else [])+(['editorial-action'] if f['host']=='editorial' else [])
    for h in row['hosts']:
        check(h['host']==f['host'],'host context');check(h['primitives']==primitives,'same primitive/order contract');check(h['sequence']==sequence,'semantic attachment order')
        check([n['kind'] for n in h['notes']]==[n['kind'] for n in ns],'same note types/order')
        for n,observed in zip(ns,h['notes']):
            for field in ('value','label','body','attribution','source_title','qualification'):
                check(not n[field] or n[field] in observed['text'],'note text/qualification retained')
        check(h['pairModes']==([pv['mode']] if pv else []),'semantic pair mode')
        check(h['rows']==(len(pv['rows']) if pv and pv['mode']=='comparison' else 0),'valid rows/cap')
        check(h['pairedItems']==(2 if pv and pv['mode']=='before-after' else 0),'exact complete beforeafter')
        check(len(h['processLists'])==int(ps is not None),'process omission')
        if ps:
            ol=h['processLists'][0];check(ol['tag']=='OL','one/many remain ordered')
            check(ol['count']==len(ps['steps']),'valid steps/cap');check(ol['headings']==[s['heading'] for s in ps['steps']],'step order')
            check(ol['indices']==[f'{i:02}' for i in range(1,len(ps['steps'])+1)],'consecutive numbering')
        check(h['apps']==int(bool(f.get('app')) and f['host']=='pdp'),'guest presence/absence')

matrix=json.loads((E/'browser-matrix.json').read_text());widths=(320,375,390,430,768,1024,1280,1440)
check(len(matrix)==256,'256 views');check({(r['fixture'],r['width']) for r in matrix}=={(f,w) for f in FIXTURES for w in widths},'complete32x8 matrix')
for row in matrix:audit(row,FIXTURES[row['fixture']])
journey=json.loads((E/'interactions.json').read_text())
check(journey[0]['focus']=={'tag':'A','href':'#evidence-1-subject','outline':'3px'},'keyboard visible source focus')
check(journey[1]['focus']=='evidence-1-subject' and journey[1]['url'].endswith('#evidence-1-subject'),'native fragment focus')
check(journey[2]['url'].endswith('/products/fixture-product') and journey[2]['heading']=='Read-only fixture context','native product stub')
for j,fid in zip(journey[3:7],('app-present','app-tall','app-removed','one-valid-step')):
    check(j['url'].endswith('?fixture='+fid),'native fixture form');audit(j['audit'],FIXTURES[fid])
check(journey[7]['focus']=='main','skip target focus')

def jpeg(path):
    data=path.read_bytes();check(data[:2]==b'\xff\xd8','actualJPEG')
    i=2
    while i<len(data):
        if data[i]!=255:i+=1;continue
        marker=data[i+1];i+=2
        if marker in (0xd8,0xd9):continue
        size=struct.unpack('>H',data[i:i+2])[0]
        if marker in (0xc0,0xc1,0xc2):
            height,width=struct.unpack('>HH',data[i+3:i+7]);return width,height
        i+=size
    raise AssertionError('JPEGdimensions')
frames=json.loads((E/'frames.json').read_text());check(len(frames)==35,'35 review frames');check({f['width'] for f in frames}==set(widths),'allwidths screenshots')
for f in frames:
    width,height=jpeg(E/f['file']);check(width==f['width'] and height>=f['height'],'full-size actual dimensions')
check(jpeg(E/'focus-390.jpg')==(390,1000),'focus screenshot')
loading=json.loads((E/'media-loading.json').read_text());check({r['file'] for r in loading}=={f['file'] for f in frames},'media proof coverage');check(all(r['unloaded']==0 for r in loading),'all captured images loaded')
for name,hashvalue in json.loads((E/'capture.json').read_text())['source_sha256'].items():check(hashlib.sha256((BASE/name).read_bytes()).hexdigest()==hashvalue,'observations/current source parity '+name)
print(f'{count} PASS / 0 FAIL; 256 observed views, 35 review frames +1 focus')
