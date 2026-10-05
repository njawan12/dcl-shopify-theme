"""Exercise B: a narrow contextual product note using canonical content/tokens."""
from html import escape
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'batch-a'))
from model import PRODUCTS

def product_note(product_id,body):
 p=PRODUCTS.get(product_id)
 if not p or not str(body).strip():return ''
 return '<section class="story-product-note"><h2>'+escape(p['title'])+'</h2><p>'+escape(str(body))+'</p><a href="'+escape(p['url'],quote=True)+'">Read product details</a></section>'
