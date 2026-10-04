"""Shared product truth and card renderer; native server-rendered shopping controls."""
from html import escape
from pathlib import Path
from urllib.parse import urlencode
import json
import re
from planner import plan

BASE = Path(__file__).resolve().parent
DATA = json.loads((BASE / 'fixtures.json').read_text())
FIXTURES = {f['id']: f for f in DATA['fixtures']}
PRODUCTS = DATA['products']

def money(amount):
    if type(amount) is not int or amount < 0:
        raise ValueError('Nonnegative integer minor units required')
    whole, cents = divmod(amount, 100)
    return f'CAD {whole:,}.{cents:02d}'


def truth(product):
    variants = product['variants']
    selected = next((v for v in variants if v['id'] == product.get('represented_variant')), None)
    if selected is None and len(variants) == 1 and not product.get('options'):
        selected = variants[0]
    prices = [v['price'] for v in variants]
    available = selected['available'] if selected else any(v['available'] for v in variants)
    price = money(selected['price']) if selected else money(min(prices)) + (' – ' + money(max(prices)) if min(prices) != max(prices) else '')
    state = 'Available' if available else 'Sold out'
    if not selected:
        state += ' · choose options on product page'
    if product.get('commerce_context'):
        state += ' · ' + product['commerce_context']
    compare = money(selected['compare_at']) if selected and selected.get('compare_at', 0) > selected['price'] else None
    unit = selected.get('unit_price') if selected else None
    return {'price': price, 'status': state, 'available': available, 'compare': compare,
            'unit': money(unit['amount']) + ' / ' + unit['reference'] if unit else None,
            'url': product['url'], 'title': product['title']}


def valid_product(ref):
    product = PRODUCTS.get(ref)
    return product if product and product.get('published', True) and re.fullmatch(r'/products/[a-z0-9-]+', product['url']) else None


def image_html(image, eager=False):
    if not image or not re.fullmatch(r'media/[a-z0-9-]+\.(jpg|svg)', image.get('src', '')) or not (BASE / image['src']).is_file():
        return '<span class="missing-media">Image unavailable</span>'
    return f'<img src="/{image["src"]}" width="{image["width"]}" height="{image["height"]}" alt="{escape(image["alt"], quote=True)}" loading="{"eager" if eager else "lazy"}" decoding="async">'


