"""Behavioral regression assertions against the shared renderer and literal baseline."""
import ast
from copy import deepcopy
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import subprocess
import sys

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
from render import DATA, FIXTURES, media_for, money, product_for, render_component, render_page

count = 0

def check(condition, name):
    global count
    assert condition, name
    count += 1


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.nodes = []
        self.stack = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        node = {'tag': tag, 'attrs': dict(attrs), 'text': '', 'ancestors': self.stack.copy()}
        self.nodes.append(node)
        if tag not in ('img', 'meta', 'link', 'input', 'br', 'hr'):
            self.stack.append(node)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1]['tag'] == tag:
            self.stack.pop()

    def handle_data(self, value):
        for node in self.stack:
            node['text'] += value

    def by_class(self, name):
        return [n for n in self.nodes if name in n['attrs'].get('class', '').split()]

    def tags(self, tag):
        return [n for n in self.nodes if n['tag'] == tag]


required = {'default', 'neutral', 'short', 'long', 'single', 'multi-option', 'sold-out', 'sale', 'unit-price', 'missing-product', 'missing-media', 'transparent', 'white-rect', 'dark-rect', 'portrait', 'square', 'landscape', 'focal-left', 'focal-right', 'focal-top', 'focal-bottom', 'long-title', 'long-cta', 'adjacent', 'deleted', 'unpublished', 'represented', 'selling-plan', 'app-owned', 'gift-card', 'multiple-images', 'no-headline', 'no-optionals', 'catalog', 'long-money', 'below-fold', 'beauty', 'jewelry', 'food', 'wide', 'two-line'}
check(required <= FIXTURES.keys(), 'all required risks have fixtures')
check(len(FIXTURES) == len(DATA['fixtures']) == 41, 'unique fixture identity')
allowed_inputs = {'id', 'label', 'product', 'headline', 'eyebrow', 'copy', 'preset', 'editorial_link', 'instances', 'below_fold'}
for fixture in DATA['fixtures']:
    check(set(fixture) <= allowed_inputs, 'no layout rescue controls in inputs')
    html = render_page(fixture['id'])
    doc = Document(html)
    instances = fixture.get('instances', 1)
    product = product_for(fixture)
    image = media_for(product) if product else None
    check(len(doc.by_class('monument')) == instances, 'one component per requested instance')
    check(len(doc.by_class('statement')) == instances and len(doc.by_class('datum')) == instances, 'statement and axis retained')
    check(len(doc.by_class('commerce')) == (instances if product else 0), 'invalid product removes entire commerce object')
    check(len(doc.by_class('object')) == (instances if image else 0), 'missing media omits entire object, not a broken frame')
    check(len(doc.tags('img')) == (instances if image else 0), 'one media object; no gallery or responsive duplicates')
    check(not doc.tags('script'), 'zero browser JavaScript')
    ids = [n['attrs']['id'] for n in doc.nodes if 'id' in n['attrs']]
    check(len(ids) == len(set(ids)), 'unique IDs including adjacent instances')
    check(all(n['attrs'].get('aria-hidden') == 'true' for n in doc.by_class('datum')), 'decorative datum excluded from accessibility tree')
    check(all(n['attrs'].get('alt') and n['attrs'].get('width') and n['attrs'].get('height') for n in doc.tags('img')), 'meaningful alt and intrinsic dimensions')
    check(len(doc.by_class('product-link')) == (instances if product else 0), 'one safe action per valid product')
    check(all(n['attrs']['href'] == product['url'] for n in doc.by_class('product-link')), 'safe destination is fixture-owned')
    check(all(n['attrs'].get('aria-label') == 'View product: ' + product['title'] for n in doc.by_class('product-link')), 'native product link names')
    check(not any(n['tag'] in ('button', 'select', 'input') and any('monument' in a['attrs'].get('class', '').split() for a in n['ancestors']) for n in doc.nodes), 'no invented commerce controls')
    for n in doc.by_class('monument'):
        regions = [x['attrs'].get('class') for x in doc.nodes if x['ancestors'] and x['ancestors'][-1] is n]
        check(regions == ['statement', 'datum'] + (['object'] if image else []) + (['commerce'] if product else []), 'single logical statement/object/commerce DOM order')
    for img in doc.tags('img'):
        check((BASE / img['attrs']['src']).is_file(), 'local existing media file')
    if product:
        title = doc.by_class('product-title')[0]['text']
        check(title == product['title'], 'commerce title from product data')
    if fixture.get('instances', 1) > 1:
        check(doc.tags('img')[1]['attrs']['loading'] == 'lazy', 'adjacent second object not eager')
    if fixture.get('below_fold'):
        check(doc.tags('img')[0]['attrs']['loading'] == 'lazy', 'below-fold object lazy')

