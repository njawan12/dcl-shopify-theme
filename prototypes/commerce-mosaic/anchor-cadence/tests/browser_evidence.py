"""Validate observed browser geometry/order evidence, never synthesize observations."""
import hashlib
import json
from pathlib import Path
import struct
import sys
BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
from render import FIXTURES, render_collection
E = BASE / 'tests/evidence'
checks = 0

def check(value, label):
    global checks
    assert value, label
    checks += 1


def verify_collection(observed, fixture, **query):
    _, result, cadence = render_collection(fixture, **query)
    check(observed['order'] == [i['key'] for i in result['items']], 'source/DOM order')
    check(observed['productCount'] == len(result['items']), 'truthful page count')
    check(observed['resultCount'] == f"{result['total']} products · showing {len(result['items'])} · page {result['page']} of {result['pages']}", 'result/filter/page count')
    check(observed['featureIndices'] == ([] if cadence['feature_index'] is None else [cadence['feature_index']]), 'one feature at planned encounter')
    check(observed['editorialAfter'] == ([] if cadence['editorial_after'] is None else [cadence['editorial_after']]), 'editorial reading position')
    check(observed['editorialCount'] == int(cadence['editorial_after'] is not None), 'editorial separate from products')
    for field in ('holes', 'placementErrors', 'itemCollisions', 'textCollisions', 'mediaCollisions', 'overflows', 'badTargets', 'uncontained', 'unloaded'):
        check(observed[field] == [], field)


matrix = json.loads((E / 'browser-matrix.json').read_text())
widths = (320,375,390,430,768,1024,1280,1440)
check(len(matrix) == len(FIXTURES)*len(widths), 'complete matrix cardinality')
check({(r['fixture'],r['width']) for r in matrix} == {(f,w) for f in FIXTURES for w in widths}, 'every fixture/width pair')
for row in matrix:
    check(row['overflow'] <= 0, 'no horizontal overflow')
    check(row['duplicateIds'] == [], 'unique IDs')
    check(row['scripts'] == 0, 'zero runtime scripts')
    f = FIXTURES[row['fixture']]
    check(len(row['collections']) == f.get('instances',1), 'component instances')
    for collection in row['collections']:
        check(collection['cols'] == (3 if row['width'] >= 1024 else 2), 'deterministic columns')
        verify_collection(collection, f)
journey = json.loads((E/'interactions.json').read_text())
verify_collection(journey[0]['audit']['collections'][0],FIXTURES['branded'],sort='price-low',availability='available')
check('sort=price-low&availability=available' in journey[0]['url'], 'native form URL')
check(journey[1]['focus'] == {'tag':'A','href':'/products/beauty-1'}, 'keyboard product focus')
check(journey[2]['url'].endswith('/products/beauty-1') and journey[2]['heading']=='Gentle hand wash', 'keyboard destination')
verify_collection(journey[3]['audit']['collections'][0],FIXTURES['page-after'],page=2)
check(journey[4]['focus']=='collection-content','skip link focus')

def jpeg_dimensions(path):
    data=path.read_bytes(); check(data[:2]==b'\xff\xd8','real JPEG')
    i=2
    while i < len(data):
        if data[i]!=255: i+=1; continue
        marker=data[i+1]; i+=2
        if marker in (0xd8,0xd9): continue
        size=struct.unpack('>H',data[i:i+2])[0]
        if marker in (0xc0,0xc1,0xc2):
            h,w=struct.unpack('>HH',data[i+3:i+7]); return w,h
        i+=size
    raise AssertionError('JPEG dimensions missing')
frames=json.loads((E/'frames.json').read_text())
check(len(frames)==36,'review frame count')
check({f['width'] for f in frames}==set(widths),'screenshot width coverage')
for f in frames:
    w,h=jpeg_dimensions(E/f['file'])
    check(w==f['width'] and h>=f['height'],'full-size screenshot dimensions')
loading=json.loads((E/'media-loading.json').read_text())
check({r['file'] for r in loading}=={f['file'] for f in frames},'loaded-media coverage')
check(all(r['unloaded']==0 for r in loading),'all screenshot images loaded')
check(jpeg_dimensions(E/'focus-390.jpg')==(390,1000),'focus frame dimensions')
for name,digest in json.loads((E/'capture.json').read_text())['source_sha256'].items():
    check(hashlib.sha256((BASE/name).read_bytes()).hexdigest()==digest,'evidence/current source parity '+name)
print(f'{checks} PASS / 0 FAIL; {len(matrix)} observed browser views; {len(frames)} review frames + 1 focus frame')
