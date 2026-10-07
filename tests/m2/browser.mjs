/* Browser-level component tests of production assets/snippets. NOT a Shopify
 * end-to-end purchase test; response stubs and platform filter adapters are explicit. */
import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { readFile, mkdir, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { render, engine, fixture } from './liquid-engine.mjs';
const root = resolve(new URL('../../', import.meta.url).pathname);
const out = process.env.M2_EVIDENCE_DIR || resolve(root, 'docs/m2/evidence/browser');
await mkdir(out, { recursive: true });
const data = fixture();
data.product = { ...data.product, title: 'Ordinary product with a long practical description', vendor: 'Example merchant', description: '<p>Ordinary merchant content, no required photography.</p>', media: [], selected_or_first_available_variant: data.variant, has_only_default_variant: true };
data.section.blocks = ['title','price','options','plans','quantity','buy','description'].map(type => ({ type, settings: { dynamic_checkout: true, recipient: true } }));
data.primary = true;
const products={};
for(const composition of ['balanced','compact','editorial']) {
 data.section.settings={composition};
 const note={type:'evidence_note',settings:{heading:'Supplied product context',kind_1:'fact',value_1:'30 g',label_1:'Declared mass',body_1:'Ordinary manual content.',qualification_1:'Merchant authored.',source_title_1:'Supplied specification',source_url_1:'/pages/specification'}};
 const pair={type:'evidence_pair',settings:{mode:'comparison',heading:'Two declared contexts',left_subject:'First',right_subject:'Second',criterion_1:'Material',left_1:'Cotton',right_1:'Wool'}};
 const process={type:'evidence_process',settings:{heading:'Care instructions',heading_1:'Read',instruction_1:'Read the supplied care label.'}};
 const baseBlocks=data.section.blocks.filter(b=>!b.type.startsWith('evidence_'));
 data.section.blocks=[...baseBlocks,note,pair,process];
 products[composition]=await render('product-surface',data);
}
const product=products.balanced;
const line = {key:'501:properties-plan',product:{title:'Ordinary product',has_only_default_variant:false},url:'/products/unit-test?variant=501',variant:data.variant,options_with_values:[{name:'Size',value:'Small'}],quantity:3,properties:{Finish:'Plain'},selling_plan_allocation:{selling_plan:{name:'Monthly'}},original_price:2400,final_price:2000,original_line_price:7200,final_line_price:6000,unit_price:1000,unit_price_measurement:data.variant.unit_price_measurement,line_level_discount_allocations:[],url_to_remove:'/cart/change?line=1&quantity=0'};
const cartSource = (await readFile(resolve(root,'theme/sections/main-cart.liquid'),'utf8')).replace(/{% schema %}[\s\S]*?{% endschema %}/,'');
const cart = await engine.parseAndRender(cartSource,{cart:{items:[line],total_price:6000},routes:{cart_url:'/cart',cart_update_url:'/cart/update'},section:{id:'cart'},shop:{}});
const navigation = '<site-navigation><details><summary>Menu</summary><nav aria-label="Main navigation"><a href="/product">Product</a><details><summary>Nested menu</summary><a href="/cart">Cart</a></details></nav></details></site-navigation>';
const search = '<predictive-search data-url="/search/suggest" data-error="Suggestions unavailable. Submit the search."><form action="/search" role="search"><label for="SearchUnit">Search</label><input id="SearchUnit" name="q" type="search"><button>Search</button></form><div data-predictions hidden></div><p data-search-status role="status"></p></predictive-search><script type="module" src="/assets/search.js"></script>';
const page = (content, guest=false) => `<!doctype html><html lang="en"><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Production component test</title><link rel="stylesheet" href="/assets/base.css"><script type="module" src="/assets/navigation.js"></script></head><body><header class="page-width">${navigation}</header><main>${content}${guest?'<div class="page-width"><div class="app-host"><div style="width:1800px;height:1000px"><button>External guest action</button></div></div></div>':''}</main><script>window.unitApplicationScriptRan=true;</script></body></html>`;
const server = createServer(async (request,response) => {
  const pathname = new URL(request.url,'http://test').pathname;
  if (pathname.startsWith('/assets/')) {
    try { const body = await readFile(resolve(root,'theme',pathname.slice(1))); response.setHeader('Content-Type',pathname.endsWith('.css')?'text/css':'text/javascript');response.end(body); }
    catch { response.writeHead(404).end(); } return;
  }
  response.setHeader('Content-Type','text/html');
  response.end(page(pathname==='/cart'?cart:pathname==='/search'?search:products[pathname.slice(1)]||product,pathname==='/guest'));
});
await new Promise(resolve => server.listen(0,'127.0.0.1',resolve));
const base = `http://127.0.0.1:${server.address().port}`;
const report={scope:'isolated production snippet/asset browser contracts with test platform adapters; NOT live Shopify checkout/editor/apps/Markets proof',engine:'Chromium',configuration:{viewport:{width:390,height:900}},observations:[],assertions:0,axe:[]};
let browser;
try {
  browser = await chromium.launch({headless:true}); report.version=browser.version();
  for (const javaScriptEnabled of [true,false]) {
    const context = await browser.newContext({javaScriptEnabled,viewport:{width:390,height:900}});
    const page = await context.newPage();
    for (const width of [320,375,390,430,768,1024,1280,1440]) {
      await page.setViewportSize({width,height:900});
      for (const route of ['/product','/compact','/editorial','/cart','/guest']) {
        await page.goto(base+route); await page.waitForLoadState('networkidle');
        const dims=await page.evaluate(() => ({viewport:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth,script:window.unitApplicationScriptRan===true}));
        assert.ok(dims.scroll<=dims.viewport+1,`${route} overflow at ${width}`);report.assertions++;
        assert.equal(dims.script,javaScriptEnabled);report.assertions++;
        report.observations.push({route,width,javaScriptEnabled,...dims});
        if (width===390 || width===1440) await page.screenshot({path:resolve(out,`${route.slice(1)}-${width}-js-${javaScriptEnabled?'on':'off'}.jpg`),fullPage:true});
      }
    }
    await page.goto(base+'/editorial');
    const fields=await page.locator('#ProductForm-test').evaluate(form => Object.fromEntries(new FormData(form)));
    assert.equal(fields.id,'501');assert.equal(fields.quantity,'3');report.assertions+=2;
    await page.getByRole('button',{name:'Add to cart',exact:true}).isEnabled().then(enabled=>assert.ok(enabled));report.assertions++;
    if (javaScriptEnabled) {
      const result=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa','wcag22aa']).analyze();
      report.axe.push({route:'/product',violations:result.violations,incomplete:result.incomplete.map(x=>x.id)});
      assert.equal(result.violations.filter(x=>['critical','serious'].includes(x.impact)).length,0);report.assertions++;
      await page.locator('site-navigation > details > summary').click();
      await page.locator('site-navigation a').first().focus();await page.keyboard.press('Escape');
      assert.equal(await page.locator('site-navigation > details').getAttribute('open'),null);report.assertions++;
      assert.equal(await page.locator('site-navigation > details > summary').evaluate(e=>document.activeElement===e),true);report.assertions++;
      await page.goto(base+'/cart');
      let requests=0;
      await page.route('**/cart/update.js',async route=>{requests++;const body=route.request().postDataJSON();assert.equal(body.updates['501:properties-plan'],5);await route.fulfill({status:422,contentType:'application/json',body:JSON.stringify({description:'Inventory changed'})});});
      await page.locator('input[name="updates[]"]').fill('5');await page.getByRole('button',{name:'Update cart'}).click();
      await page.getByText('Inventory changed',{exact:true}).waitFor();
      assert.equal(requests,1);report.assertions++;
      assert.equal(await page.getByRole('button',{name:'Update cart'}).isEnabled(),true);report.assertions++;
      assert.equal(await page.locator('[data-cart-error]').evaluate(e=>document.activeElement===e),true);report.assertions++;
      const resultCart=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa','wcag22aa']).analyze();
      report.axe.push({route:'/cart',violations:resultCart.violations,incomplete:resultCart.incomplete.map(x=>x.id)});
      assert.equal(resultCart.violations.filter(x=>['critical','serious'].includes(x.impact)).length,0);report.assertions++;
      await page.goto(base+'/search');
      await page.route('**/search/suggest?*',route=>route.fulfill({status:500,body:'test failure'}));
      await page.locator('input[name=q]').fill('cream');await page.getByText('Suggestions unavailable. Submit the search.',{exact:true}).waitFor();
      assert.equal(await page.getByRole('button',{name:'Search',exact:true}).isEnabled(),true);report.assertions++;
      await page.emulateMedia({reducedMotion:'reduce'});
      assert.equal(await page.evaluate(()=>matchMedia('(prefers-reduced-motion: reduce)').matches),true);report.assertions++;
      // Disconnect/reconnect actual custom elements; aborting controllers prevents stale listeners.
      await page.locator('predictive-search').evaluate(element=>{const parent=element.parentElement;element.remove();parent.append(element);});
      assert.equal(await page.locator('predictive-search input').count(),1);report.assertions++;
    } else {
      assert.equal(await page.evaluate(()=>customElements.get('native-cart')),undefined);report.assertions++;
    }
    await context.close();
  }
  report.result='PASS';
} catch(error) {
  report.result='FAIL';report.error=error.stack;throw error;
} finally {
  await writeFile(resolve(out,'browser-results.json'),JSON.stringify(report,null,2)+'\n');
  await browser?.close();server.close();
}
console.log(JSON.stringify({result:report.result,version:report.version,observations:report.observations.length,assertions:report.assertions,scope:report.scope}));
