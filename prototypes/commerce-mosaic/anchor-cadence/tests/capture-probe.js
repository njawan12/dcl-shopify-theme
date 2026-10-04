// Read-only DOM evidence probe. Never loaded by prototype pages.
(()=>{
 const rect=e=>{const r=e.getBoundingClientRect();return {x:r.x,y:r.y,width:r.width,height:r.height,right:r.right,bottom:r.bottom}};
 const overlap=(a,b)=>Math.min(a.right,b.right)-Math.max(a.x,b.x)>1&&Math.min(a.bottom,b.bottom)-Math.max(a.y,b.y)>1;
 const ids=[...document.querySelectorAll('[id]')].map(e=>e.id);
 return {width:innerWidth,overflow:Math.max(document.documentElement.scrollWidth,document.body.scrollWidth)-innerWidth,scripts:document.scripts.length,duplicateIds:ids.filter((id,i)=>ids.indexOf(id)!==i),collections:[...document.querySelectorAll('.collection')].map(section=>{
 const grid=section.querySelector('.product-grid'),style=getComputedStyle(grid),box=rect(grid),children=[...grid.children];
 const cols=style.gridTemplateColumns.split(' ').map(v=>Number.parseFloat(v)).filter(Number.isFinite),rows=style.gridTemplateRows.split(' ').map(v=>Number.parseFloat(v)).filter(Number.isFinite),cg=Number.parseFloat(style.columnGap),rg=Number.parseFloat(style.rowGap);
 let tops=[],y=box.y;for(let h of rows){tops.push(y);y+=h+rg;}let cells=rows.map(()=>cols.map(()=>0)),placementErrors=[];
 for(let child of children){const r=rect(child),col=Math.round((r.x-box.x)/(cols[0]+cg)),span=Math.round((r.width+cg)/(cols[0]+cg)),first=tops.findIndex(v=>Math.abs(v-r.y)<2);let last=rows.findIndex((h,i)=>Math.abs(tops[i]+h-r.bottom)<2);
 if(first<0||last<first||col<0||col+span>cols.length){placementErrors.push(child.className);continue;}for(let i=first;i<=last;i++)for(let j=col;j<col+span;j++)cells[i][j]++;}
 let holes=[];for(let i=0;i<cells.length-1;i++)for(let j=0;j<cols.length;j++)if(cells[i][j]!==1)holes.push([i,j,cells[i][j]]);
 let itemCollisions=[];for(let i=0;i<children.length;i++)for(let j=i+1;j<children.length;j++)if(overlap(rect(children[i]),rect(children[j])))itemCollisions.push([i,j]);
 const products=[...section.querySelectorAll('.product-card')];let textCollisions=[],mediaCollisions=[],overflows=[],badTargets=[],uncontained=[],unloaded=[];
 for(let card of products){let info=card.querySelector('.product-info'),media=card.querySelector('.media');if(overlap(rect(info),rect(media)))mediaCollisions.push(card.dataset.product);const t=[...info.children];for(let i=0;i<t.length;i++)for(let j=i+1;j<t.length;j++)if(overlap(rect(t[i]),rect(t[j])))textCollisions.push([card.dataset.product,t[i].className,t[j].className]);}
 for(let e of section.querySelectorAll('h2,h3,p,a,span.destination')){if(e.scrollWidth>e.clientWidth+1)overflows.push([e.className,e.scrollWidth,e.clientWidth]);}
 for(let e of section.querySelectorAll('a')){let r=rect(e);if(r.height<44||r.width<44)badTargets.push([e.textContent,r.width,r.height]);if(r.x<-1||r.right>innerWidth+1)uncontained.push(e.textContent);}
 for(let img of section.querySelectorAll('img')){let r=rect(img),p=rect(img.parentElement);if(r.x<p.x-1||r.right>p.right+1||r.y<p.y-1||r.bottom>p.bottom+1||getComputedStyle(img).objectFit!=='contain')uncontained.push(img.getAttribute('src'));if(!img.naturalWidth&&img.loading!=='lazy')unloaded.push(img.getAttribute('src'));}
 return {rect:rect(section),order:products.map(e=>e.dataset.product),featureIndices:products.map((e,i)=>e.classList.contains('feature')?i:-1).filter(i=>i>=0),editorialAfter:children.filter(e=>e.classList.contains('editorial')).map(e=>children.slice(0,children.indexOf(e)).filter(c=>c.classList.contains('product-card')).length),productCount:products.length,editorialCount:section.querySelectorAll('.editorial').length,imageCount:section.querySelectorAll('.product-card img').length,missingMedia:section.querySelectorAll('.product-card .missing-media').length,cols:cols.length,rows:rows.length,holes,placementErrors,itemCollisions,textCollisions,mediaCollisions,overflows,badTargets,uncontained,unloaded,resultCount:section.querySelector('.result-count').textContent};
 })};
})
