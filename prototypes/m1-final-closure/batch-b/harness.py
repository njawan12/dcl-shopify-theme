"""Bounded native-form operator harness; unchanged Batch A renderer/model imports."""
from pathlib import Path
import sys,copy,json,mimetypes
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlsplit,parse_qs
A=Path(__file__).resolve().parent.parent/'batch-a'
sys.path.insert(0,str(A))
import model,render
STATES={}
DEFAULT={'product':'daily-cleanser','media':'product','copy':'Manual product context','layout':'balanced','order':'note-process','binding':'manual','scheme':'beauty','optional':'show','assembly':'story-collection'}
CHOICES={'product':list(model.PRODUCTS),'media':['product','barrier-cream','none'],'layout':['balanced','compact','editorial'],'order':['note-process','process-note'],'binding':['manual','connected','disconnected'],'scheme':['beauty','neutral'],'optional':['show','omit'],'assembly':['story-collection','collection-story']}
LABELS={'product':'Product','media':'Media source','copy':'Manual context','layout':'PDP composition','order':'Evidence order','binding':'Evidence binding','scheme':'Global brand scheme','optional':'Optional context','assembly':'Story / collection order'}
def state(operator):return STATES.setdefault(operator,copy.deepcopy(DEFAULT))
def preview(s):
 p=copy.deepcopy(model.PRODUCTS[s['product']]);p['description']=s['copy'] if s['optional']=='show' else ''
 if s['media']=='none':p['media']=[]
 elif s['media']!='product':p['media']=copy.deepcopy(model.PRODUCTS[s['media']]['media'])
 p['evidence']=[{'kind':'fact','label':'Product context','body':('Connected source-shaped product context' if s['binding']=='connected' else s['copy']),'qualification':'Synthetic manual/source-shaped fixture; no verified claim.'}]
 if s['optional']=='omit':p['evidence']=[]
 f={'product':p,'choices':[],'name':'balanced','layout':s['layout'],'binding':'manual'}
 # Reorder complete approved primitive outputs, without changing their renderers.
 body=render.pdp(f)
 note=render.rail.render_notes(p['evidence'],'operator-note')
 process=render.rail.render_process({'heading':'Care sequence','steps':p['usage']},'operator-process')
 ordered=note+process if s['order']=='note-process' else process+note
 # Reordering exercise is a separately labelled attachment host, not duplicated responsive markup.
 story='<section><h2>Operator story context</h2><p>'+render.e(s['copy'])+'</p></section>'
 collection=render.collection(12,s['scheme'])
 return body+'<section class="evidence-host" aria-label="Reorderable attachment proof">'+ordered+'</section>'+ (story+collection if s['assembly']=='story-collection' else collection+story)
def page(operator):
 s=state(operator);fields=''
 for k,label in LABELS.items():
  if k=='copy':control='<textarea id="'+k+'" name="'+k+'">'+render.e(s[k])+'</textarea>'
  else:control='<select id="'+k+'" name="'+k+'">'+''.join('<option value="'+render.e(v)+'"'+(' selected' if v==s[k] else '')+'>'+render.e(v)+'</option>' for v in CHOICES[k])+'</select>'
  fields+='<label for="'+k+'">'+label+'</label>'+control
 return '<!doctype html><html lang="en" data-preset="'+s['scheme']+'"><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Bounded operator proof</title>'+''.join('<link rel="stylesheet" href="/'+v+'">' for v in ['reuse/mosaic/mosaic.css','reuse/rail/evidence.css','tokens.css','system.css'])+'</head><body class="integrated"><header><h1>Bounded operator proof</h1><p>Non-production UI. Native form; no source editing. Two isolated operation states.</p></header><form method="post"><input type="hidden" name="operator" value="'+render.e(operator)+'">'+fields+'<button>Apply supported changes</button><button name="reset" value="1">Reset to default</button></form><p role="status">Saved settings for '+render.e(operator)+'</p><dl aria-label="Saved state">'+''.join('<dt>'+LABELS[k]+'</dt><dd data-field="'+k+'">'+render.e(v)+'</dd>' for k,v in s.items())+'</dl><main>'+preview(s)+'</main></body></html>'
class Handler(BaseHTTPRequestHandler):
 def log_message(self,*args):pass
 def send(self,b,kind='text/html',status=200):
  self.send_response(status);self.send_header('Content-Type',kind+'; charset=utf-8');self.send_header('Content-Length',str(len(b)));self.end_headers();self.wfile.write(b)
 def do_GET(self):
  q=parse_qs(urlsplit(self.path).query);path=urlsplit(self.path).path
  if path=='/':return self.send(page(q.get('operator',['operator-one'])[0]).encode())
  p=(A/path.lstrip('/')).resolve()
  if p.is_relative_to(A) and p.is_file() and p.suffix in ['.css','.svg','.jpg','.png']:return self.send(p.read_bytes(),mimetypes.guess_type(str(p))[0])
  self.send(b'Not found','text/plain',404)
 def do_POST(self):
  q={k:v[-1] for k,v in parse_qs(self.rfile.read(int(self.headers['Content-Length'])).decode(),keep_blank_values=True).items()};operator=q.get('operator','operator-one');s=state(operator)
  if q.get('reset'):STATES[operator]=copy.deepcopy(DEFAULT)
  else:
   for k in DEFAULT:
    if k=='copy':s[k]=q.get(k,s[k])[:1200]
    elif q.get(k) in CHOICES[k]:s[k]=q[k]
  self.send(page(operator).encode())
if __name__=='__main__':ThreadingHTTPServer(('127.0.0.1',3006),Handler).serve_forever()
