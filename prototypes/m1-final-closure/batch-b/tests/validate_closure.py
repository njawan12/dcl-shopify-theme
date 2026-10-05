"""Validate recorded closure evidence and preservation; never substitute counts for JS-off."""
from pathlib import Path
import json,hashlib,subprocess
B=Path(__file__).resolve().parent.parent
R=B.parents[2]
E=B/'tests/evidence'
results=[]
def check(name,ok):
 results.append({'test':name,'pass':bool(ok)})
def read(name):return json.loads((E/name).read_text())
for path,digest in read('preservation-before.json').items():
 p=R/path
 check('preserved '+path,p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==digest)
tasks=read('merchant-tasks.json')
check('exactly22 final task records',len(tasks)==22)
for op in ['operator-one','operator-two']:
 t=[r for r in tasks if r['operator']==op];o=[r['observation'] for r in t]
 check(op+' 11 tasks',len(t)==11)
 check(op+' defaults at start',t[0]['startingState']==['daily-cleanser','product','Manual product context','balanced','note-process','manual','beauty','show','story-collection'])
 for r in t:
  check(op+' '+r['task']+' bounded completion',r['completion'] and not r['sourceEditing'] and not r['helpRequired'] and r['elapsedMs']>=0 and bool(r['controls']))
 check(op+' rendered canonical replacement',o[0]['product']=='woven-cloth' and 'Reusable cleansing cloth' in o[0]['body'])
 check(op+' distinct media replacement',o[1]['media']!=o[0]['media'] and o[1]['product']==o[0]['product'])
 check(op+' manual body replacement','Operator-authored ordinary product context' in o[2]['body'])
 check(op+' existing layout preserves applicable inputs',o[3]['layout']=='editorial' and all(o[3]['saved'][k]==o[2]['saved'][k] for k in ['product','media','copy']))
 check(op+' attachment reordering',o[4]['attachmentOrder']==list(reversed(o[3]['attachmentOrder'])))
 check(op+' source-shaped value appears','Connected source-shaped product context' in o[5]['body'])
 check(op+' disconnect valid fallback','Connected source-shaped product context' not in o[6]['body'] and 'Operator-authored ordinary product context' in o[6]['body'])
 check(op+' actual global token propagation',len(o[7]['tokens'])==4 and all(v=='#202020' for v in o[7]['tokens']))
 check(op+' optional Note omitted','Details with a place in the story.' not in o[8]['headings'] and o[8]['product']=='woven-cloth')
 check(op+' mobile fit',o[9]['width']==320 and o[9]['scrollWidth']==320)
 check(op+' actual host assembly',o[10]['headings'].index('Everyday care. Considered choices.')<o[10]['headings'].index('Operator story context'))
r=read('reflow.json')
check('10 reflow/text observations',len(r)==10)
for v in r:
 n=v['fixture']+' scale '+str(v['scale'])
 check(n+' document fit',v['width']==320 and v['scrollWidth']==320)
 check(n+' visible controls within page',all(c['x']>=-1 and c['right']<=321 for c in v['controls']))
 check(n+' no ordinary clipped content',all(c.get('tag')=='INPUT' for c in v['clipped']))
for fixture in ['balanced','compact','editorial','cart-populated','story']:
 pair=[v for v in r if v['fixture']==fixture]
 check(fixture+' semantic heading retention',len(pair)==2 and pair[0]['headings']==pair[1]['headings'])
check('200% native cart quantity action',read('text-resize-action.json')=={'quantity':'3','scrollWidth':320,'width':320})
x=read('extensions-results.json')
check('27 actual extension assertions pass',len(x)==27 and all(v['pass'] for v in x))
m=read('extension-metrics.json')
check('exactly two extensions',len(m)==2 and {v['exercise'] for v in m}=={'purchase','story'})
for v in m:
 p=R/v['files_touched'][0]
 check(v['exercise']+' measured source',hashlib.sha256(p.read_bytes()).hexdigest()==v['sha256'] and len(p.read_text().splitlines())==v['additions'] and p.stat().st_size==v['bytes'])
 check(v['exercise']+' bounded costs',all(v[k]==0 for k in ['deletions','global_token_changes','css_additions','js_additions','commerce_state_additions','existing_surfaces_changed','controls_added']))
c=json.loads((B/'controls.json').read_text())
initial=conditional=0
for k,v in c.items():
 if isinstance(v,dict) and 'initial' in v:
  initial+=len(v['initial']);conditional+=len(v['conditional'])
  check(k+' initial ceiling',len(v['initial'])<=v['ceiling'])
  check(k+' conditional ceiling',len(v['conditional'])<=v.get('conditional_ceiling',0))
check('37initial8conditional decisions',initial==37 and conditional==8)
check('nine bounded UI fields',len(c['batch_b_harness']['fields'])==9)
check('no promoted production settings',c['batch_b_harness']['new_production_settings']==0)
# JS-off is an evidence-integrity check, explicitly NOT a journey pass.
j=read('js-disabled.json')
check('JS-off absence disclosed, not passed',all(v.get('status','').startswith('NOT EXECUTED') and not v.get('steps') for v in j))
for n in ['incumbent-home','incumbent-pdp','incumbent-collection']:
 check(n+' observed evidence present',bool(read(n+'.json')))
rows=[line for line in (B/'shopify-register.md').read_text().splitlines() if line.startswith('|') and line[1:3].isdigit()]
check('30 dated official register rows',len(rows)==30 and all('2026-10-05' in line and 'https://shopify.dev/' in line for line in rows))
pins=json.loads((B.parent/'batch-a/tests/evidence/preservation.json').read_text())['refs']
observed={}
for pin in pins:
 branch,expected=pin.split()
 if branch=='m1-final-closure-batch-a':expected='6dd6619d1fc2d3ea85824d06cb81881b1299a871'
 actual=subprocess.check_output(['git','rev-parse',branch],cwd=R,text=True).strip()
 observed[branch]={'expected':expected,'actual':actual}
 check('unchanged reference '+branch,actual==expected)
(E/'preservation-after.json').write_text(json.dumps({'parent_files':len(read('preservation-before.json')),'all_hashes_unchanged':all(v['pass'] for v in results if v['test'].startswith('preserved ')),'refs':observed},indent=2)+'\n')
(E/'closure-results.json').write_text(json.dumps(results,indent=2)+'\n')
failed=[v['test'] for v in results if not v['pass']]
print(json.dumps({'pass':len(results)-len(failed),'fail':len(failed),'failed':failed}))
raise SystemExit(bool(failed))
