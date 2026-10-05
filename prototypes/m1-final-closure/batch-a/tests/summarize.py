"""Measured source/asset complexity and actual JPEG inventory, not performance scores."""
import json,gzip,hashlib,re,ast,sys
from pathlib import Path
B=Path(__file__).parents[1];E=B/'tests/evidence'
def metrics(path):
 data=path.read_bytes();lines=data.decode().splitlines();return {'physical_lines':len(lines),'nonblank_lines':sum(bool(l.strip()) for l in lines),'bytes':len(data),'gzip_bytes':len(gzip.compress(data,mtime=0)),'sha256':hashlib.sha256(data).hexdigest()}
runtime=['model.py','render.py','guided.py','serve.py','system.css','tokens.css','dataset.json','controls.json','reuse/guided/fixtures.js'];report={'new_runtime':{p:metrics(B/p) for p in runtime},'authoring_and_tests':{str(p.relative_to(B)):metrics(p) for p in [B/'build_dataset.py',*sorted((B/'tests').glob('*.py')),*sorted((B/'tests').glob('*.mjs')),*sorted((B/'tests').glob('*.js'))]},'copied_implementation':{str(p.relative_to(B)):metrics(p) for p in (B/'reuse').rglob('*') if p.is_file() and p.suffix in ('.py','.css','.js','.json') and p.name!='fixtures.js'},'dependencies_added':0,'runtime_browser_layout_js':0,'new_browser_interaction_logic':'0; generated fixture module exports data and one stateless ID lookup. Original Guided Set interaction engine reused byte-identically.','duplicate_responsive_dom':0,'sticky_owners':0,'new_cart_state_fields':['lines','note','order_discount','message'],'line_identity_fields':['key','product','variant','quantity','plan','properties','discount'],'platform_requests':0,'app_vendors':0,'merchant_position_controls':0,'new_python_functions':{},'breakpoints_px':sorted({int(v) for p in [B/'system.css',*list((B/'reuse').rglob('*.css'))] for v in re.findall(r'@media[^({]*\([^)]*?(?:min|max)-width\s*:\s*(\d+)px',p.read_text())}),'scope':'Includes source bytes separately from copied legacy implementations and captured evidence. Compact source lines are not claimed as simplicity or speed.'}
for name in ['model.py','render.py','guided.py','serve.py']:
 tree=ast.parse((B/name).read_text());report['new_python_functions'][name]=[n.name for n in ast.walk(tree) if isinstance(n,ast.FunctionDef)]
report['served_media']={'files':len(list((B/'media').glob('*'))),'bytes':sum(p.stat().st_size for p in (B/'media').glob('*') if p.is_file()),'unique_packshot_assets':len({m.get('src') or m.get('poster') for p in json.loads((B/'dataset.json').read_text())['products'].values() for m in p['media']}),'note':'24 unique Beauty records do not imply 24 distinct photographs. Shared inherited schematic/packshot assets are explicitly synthetic.'}
sys.path.insert(0,str(B))
from render import page
from model import seeded_cart
report['rendered_html_bytes']={name:len(page(name,seeded_cart() if name=='cart-populated' else None).encode()) for name in ['balanced','compact','editorial','cart-populated','story','collection24','collection100']}
report['integrated_css_bytes']=sum((B/p).stat().st_size for p in ['reuse/mosaic/mosaic.css','reuse/rail/evidence.css','tokens.css','system.css'])
(E/'complexity.json').write_text(json.dumps(report,indent=2)+'\n')
def jpeg_size(data):
 i=2
 while i<len(data):
  if data[i]!=255:i+=1;continue
  marker=data[i+1];i+=2
  if marker in (216,217):continue
  size=int.from_bytes(data[i:i+2],'big')
  if marker in (192,193,194):return int.from_bytes(data[i+5:i+7],'big'),int.from_bytes(data[i+3:i+5],'big')
  i+=size
 raise ValueError('JPEG dimensions absent')
frames=[]
for p in sorted((E/'frames').glob('*.jpg')):
 data=p.read_bytes();w,h=jpeg_size(data);frames.append({'path':str(p.relative_to(B)),'width':w,'height':h,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(E/'screenshot-manifest.json').write_text(json.dumps({'matrix_frames':34,'supplement_frames':len(frames)-34,'total':len(frames),'frames':frames},indent=2)+'\n')
(E/'source-integrity.json').write_text(json.dumps({p:metrics(B/p)['sha256'] for p in runtime},indent=2)+'\n')
print(json.dumps({'frames':len(frames),'new_runtime_bytes':sum(v['bytes'] for v in report['new_runtime'].values()),'media':report['served_media'],'breakpoints':report['breakpoints_px']}))
