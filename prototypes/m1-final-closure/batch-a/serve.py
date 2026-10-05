"""Loopback-only, dependency-free non-production GET/POST simulation."""
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlsplit,parse_qs
from http.cookies import SimpleCookie
import mimetypes,secrets,json
from model import BASE,PRODUCTS,FIXTURES,new_cart,seeded_cart,mutate
from render import page,repeated_page
from guided import page as guided_page,write_adapter
SESSIONS={};write_adapter()
class Handler(BaseHTTPRequestHandler):
 def log_message(self,*args):pass
 def respond(self,data,status=200,kind='text/html; charset=utf-8',cookie=None):
  self.send_response(status);self.send_header('Content-Type',kind);self.send_header('Cache-Control','no-store');self.send_header('Content-Length',str(len(data)))
  if cookie:self.send_header('Set-Cookie','proof='+cookie+'; Path=/; HttpOnly; SameSite=Lax')
  self.end_headers();self.wfile.write(data)
 def session(self):
  c=SimpleCookie(self.headers.get('Cookie',''));sid=c['proof'].value if 'proof' in c else secrets.token_hex(16)
  if sid not in SESSIONS:SESSIONS[sid]=new_cart()
  return sid,SESSIONS[sid]
 def do_GET(self):
  url=urlsplit(self.path);q={k:v[-1] for k,v in parse_qs(url.query).items()};name=q.get('fixture','balanced');sid,cart=self.session()
  if url.path=='/repeated':return self.respond(repeated_page().encode())
  if url.path=='/guided':return self.respond(guided_page(q.get('fixture','beauty')).encode())
  if url.path.startswith('/sources/'):
   return self.respond(b'<html><head><title>Synthetic source qualification</title></head><body><h1>Synthetic catalog source</h1><p>No genuine merchant provenance, measured result, certification or verified review. Source URL structural validity is not credibility assessment.</p><a href="/pages/story">Return to story</a></body></html>')
  if url.path in ('/','/collection','/cart','/pages/story','/checkout-preview') or url.path.startswith('/products/'):
   product=None
   if 'fixture' not in q:
    name={'/collection':'collection24','/cart':'cart-populated','/pages/story':'story','/checkout-preview':'checkout-preview'}.get(url.path,'balanced')
   if url.path.startswith('/products/'):
    product=url.path.split('/')[-1]
    if product not in PRODUCTS:return self.respond(b'Product reference unavailable',404,'text/plain')
   if name in ('cart-empty','cart-populated','cart-error') and 'fixture' in q:
    cart=new_cart() if name=='cart-empty' else seeded_cart();SESSIONS[sid]=cart
   error='Simulated update failed. Review unchanged line identities and retry.' if name=='cart-error' else ''
   choices=[q.get('option-'+str(i),'') for i in range(2)] if any(k.startswith('option-') for k in q) else None
   choice_product=product or q.get('product')
   if choice_product in PRODUCTS:choices=[q.get('option-'+str(i),'') for i in range(len(PRODUCTS[choice_product]['options']))] if any(k.startswith('option-') for k in q) else None
   try:scale=float(q.get('scale','1'));scale=scale if scale in (1,2,4) else 1
   except ValueError:scale=1
   return self.respond(page(name,cart,error,product or q.get('product'),choices,scale,q.get('preset')).encode(),cookie=sid)
  path=(BASE/url.path.lstrip('/')).resolve()
  if not path.is_relative_to(BASE.resolve()) or not path.is_file() or path.suffix not in ('.css','.js','.jpg','.svg','.png'):return self.respond(b'Not found',404,'text/plain')
  return self.respond(path.read_bytes(),kind=mimetypes.guess_type(str(path))[0] or 'application/octet-stream')
 def do_POST(self):
  if self.path!='/action':return self.respond(b'Not found',404)
  size=int(self.headers.get('Content-Length','0'))
  if size>4096:return self.respond(b'Fixture input too large',413)
  raw={k:v[-1] for k,v in parse_qs(self.rfile.read(size).decode(),keep_blank_values=True).items()};sid,cart=self.session();action=raw.pop('action','');error=''
  try:
   if action=='add':raw['properties']={k:raw.pop('property-'+str(i),'') for i,k in enumerate(PRODUCTS[raw['product']]['required_properties'])}
   if 'fail' in raw:raw['fail']=True
   SESSIONS[sid]=mutate(cart,action,**raw)
  except (ValueError,KeyError) as exc:error=str(exc)
  return self.respond(page('cart-populated',SESSIONS[sid],error).encode(),cookie=sid)
if __name__=='__main__':print('Batch A http://127.0.0.1:3005',flush=True);ThreadingHTTPServer(('127.0.0.1',3005),Handler).serve_forever()
