# Figure Planning and Consent

## Manuscript-first proposal

When a figure could improve comprehension, mark the exact location before rendering it. Do not wait for the user to know that a figure is useful, but do not make the final decision for them.

Every proposal must state:

- manuscript section and placement anchor;
- proposed figure number or temporary ID;
- class: `RESULT`, `EXPLANATORY`, or `ENHANCEMENT`;
- working title;
- communication problem it solves;
- proposed panels and their reading order;
- what the figure will not claim;
- required data, code, text, labels, images, or reference figures;
- rendering route;
- journal-space, complexity, and verification tradeoffs.

Use `templates/figure-proposal-card.md` and require one choice:

- `A` approve the proposal;
- `B` revise content or panels;
- `C` use overview only;
- `D` defer or decline;
- `E` upload a reference image;
- `F` request a different split or merge plan.

Do not treat silence, a general request to improve the paper, or approval of the prose as approval to render a proposed explanatory or enhancement figure.

## Manuscript figure map

For multi-figure papers, maintain a figure map containing:

- figure ID and manuscript location;
- one primary communication task;
- class and evidence status;
- overview/module/result relationship;
- required source materials;
- rendering and QA status;
- user rendering and final approval status.

The map may recommend figures at three priority levels:

- `ESSENTIAL_EVIDENCE` — needed to inspect a core result;
- `STRONGLY_RECOMMENDED_EXPLANATION` — materially improves method or argument comprehension;
- `OPTIONAL_ENHANCEMENT` — improves navigation, synthesis, or presentation.

Priority is advice, not an automatic insertion decision.

## Draft-to-final consent

After rendering, show the preview and QA summary through `templates/figure-review-card.md`. The user may approve, request layout changes, request structural redesign, flag content mismatch, or reject the figure.

Only explicit final approval allows manuscript insertion and final packaging.
