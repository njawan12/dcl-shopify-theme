"""Behavior assertions against geometry and keyboard evidence captured in the browser.

This verifies a saved audit, not a replacement for capturing fresh browser evidence
when component source changes. See capture metadata for source fingerprints.
"""
from pathlib import Path
import hashlib
import json
import struct
import sys

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
from render import DATA, FIXTURES, media_for, product_for

EVIDENCE = BASE / 'tests/evidence'
rows = json.loads((EVIDENCE / 'browser-matrix.json').read_text())
count = 0


def check(condition, name):
    global count
    assert condition, name
    count += 1


def overlaps(a, b):
    return min(a['right'], b['right']) - max(a['x'], b['x']) > 1 and min(a['bottom'], b['bottom']) - max(a['y'], b['y']) > 1


widths = (320, 375, 390, 430, 768, 1024, 1280, 1440)
check(len(rows) == len(FIXTURES) * len(widths) == 328, 'complete fixture/width matrix')
check({(r['fixture'], r['width']) for r in rows} == {(f, w) for f in FIXTURES for w in widths}, 'each exact fixture/width audited once')
for row in rows:
    name = f"{row['fixture']} at {row['width']}"
    fixture = FIXTURES[row['fixture']]
    product = product_for(fixture)
    image = media_for(product) if product else None
    check(row['overflow'] <= 1, name + ': no horizontal page overflow')
    check(not row['duplicateIds'], name + ': no duplicate IDs')
    check(row['scripts'] == 0, name + ': zero page JavaScript')
    check(len(row['components']) == fixture.get('instances', 1), name + ': one shared semantic component per instance')
    for c in row['components']:
        root, axis, obj, commerce = c['root'], c['axis'], c['object'], c['commerce']
        check(bool(commerce) == bool(product), name + ': unsafe/absent product omits commerce')
        check(bool(obj) == bool(image), name + ': missing media omits frame')
        check(len(c['images']) == int(bool(image)), name + ': no duplicate responsive media')
        check(root['width'] <= row['width'] + 1 and root['x'] >= -1, name + ': instance horizontally contained')
        if obj:
            check(obj['x'] >= -1 and obj['right'] <= row['width'] + 1 and obj['bottom'] <= root['bottom'] + 1, name + ': media contained in instance')
            check(not overlaps(obj, c['statement']), name + ': media does not collide with statement')
            check(not commerce or not overlaps(obj, commerce), name + ': media does not collide with commerce')
            if row['width'] >= 768:
                crossing = obj['y'] < axis['bottom'] < obj['bottom']
            else:
                crossing = obj['x'] < axis['x'] < obj['right'] and axis['y'] < obj['y'] and axis['bottom'] > obj['bottom']
            check(crossing, name + ': one deterministic axis crossing with visible rail beyond object')
        for img in c['images']:
            check(img['fit'] == 'contain', name + ': entire media identity retained')
            # Offscreen lazy media is intentionally not forced eager for an audit.
            check(img['naturalWidth'] > 0 or img['loading'] == 'lazy', name + ': eager image loaded; offscreen lazy image permitted')
        for target in c['targets']:
            check(target['rect']['height'] >= 44 and target['rect']['width'] >= 44, name + ': primary target >=44px')
            check(target['rect']['x'] >= -1 and target['rect']['right'] <= row['width'] + 1, name + ': link text stays in viewport')
        for text in c['text']:
            check(text['scrollWidth'] <= text['clientWidth'] + 1, name + ': long text fits horizontally')
            # Display glyph ink can exceed the typographic line box. It is never
            # clipped: overflow remains visible and following regions have space.
            check(text['overflow'] not in ('hidden', 'clip') and text['whiteSpace'] != 'nowrap', name + ': text has visible overflow and can wrap')
            check(text['rect']['bottom'] <= root['bottom'] + 1, name + ': text remains inside component')
    for first, second in zip(row['components'], row['components'][1:]):
        check(first['root']['bottom'] <= second['root']['y'] + 1, name + ': adjacent instances do not collide')

journey = json.loads((EVIDENCE / 'interaction.json').read_text())
check(journey['fixtureURL'].endswith('?fixture=multi-option') and journey['visible'], 'native GET form selects unresolved fixture')
check(journey['productURL'].endswith('/products/canvas-bag') and journey['destinationTruth'], 'keyboard product link reaches truthful read-only destination')
check(journey['returnURL'] == 'http://localhost:3001/', 'native return link works')
for key, tag in [('focus', 'A'), ('selectFocus', 'SELECT'), ('buttonFocus', 'BUTTON')]:
    check(journey[key]['tag'] == tag and journey[key]['outline'] == 'solid' and journey[key]['outlineWidth'] == '3px', 'visible keyboard focus: ' + key)
check(journey['skipFocus'] == {'id': 'monument-content', 'tag': 'MAIN'}, 'skip link focuses main')

frames = json.loads((EVIDENCE / 'frames.json').read_text())
required = {('default',1440),('neutral',1440),('default',390),('neutral',390),('white-rect',1440),('white-rect',390),('long',1440),('long',390),('missing-media',1440),('missing-product',1440),('sold-out',1440),('adjacent',1440),('long',320),('landscape',768)}
check(required <= {(f['fixture'],f['width']) for f in frames}, 'required controlling and stress evidence exists')
for frame in frames:
    data = (EVIDENCE / frame['file']).read_bytes()
    check(data[:2] == b'\xff\xd8' and data[-2:] == b'\xff\xd9', 'actual JPEG capture: ' + frame['file'])
    # Parse a JPEG start-of-frame marker rather than trusting a filename.
    pos = 2; dimensions = None
    while pos < len(data):
        if data[pos] != 255:
            pos += 1; continue
        marker = data[pos+1]; pos += 2
        if marker in (0xD8,0xD9): continue
        size = int.from_bytes(data[pos:pos+2], 'big')
        if marker in (0xC0,0xC1,0xC2):
            height,width = struct.unpack('>HH', data[pos+3:pos+7]); dimensions=(width,height); break
        pos += size
    check(dimensions and dimensions[0] == frame['width'] and dimensions[1] >= frame['height'], 'correct full-page capture dimensions: ' + frame['file'])
metadata = json.loads((EVIDENCE / 'capture.json').read_text())
for file, digest in metadata['source_sha256'].items():
    check(hashlib.sha256((BASE / file).read_bytes()).hexdigest() == digest, 'captured evidence matches source: ' + file)
print(f'PASS: {count} browser-evidence regression assertions across {len(rows)} fixture/width views; {len(frames)} full-page frames.')
