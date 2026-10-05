"""Exercise A: optional native disclosure, shared purchase truth unchanged."""
from html import escape
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'batch-a'))
from render import purchase
from model import truth

def with_support(product,choices,name,support=None):
 body=purchase(product,choices,name)
 if support and support.get('body','').strip():
  body+='<details class="purchase-support"><summary>'+escape(support.get('label','Purchase information'))+'</summary><p>'+escape(support['body'])+'</p></details>'
 return body,truth(product,choices)
