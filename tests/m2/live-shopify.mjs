// Real Shopify browser validation. No request mocks, DOM injection or API mutation.
import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';
import assert from 'node:assert/strict';
import { mkdir, writeFile } from 'node:fs/promises';
import { spawnSync } from 'node:child_process';
const out=process.env.M2_LIVE_EVIDENCE_DIR||'/tmp/m2a-live-evidence';await mkdir(out,{recursive:true});
const origin='https://dcl-theme-dev.myshopify.com';
const secret=process.env.M2A_SHOPIFY_PREVIEW_URL;assert.ok(secret,'temporary preview secret required');
const preview=new URL(secret);assert.equal(preview.hostname,'dcl-theme-dev.myshopify.com');assert.equal(preview.searchParams.get('preview_theme_id'),'185844367583');
const redact=value=>JSON.parse(JSON.stringify(value,(k,v)=>{
 if(/cookie|authorization|token|secret/i.test(k))return '[omitted]';
 if(typeof v==='string')return v.replace(/https?:\/\/[^\s"<>]+/g,s=>{try{const u=new URL(s);for(const key of [...u.searchParams.keys()])if(/key|token|_bt|hmac|session|_r|oseid/i.test(key))u.searchParams.delete(key);if(u.pathname.startsWith('/checkouts/'))u.pathname='/checkouts/[session]';return u.toString()}catch{return s}}).replaceAll(secret,'[preview credential omitted]');return v;
}));
const report={store:preview.hostname,themeId:185844367583,uploadedCommit:'b8d10863e668d8660b8b509ff2416f52620a894a',engine:'Chromium',journeys:[],surfaces:[],axe:[],states:[],performance:[],exceptions:[]};
const save=async()=>writeFile(out+'/live-results.json',JSON.stringify(redact(report),null,2)+'\n');
const observe=async(page,label)=>{const data=await page.evaluate(()=>({path:location.pathname+location.search,title:document.title,viewport:innerWidth,scroll:document.documentElement.scrollWidth,liquidError:/Liquid (error|syntax error)|translation missing/i.test(document.body.innerText),header:!!document.querySelector('header'),footer:!!document.querySelector('footer'),headings:[...document.querySelectorAll('h1')].map(e=>e.textContent.trim()),themeAssets:[...document.querySelectorAll('link[href],script[src]')].map(e=>e.href||e.src).filter(s=>s.includes('base.css')||s.includes('navigation.js'))}));assert.equal(data.liquidError,false,label+' Liquid error');assert.ok(data.scroll<=data.viewport+1,label+' overflow');report.surfaces.push({label,...data});await page.screenshot({path:`${out}/${label}.jpg`,fullPage:true});return data;};
const countryUS=async page=>{const select=page.locator('header select[name=country_code]');if(await select.count()&&await select.inputValue()!=='US'){await select.selectOption('US');await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.locator('header form.localization button').click()]);assert.equal(await page.locator('header select[name=country_code]').inputValue(),'US');}};
const go=async(page,path)=>{await page.goto(origin+path,{waitUntil:'domcontentloaded'});await page.locator('main').waitFor();};
let browser;
try {
 browser=await chromium.launch({headless:true});report.browserVersion=browser.version();
 for(const javaScriptEnabled of [true,false]){
  const context=await browser.newContext({javaScriptEnabled,viewport:{width:390,height:900}});const page=await context.newPage();const consoleMessages=[];page.on('console',m=>consoleMessages.push({type:m.type(),text:m.text()}));
  await page.goto(secret,{waitUntil:'domcontentloaded'});await page.locator('header').waitFor();await countryUS(page);
  await go(page,'/products/the-complete-snowboard');const initial=await page.locator('input[name=id]').inputValue();
  await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.getByRole('link',{name:'Dawn',exact:true}).click()]);
  const variant=await page.locator('input[name=id]').inputValue();assert.equal(variant,'67931960606943');
  const product=await page.locator('[data-product-id]').getAttribute('data-product-id');assert.equal(product,'15414509732063');
  assert.equal(await page.locator('.option-link[aria-current]').innerText(),'Dawn');assert.match(await page.locator('main .price').innerText(),/699\.95/);
  await page.getByRole('spinbutton',{name:'Quantity',exact:true}).fill('2');assert.ok(await page.getByRole('button',{name:'Add to cart',exact:true}).isEnabled());
  await observe(page,`product-js-${javaScriptEnabled?'on':'off'}-390`);
  await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.getByRole('button',{name:'Add to cart',exact:true}).click()]);
  assert.equal(new URL(page.url()).pathname,'/cart');assert.equal(await page.locator('input[name="updates[]"]').inputValue(),'2');
  const key=await page.locator('[data-line-key]').getAttribute('data-line-key');assert.ok(key.startsWith(variant+':'));assert.match(await page.locator('main').innerText(),/Dawn/);assert.match(await page.locator('main').innerText(),/1,399\.90/);
  const cart=await observe(page,`cart-js-${javaScriptEnabled?'on':'off'}-390`);
  // Read-only real Shopify cart endpoint verifies server identity after native browser submission.
  const response=await context.request.get(origin+'/cart.js');const actual=await response.json();assert.equal(actual.items.length,1);const item=actual.items[0];assert.equal(item.product_id,Number(product));assert.equal(item.variant_id,Number(variant));assert.equal(item.quantity,2);assert.equal(item.final_price,69995);assert.equal(actual.currency,'USD');assert.equal(item.key,key);assert.equal(item.variant_title,'Dawn');
  report.journeys.push({javaScriptEnabled,viewport:{width:390,height:900},initialVariant:initial,productId:product,variantId:variant,selectedOptions:'Color: Dawn',quantity:2,priceMinor:69995,currency:'USD',lineKey:key,cartPath:cart.path,nativeFormSubmitted:true,scriptPolicy:javaScriptEnabled?'enabled':'browser-context disabled; no script-removal/CSP/failure simulation',serverCartVerified:true,consoleMessages});
  await page.locator('input[name="updates[]"]').fill('3');await page.locator('textarea[name=note]').fill('M2A real-store test note');
  if(javaScriptEnabled){await page.getByRole('button',{name:'Update cart',exact:true}).click();await page.waitForFunction(()=>document.querySelector('main')?.innerText.includes('2,099.85'));}else await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.getByRole('button',{name:'Update cart',exact:true}).click()]);
  assert.equal(await page.locator('input[name="updates[]"]').inputValue(),'3');assert.equal(await page.locator('textarea[name=note]').inputValue(),'M2A real-store test note');report.journeys.at(-1).updateAndNotePassed=true;
  if(javaScriptEnabled){const result=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa','wcag22aa']).analyze();report.axe.push({surface:'cart',violations:result.violations,incomplete:result.incomplete.map(x=>x.id)});await page.getByRole('button',{name:'Checkout',exact:true}).click();await page.waitForURL('**/checkouts/**');report.journeys.at(-1).checkoutBoundaryReached=true;await page.screenshot({path:out+'/checkout-boundary.jpg',fullPage:true});await go(page,'/cart');}
  await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.getByRole('link',{name:'Remove The Complete Snowboard',exact:true}).click()]);assert.match(await page.locator('main').innerText(),/Your cart is empty/);report.journeys.at(-1).removePassed=true;
  if(javaScriptEnabled){
   for(const width of [390,1440,320]){await page.setViewportSize({width,height:900});for(const [label,path] of [['home','/'],['product','/products/the-complete-snowboard'],['collection','/collections/all'],['cart','/cart'],['search','/search?q=snowboard'],['contact','/pages/contact'],['404','/m2a-live-gate-not-found']]){await go(page,path);await observe(page,`${label}-${width}`);if(width===390&&['home','product','collection'].includes(label)){const a=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa','wcag22aa']).analyze();report.axe.push({surface:label,violations:a.violations,incomplete:a.incomplete.map(x=>x.id)});}}}
   await page.setViewportSize({width:390,height:900});
   for(const [name,path] of [['sold-out','/products/the-out-of-stock-snowboard'],['compare-at','/products/the-compare-at-price-snowboard'],['multiple-media','/products/the-videographer-snowboard'],['gift-product','/products/gift-card'],['selling-plans','/products/selling-plans-ski-wax']]){await go(page,path);const text=await page.locator('main').innerText();report.states.push({name,path,text});await observe(page,`${name}-390`);}
   await go(page,'/search');await page.locator('main input[name=q]').fill('snow');await page.locator('main [data-predictions] a').first().waitFor({timeout:15000});report.predictiveSearch={actualEndpoint:true,suggestions:await page.locator('main [data-predictions] a').allTextContents()};
   await go(page,'/collections/all');await page.locator('select[name=sort_by]').selectOption('price-descending');await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.locator('main form button').click()]);assert.match(page.url(),/sort_by=price-descending/);report.sorting=true;
   await page.getByText('Availability (0)',{exact:true}).click().catch(()=>{});const filters=await page.locator('main input[type=checkbox]').count();report.filterControls=filters;
   if(filters){await page.locator('main input[type=checkbox]').first().check();await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.locator('main form button').click()]);report.filterSubmission={path:new URL(page.url()).pathname+new URL(page.url()).search,results:await page.locator('main article').count()};}
   await page.emulateMedia({reducedMotion:'reduce'});report.reducedMotion=await page.evaluate(()=>matchMedia('(prefers-reduced-motion: reduce)').matches);
  }
  await context.close();await save();
 }
 await browser.close();browser=null;
 // Lighthouse uses a real persistent Chromium profile authenticated through Shopify preview,
 // preserves store cookies and never logs or measures the signed credential URL.
 const persistent=await chromium.launchPersistentContext('/tmp/m2a-lighthouse-profile',{headless:true,args:['--remote-debugging-port=9222'],viewport:{width:1440,height:1000}});const lp=await persistent.newPage();await lp.goto(secret,{waitUntil:'domcontentloaded'});await countryUS(lp);
 for(const mode of ['mobile','desktop'])for(const [name,path] of [['home','/'],['product','/products/the-complete-snowboard'],['collection','/collections/all']]){
  const file=`${out}/lighthouse-${name}-${mode}.json`;const args=[process.env.M2_LIGHTHOUSE_CLI,origin+path+'?preview_theme_id=185844367583','--port=9222','--quiet','--disable-storage-reset','--only-categories=performance,accessibility','--output=json','--output-path='+file];if(mode==='desktop')args.push('--preset=desktop');const r=spawnSync(process.execPath,args,{timeout:120000,encoding:'utf8'});
  if(r.status!==0){report.exceptions.push({category:'Lighthouse',name,mode,error:r.stderr||'process failed'});continue;}
  const {readFile}=await import('node:fs/promises');const lhr=JSON.parse(await readFile(file,'utf8'));await writeFile(file,JSON.stringify(redact(lhr),null,2)+'\n');report.performance.push({surface:name,mode,lighthouseVersion:lhr.lighthouseVersion,performance:lhr.categories.performance.score*100,accessibility:lhr.categories.accessibility.score*100,LCP:lhr.audits['largest-contentful-paint'].numericValue,CLS:lhr.audits['cumulative-layout-shift'].numericValue,TBT:lhr.audits['total-blocking-time'].numericValue,INP:'not available as field metric in lab',finalUrl:lhr.finalDisplayedUrl,runtimeError:lhr.runtimeError||null});await save();
 }
 await persistent.close();report.result='PASS_EXECUTED_FUNCTIONAL_CHECKS';
}catch(error){report.result='FAIL';report.error=error.stack;process.exitCode=1;}finally{await save();await browser?.close();}
console.log(JSON.stringify({result:report.result,engine:report.engine,version:report.browserVersion,journeys:report.journeys.length,surfaces:report.surfaces.length,axe:report.axe.map(x=>({surface:x.surface,violations:x.violations.length})),performance:report.performance}));