def result_sequence(fixture, sort=None, availability=None, page=None):
    # References are collection-driven fixture inputs; invalid/unpublished records are excluded.
    source = []
    for ordinal, ref in enumerate(fixture['products']):
        product = valid_product(ref)
        if product:
            source.append({'product': product, 'key': f'{ordinal}-{ref}'})
    sort = sort if sort in ('collection', 'price-low', 'title') else fixture.get('sort', 'collection')
    availability = availability if availability in ('all', 'available', 'sold-out') else fixture.get('filter', 'all')
    if availability != 'all':
        source = [item for item in source if truth(item['product'])['available'] == (availability == 'available')]
    if sort == 'price-low':
        source = sorted(source, key=lambda item: min(v['price'] for v in item['product']['variants']))
    elif sort == 'title':
        source = sorted(source, key=lambda item: item['product']['title'])
    total = len(source)
    size = fixture.get('page_size', max(total, 1))
    page = page if type(page) is int and page >= 1 else fixture.get('page', 1)
    page = min(page, max(1, (total + size - 1) // size))
    start = (page - 1) * size
    return {'items': source[start:start + size], 'total': total, 'start': start, 'page': page,
            'pages': max(1, (total + size - 1) // size), 'sort': sort, 'filter': availability}


def render_card(product, key, ordinal, instance, feature=False, eager=False):
    t = truth(product)
    identity = f'mosaic-{instance}-product-{ordinal}'
    parts = [f'<li class="product-card{" feature" if feature else ""}" data-product="{escape(key, quote=True)}"><a class="product-link" href="{t["url"]}" aria-labelledby="{identity}">',
             '<figure class="media">' + image_html(product.get('image'), eager) + '</figure>',
             '<div class="product-info">', f'<span class="encounter" aria-hidden="true">{ordinal:02d}</span>',
             f'<h3 id="{identity}">{escape(t["title"])}</h3>']
    if feature:
        parts.append('<p class="feature-label">Featured product</p>')
    if product.get('vendor'):
        parts.append(f'<p class="vendor">{escape(product["vendor"])}</p>')
    parts.append(f'<p class="price">{escape(t["price"])}</p>')
    if t['compare']:
        parts.append(f'<p class="compare">Previously <s>{escape(t["compare"])}</s></p>')
    if t['unit']:
        parts.append(f'<p class="unit">{escape(t["unit"])}</p>')
    parts.append(f'<p class="status">{escape(t["status"])}</p>')
    if product.get('badge'):
        parts.append(f'<p class="badge">{escape(product["badge"])}</p>')
    if product.get('options'):
        parts.append(f'<p class="options">Options: {escape(" · ".join(product["options"]))}</p>')
    parts += ['<span class="destination">View product ↗</span>', '</div></a>']
    if product.get('app_note'):
        # App guest seam is outside the product link, never a nested interaction.
        parts.append(f'<aside class="app-seam" aria-label="Fixture app content"><p>{escape(product["app_note"])}</p><a href="/pages/product-notes">Read product notes</a></aside>')
    parts.append('</li>')
    return '\n'.join(parts)


def render_editorial(editorial, instance):
    parts = [f'<li class="editorial"><article aria-labelledby="mosaic-{instance}-story"><div class="story-copy"><p class="eyebrow">Field notes · Editorial</p>',
             f'<h3 id="mosaic-{instance}-story">{escape(editorial["title"])}</h3>',
             f'<p>{escape(editorial.get("body", ""))}</p>']
    link = editorial.get('link')
    if link and re.fullmatch(r'/pages/[a-z0-9-]+', link['url']):
        parts.append(f'<a href="{link["url"]}">{escape(link["label"])} ↗</a>')
    parts.append('</div>')
    if editorial.get('image'):
        parts.append('<figure class="story-media">' + image_html(editorial['image']) + '</figure>')
    parts.append('</article></li>')
    return '\n'.join(parts)


def render_collection(fixture, instance=1, sort=None, availability=None, page=None):
    result = result_sequence(fixture, sort, availability, page)
    editorial = fixture.get('editorial')
    editorial_ready = bool(editorial and editorial.get('enabled', True) and editorial.get('title'))
    rhythm = fixture.get('rhythm', 'anchor')
    cadence = plan(len(result['items']), rhythm, fixture.get('feature_source', 'automatic') == 'automatic', editorial_ready, result['start'])
    preset = fixture.get('preset', 'beauty')
    density = fixture.get('density', 'balanced')
    if preset not in ('beauty', 'neutral', 'jewelry', 'food'): preset = 'beauty'
    if density not in ('compact', 'balanced', 'spacious'): density = 'balanced'
    parts = [f'<section class="collection {preset} {density}" aria-labelledby="mosaic-{instance}-heading">',
             '<header class="collection-intro"><p class="eyebrow">Collection / Anchor Cadence proof</p>',
             f'<h2 id="mosaic-{instance}-heading">{escape(fixture["title"])}</h2>', f'<p>{escape(fixture.get("description", ""))}</p>',
             f'<p class="result-count">{result["total"]} products · showing {len(result["items"])} · page {result["page"]} of {result["pages"]}</p></header>',
             f'<ul class="product-grid {"standard" if rhythm == "standard" else "anchor"}" aria-label="Products and optional editorial story">']
    for i, item in enumerate(result['items']):
        parts.append(render_card(item['product'], item['key'], i + 1, instance, i == cadence['feature_index'], eager=result['start'] == 0 and i < 3 and instance == 1))
        if i + 1 == cadence['editorial_after']:
            parts.append(render_editorial(editorial, instance))
    parts.append('</ul>')
    if not result['items']:
        message = 'No products match this filter.' if result['filter'] != 'all' else 'This collection has no available product references.'
        parts.append(f'<p class="empty">{message}</p>')
    if result['pages'] > 1:
        parts.append('<nav class="pagination" aria-label="Collection pages">')
        for number in range(1, result['pages'] + 1):
            query = urlencode({'fixture': fixture['id'], 'sort': result['sort'], 'availability': result['filter'], 'page': number})
            parts.append(f'<a href="/?{query}"{" aria-current=\"page\"" if number == result["page"] else ""}>Page {number}</a>')
        parts.append('</nav>')
    parts.append('</section>')
    return '\n'.join(parts), result, cadence


def render_page(fixture_id='branded', sort=None, availability=None, page=None):
    fixture = FIXTURES.get(fixture_id, FIXTURES['branded'])
    _, result, _ = render_collection(fixture, 1, sort, availability, page)
    options = ''.join(f'<option value="{f["id"]}"{" selected" if f["id"] == fixture["id"] else ""}>{escape(f["label"])}</option>' for f in DATA['fixtures'])
    sorts = ''.join(f'<option value="{v}"{" selected" if v == result["sort"] else ""}>{label}</option>' for v, label in [('collection','Collection order'),('price-low','Price: low to high'),('title','Title')])
    filters = ''.join(f'<option value="{v}"{" selected" if v == result["filter"] else ""}>{label}</option>' for v, label in [('all','All products'),('available','Available'),('sold-out','Sold out')])
    collections = '\n'.join(render_collection(fixture, i + 1, sort, availability, page)[0] for i in range(fixture.get('instances', 1)))
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Commerce Mosaic · Anchor Cadence M1</title><link rel="stylesheet" href="/mosaic.css"></head><body>
<a class="skip" href="#collection-content">Skip to collection</a><header class="harness"><h1>M1 / Commerce Mosaic</h1><p>Isolated fixture catalog · no real checkout · PENDING HUMAN REVIEW</p><form method="get" action="/"><div><label for="fixture">Test fixture</label><select id="fixture" name="fixture">{options}</select></div><div><label for="sort">Sort</label><select id="sort" name="sort">{sorts}</select></div><div><label for="availability">Availability</label><select id="availability" name="availability">{filters}</select></div><button type="submit">Apply</button></form></header>
<main id="collection-content" tabindex="-1">{collections}</main><footer class="harness">One Anchor Cadence + Standard Grid fallback. Visual verdict: PENDING HUMAN REVIEW.</footer></body></html>'''


if __name__ == '__main__':
    (BASE / 'index.html').write_text(render_page())
