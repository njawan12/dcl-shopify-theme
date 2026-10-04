"""Loopback-only read-only fixture server; no dependencies or commerce mutations."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
from html import escape
import mimetypes
import os
from render import BASE, PRODUCTS, render_page

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        request = urlparse(self.path)
        query = parse_qs(request.query)
        if request.path in ('/', '/index.html'):
            try: page = int(query.get('page', ['0'])[0])
            except ValueError: page = None
            body = render_page(query.get('fixture', ['branded'])[0], query.get('sort', [None])[0], query.get('availability', [None])[0], page)
            self.send(body.encode(), 'text/html; charset=utf-8'); return
        if request.path.startswith('/products/'):
            product = next((p for p in PRODUCTS.values() if p['url'] == request.path and p.get('published', True)), None)
            if not product: self.send_error(404); return
            self.destination(product['title']); return
        if request.path in ('/pages/field-notes', '/pages/product-notes'):
            self.destination('Fixture editorial / app notes'); return
        path = (BASE / request.path.lstrip('/')).resolve()
        if not path.is_relative_to(BASE) or not path.is_file() or path.suffix not in ('.html', '.css', '.svg', '.jpg', '.json'):
            self.send_error(404); return
        self.send(path.read_bytes(), mimetypes.guess_type(path)[0] or 'application/octet-stream')

    def destination(self, title):
        self.send(f'<!doctype html><html lang="en"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{escape(title)}</title><link rel="stylesheet" href="/mosaic.css"><main class="destination-page"><h1>{escape(title)}</h1><p>Read-only fixture navigation proof. No real Shopify product page, app or checkout.</p><a href="/">Return to collection</a></main></html>'.encode(), 'text/html; charset=utf-8')

    def send(self, body, kind):
        self.send_response(200); self.send_header('Content-Type', kind)
        self.send_header('Content-Length', str(len(body))); self.send_header('Cache-Control', 'no-store'); self.end_headers(); self.wfile.write(body)

    def log_message(self, *args): pass

if __name__ == '__main__':
    port = int(os.environ.get('PORT', '3002'))
    print(f'Anchor Cadence: http://localhost:{port}/', flush=True)
    ThreadingHTTPServer(('127.0.0.1', port), Handler).serve_forever()
