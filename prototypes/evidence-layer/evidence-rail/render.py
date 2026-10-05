"""Server-rendered narrow primitives. Fixture identity never selects composition."""
from html import escape
from pathlib import Path
from fixtures import FIXTURES
from content import normalize_note,normalize_pair,normalize_process,media,valid_url
BASE=Path(__file__).parent
LABELS={'fact':'Fact / specification','metric':'Authored metric','claim':'Merchant-authored claim','certification':'Certification record','quote':'Merchant-authored quotation'}
def e(value):return escape(str(value),quote=True)
def paragraph(value,cls=''):return f'<p class="{cls}">{e(value)}</p>' if value else ''
def image(name,alt,eager=False):
    name=media(name)
    return f'<img src="/media/{e(name)}" alt="{e(alt)}" width="800" height="800" loading="{"eager" if eager else "lazy"}">' if name else ''
def source(record,instance):
    title=record.get('source_title','');url=record.get('source_url','')
    url=f'#{instance}-subject' if url=='#subject' else url
    url=valid_url(url,targets=(instance+'-subject',))
    if not title:return ''
    return f'<a class="source" href="{e(url)}">{e(title)}</a>' if url else paragraph(title,'source-text')
def foot(record,instance):
    return '<footer class="qualification">'+paragraph(record.get('qualification',''))+paragraph(record.get('attribution',''),'attribution')+source(record,instance)+'</footer>'
def render_notes(raw,instance):
    notes=[n for r in raw[:3] if (n:=normalize_note(r))]
    if not notes:return ''
    items=[]
    for i,n in enumerate(notes,1):
        statement=('<blockquote>'+paragraph(n['body'])+'</blockquote>') if n['kind']=='quote' else paragraph(n['body'])
        items.append(f'<li role="listitem" class="note" data-kind="{n["kind"]}"><div class="encounter"><span aria-hidden="true">{i:02}</span><p>{LABELS[n["kind"]]}</p></div><div class="note-statement">'+(f'<p class="value">{e(n["value"])}</p>' if n['value'] else '')+paragraph(n['label'],'label')+statement+'</div>'+foot(n,instance)+'</li>')
    return '<section class="attachment notes" data-block="notes" aria-labelledby="'+instance+'-notes"><header class="attachment-title"><p>Evidence / 01</p><h2 id="'+instance+'-notes">Details with a place in the story.</h2></header><ol class="rail note-rail" role="list">'+''.join(items)+'</ol></section>'
def render_pair(raw,instance):
    p=normalize_pair(raw)
    if not p:return ''
    if p['mode']=='before-after':
        body='<div class="paired-media">'+''.join('<figure>'+image(s['media'],s['alt'])+'<figcaption><h3>'+e(s['label'])+'</h3>'+paragraph(s['caption'])+'</figcaption></figure>' for s in p['sides'])+'</div>'
    else:
        body='<table class="comparison"><caption>'+e(p['heading'])+'</caption><thead><tr><th scope="col">Criterion</th>'+''.join('<th scope="col">'+e(s)+'</th>' for s in p['subjects'])+'</tr></thead><tbody>'+''.join('<tr><th scope="row">'+e(r['criterion'])+paragraph(r['qualification'],'row-qualification')+'</th><td>'+e(r['left'])+'</td><td>'+e(r['right'])+'</td></tr>' for r in p['rows'])+'</tbody></table>'
    return '<section class="attachment pair" data-block="pair" data-mode="'+p['mode']+'" aria-labelledby="'+instance+'-pair"><header class="attachment-title"><p>Evidence / 02</p><h2 id="'+instance+'-pair">'+e(p['heading'])+'</h2>'+paragraph(p['introduction'])+'</header><div class="rail pair-content">'+body+foot(p,instance)+'</div></section>'
