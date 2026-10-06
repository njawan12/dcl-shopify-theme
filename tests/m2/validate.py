"""Structural production contract checks. These do not certify live Shopify behavior."""
from pathlib import Path
import json,re,gzip,subprocess,os
ROOT=Path(__file__).resolve().parents[2]; T=ROOT/'theme'; results=[]
def check(name,condition):
 results.append({'name':name,'pass':bool(condition)})
 if not condition:raise AssertionError(name)
def text(path):return (T/path).read_text()
def flat(d,prefix=''):
 out={}
 for k,v in d.items():
  name=prefix+k
  if isinstance(v,dict):out.update(flat(v,name+'.'))
  else:out[name]=v
 return out
locale=flat(json.loads(text('locales/en.default.json'))); schema_locale=flat(json.loads(text('locales/en.default.schema.json')))
required='404 article blog cart collection index list-collections page page.contact password product search'.split()
for name in required:
 x=json.loads(text('templates/'+name+'.json'));check('template:'+name,set(x['order'])==set(x['sections']))
 for section in x['sections'].values():check('template-reference:'+name,(T/'sections'/(section['type']+'.liquid')).exists())
for f in ['layout/theme.liquid','templates/gift_card.liquid','config/settings_schema.json','config/settings_data.json']:
 check('required:'+f,(T/f).is_file())
check('no-markets',not (T/'config/markets.json').exists())
allowed={'assets','blocks','config','layout','locales','sections','snippets','templates'}
check('supported-directories',all(p.name in allowed for p in T.iterdir() if p.is_dir()))
check('root-controls',set(p.name for p in T.iterdir() if p.is_file() and p.suffix != '.zip')=={'.theme-check.yml'})
for f in T.rglob('*'):
 if not f.is_file():continue
 if f.parent==T and f.suffix=='.zip':continue  # CLI-generated artifact, checked separately; never theme source
 check('no-forbidden-extension:'+str(f.relative_to(T)),f.suffix not in {'.scss','.sass','.zip'})
 if f.suffix not in {'.liquid','.css','.js','.json','.yml'}:continue
 s=f.read_text()
 check('no-theme-contamination:'+str(f.relative_to(T)),not re.search(r'\b(Dawn|Horizon|Skeleton|jquery|React|Alpine)\b',s,re.I))
 check('no-legacy-liquid:'+str(f.relative_to(T)),not re.search(r'{%\s*(include|partial)\b|\|\s*img_url\b',s))
 if f.suffix in {'.css','.js'}:
  check('readable:'+str(f.relative_to(T)),s.count('\n')>=3 and max(map(len,s.splitlines()))<500)
  if f.suffix=='.js':
   parsed=subprocess.run(['node','--check',str(f)],capture_output=True,text=True)
   check('javascript-syntax:'+f.name,parsed.returncode==0)
 if f.suffix=='.json':json.loads(s)
 for key in re.findall(r"['\"]([a-zA-Z_][\w.]+)['\"]\s*\|\s*t\b",s):
  check('translation:'+key,key in locale or key+'.one' in locale)
 for snippet in re.findall(r"{%[-\s]*render\s+'([^']+)'",s):check('snippet:'+snippet,(T/'snippets'/(snippet+'.liquid')).exists())
settings=json.loads(text('config/settings_schema.json')); controls=[v for group in settings for v in group.get('settings',[]) if 'id' in v]
check('global-count',len(controls)<=19)
check('unique-global-ids',len({v['id'] for v in controls})==len(controls))
check('no-arbitrary-controls',not any(v['type'] in {'range','textarea','liquid'} for v in controls))
check('four-color-pairs',all(any(v['id']==role+'_'+str(i) for v in controls) for i in range(1,5) for role in ['foreground','background']))
section_inventory={}
for f in (T/'sections').glob('*.liquid'):
 match=re.search(r'{% schema %}(.*?){% endschema %}',f.read_text(),re.S);check('schema:'+f.name,bool(match))
 schema=json.loads(match.group(1));section_inventory[f.stem]=schema
 check('section-name:'+f.stem,schema['name'].removeprefix('t:') in schema_locale)
 ss=[v for v in schema.get('settings',[]) if 'id' in v];check('section-budget:'+f.stem,len(ss)<=12)
 check('section-setting-ids:'+f.stem,len({v['id'] for v in ss})==len(ss))
 for b in schema.get('blocks',[]):check('block-budget:'+f.stem+':'+b['type'],len(b.get('settings',[]))<=8)
 for node in [schema,*schema.get('settings',[]),*schema.get('blocks',[])]:
  for k in ['label','name','content']:
   if isinstance(node.get(k),str) and node[k].startswith('t:'):check('schema-label:'+node[k],node[k][2:] in schema_locale)
