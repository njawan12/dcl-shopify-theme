"""HTTP response evidence; local server must run on port3004."""
from urllib.request import urlopen
from urllib.error import HTTPError
from pathlib import Path
import sys
BASE=Path(__file__).resolve().parents[1];sys.path.insert(0,str(BASE))
from fixtures import FIXTURES
from render import page
checks=0
def check(v,label):
 global checks
 assert v,label
 checks+=1
for name in FIXTURES:
 with urlopen('http://127.0.0.1:3004/?fixture='+name) as res:
  check(res.status==200,name+' response');check(res.read().decode()==page(name),name+' actual baseline');check(res.headers['Cache-Control']=='no-store',name+' cache')
for query in ['unknown','%3Cscript%3E','']:
 check(urlopen('http://127.0.0.1:3004/?fixture='+query).read().decode()==page(),'unknown query fallback')
for path in ['products/fixture-object','editorial-destination','guest-destination','tests/guests/plain.html','tests/guests/tall.html','tests/guests/wide.html','media/care-pump.jpg','evidence.css']:
 with urlopen('http://127.0.0.1:3004/'+path) as res:check(res.status==200 and len(res.read())>0,'served '+path)
try:urlopen('http://127.0.0.1:3004/%2e%2e/.git/config');check(False,'traversal blocked')
except HTTPError as ex:check(ex.code==403,'traversal blocked')
print(f'{checks} PASS / 0 FAIL;38 actual fixture responses')
