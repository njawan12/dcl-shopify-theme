// One genuine JS-disabled journey only. No CSP, omitted scripts, fake route or failure hook.
const fs = require('node:fs');
const path = require('node:path');
const pw = require('playwright');
const output = process.env.JS_OFF_EVIDENCE_DIR || path.join(__dirname,'evidence/js-off-01');
fs.mkdirSync(output,{recursive:true});
const startURL = 'http://127.0.0.1:3005/guided?fixture=beauty';
const viewport = {width:390,height:900};
const expected = {product:'daily-cleanser',title:'Daily cleansing milk',variant:'daily-cleanser-v1',quantity:2,unitPrice:'CAD 24.00',linePrice:'CAD 48.00',lineKey:'b49262fe6797dab1'};
const plannedSteps = ['Open actual Guided route','Confirm visible native fallback','Confirm aggregate controls absent/inert','Confirm ordinary real product link','Activate link through browser','Assert canonical product/variant and native purchase form','Fill quantity and submit native form','Assert resulting cart product/variant/quantity/price','Check page overflow and critical-action accessibility at each route'];
(async()=>{
 const result = {test:'JS-OFF-01',date:new Date().toISOString(),commit:process.env.GITHUB_SHA || null,runURL:process.env.GITHUB_SERVER_URL && process.env.GITHUB_RUN_ID ? `${process.env.GITHUB_SERVER_URL}/${process.env.GITHUB_REPOSITORY}/actions/runs/${process.env.GITHUB_RUN_ID}` : null,startURL,contextConfiguration:{javaScriptEnabled:false,viewport},expected,plannedSteps,attempts:[],verdict:'NOT EXECUTED — ENVIRONMENT BLOCKED'};
 for(const [engine,type] of [['Chromium',pw.chromium]]){
  let browser,context;
  const attempt = {engine,version:null,launch:{headless:true,timeout:30000},contextConfiguration:{javaScriptEnabled:false,viewport},contextCreated:false,steps:[],screenshots:[],console:[],pageErrors:[],scriptRequests:[],documentRequests:[],status:'NOT EXECUTED',authorJavaScriptExecuted:'UNOBSERVED — no context created'};
  const record = (step,assertions,observations)=>{attempt.steps.push({step,assertions,observations,pass:Object.values(assertions).every(Boolean)});if(!Object.values(assertions).every(Boolean))throw new Error('Functional assertion failed: '+step);};
  const inspect = async(page,criticalSelector)=>{
   // Automation read-only DOM inspection is distinct from author-page execution.
   const geometry = await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth}));
   const control=page.locator(criticalSelector).first();await control.scrollIntoViewIfNeeded();const box=await control.boundingBox();
   return {url:page.url(),...geometry,criticalVisible:await control.isVisible(),criticalEnabled:await control.isEnabled(),criticalBox:box,criticalContained:!!box&&box.x>=-1&&box.x+box.width<=391};
  };
  try{
   browser=await type.launch(attempt.launch);attempt.version=browser.version();context=await browser.newContext(attempt.contextConfiguration);attempt.contextCreated=true;
   context.setDefaultTimeout(15000);context.setDefaultNavigationTimeout(30000);
   const page=await context.newPage();page.on('console',m=>attempt.console.push({type:m.type(),text:m.text()}));page.on('pageerror',e=>attempt.pageErrors.push(e.message));page.on('request',r=>{if(r.resourceType()==='script')attempt.scriptRequests.push(r.url());if(r.resourceType()==='document')attempt.documentRequests.push({method:r.method(),url:r.url(),postData:r.postData()})});
   await page.goto(startURL,{waitUntil:'load'});
   record('1 actual Guided route',{actualRoute:page.url()===startURL},{url:page.url()});
   const nativeText=await page.locator('noscript').innerText();
   record('2 usable server/native fallback',{notice:await page.locator('noscript').isVisible(),products:await page.locator('.step .product-title').count()===2,expectedProduct:await page.getByRole('heading',{name:expected.title,exact:true}).isVisible()},{nativeText});
   const aggregate=await page.locator('[data-include],.selection-summary').count();
   record('3 enhancement-dependent aggregate absent',{aggregateAbsent:aggregate===0,originalModuleStillPresent:await page.locator('script[type=module][src="/reuse/guided/split-tension.js"]').count()===1},{aggregateCount:aggregate});
   const link=page.getByRole('link',{name:'View product: '+expected.title,exact:true});const href=await link.getAttribute('href');const guidedGeometry=await inspect(page,'a.product-link');
   record('4 real navigable product link and Guided fit',{href:href==='/products/'+expected.product,visible:await link.isVisible(),fit:guidedGeometry.scrollWidth===390,critical:guidedGeometry.criticalContained&&guidedGeometry.criticalVisible&&guidedGeometry.criticalEnabled},{href,geometry:guidedGeometry});
   const guidedShot=path.join(output,'guided-390.jpg');await page.screenshot({path:guidedShot,fullPage:true});attempt.screenshots.push(path.basename(guidedShot));
   await link.click();await page.waitForLoadState('load');record('5 native link navigation',{destination:page.url()==='http://127.0.0.1:3005/products/'+expected.product},{url:page.url()});
   const facts=page.locator('.product-facts');const variant=await facts.getAttribute('data-variant');const product=await facts.getAttribute('data-product');const price=await facts.locator('.price').innerText();const form=page.locator('.purchase-form');const productGeometry=await inspect(page,'.purchase-form button');
   record('6 canonical product and native purchase',{product:product===expected.product,variant:variant===expected.variant,title:await page.getByRole('heading',{name:expected.title,exact:true}).isVisible(),price:price===expected.unitPrice,method:(await form.getAttribute('method')).toLowerCase()==='post',action:await form.getAttribute('action')==='/action',enabled:await form.locator('button').isEnabled(),fit:productGeometry.scrollWidth===390,critical:productGeometry.criticalContained&&productGeometry.criticalVisible&&productGeometry.criticalEnabled},{url:page.url(),product,variant,price,geometry:productGeometry});
   await form.locator('[name=quantity]').fill(String(expected.quantity));const productShot=path.join(output,'product-390.jpg');await page.screenshot({path:productShot,fullPage:true});attempt.screenshots.push(path.basename(productShot));
   await form.getByRole('button',{name:'Add to simulated cart',exact:true}).click();await page.waitForLoadState('load');const nativePost=attempt.documentRequests.find(r=>r.method==='POST'&&r.url==='http://127.0.0.1:3005/action');const posted=new URLSearchParams(nativePost?.postData||'');record('7 native HTML purchase POST',{actionRoute:page.url()==='http://127.0.0.1:3005/action',browserPOST:!!nativePost,product:posted.get('product')===expected.product,variant:posted.get('variant')===expected.variant,quantity:posted.get('quantity')===String(expected.quantity)},{url:page.url(),nativePost});
   const line=page.locator('[data-line]');const lineText=await line.innerText();const lineKey=await line.getAttribute('data-line');const quantity=await line.locator('[name=quantity]').inputValue();
   record('8 canonical cart identity',{oneLine:await line.count()===1,title:lineText.includes(expected.title),variantIdentity:lineKey===expected.lineKey,singleVariant:lineText.includes('Variant: Single variant'),quantity:quantity===String(expected.quantity),unitPrice:lineText.includes(expected.unitPrice+' per item'),linePrice:(await line.locator(':scope > strong').innerText())===expected.linePrice},{url:page.url(),lineKey,quantity,lineText});
   const cartGeometry=await inspect(page,'[data-line] button');attempt.authorJavaScriptExecuted='NO AUTHOR EXECUTION OBSERVED — context JavaScript disabled; native noscript visible, enhancements absent.';
   record('9 cart fit and script observations',{fit:cartGeometry.scrollWidth===390,critical:cartGeometry.criticalContained&&cartGeometry.criticalVisible&&cartGeometry.criticalEnabled},{geometry:cartGeometry,console:attempt.console,pageErrors:attempt.pageErrors,scriptRequests:attempt.scriptRequests,inspection:'Only read-only automation DOM/geometry inspection; no init script, DOM injection, routing interception, CSP or script removal.'});
   const cartShot=path.join(output,'cart-390.jpg');await page.screenshot({path:cartShot,fullPage:true});attempt.screenshots.push(path.basename(cartShot));attempt.status='PASS';result.verdict='PASS';
  }catch(e){attempt.status=attempt.contextCreated?'FAIL — FUNCTIONAL JOURNEY':'NOT EXECUTED — ENGINE LAUNCH BLOCKED';attempt.error=e.message;attempt.stepsExecuted=attempt.steps.length;if(attempt.contextCreated)result.verdict='FAIL — FUNCTIONAL JOURNEY';}
  finally{if(context)await context.close();if(browser)await browser.close();result.attempts.push(attempt);}
  if(attempt.contextCreated)break; // A functional failure is not concealed by switching engines.
 }
 fs.writeFileSync(path.join(output,'js-off-01.json'),JSON.stringify(result,null,2)+'\n');
 console.log(JSON.stringify({verdict:result.verdict,attempts:result.attempts.map(a=>({engine:a.engine,version:a.version,status:a.status,steps:a.steps.length}))}));
 process.exitCode=result.verdict==='PASS'?0:2;
})();
