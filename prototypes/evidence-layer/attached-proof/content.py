"""Completeness and structural rendering checks, never factual/credibility assessment."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import re
import ipaddress
BASE=Path(__file__).resolve().parent
NOTE_FIELDS=('kind','value','label','body','attribution','source_title','source_url','qualification')

def text(value):
    return value.strip() if isinstance(value,str) else ''


def resolve(value):
    if isinstance(value,dict) and 'connected' in value:
        return value.get('source') if value['connected'] is True else value.get('manual')
    return value


def url(value,targets):
    value=text(value)
    if not value or re.search(r'[\s\\<>"\x00-\x1f\x7f]',value) or re.search(r'%(?![0-9a-fA-F]{2})',value):return None
    if re.search(r'[\x00-\x1f\x7f\\]',unquote(value)):return None
    if value.startswith('#'):return '#'+targets[value[1:]] if value[1:] in targets else None
    try:
        parts=urlsplit(value)
        if parts.scheme in ('http','https') and parts.hostname and not parts.username and not parts.password:
            parts.hostname.encode('idna');port=parts.port
            if port is not None and not 0<=port<=65535:return None
            if ':' in parts.hostname:
                ipaddress.IPv6Address(parts.hostname)
            elif not all(re.fullmatch(r'[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?',label) for label in parts.hostname.encode('idna').decode().rstrip('.').split('.')):return None
            if parts.netloc.endswith(':'):return None
            return value
        if not parts.scheme and not parts.netloc and value.startswith('/') and not value.startswith('//'):
            if parts.path not in ('/pages/fixture-source','/products/fixture-product'):return None
            if any(segment in ('.','..') for segment in unquote(parts.path).split('/')):return None
            return value
    except (ValueError,UnicodeError):pass
    return None


def media(value):
    if not isinstance(value,str) or not re.fullmatch(r'[a-z0-9-]+\.(jpg|svg)',value):return None
    return value if (BASE/'media'/value).is_file() else None


def notes(value):
    value=resolve(value)
    if not isinstance(value,list):return []
    valid=[]
    for raw in value:
        if not isinstance(raw,dict):continue
        n={key:text(raw.get(key)) for key in NOTE_FIELDS};k=n['kind']
        accepted=(k=='metric' and n['value'] and n['label'] or k=='fact' and n['label'] and (n['value'] or n['body']) or k=='claim' and n['body'] or k=='certification' and n['label'] and n['attribution'] or k=='quote' and n['body'] and n['attribution'])
        if accepted:valid.append(n)
    return valid[:3]


def pair(value):
    value=resolve(value)
    if not isinstance(value,dict) or not text(value.get('heading')):return None
    common={k:text(value.get(k)) for k in ('heading','introduction','qualification','source_title','source_url')}
    mode=value.get('mode')
    if mode=='before-after':
        items=value.get('items')
        if not isinstance(items,list) or len(items)!=2:return None
        normalized=[]
        for item in items:
            if not isinstance(item,dict) or not text(item.get('label')) or not media(item.get('media')) or not text(item.get('alt')):return None
            normalized.append({k:text(item.get(k)) for k in ('label','media','alt','caption')})
        return {**common,'mode':mode,'items':normalized}
    if mode=='comparison':
        subjects=value.get('subjects');rows=value.get('rows')
        if not isinstance(subjects,list) or len(subjects)!=2 or not all(text(s) for s in subjects) or not isinstance(rows,list):return None
        valid=[{k:text(r.get(k)) for k in ('criterion','left','right','qualification')} for r in rows if isinstance(r,dict) and all(text(r.get(k)) for k in ('criterion','left','right'))][:4]
        if valid:return {**common,'mode':mode,'subjects':[text(s) for s in subjects],'rows':valid}
    return None


def process(value):
    value=resolve(value)
    if not isinstance(value,dict) or not text(value.get('heading')) or not isinstance(value.get('steps'),list):return None
    steps=[]
    for raw in value['steps']:
        if not isinstance(raw,dict) or not text(raw.get('heading')) or not text(raw.get('instruction')):continue
        step={k:text(raw.get(k)) for k in ('heading','instruction','alt','qualification')}
        step['media']=media(raw.get('media')) if step['alt'] else None
        steps.append(step)
    if not steps:return None
    return {**{k:text(value.get(k)) for k in ('heading','introduction','source_title','source_url')},'steps':steps[:4]}
