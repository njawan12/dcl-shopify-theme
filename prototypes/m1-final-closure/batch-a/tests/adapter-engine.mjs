// Canonical adapter proof only; preserved engine's old adversarial suite is not rerun.
import assert from 'node:assert/strict';
import {writeFileSync} from 'node:fs';
import {fixtures} from '../reuse/guided/fixtures.js';
import {createState,resolve,summary,includeStep,beginRequest,finishRequest} from '../reuse/guided/split-tension.js';
let pass=0;const check=(ok,label)=>{assert.ok(ok,label);pass++};
for(const f of fixtures){
 const state=createState(f);check(state.steps.length===f.steps.length,'canonical schema accepted');check(summary(state).count===0,'explicit inclusion');
 f.steps.forEach((s,i)=>{const r=resolve(state,i);check(r.variant.id===s.product.variants[0].id,'shared variant identity');check(r.variant.price===s.product.variants[0].price,'shared price');check(r.eligible,'canonical simple product eligible')});
 let selected=includeStep(state,0,true);selected=includeStep(selected,1,true);check(summary(selected).total===f.steps[0].product.variants[0].price+f.steps[1].product.variants[0].price,'canonical total');
 const pending=beginRequest(selected);check(pending.state.request.payload.length===2,'aggregate payload');const done=finishRequest(pending.state,pending.token,'success');check(done.request.status==='success','same preserved simulation engine');check(summary(state).count===0,'second instance untouched');
}
writeFileSync(new URL('evidence/adapter-results.json',import.meta.url),JSON.stringify({pass,fail:0,scope:'Canonical adapter against exact preserved engine; no DOM/browser fallback claim.'},null,2)+'\n');console.log(`${pass} PASS / 0 FAIL`);
