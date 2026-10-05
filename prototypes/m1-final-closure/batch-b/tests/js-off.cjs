// One genuine JS-disabled journey only. No CSP, omitted scripts, fake route or failure hook.
const fs = require('node:fs');
const path = require('node:path');
const pw = require('/Users/nj/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const scratch = '/Users/nj/Documents/Codex/2026-10-03/files-pasted-by-the-user-implement/work/batch-b-browsers';
const startURL = 'http://127.0.0.1:3005/guided?fixture=beauty';
const viewport = {width:390,height:900};
const expected = {product:'daily-cleanser',title:'Daily cleansing milk',variant:'daily-cleanser-v1',quantity:2,unitPrice:'CAD 24.00',linePrice:'CAD 48.00',lineKey:'b49262fe6797dab1'};
const plannedSteps = ['Open actual Guided route','Confirm visible native fallback','Confirm aggregate controls absent/inert','Confirm ordinary real product link','Activate link through browser','Assert canonical product/variant and native purchase form','Fill quantity and submit native form','Assert resulting cart product/variant/quantity/price','Check page overflow and critical-action accessibility at each route'];
(async()=>{
 const result = {date:'2026-10-05',acceptedParent:'8486976676b9b901639e92bb43e66040dd0e9bdb',startURL,contextConfiguration:{javaScriptEnabled:false,viewport},expected,plannedSteps,attempts:[],nativeAlternative:{mechanism:'Documented CUA native Google Chrome control; intended dedicated tab and DevTools Disable JavaScript',version:null,stepsExecuted:0,status:'NOT EXECUTED',errors:['First app accessibility snapshot available; no version or JS-disable configuration reached.','pressKey(super+t): Computer Use server error -10005: frontmostApplicationChanged','getAXState(): SCStreamErrorDomain Code=-3801: The user declined TCCs for application, window, display capture']},inAppAlternative:{availableCapabilities:['visibility','viewport'],documentedJSDisableControl:false},verdict:'NOT EXECUTED — ENVIRONMENT BLOCKED'};
 for(const [engine,type,executablePath] of [
  ['Chromium',pw.chromium,'/Users/nj/Library/Caches/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-mac-arm64/chrome-headless-shell'],
  ['Firefox',pw.firefox,scratch+'/firefox-1538/firefox/Nightly.app/Contents/MacOS/firefox'],
  ['WebKit',pw.webkit,scratch+'/webkit-2336/pw_run.sh']]){
  let browser,context;
  const attempt = {engine,version:null,launch:{executablePath,headless:true,timeout:15000},contextConfiguration:{javaScriptEnabled:false,viewport},contextCreated:false,steps:[],screenshots:[],console:[],pageErrors:[],scriptRequests:[],status:'NOT EXECUTED',authorJavaScriptExecuted:'UNOBSERVED — no context created'};
  const record = (step,assertions,observations)=>{attempt.steps.push({step,assertions,observations,pass:Object.values(assertions).every(Boolean)});if(!Object.values(assertions).every(Boolean))throw new Error('Functional assertion failed: '+step);};
  const inspect = async(page,criticalSelector)=>{
   // Automation read-only DOM inspection is distinct from author-page execution.
   const geometry = await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth}));
   const control=page.locator(criticalSelector).first();const box=await control.boundingBox();
   return {url:page.url(),...geometry,criticalVisible:await control.isVisible(),criticalEnabled:await control.isEnabled(),criticalBox:box,criticalContained:!!box&&box.x>=-1&&box.x+box.width<=391};
  };
  try{
   browser=await type.launch(attempt.launch);attempt.version=browser.version();context=await browser.newContext(attempt.contextConfiguration);attempt.contextCreated=true;
   // Browser must suppress author-context init script as well as real module scripts.
   await context.addInitScript("window.__jsDisabledAuthorCanary = 'executed'; console.log('JS_DISABLED_AUTHOR_CANARY_EXECUTED')");
   const page=await context.newPage();page.on('console',m=>attempt.console.push({type:m.type(),text:m.text()}));page.on('pageerror',e=>attempt.pageErrors.push(e.message));page.on('request',r=>{if(r.resourceType()==='script')attempt.scriptRequests.push(r.url())});
   await page.goto(startURL,{waitUntil:'load'});
   record('1 actual Guided route',{actualRoute:page.url()===startURL},{url:page.url()});
   const nativeText=await page.locator('noscript').innerText();
   record('2 usable server/native fallback',{notice:await page.locator('noscript').isVisible(),products:await page.locator('.step .product-title').count()===2,expectedProduct:await page.getByRole('heading',{name:expected.title,exact:true}).isVisible()},{nativeText});
   const aggregate=await page.locator('[data-include],.selection-summary').count();
   record('3 enhancement-dependent aggregate absent',{aggregateAbsent:aggregate===0},{aggregateCount:aggregate});
   const link=page.getByRole('link',{name:'View product: '+expected.title,exact:true});const href=await link.getAttribute('href');const guidedGeometry=await inspect(page,'a.product-link');
   record('4 real navigable product link and Guided fit',{href:href==='/products/'+expected.product,visible:await link.isVisible(),fit:guidedGeometry.scrollWidth===390,critical:guidedGeometry.criticalContained},{href,geometry:guidedGeometry});
   const guidedShot=path.join(__dirname,'evidence/js-disabled-guided-390.jpg');await page.screenshot({path:guidedShot,fullPage:true});attempt.screenshots.push(path.basename(guidedShot));
   await link.click();await page.waitForLoadState('load');record('5 native link navigation',{destination:page.url()==='http://127.0.0.1:3005/products/'+expected.product},{url:page.url()});
   const facts=page.locator('.product-facts');const variant=await facts.getAttribute('data-variant');const product=await facts.getAttribute('data-product');const price=await facts.locator('.price').innerText();const form=page.locator('.purchase-form');const productGeometry=await inspect(page,'.purchase-form button');
   record('6 canonical product and native purchase',{product:product===expected.product,variant:variant===expected.variant,title:await page.getByRole('heading',{name:expected.title,exact:true}).isVisible(),price:price===expected.unitPrice,method:(await form.getAttribute('method')).toLowerCase()==='post',action:await form.getAttribute('action')==='/action',enabled:await form.locator('button').isEnabled(),fit:productGeometry.scrollWidth===390,critical:productGeometry.criticalContained},{url:page.url(),product,variant,price,geometry:productGeometry});
   await form.locator('[name=quantity]').fill(String(expected.quantity));const productShot=path.join(__dirname,'evidence/js-disabled-product-390.jpg');await page.screenshot({path:productShot,fullPage:true});attempt.screenshots.push(path.basename(productShot));
   await form.getByRole('button',{name:'Add to simulated cart',exact:true}).click();await page.waitForLoadState('load');record('7 native HTML purchase POST',{actionRoute:page.url()==='http://127.0.0.1:3005/action'},{url:page.url()});
   const line=page.locator('[data-line]');const lineText=await line.innerText();const lineKey=await line.getAttribute('data-line');const quantity=await line.locator('[name=quantity]').inputValue();
   record('8 canonical cart identity',{oneLine:await line.count()===1,title:lineText.includes(expected.title),variantIdentity:lineKey===expected.lineKey,singleVariant:lineText.includes('Variant: Single variant'),quantity:quantity===String(expected.quantity),unitPrice:lineText.includes(expected.unitPrice+' per item'),linePrice:(await line.locator(':scope > strong').innerText())===expected.linePrice},{url:page.url(),lineKey,quantity,lineText});
   const cartGeometry=await inspect(page,'[data-line] button');const canary=await page.evaluate(()=>window.__jsDisabledAuthorCanary||null);attempt.authorJavaScriptExecuted=canary===null&&!attempt.console.some(m=>m.text.includes('JS_DISABLED_AUTHOR_CANARY_EXECUTED'))?'NO AUTHOR EXECUTION OBSERVED':'EXECUTION OBSERVED';
   record('9 cart fit and author-script suppression',{fit:cartGeometry.scrollWidth===390,critical:cartGeometry.criticalContained,authorCanarySuppressed:canary===null},{geometry:cartGeometry,canary,inspection:'Read-only automation DOM inspection executed; author page scripts disabled by context configuration.'});
   const cartShot=path.join(__dirname,'evidence/js-disabled-cart-390.jpg');await page.screenshot({path:cartShot,fullPage:true});attempt.screenshots.push(path.basename(cartShot));attempt.status='PASS';result.verdict='PASS';
  }catch(e){attempt.status=attempt.contextCreated?'FAIL — FUNCTIONAL JOURNEY':'NOT EXECUTED — ENGINE LAUNCH BLOCKED';attempt.error=e.message;attempt.stepsExecuted=attempt.steps.length;if(attempt.contextCreated)result.verdict='FAIL — FUNCTIONAL JOURNEY';}
  finally{if(context)await context.close();if(browser)await browser.close();result.attempts.push(attempt);}
  if(attempt.contextCreated)break; // A functional failure is not concealed by switching engines.
 }
 fs.writeFileSync(path.join(__dirname,'evidence/js-disabled-final-attempt.json'),JSON.stringify(result,null,2)+'\n');
 console.log(JSON.stringify({verdict:result.verdict,attempts:result.attempts.map(a=>({engine:a.engine,version:a.version,status:a.status,steps:a.steps.length}))}));
 process.exitCode=result.verdict==='PASS'?0:2;
})();
