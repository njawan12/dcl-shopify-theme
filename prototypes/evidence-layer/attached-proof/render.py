"""Three narrow evidence renderers shared by fixed PDP/editorial proof contexts."""
from html import escape
from pathlib import Path
import json
from content import text,notes,pair,process,url,media
BASE=Path(__file__).resolve().parent
DATA=json.loads((BASE/'fixtures.json').read_text())
FIXTURES={f['id']:f for f in DATA['fixtures']}

def e(value):return escape(text(value),quote=True)

def paragraph(value,klass=''):
    return f'<p{f" class=\"{klass}\"" if klass else ""}>{e(value)}</p>' if text(value) else ''

def source(title,address,targets):
    title=text(title)
    if not title:return ''
    href=url(address,targets)
    return '<p class="source">'+(f'<a href="{e(href)}">{e(title)}</a>' if href else e(title))+'</p>'

def image(name,alt,eager=False):
    name=media(name)
    if not name:return ''
    dimensions={'care-pump.jpg':(1254,1254),'utility-case.jpg':(1254,1254),'metal-ring.svg':(600,600),'pantry-jar.svg':(600,600),'storage-before.svg':(800,600),'storage-after.svg':(800,600)}
    w,h=dimensions[name]
    return f'<img src="/media/{name}" alt="{e(alt)}" width="{w}" height="{h}" loading="{"eager" if eager else "lazy"}" decoding="async">'

def render_notes(items,identity,targets):
    if not items:return ''
    out=[f'<section class="note-group" data-primitive="notes" aria-labelledby="{identity}-notes"><h3 id="{identity}-notes" class="eyebrow">Attached information</h3><ul class="notes">']
    for i,n in enumerate(items,1):
        out.append(f'<li class="evidence-note" data-kind="{n["kind"]}">')
        if n['label']:out.append(f'<h4>{e(n["label"])}</h4>')
        if n['value']:out.append(paragraph(n['value'],'value'))
        if n['kind']=='quote':out.append(f'<blockquote>{paragraph(n["body"])}</blockquote><p class="attribution">{e(n["attribution"])}</p>')
        else:out.extend([paragraph(n['body']),paragraph(n['attribution'],'attribution')])
        out.extend([paragraph(n['qualification'],'qualification'),source(n['source_title'],n['source_url'],targets),'</li>'])
    out.append('</ul></section>');return '\n'.join(out)

def render_pair(value,identity,targets):
    if value is None:return ''
    out=[f'<section class="education pair" data-primitive="pair" data-mode="{value["mode"]}" aria-labelledby="{identity}-pair"><header><p class="eyebrow">Compare / Context</p><h3 id="{identity}-pair">{e(value["heading"])}</h3>{paragraph(value["introduction"])}</header>']
    if value['mode']=='before-after':
        out.append('<div class="paired-media">')
        for item in value['items']:
            out.append(f'<figure><h4>{e(item["label"])}</h4><div class="media">{image(item["media"],item["alt"])}</div><figcaption>{e(item["caption"])}</figcaption></figure>')
        out.append('</div>')
    else:
        out.append('<div class="comparison"><p class="subjects">'+e(value['subjects'][0])+' / '+e(value['subjects'][1])+'</p><dl>')
        for row in value['rows']:
            out.append('<div class="comparison-row"><dt>'+e(row['criterion'])+'</dt><dd><span class="subject-name">'+e(value['subjects'][0])+'</span>'+e(row['left'])+'</dd><dd><span class="subject-name">'+e(value['subjects'][1])+'</span>'+e(row['right'])+'</dd>'+('<dd class="qualification">'+e(row['qualification'])+'</dd>' if row['qualification'] else '')+'</div>')
        out.append('</dl></div>')
    out.extend([paragraph(value['qualification'],'qualification'),source(value['source_title'],value['source_url'],targets),'</section>']);return '\n'.join(out)

def render_process(value,identity,targets):
    if value is None:return ''
    out=[f'<section class="education process" data-primitive="process" aria-labelledby="{identity}-process"><header><p class="eyebrow">Process / In order</p><h3 id="{identity}-process">{e(value["heading"])}</h3>{paragraph(value["introduction"])}</header><ol class="steps" role="list">']
    for i,step in enumerate(value['steps'],1):
        out.append(f'<li class="step"><span class="step-index" aria-hidden="true">{i:02}</span><div class="step-content"><h4>{e(step["heading"])}</h4>{paragraph(step["instruction"])}'+(f'<figure class="media">{image(step["media"],step["alt"])}</figure>' if step['media'] else '')+paragraph(step['qualification'],'qualification')+'</div></li>')
    out.extend(['</ol>',source(value['source_title'],value['source_url'],targets),'</section>']);return '\n'.join(out)

