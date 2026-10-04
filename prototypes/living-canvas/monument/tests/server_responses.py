"""Read-only live loopback response checks; no external service or commerce mutation."""
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen
import sys

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
from render import DATA, render_page

count = 0

def check(condition, name):
    global count
    assert condition, name
    count += 1


def get(path):
    with urlopen('http://127.0.0.1:3001' + path, timeout=5) as response:
        return response.status, response.headers, response.read()


for fixture in DATA['fixtures']:
    status, headers, body = get('/?fixture=' + fixture['id'])
    check(status == 200 and headers['Content-Type'] == 'text/html; charset=utf-8', 'fixture serves HTML')
    check(body.decode() == render_page(fixture['id']), 'live response uses current shared renderer: ' + fixture['id'])
    check(headers['Cache-Control'] == 'no-store', 'fixture selection cannot reuse stale cached HTML')
for asset in [BASE / 'monument.css', *sorted((BASE / 'media').iterdir())]:
    status, headers, body = get('/' + str(asset.relative_to(BASE)))
    check(status == 200 and body == asset.read_bytes(), 'local asset response matches source: ' + asset.name)
status, headers, body = get('/?fixture=unknown')
check(status == 200 and body.decode() == render_page('default'), 'unknown fixture uses safe default')
for path in ['/render.py', '/../../docs/m1-signature-system.md', '/products/not-a-product', '/products/unpublished-product']:
    try:
        get(path)
        check(False, 'unsafe or missing route must return 404')
    except HTTPError as error:
        check(error.code == 404, 'source/escape/missing product route unavailable')
status, headers, body = get('/pages/materials')
check(status == 200 and b'Read-only local editorial link proof.' in body, 'optional editorial destination resolves')
print(f'PASS: {count} read-only HTTP assertions; {len(DATA["fixtures"])} fixture responses match the shared renderer.')
