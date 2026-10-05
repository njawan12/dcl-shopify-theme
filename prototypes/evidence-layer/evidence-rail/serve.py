"""Local read-only fixture server, no Shopify API or merchant data service."""
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from urllib.parse import urlsplit,parse_qs,unquote
from pathlib import Path
import os
from render import page,BASE
class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs):super().__init__(*args,directory=str(BASE),**kwargs)
    def log_message(self,*args):pass
    def do_GET(self):
        url=urlsplit(self.path);path=unquote(url.path)
        if '..' in Path(path).parts:self.send_error(403);return
        if path in ('/','/index.html'):
            result=page(parse_qs(url.query).get('fixture',['branded-pdp'])[0])
            if parse_qs(url.query).get('test')==['reflow']:result=result.replace('</head>','<link rel="stylesheet" href="/tests/reflow.css"></head>')
        elif path in ('/products/fixture-object','/editorial-destination','/guest-destination'):
            result='<!doctype html><html lang="en"><title>Read-only destination</title><h1>Read-only fixture destination</h1><p>No real cart, review service or product claim.</p><a href="/">Return to evidence</a></html>'
        else:super().do_GET();return
        data=result.encode();self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.send_header('Content-Length',str(len(data)));self.send_header('Cache-Control','no-store');self.end_headers();self.wfile.write(data)
if __name__=='__main__':ThreadingHTTPServer(('127.0.0.1',int(os.environ.get('EVIDENCE_RAIL_PORT','3004'))),Handler).serve_forever()
