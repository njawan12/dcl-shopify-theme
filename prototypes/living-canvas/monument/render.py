"""One server-side semantic rendering path. No browser script or commerce mutation."""
from html import escape
from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parent
DATA = json.loads((BASE / 'fixtures.json').read_text())
FIXTURES = {f['id']: f for f in DATA['fixtures']}


def money(amount, context):
    if type(amount) is not int or amount < 0:
        raise ValueError('Money must be nonnegative integer minor units')
    digits = context['digits']
    whole, fraction = divmod(amount, 10 ** digits)
    separator = ',' if context.get('locale') == 'de' else '.'
    grouped = f"{whole:,}".replace(',', '.') if separator == ',' else f"{whole:,}"
    return f"{context['currency']} {grouped}" + (f'{separator}{fraction:0{digits}d}' if digits else '')


def product_for(fixture):
    source = DATA['products'].get(fixture.get('product'))
    if not source or not source.get('published', True):
        return None
    if not re.fullmatch(r'/products/[a-z0-9-]+', source['url']):
        return None
    return source


def representation(product):
    variants = product['variants']
    requested = product.get('represented_variant')
    selected = next((v for v in variants if v['id'] == requested), None)
    if selected is None and not product.get('options') and len(variants) == 1:
        selected = variants[0]
    if selected:
        status = 'Available on the product page.' if selected['available'] else 'Sold out. View product for details.'
    elif not any(v['available'] for v in variants):
        status = 'Sold out. View product for details.'
    else:
        status = 'Choose options on the product page.'
    if product.get('purchase_context'):
        status += ' ' + product['purchase_context']
    return selected, status


def media_for(product):
    # Gallery data can contain several images; this component owns one dominant object.
    media = product.get('images', [])
    if not media:
        return None
    image = media[0]
    if not re.fullmatch(r'media/[a-z0-9-]+\.(jpg|svg)', image['src']):
        return None
    if not (BASE / image['src']).is_file():
        return None
    return image


def render_component(fixture, instance=1, below_fold=False):
    product = product_for(fixture)
    image = media_for(product) if product else None
    preset = fixture.get('preset', 'branded')
    if preset not in ('branded', 'neutral', 'beauty', 'jewelry', 'food'):
        preset = 'branded'
    headline = fixture.get('headline') or (product['title'] if product else 'A little space.')
    heading_id = f'monument-{instance}-heading'
    chunks = [f'<section class="monument {preset}" aria-labelledby="{heading_id}">', '<header class="statement">']
    if fixture.get('eyebrow'):
        chunks.append(f'<p class="eyebrow">{escape(fixture["eyebrow"])}</p>')
    chunks.append(f'<h1 id="{heading_id}">{escape(headline)}</h1>')
    if fixture.get('copy'):
        chunks.append(f'<p class="support">{escape(fixture["copy"])}</p>')
    editorial = fixture.get('editorial_link')
    if editorial and re.fullmatch(r'/pages/[a-z0-9-]+', editorial['url']):
        chunks.append(f'<a class="editorial-link" href="{escape(editorial["url"], quote=True)}">{escape(editorial["label"])}</a>')
    chunks += ['</header>', '<div class="datum" aria-hidden="true"></div>']
    if image:
        loading = 'lazy' if below_fold or instance > 1 else 'eager'
        chunks.append(f'<figure class="object"><img src="{image["src"]}" width="{image["width"]}" height="{image["height"]}" alt="{escape(image["alt"], quote=True)}" loading="{loading}"></figure>')
    if product:
        variant, status = representation(product)
        context = product['money']
        if variant:
            price = money(variant['price'], context)
        else:
            prices = [v['price'] for v in product['variants']]
            price = money(min(prices), context)
            if min(prices) != max(prices):
                price += ' – ' + money(max(prices), context)
            price += ' · choose options'
        chunks += ['<div class="commerce">', f'<h2 class="product-title">{escape(product["title"])}</h2>', f'<p class="price">{escape(price)}</p>']
        if variant and variant.get('compare_at', 0) > variant['price']:
            chunks.append(f'<p class="compare-at">Previously <s>{escape(money(variant["compare_at"], context))}</s></p>')
        if variant and variant.get('unit_price'):
            unit = variant['unit_price']
            chunks.append(f'<p class="unit-price">{escape(money(unit["amount"], context))} / {escape(unit["reference"])}</p>')
        chunks += [f'<p class="availability">{escape(status)}</p>', f'<a class="product-link" href="{product["url"]}" aria-label="{escape("View product: " + product["title"], quote=True)}">View product<span aria-hidden="true"> ↗</span></a>', '</div>']
    chunks.append('</section>')
    return '\n'.join(chunks)


def render_page(fixture_id='default'):
    fixture = FIXTURES.get(fixture_id, FIXTURES['default'])
    options = '\n'.join(f'<option value="{f["id"]}"{" selected" if f["id"] == fixture["id"] else ""}>{escape(f["label"])}</option>' for f in DATA['fixtures'])
    before = '<aside class="section-context"><h2>Earlier page content</h2><p>Test-only preceding section. Monument must also work below the fold.</p></aside>' if fixture.get('below_fold') else ''
    components = '\n'.join(render_component(fixture, i + 1, fixture.get('below_fold', False)) for i in range(fixture.get('instances', 1)))
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Monument · isolated M1 proof</title><link rel="stylesheet" href="/monument.css"></head>
<body><a class="skip-link" href="#monument-content">Skip to Monument</a>
<header class="harness" aria-label="Prototype test controls"><div><strong>M1 / Monument</strong><p>One Line, One Object · fixture data · no real commerce</p></div><form method="get" action="/"><label for="fixture">Test fixture</label><div class="fixture-controls"><select id="fixture" name="fixture">{options}</select><button type="submit">Load fixture</button></div></form><p class="diagnostic">{escape(fixture['label'])}. Server-rendered evidence; no browser JavaScript.</p></header>
<main id="monument-content" tabindex="-1">{before}{components}</main>
<footer class="harness-footer">Isolated M1 Monument. Visual verdict: PENDING HUMAN REVIEW.</footer></body></html>'''


if __name__ == '__main__':
    (BASE / 'index.html').write_text(render_page())