for product in DATA['products'].values():
    check(bool(re.fullmatch(r'/products/[a-z0-9-]+', product['url'])), 'product URL whitelist')
    for variant in product['variants']:
        check(type(variant['price']) is int and variant['price'] >= 0, 'integer nonnegative money')
    check(product['money']['digits'] in (0, 1, 2, 3), 'bounded currency minor units')

check('choose options' in render_component(FIXTURES['multi-option']) and 'CAD 48.00 – CAD 62.00' in render_component(FIXTURES['multi-option']), 'unresolved range, no arbitrary selected variant')
check('Sold out.' in render_component(FIXTURES['represented']) and 'CAD 62.00' in render_component(FIXTURES['represented']), 'explicit represented variant matches price and availability')
check('Previously <s>CAD 48.00</s>' in render_component(FIXTURES['sale']), 'valid compare-at truthful')
check('compare-at' not in render_component(FIXTURES['default']), 'no absent sale shell')
check('CAD 24.00 / 1 metre' in render_component(FIXTURES['unit-price']), 'unit price stays with object')
check('KWD 123.456,789' in render_component(FIXTURES['long-money']), 'exact three-digit localized money')
check(money(101, {'currency': 'KWD', 'digits': 3}) == 'KWD 0.101', 'integer money without floating point')
check(money(202, {'currency': 'JPY', 'digits': 0}) == 'JPY 202', 'zero-digit currency')
for invalid in (-1, 1.1, True):
    try:
        money(invalid, {'currency': 'CAD', 'digits': 2})
        check(False, 'invalid money rejected')
    except ValueError:
        check(True, 'invalid money rejected')
check(len(FIXTURES['long']['copy']) * 2 == len(FIXTURES['default']['copy']) * 3, 'exact 50 percent supporting-copy expansion')
check(Document(render_component(FIXTURES['multiple-images'])).tags('img')[0]['attrs']['src'] == DATA['products']['bag']['images'][0]['src'], 'one deterministic dominant media choice')
check(render_page('unknown') == render_page('default'), 'unknown fixture safe fallback')
check((BASE / 'index.html').read_text() == render_page('default'), 'literal default is exactly the shared server renderer')
neutral = deepcopy(FIXTURES['default']); neutral['preset'] = 'neutral'
check(render_component(neutral).replace('monument neutral', 'monument branded') == render_component(FIXTURES['default']), 'tokens do not fork component markup')
injected = deepcopy(FIXTURES['default']); injected['headline'] = '<script>alert(1)</script>'
check('&lt;script&gt;' in render_component(injected) and not Document(render_component(injected)).tags('script'), 'authored text escaped')
unsafe = deepcopy(DATA['products']['bag']); unsafe['images'] = [{'src': '../bad.jpg'}]
check(media_for(unsafe) is None, 'unsafe media omitted')
css = (BASE / 'monument.css').read_text()
check(':focus-visible' in css and '44px' in css, 'focus and target baseline')
check('prefers-reduced-motion' in css, 'reduced motion explicit')
check('object-fit: contain' in css, 'product identity not cropped')
check('position: absolute' not in css[css.index('.monument {'):], 'no absolute component geometry')
check(not re.search(r'overflow\s*:\s*(hidden|clip)|nth-child|nth-of-type', css), 'no clipping or fixture placement shortcuts')
check(not any(re.search(r'\.' + re.escape(f['id']) + r'(?:\s|\[|\{|:)', css) for f in DATA['fixtures'] if f['id'] not in ('neutral', 'beauty', 'jewelry', 'food')), 'no fixture-name layout selectors')
check(not re.search(r'https?://|@import|@font-face', css), 'no external CSS/font dependency')
check(not list(BASE.glob('*.js')), 'zero shipped JS files')
for file in [BASE / 'render.py', BASE / 'serve.py']:
    ast.parse(file.read_text())
    check(True, 'Python source syntax parses')
status = subprocess.check_output(['git', 'status', '--porcelain', '-z', '--untracked-files=all'], cwd=BASE, text=True)
paths = [entry[3:] for entry in status.split('\0') if entry]
check(all(p.startswith('prototypes/living-canvas/monument/') for p in paths), 'all working-tree changes in authorized path')
print(f'PASS: {count} static/render regression assertions across {len(FIXTURES)} fixtures.')