def render_app(value,identity):
    if not isinstance(value,dict) or not text(value.get('heading')) or not text(value.get('body')):return ''
    href=url(value.get('link'),{})
    return f'<aside class="app-slot" data-app="guest" aria-labelledby="{identity}-app"><div class="guest"><h3 id="{identity}-app">{e(value["heading"])}</h3>{paragraph(value["body"])}'+(f'<a href="{e(href)}">Guest context</a>' if href else '')+'</div></aside>'

def render_host(f,instance=1):
    identity=f'evidence-{instance}';ns=notes(f.get('notes'));pv=pair(f.get('pair')) if f['host']=='pdp' else None;ps=process(f.get('process'))
    if f['host']=='editorial' and ns:ps=None
    targets={'subject':identity+'-subject'}
    if pv:targets['pair']=identity+'-pair'
    if ps:targets['process']=identity+'-process'
    preset=f.get('preset','neutral');preset=preset if preset in ('beauty','neutral','jewelry','food') else 'neutral'
    density=f.get('density','balanced');density=density if density in ('compact','balanced','spacious') else 'balanced'
    emphasis=f.get('emphasis','quiet');emphasis=emphasis if emphasis in ('quiet','strong') else 'quiet'
    out=[f'<section class="host {f["host"]} {preset} {density} {emphasis}" data-host="{f["host"]}" aria-labelledby="{identity}-heading"><header class="intro"><p class="eyebrow">{"Product / Attached information" if f["host"]=="pdp" else "Editorial / Attached information"}</p><h2 id="{identity}-heading">{e(f["title"])}</h2>{paragraph(f.get("introduction"))}</header>']
    product=f['product'];subject=f'<figure class="subject" tabindex="-1" id="{identity}-subject"><div class="media">{image(product.get("media"),product.get("alt"),instance==1) or paragraph("Subject image unavailable")}</div><figcaption>{e(product["title"])}</figcaption></figure>'
    if f['host']=='pdp':
        out.append('<div class="pdp-opening"><div class="media-attachment">'+subject+render_notes(ns,identity,targets)+'</div><section class="commerce" aria-labelledby="'+identity+'-product"><p class="eyebrow">Read-only product context</p><h3 id="'+identity+'-product">'+e(product['title'])+'</h3>'+paragraph(product['price'],'price')+paragraph(product['status'])+'<a href="/products/fixture-product">View fixture product</a>'+paragraph('No add-to-cart or real Shopify commerce is represented.','qualification')+'</section></div>')
        out.extend([render_pair(pv,identity,targets),render_process(ps,identity,targets),render_app(f.get('app'),identity)])
    else:
        out.append('<div class="editorial-attachment">'+subject+render_notes(ns,identity,targets)+render_process(ps,identity,targets)+'</div><a class="editorial-action" href="/pages/fixture-source">Read the fixture context</a>')
    out.append('</section>');return '\n'.join(out)

def render_page(fid='branded-pdp'):
    f=FIXTURES.get(fid,FIXTURES['branded-pdp'])
    options=''.join(f'<option value="{e(k)}"{" selected" if k==f["id"] else ""}>{e(v["label"])}</option>' for k,v in FIXTURES.items())
    hosts='\n'.join(render_host(f,i+1) for i in range(f.get('instances',1)))
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>M1 Evidence Layer — PENDING HUMAN REVIEW</title><link rel="stylesheet" href="/evidence.css"></head><body><a class="skip" href="#main">Skip to evidence</a><header class="harness"><h1>M1 / Evidence Layer</h1><p>{e(DATA["disclaimer"])}</p><form method="get"><label for="fixture">Test fixture</label><select id="fixture" name="fixture">{options}</select><button>Apply</button></form></header><main id="main" tabindex="-1">{hosts}</main><footer>Isolated prototype. Visual verdict: PENDING HUMAN REVIEW.</footer></body></html>'

if __name__=='__main__':(BASE/'index.html').write_text(render_page())
