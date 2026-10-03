# M1 visual direction brief — Beauty/Wellness

## Status

Controlling M1 visual brief. This is product/design direction, not production implementation and not final Theme Store listing copy.

## Market reality — 2026-10-03

The Shopify Theme Store currently contains well over one thousand themes and Beauty/Wellness already has dedicated premium products. Prestige/Vogue explicitly targets beauty and wellness with a luxury aesthetic and 30+ configurable sections; Beautify is positioned specifically for Beauty & Wellness and markets flexible/no-code customization; Flawless/Routine has recently been revamped for premium beauty/skincare.

Therefore DCL cannot differentiate by beige minimalism, serif typography, ingredient sections, before/after, sticky ATC, or "built for beauty" alone.

## Visual objective

Create a storefront that feels like a strong independent brand studio designed it for a serious modern wellness company, while still being recognizably commerce-first.

Target impression:

**Editorial science + tactile product desirability + unusually clear commerce.**

Not clinical SaaS. Not generic luxury. Not soft beige template. Not loud supplement direct response.

## Reference-direction synthesis

Useful visual territories observed in current/reference commerce:
- disciplined product hierarchy and negative space;
- strong product-as-object imagery;
- factual benefits/ingredients/usage integrated into the product story;
- purchase UI that remains obvious despite editorial art direction;
- asymmetric/editorial compositions where they add hierarchy;
- restrained proof/results presentation;
- mobile layouts that preserve product desirability rather than becoming stacked cards.

These are references for principles only; no competitor layout, styling system, asset or code is to be copied.

## Direction A — Modern Apothecary

Warm, tactile, ingredient-led. Editorial serif display role paired with highly legible functional sans. Organic photography, material textures, restrained earth/mineral palette, strong whitespace.

Risk: extremely crowded category aesthetic. Must not become another beige wellness theme.

## Direction B — Clinical Editorial

Sharper grid, high information confidence, stronger typographic contrast, evidence/ingredient/product facts treated as premium editorial material. Neutral base with disciplined accent use. Product imagery feels laboratory-clean without looking pharmaceutical.

Risk: can become cold or generic "science skincare."

## Direction C — Contemporary Ritual

More expressive composition and pacing. Product routines, usage and sensory experience become visual storytelling. Stronger image crops, deliberate rhythm changes, bolder type scale and selective motion while commerce remains calm.

Risk: art direction can overpower usability or become photography-dependent.

## M1 recommendation

Prototype all three using the same six-system architecture. Do not choose a winner from moodboards.

The architecture passes only if each direction is recognizably different after normalizing brand name, catalog, copy volume and product data—and if the differences do not require separate code architectures or settings explosion.

## Shared visual invariants

Regardless of direction:
- premium zero-setup state;
- product is visually dominant;
- price/options/purchase action are immediately understandable;
- semantic global tokens rather than per-section styling escape hatches;
- typography remains readable under long/localized content;
- product cards have deliberate hierarchy, not generic image/title/price treatment;
- badges are factual and subordinate;
- product education feels composed, not like stacked FAQ widgets;
- cart continues the same visual system;
- app insertions have intentional seams;
- mobile is designed independently at the composition level while preserving one content source;
- reduced-motion, keyboard, focus, contrast and reflow requirements are first-class;
- no fake clinical proof, fake reviews, invented scarcity or unsupported claims in demo content.

## First prototype surface

Start with the PDP because it concentrates the highest-value historical DCL customization demand and exposes whether the architecture is genuinely flexible.

The first visual prototype must include:
1. header context;
2. product media;
3. product identity/title;
4. price/status;
5. review/app seam placeholder;
6. options/variants;
7. one-time/selling-plan-compatible purchase region without vendor-specific logic;
8. quantity/add-to-cart;
9. 3–4 concise factual benefit/product-fact items;
10. ingredient/specification content;
11. usage/process content;
12. one proof/results content region;
13. complementary product/routine handoff;
14. mobile purchase behavior.

## Visual originality test

For each direction capture:
- desktop PDP above fold;
- desktop PDP education/story continuation;
- mobile PDP above fold;
- product card;
- cart state.

Then run a stripped comparison:
- same product/catalog;
- equivalent copy/data;
- neutralized photography where feasible;
- remove direction-specific color;
- remove direction-specific fonts;
- disable motion.

At least three material structural differences must remain between each direction pair. Pure decoration does not count.

## Anti-convergence rules

Do not:
- imitate Aesop/Prestige/Beautify/any named brand or theme;
- use "luxury = serif + beige + huge whitespace" as the system;
- use a 30/40-section count as a design objective;
- build universal sections to recreate screenshots;
- create arbitrary desktop/mobile layout settings;
- hide commerce to make the page look editorial;
- make metafields mandatory for the default PDP;
- use visual novelty that harms accessibility or performance.

## Decision gate

No production code follows from this brief.

M1 visual direction passes only after the three PDP directions are actually visualized, compared against this brief, stress-tested with realistic content, and one coherent system is selected or synthesized with Nouman's approval.
