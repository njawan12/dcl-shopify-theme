"""Live read-only localhost checks. Server must be running on port 3002."""
from pathlib import Path
from urllib.request import urlopen
from urllib.error import HTTPError
import sys
BASE=Path(__file__).resolve().parents[1];sys.path.insert(0,str(BASE))
from render import DATA, render_page
count=0

def check(ok,name):
    global count
    assert ok,name
    count+=1

def get(path):
    with urlopen('http://127.0.0.1:3002'+path,timeout=5) as r:return r.status,r.headers,r.read()

for f in DATA['fixtures']:
    status,h,b=get('/?fixture='+f['id'])
    check(status==200 and h['Content-Type']=='text/html; charset=utf-8','valid fixture response')
    check(b.decode()==render_page(f['id']),'current shared rendered response')
    check(h['Cache-Control']=='no-store','no stale fixture cache')
for query,args in [('fixture=neutral&sort=price-low',{'fixture_id':'neutral','sort':'price-low'}),('fixture=neutral&availability=sold-out',{'fixture_id':'neutral','availability':'sold-out'}),('fixture=page-after&page=2',{'fixture_id':'page-after','page':2})]:
    check(get('/?'+query)[2].decode()==render_page(**args),'native filter/sort/page query truth')
for asset in [BASE/'mosaic.css',*sorted((BASE/'media').iterdir())]:
    check(get('/'+str(asset.relative_to(BASE)))[2]==asset.read_bytes(),'served local asset bytes')
for path in ['/render.py','/planner.py','/../../docs/engineering-compliance-standard.md','/products/unpublished','/products/deleted-ref']:
    try:get(path);check(False,'source/escape/unpublished route must fail')
    except HTTPError as e:check(e.code==404,'unsafe/missing route returns 404')
for path in ['/products/beauty-7','/pages/field-notes','/pages/product-notes']:
    check(b'Read-only fixture navigation proof' in get(path)[2],'safe navigation destination')
print(f'PASS: {count} live HTTP assertions.')
