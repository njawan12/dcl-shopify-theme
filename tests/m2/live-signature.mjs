// M2B actual Shopify extension to the existing native-browser harness.
import assert from 'node:assert/strict';
import AxeBuilder from '@axe-core/playwright';
export async function runSignature({browser,secret,origin,go,countryUS,observe,report,out,save}) {
 report.signature={compositions:[],nativeJourneys:[],nativeAdvanced:[],stress:[],app:[],keyboard:[]};
 const fixtures=[['ordinary','the-complete-snowboard'],['complex','m2a-integration-test-two-options-no-media'],['plan','selling-plans-ski-wax'],['sold-out','the-out-of-stock-snowboard'],['compare','the-compare-at-price-snowboard'],['media','the-videographer-snowboard']];
 for(const javaScriptEnabled of [true,false]) {
  const ctx=await browser.newContext({javaScriptEnabled,viewport:{width:390,height:900}});const page=await ctx.newPage();
  await page.goto(secret,{waitUntil:'domcontentloaded'});await page.locator('.site-header').waitFor();await countryUS(page);
  for(const composition of ['balanced','compact','editorial']) {
   const query=composition==='balanced'?'':'?view='+composition;
   if(javaScriptEnabled) {
    for(const [fixture,handle] of fixtures)for(const width of [1440,390]) {
     await page.setViewportSize({width,height:900});await go(page,'/products/'+handle+query);
     assert.equal(await page.locator('[data-composition]').getAttribute('data-composition'),composition);
     assert.equal(await page.locator('form.product-form').count(),1);
     const obs=await observe(page,`${composition}-${fixture}-${width}`);
     const state={composition,fixture,width,path:obs.path,productId:await page.locator('[data-product-id]').getAttribute('data-product-id'),variantId:await page.locator('input[name=id]').inputValue(),price:await page.locator('main .price').allTextContents(),buttons:await page.locator('.product-form > button').allTextContents()};
     if(fixture==='sold-out')assert.ok(await page.getByRole('button',{name:'Sold out',exact:true}).isDisabled());
     if(fixture==='complex'){assert.ok(await page.locator('.media-placeholder').count());assert.match(state.price.join(' '),/12\.00/);assert.match(state.price.join(' '),/6\.00/);}
     if(fixture==='compare')assert.equal(await page.locator('main .price s').count(),1);
     const guests=await page.locator('.app-host').evaluateAll(es=>es.map(e=>({width:e.clientWidth,scroll:e.scrollWidth,childCount:e.children.length,insideEvidenceList:!!e.closest('.evidence-rail-list,.evidence-steps')})));assert.ok(guests.length>0,'real configured app guest required');assert.ok(guests.every(g=>!g.insideEvidenceList));report.signature.app.push({composition,fixture,width,guests});report.signature.compositions.push(state);await save();
    }
    for(const width of [320,375,430,768,1024,1280]) {
     await page.setViewportSize({width,height:900});await go(page,'/products/the-complete-snowboard'+query);const data=await page.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth}));assert.ok(data.scroll<=width+1);report.signature.stress.push({composition,kind:'width',...data});
    }
    await page.setViewportSize({width:320,height:900});await go(page,'/products/the-complete-snowboard'+query);await page.addStyleTag({content:'html {font-size:200% !important}'});await observe(page,composition+'-text-200-320');
    report.signature.stress.push({composition,kind:'controlled 200% text feasibility; not native zoom certification',...await page.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth}))});
    await page.setViewportSize({width:390,height:900});await go(page,'/products/the-complete-snowboard'+query);
    const a=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa','wcag22aa']).analyze();report.axe.push({surface:composition,violations:a.violations,incomplete:a.incomplete.map(x=>x.id)});
    assert.equal(a.violations.filter(x=>x.impact==='critical'||x.impact==='serious').filter(x=>!(x.id==='frame-title'&&x.nodes.every(n=>n.target.join(' ').includes('PBarNextFrame')))).length,0,'theme-owned serious accessibility issue');
    for(let i=0;i<24;i++){await page.keyboard.press('Tab');report.signature.keyboard.push({composition,...await page.evaluate(()=>({tag:document.activeElement.tagName,text:(document.activeElement.innerText||document.activeElement.getAttribute('aria-label')||'').slice(0,80),outline:getComputedStyle(document.activeElement).outlineStyle}))});}
    await page.emulateMedia({reducedMotion:'reduce'});assert.equal(await page.evaluate(()=>matchMedia('(prefers-reduced-motion: reduce)').matches),true);
    report.signature.stress.push({composition,reducedMotion:true});
    // Neutralization is disclosed diagnostic CSS on the actual real-store DOM, never a fixture substitute.
    if(composition==='editorial')for(const width of [1440,390]){
     await page.setViewportSize({width,height:900});await go(page,'/products/the-complete-snowboard'+query);
     await page.addStyleTag({content:':root {--font-body:system-ui;--font-heading:system-ui;--background-1:#fff;--foreground-1:#111;--background-2:#eee;--foreground-2:#111;--accent:#111} * {animation:none!important;transition:none!important}'});
     await observe(page,'editorial-neutral-'+width);
    }
   }
   // Each structure preserves native variant navigation and browser-submitted cart truth with JS on/off.
   await page.setViewportSize({width:390,height:900});await go(page,'/products/the-complete-snowboard'+query);
   await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.getByRole('link',{name:'Dawn',exact:true}).click()]);
   assert.equal(await page.locator('[data-composition]').getAttribute('data-composition'),composition);
   assert.equal(await page.locator('input[name=id]').inputValue(),'67931960606943');
   await page.getByRole('spinbutton',{name:'Quantity',exact:true}).fill('2');
   await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.getByRole('button',{name:'Add to cart',exact:true}).click()]);
   assert.equal(new URL(page.url()).pathname,'/cart');const cart=await (await ctx.request.get(origin+'/cart.js')).json();
   assert.equal(cart.items.length,1);const item=cart.items[0];assert.equal(item.product_id,15414509732063);assert.equal(item.variant_id,67931960606943);assert.equal(item.quantity,2);assert.equal(item.final_price,69995);assert.equal(cart.currency,'USD');
   const cartObs=await observe(page,`${composition}-cart-js-${javaScriptEnabled?'on':'off'}-390`);
   report.signature.nativeJourneys.push({composition,javaScriptEnabled,viewport:{width:390,height:900},nativeVariantLink:true,nativeFormSubmitted:true,productId:item.product_id,variantId:item.variant_id,quantity:item.quantity,priceMinor:item.final_price,currency:cart.currency,cartPath:cartObs.path});
   await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.getByRole('link',{name:'Remove The Complete Snowboard',exact:true}).click()]);
   await save();
   if(!javaScriptEnabled) {
    await go(page,'/products/m2a-integration-test-two-options-no-media'+query);
    await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.getByRole('link',{name:'Large',exact:true}).click()]);
    await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.getByRole('link',{name:/^Gloss/}).click()]);
    assert.equal(await page.locator('[data-composition]').getAttribute('data-composition'),composition);assert.ok(await page.getByRole('button',{name:'Unavailable',exact:true}).isDisabled());assert.equal(await page.locator('main .price').count(),0);await observe(page,composition+'-unresolved-js-off-390');
    await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.getByRole('link',{name:'Small',exact:true}).click()]);
    await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.getByRole('button',{name:'Add to cart',exact:true}).click()]);
    let actual=await (await ctx.request.get(origin+'/cart.js')).json();assert.equal(actual.items.length,1);assert.equal(actual.items[0].variant_id,67933304029407);assert.equal(actual.items[0].final_price,1200);assert.equal(actual.items[0].unit_price,600);await observe(page,composition+'-unit-cart-js-off-390');
    report.signature.nativeAdvanced.push({composition,javaScriptEnabled:false,kind:'nonexistent tuple recovery / unit price',variantId:actual.items[0].variant_id,quantity:actual.items[0].quantity,priceMinor:actual.items[0].final_price,unitPrice:actual.items[0].unit_price});
    await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.getByRole('link',{name:'Remove M2A Integration Test — Two Options (no media)',exact:true}).click()]);
    await go(page,'/products/selling-plans-ski-wax'+query);await page.locator('select[name=selling_plan]').selectOption('8657469663');
    await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.locator('main form[method=get] button').click()]);
    assert.equal(await page.locator('[data-composition]').getAttribute('data-composition'),composition);assert.match(await page.locator('main .price').innerText(),/21.21/);await observe(page,composition+'-allocated-plan-js-off-390');
    await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.getByRole('button',{name:'Add to cart',exact:true}).click()]);
    actual=await (await ctx.request.get(origin+'/cart.js')).json();assert.equal(actual.items.length,1);assert.equal(actual.items[0].selling_plan_allocation.selling_plan.id,8657469663);assert.equal(actual.items[0].final_price,2121);await observe(page,composition+'-plan-cart-js-off-390');
    report.signature.nativeAdvanced.push({composition,javaScriptEnabled:false,kind:'native weekly allocation',variantId:actual.items[0].variant_id,planId:8657469663,quantity:actual.items[0].quantity,priceMinor:actual.items[0].final_price});
    await Promise.all([page.waitForNavigation({waitUntil:'domcontentloaded'}),page.getByRole('link',{name:'Remove Selling Plans Ski Wax',exact:true}).click()]);await save();
   }
  }
  if(javaScriptEnabled)for(const [name,path] of [['home','/'],['story','/?view=evidence']])for(const width of [1440,390]){await page.setViewportSize({width,height:900});await go(page,path);await observe(page,name+'-'+width);}
  await ctx.close();
 }
}
