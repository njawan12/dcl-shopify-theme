// Read-only browser observations. Never loaded by storefront pages.
(()=>{
 const r=e=>{const b=e.getBoundingClientRect();return {x:b.x,y:b.y,right:b.right,bottom:b.bottom,width:b.width,height:b.height}};
 const overlap=(a,b)=>Math.min(a.right,b.right)-Math.max(a.x,b.x)>1&&Math.min(a.bottom,b.bottom)-Math.max(a.y,b.y)>1;
 const ids=[...document.querySelectorAll('[id]')].map(e=>e.id);
 let textOverflow=[],collisions=[],targets=[],unloaded=[];
 for(let el of document.querySelectorAll('.evidence-host h1,.evidence-host h2,.evidence-host h3,.evidence-host p,.evidence-host td,.evidence-host th,.evidence-host blockquote')){
   if(el.closest('.guest-viewport'))continue;
   if(el.scrollWidth>el.clientWidth+1)textOverflow.push([el.className,el.scrollWidth,el.clientWidth]);
 }
 for(let group of document.querySelectorAll('.subject,.note,.process-step,.paired-media,.qualification')){
   const children=[...group.children].filter(e=>r(e).width>0&&r(e).height>0);
   for(let i=0;i<children.length;i++)for(let j=i+1;j<children.length;j++)if(overlap(r(children[i]),r(children[j])))collisions.push([group.className,children[i].className,children[j].className]);
 }
 for(let el of document.querySelectorAll('a,button,select,.guest-viewport')){
   if(el.classList.contains('skip'))continue;
   let b=r(el);if(b.height<44||b.width<44)targets.push([el.textContent,b.width,b.height]);
 }
 for(let img of document.images)if(!img.naturalWidth&&img.loading!=='lazy')unloaded.push(img.getAttribute('src'));
 return {width:innerWidth,height:innerHeight,overflow:Math.max(document.documentElement.scrollWidth,document.body.scrollWidth)-innerWidth,duplicateIds:ids.filter((v,i)=>ids.indexOf(v)!==i),scripts:document.scripts.length,textOverflow,collisions,targets,unloaded,scrollY,scrollHeight:document.documentElement.scrollHeight,hosts:[...document.querySelectorAll('.evidence-host')].map(host=>({instance:host.dataset.instance,host:host.dataset.host,dir:host.getAttribute('dir'),order:[...host.children].filter(e=>e.dataset.block).map(e=>e.dataset.block),kinds:[...host.querySelectorAll('.note')].map(e=>e.dataset.kind),notes:host.querySelectorAll('.note').length,rows:host.querySelectorAll('.comparison tbody tr').length,pairs:host.querySelectorAll('.pair').length,sides:host.querySelectorAll('.paired-media figure').length,steps:host.querySelectorAll('.process-step').length,ordered:host.querySelector('.process-rail')?.tagName||'',apps:host.querySelectorAll('.app-guest').length,guests:[...host.querySelectorAll('.guest-viewport')].map(e=>({width:e.clientWidth,scrollWidth:e.scrollWidth,tabindex:e.getAttribute('tabindex'),rect:r(e)})),links:[...host.querySelectorAll('a')].map(e=>e.getAttribute('href')),text:host.innerText}))};
})()