def render_process(raw,instance):
    p=normalize_process(raw)
    if not p:return ''
    items=[]
    for i,s in enumerate(p['steps'],1):
        items.append('<li role="listitem" class="process-step"><span class="step-number" aria-hidden="true">'+f'{i:02}'+'</span><div><h3>'+e(s['heading'])+'</h3>'+paragraph(s['instruction'])+paragraph(s['qualification'],'step-qualification')+'</div>'+image(s['media'],s['alt'])+'</li>')
    return '<section class="attachment process" data-block="process" aria-labelledby="'+instance+'-process"><header class="attachment-title"><p>Process / sequence</p><h2 id="'+instance+'-process">'+e(p['heading'])+'</h2>'+paragraph(p['introduction'])+'</header><ol class="rail process-rail" role="list">'+''.join(items)+'</ol>'+source(p,instance)+'</section>'
def guest(kind,instance):
    if kind not in ('plain','tall','wide'):return ''
    # Trusted independent harness registry only, never merchant raw-HTML injection.
    fragment=(BASE/'tests/guests'/f'{kind}.html').read_text()
    return '<aside class="app-guest" data-block="app" aria-label="Independent app guest test content"><p class="guest-label">External guest / test document</p><div class="guest-viewport" tabindex="0" role="region" aria-label="Scrollable guest content">'+fragment+'</div></aside>'
def render_instance(f,index):
    instance='rail-'+str(index);s=f['subject'];host=f['host'];blocks=[]
    renderers={'notes':lambda:render_notes(f['notes'],instance),'pair':lambda:render_pair(f['pair'],instance),'process':lambda:render_process(f['process'],instance)}
    allowed=f['order'] if host=='pdp' else (['process'] if f['order']==['process'] else ['notes'])
    g=guest(f['guest'],instance)
    if f['guest_position']=='before':blocks.append(g)
    for i,key in enumerate(allowed):
        blocks.append(renderers[key]())
        if f['guest_position']=='between' and i==0:blocks.append(g)
    if f['guest_position']=='after':blocks.append(g)
    media_html=image(s['media'],s['alt'],eager=True)
    context='<div class="commerce"><h2>'+e(s['product'])+'</h2>'+paragraph(s['price'],'price')+paragraph('Read-only fixture product context; no purchase or inventory promise.')+'<a class="action" href="/products/fixture-object">View product details</a></div>' if host=='pdp' else ''
    subject='<header class="subject" id="'+instance+'-subject" tabindex="-1" data-block="subject"><div class="statement"><p class="eyebrow">'+('Product / evidence' if host=='pdp' else 'Editorial / evidence')+'</p><h1>'+e(s['title'])+'</h1>'+paragraph(s['intro'],'intro')+'</div>'+(f'<figure class="subject-media">{media_html}<figcaption>{e(s["product"])}</figcaption></figure>' if media_html else '')+context+'</header>'
    return '<article class="evidence-host preset-'+f['preset']+' density-'+f['density']+'" dir="'+f['dir']+'" data-instance="'+instance+'" data-host="'+host+'">'+subject+''.join(blocks)+('<a class="action editorial-action" href="/editorial-destination">Continue the story</a>' if host=='editorial' else '')+'</article>'
def page(name='branded-pdp'):
    name=name if name in FIXTURES else 'branded-pdp';f=FIXTURES[name]
    options=''.join('<option value="'+e(k)+'"'+(' selected' if k==name else '')+'>'+e(k)+'</option>' for k in FIXTURES)
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>M1 Evidence Rail — '+e(name)+'</title><link rel="stylesheet" href="/evidence.css"></head><body class="preset-'+f['preset']+'"><a class="skip" href="#content">Skip to evidence</a><div class="harness"><p>M1 Evidence Rail · synthetic test content · not merchant proof</p><form method="get"><label for="fixture">Fixture</label><select id="fixture" name="fixture">'+options+'</select><button type="submit">Load fixture</button></form></div><main id="content" tabindex="-1">'+''.join(render_instance(f,i+1) for i in range(f['instances']))+'</main><footer class="site-footer">Isolated M1 proof. Visual verdict: PENDING HUMAN REVIEW.</footer></body></html>'
if __name__=='__main__':(BASE/'index.html').write_text(page())
