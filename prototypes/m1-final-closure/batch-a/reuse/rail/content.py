"""Completeness and structural rendering checks only; never claim/source credibility."""
from pathlib import Path
from urllib.parse import urlsplit
BASE=Path(__file__).parent
KINDS={'metric','fact','claim','certification','quote'}
NOTE_FIELDS=('kind','value','label','body','attribution','source_title','source_url','qualification')

def text(value): return str(value).strip() if isinstance(value,(str,int,float)) and not isinstance(value,bool) else ''
def bind(raw):
    if not isinstance(raw,dict): return {}
    binding=raw.get('binding')
    if not isinstance(binding,dict): return raw
    return binding.get('value',{}) if binding.get('state')=='connected' else binding.get('fallback',{})
def valid_url(value,targets=()):
    value=text(value)
    if not value or any(ord(c)<33 or c in '<>"\\' for c in value): return ''
    if value.startswith('#'): return value if value[1:] in targets else ''
    try:
        parts=urlsplit(value)
        if value.startswith('/') and not value.startswith('//'): return value if not parts.scheme and not parts.netloc else ''
        if parts.scheme in ('http','https') and parts.hostname and not parts.username and not parts.password:
            _=parts.port
            return value
    except ValueError: pass
    return ''
def media(value):
    name=text(value)
    return name if name and Path(name).name==name and name.endswith(('.jpg','.svg','.png')) and (BASE/'media'/name).is_file() else ''
def normalize_note(raw):
    raw=bind(raw)
    if not isinstance(raw,dict): return None
    n={k:text(raw.get(k)) for k in NOTE_FIELDS}
    kind=n['kind']
    valid=(kind=='metric' and n['value'] and n['label'] or kind=='fact' and n['label'] and (n['value'] or n['body']) or kind=='claim' and n['body'] or kind=='certification' and n['label'] and n['attribution'] or kind=='quote' and n['body'] and n['attribution'])
    return n if kind in KINDS and valid else None

def normalize_pair(raw):
    raw=bind(raw)
    if not isinstance(raw,dict) or not text(raw.get('heading')):return None
    p={k:text(raw.get(k)) for k in ('mode','heading','introduction','qualification','source_title','source_url')}
    if p['mode']=='before-after':
        sides=raw.get('sides',[])[:2]
        if len(sides)!=2 or not all(text(s.get('label')) and media(s.get('media')) and text(s.get('alt')) for s in sides): return None
        p['sides']=[{k:text(s.get(k)) for k in ('label','media','alt','caption')} for s in sides]
    elif p['mode']=='comparison':
        subjects=[text(v) for v in raw.get('subjects',[])[:2]]
        rows=[{k:text(r.get(k)) for k in ('criterion','left','right','qualification')} for r in raw.get('rows',[])[:4] if all(text(r.get(k)) for k in ('criterion','left','right'))]
        if len(subjects)!=2 or not all(subjects) or not rows:return None
        p.update(subjects=subjects,rows=rows)
    else:return None
    return p

def normalize_process(raw):
    raw=bind(raw)
    if not isinstance(raw,dict) or not text(raw.get('heading')):return None
    p={k:text(raw.get(k)) for k in ('heading','introduction','source_title','source_url')}
    p['steps']=[{k:(media(s.get(k)) if k=='media' else text(s.get(k))) for k in ('heading','instruction','media','alt','qualification')} for s in raw.get('steps',[])[:4] if text(s.get('heading')) and text(s.get('instruction'))]
    return p if p['steps'] else None
