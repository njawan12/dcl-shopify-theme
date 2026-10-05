"""Read-only local HTTP integrity/navigation/source-route tests."""
from pathlib import Path
import sys
from urllib.request import urlopen
from urllib.error import HTTPError
BASE=Path(__file__).resolve().parents[1];sys.path.insert(0,str(BASE))
from render import FIXTURES,render_page
count=0

def check(value,label):
    global count
    assert value,label;count+=1
for fixture in FIXTURES:
    with urlopen('http://127.0.0.1:3003/?fixture='+fixture) as response:
        check(response.status==200,'fixture200');check(response.read().decode()==render_page(fixture),'live shared render');check(response.headers['Cache-Control']=='no-store','no stale cache')
for path in [BASE/'evidence.css',*sorted((BASE/'media').iterdir())]:
    with urlopen('http://127.0.0.1:3003/'+str(path.relative_to(BASE))) as response:
        check(response.read()==path.read_bytes(),'current asset parity')
for path in ['/products/fixture-product','/pages/fixture-source']:
    with urlopen('http://127.0.0.1:3003'+path) as response:check(b'Synthetic test navigation only' in response.read(),'truthful navigation stub')
for path in ['/content.py','/render.py','/tests/capture-probe.js','/media/../../content.py','/media/%2e%2e/%2e%2e/docs/m1-evidence-layer-prebuild-contract.md','/pages/unknown','/media/missing.jpg']:
    try:urlopen('http://127.0.0.1:3003'+path);check(False,'must reject '+path)
    except HTTPError as error:check(error.code==404,'rejected '+path)
print(f'{count} PASS / 0 FAIL; read-only HTTP integrity')
