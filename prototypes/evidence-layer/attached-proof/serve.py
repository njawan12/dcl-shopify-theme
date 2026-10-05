"""Loopback, read-only stdlib fixture server. No Shopify/app integration."""
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit,parse_qs,unquote
import mimetypes
from render import render_page,BASE
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed=urlsplit(self.path);path=unquote(parsed.path)
        if path in ('/','/index.html'):
            data=render_page(parse_qs(parsed.query).get('fixture',['branded-pdp'])[0]).encode();kind='text/html; charset=utf-8'
        elif path in ('/products/fixture-product','/pages/fixture-source'):
            data=b'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Read-only fixture context</title><h1>Read-only fixture context</h1><p>Synthetic test navigation only. No Shopify commerce, source credibility or factual claim validation.</p><a href="/">Return to evidence</a></html>';kind='text/html; charset=utf-8'
        elif path=='/evidence.css' or path.startswith('/media/'):
            candidate=(BASE/path.lstrip('/')).resolve()
            if not candidate.is_relative_to(BASE) or not candidate.is_file() or candidate.suffix not in ('.css','.svg','.jpg'):
                self.send_error(404);return
            data=candidate.read_bytes();kind=mimetypes.guess_type(candidate.name)[0] or 'application/octet-stream'
        else:self.send_error(404);return
        self.send_response(200);self.send_header('Content-Type',kind);self.send_header('Cache-Control','no-store');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
    def log_message(self,*args):pass
if __name__=='__main__':ThreadingHTTPServer(('127.0.0.1',3003),Handler).serve_forever()
