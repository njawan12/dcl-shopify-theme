"""Validate recorded real-browser observations, never synthesize browser measurements."""
import json
from pathlib import Path
B=Path(__file__).parents[1];E=B/'tests/evidence';N=0
def read(name):return json.loads((E/name).read_text())
def check(ok,label):
 global N;N+=1
 if not ok:raise AssertionError(label)
views=read('browser-views.json');check(len(views)==264,'required matrix');check(len({(v['requestedFixture'],v['width']) for v in views})==264,'unique views')
by={(v['requestedFixture'],v['width']):v for v in views}
for v in views:
 name=v['requestedFixture'];w=v['width']
 check(w==v['requestedWidth'],'actual width');check(v['scrollWidth']<=w+1,'document overflow');check(v['spillCount']==0,'visible descendants bounded');check(not v['duplicates'],'scoped IDs');check(len(v['heading'])==1,'one primary heading');check(not any(g['collision'] for g in v['groups']),'principal groups separated');check(not v['stickyOwners'],'zero sticky owners');check(v['rootFont']=='16px','normal-scale observation');check(v['main']['w']<=w+1,'main fits');check(v['mainOrder']==by[name,320]['mainOrder'],'same desktop/mobile semantic order')
 if name.startswith('collection'):check(v['cardCount']==int(name[10:]),'exact encounter count')
 if name.startswith('guided-'):check(len(v['controls'])>=3,'real enhancement initialized')
 if name=='cart-empty':check(len(v['cartLines'])==0,'cart empty')
 if name in ('cart-populated','cart-error'):check(len(v['cartLines'])==3,'canonical seeded lines')
 if name in ('nonexistent','sold-out'):check(v['purchase']['addDisabled'],'unsafe combination action disabled')
for w in [320,375,390,430,768,1024,1280,1440]:
 for name in ['compact','editorial']:
  check(by[name,w]['purchase']==by['balanced',w]['purchase'],'same-data rendered purchase');check(by[name,w]['media']==by['balanced',w]['media'],'same-data rendered media')
frames=read('frames.json');check(len(frames)==34,'controlling and stress frames')
for f in frames:check((B/f['path']).is_file(),'captured frame exists');check(f['imagesLoaded']==f['imagesTotal'],'actual image loading before capture')
journeys=read('browser-journeys.json')
for j in journeys:check(j['pass'],'native journey '+j['label'])
for v in read('repeated.json'):
 check(not v['duplicates'],'repeated IDs');check(v['cardCount']==24,'two independent collections');check(v['scrollWidth']<=v['width'],'repeated fits');check(len(v['tokens'])==5,'two evidence and two collection hosts')
tokens=read('shared-tokens.json')
for row in tokens:
 expected='#203d32' if row['preset']=='beauty' else '#202020'
 for t in row['tokens']:check(t['ink']==expected,'global ink reaches host');check(t['type']=='system-ui, sans-serif','global type reaches host')
reflow=read('reflow.json');reflow_pass=[v for v in reflow if v['scrollWidth']<=v['width']+1 and v['spillCount']==0];reflow_fail=[v for v in reflow if v not in reflow_pass]
report={'pass':N,'fail':0,'matrix_views':264,'native_journey_assertions':len(journeys),'repeated_supplement_views':2,'token_supplement_views':len(tokens),'reflow_supplement_views':len(reflow),'reflow_fitting':len(reflow_pass),'reflow_overflow':[{ 'fixture':v['requestedFixture'],'root_font':v['rootFont'],'width':v['width'],'scroll_width':v['scrollWidth'],'spill_count':v['spillCount']} for v in reflow_fail],'scope':'Passing assertions concern normal matrix/native actions. 400% text-overflow observations are explicitly separate unsuccessful feasibility results. Actual browser-JS-disabled journey NOT EXECUTED (locked Mac).'}
(E/'browser-results.json').write_text(json.dumps(report,indent=2)+'\n');print(f'{N} PASS / 0 FAIL normal matrix/actions; {len(reflow_pass)}/10 text reflow observations fit; {len(reflow_fail)}/10 overflow')
