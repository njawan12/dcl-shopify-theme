// Actual engine configuration; no CSP, script omission or failure-hook substitution.
const fs=require('node:fs');const path=require('node:path');
const pw=require('/Users/nj/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{let results=[];for(const [name,type,executablePath] of [
 ['Chromium',pw.chromium,'/Users/nj/Library/Caches/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-mac-arm64/chrome-headless-shell'],
 ['Firefox',pw.firefox,'/Users/nj/Documents/Codex/2026-10-03/files-pasted-by-the-user-implement/work/batch-b-browsers/firefox-1538/firefox/Nightly.app/Contents/MacOS/firefox']]){
 let b;let r={browser:name,executablePath,headless:true,javaScriptEnabled:false,steps:[],status:'NOT EXECUTED'};
 try{b=await type.launch({executablePath,headless:true,timeout:15000});r.version=b.version();const c=await b.newContext({javaScriptEnabled:false,viewport:{width:390,height:900}});const p=await c.newPage();await p.goto('http://127.0.0.1:3005/guided?fixture=beauty');r.steps.push({step:'Actual JS-disabled Guided page',nativeLinks:await p.locator('a[href^="/products/"]').count()});await p.locator('a[href^="/products/"]').first().click();r.steps.push({step:'Native product destination',url:p.url(),purchase:await p.locator('.purchase-form').count()});await p.getByRole('button',{name:'Add to simulated cart',exact:true}).click();r.steps.push({step:'Native POST cart',lines:await p.locator('[data-line]').count()});await p.screenshot({path:path.join(__dirname,'evidence/js-disabled-390.jpg')});r.status=r.steps[0].nativeLinks>0&&r.steps[1].purchase===1&&r.steps[2].lines>0?'PASS':'FAIL';}
 catch(e){r.status='NOT EXECUTED — ENGINE LAUNCH BLOCKED';r.error=e.message;r.stepsExecuted=r.steps.length;}
 finally{if(b)await b.close();results.push(r);}}
 fs.writeFileSync(path.join(__dirname,'evidence/js-disabled.json'),JSON.stringify(results,null,2)+'\n');console.log(JSON.stringify(results.map(x=>({browser:x.browser,status:x.status,steps:x.steps.length}))));})();
