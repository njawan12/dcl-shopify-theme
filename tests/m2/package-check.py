from pathlib import Path
import zipfile,json,hashlib,shutil,sys
root=Path(__file__).resolve().parents[2]
archives=list(root.glob('*.zip'))+list((root/'theme').glob('*.zip'))
assert len(archives)==1,archives
archive=archives[0];allowed={'assets','blocks','config','layout','locales','sections','snippets','templates'}
with zipfile.ZipFile(archive) as z:
 names=[p for p in z.namelist() if not p.endswith('/')]
 assert all(p.split('/')[0] in allowed for p in names),names
 assert 'layout/theme.liquid' in names and 'templates/product.json' in names
 assert 'config/markets.json' not in names
 assert not any('node_modules' in p or 'prototypes' in p for p in names)
 for name in names:assert z.read(name)==(root/'theme'/name).read_bytes(),name
expected={str(p.relative_to(root/'theme')) for p in (root/'theme').rglob('*') if p.is_file() and p.parts[len((root/'theme').parts)] in allowed}
assert set(names)==expected,(set(names)^expected)
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
if archive.parent!=out:shutil.copy2(archive,out/archive.name)
report={'archive':archive.name,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'bytes':archive.stat().st_size,'files':len(names),'source_identical':True,'contents':names,'scope':'supported-file distributable package integrity; clean Shopify store install remains untested'}
(out/'package-results.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ['archive','sha256','bytes','files','source_identical']}))