for group in ['header','footer']:
 check('group-render:'+group,"{% sections '"+group+"-group' %}" in text('layout/theme.liquid'))
 check('group-file:'+group,json.loads(text('sections/'+group+'-group.json'))['type']==group)
for host in ['main-product','featured-product','apps']:
 check('app-host:'+host,any(b['type']=='@app' for b in section_inventory[host]['blocks']))
check('no-static-app-block',"{% render block %}" in text('sections/apps.liquid') and "{% render block %}" in text('snippets/product-surface.liquid'))
check('main-featured-shared',all("render 'product-surface'" in text('sections/'+host+'.liquid') for host in ['main-product','featured-product']))
check('custom-liquid-everywhere','enabled_on' not in section_inventory['custom-liquid'] and 'disabled_on' not in section_inventory['custom-liquid'])
check('no-variant-enumeration',all('product.variants' not in p.read_text() for p in T.rglob('*.liquid')))
check('product-native-form',"form 'product'" in text('snippets/product-form.liquid'))
check('cart-native-form','action="{{ routes.cart_url }}" method="post"' in text('sections/main-cart.liquid'))
check('native-option-route','?option_values=' in text('snippets/variant-options.liquid'))
check('native-plan-route','method="get"' in text('snippets/selling-plans.liquid'))
check('gift-recipient-flag','__shopify_send_gift_card_to_recipient' in text('snippets/gift-recipient.liquid'))
check('account-component','<shopify-account>' in text('sections/header.liquid'))
check('header-untouched','{{ content_for_header }}' in text('layout/theme.liquid'))
check('skip-link','href="#MainContent"' in text('layout/theme.liquid'))
check('reduced-motion','prefers-reduced-motion: reduce' in text('assets/base.css'))
check('css-logical','margin-inline' in text('assets/base.css') and 'min-inline-size' in text('assets/base.css'))
check('image-priority','loading: image_loading' in text('snippets/image.liquid') and "assign image_loading = 'lazy'" in text('snippets/image.liquid'))
check('responsive-image','widths:' in text('snippets/image.liquid') and 'sizes: sizes' in text('snippets/image.liquid'))
check('media-types',all("when '"+k+"'" in text('snippets/product-media.liquid') for k in ['image','video','external_video','model']))
assets={p.name:{'bytes':p.stat().st_size,'gzip_bytes':len(gzip.compress(p.read_bytes(),mtime=0))} for p in (T/'assets').glob('*')}
check('css-budget',assets['base.css']['gzip_bytes']<=45000)
check('global-js-budget',assets['navigation.js']['gzip_bytes']<=25000)
check('total-js-budget',sum(x['gzip_bytes'] for name,x in assets.items() if name.endswith('.js'))<=45000)
check('cart-route-budget',assets['cart.js']['gzip_bytes']+assets['cart-state.js']['gzip_bytes']<=20000)
# Existing tracked baseline, including old workflows/docs/evidence, must be identical.
base='5d7396fdd4b4e5fbaa61334852bfc5a37775255e'
before=subprocess.check_output(['git','ls-tree','-r',base],cwd=ROOT,text=True).splitlines()
for line in before:
 meta,path=line.split('\t',1);expected=meta.split()[2]
 actual=subprocess.check_output(['git','hash-object',path],cwd=ROOT,text=True).strip()
 check('preserved:'+path,actual==expected)
report={'scope':'static architecture/schema/reference/budget and preservation; not live Shopify certification','checks':len(results),'passed':len(results),'failed':0,'global_editable_settings':len(controls),'presentation_controls':len(controls)-2,'platform_brand_controls':2,'assets':assets,'product_blocks':[x['type'] for x in section_inventory['main-product']['blocks']],'section_controls':{k:len([v for v in s.get('settings',[]) if 'id' in v]) for k,s in section_inventory.items()},'required_templates':[x+'.json' for x in required]+['gift_card.liquid'],'results':results}
out=Path(os.environ.get('M2_EVIDENCE_DIR',ROOT/'docs/m2/evidence'));out.mkdir(parents=True,exist_ok=True);(out/'structural-results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['checks','passed','failed','global_editable_settings','presentation_controls','assets']},indent=2))
