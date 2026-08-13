# Figure Decomposition

## Core rule

Do not force a complex algorithm, system, experiment, or theoretical framework into one crowded image. Start with the reader's questions and assign each panel or figure a bounded explanatory task.

## Recommended layers

For an algorithm or model, consider:

1. overview — inputs, major stages, information flow, and outputs;
2. module detail — internal operations of each novel or difficult component;
3. training or execution — objective, loss, optimization, intervention, or processing sequence;
4. evaluation design — data split, baselines, metrics, and validation route;
5. results — main performance, ablation, robustness, error analysis, or interpretation.

For an experiment, consider:

1. study or sample flow;
2. intervention or acquisition sequence;
3. measurement and preprocessing;
4. analysis and quality-control route;
5. result figures generated separately from real inputs.

For theory or review work, consider:

1. concept or field overview;
2. branches, mechanisms, or argument modules;
3. development trajectory or evidence relationships;
4. unresolved tensions or future directions.

## Required choice

Offer at least two architectures when complexity is non-trivial:

- `Option 1`: one multi-panel figure with a clear overview and subordinate module panels;
- `Option 2`: a standalone overview plus one or more module/detail figures.

Explain the tradeoff in readability, journal space, visual density, reuse in slides, and production burden. Let the user split, merge, defer, or decline.

## Panel test

For every planned panel, ask:

- What reader question does it answer?
- What source material supports it?
- Is it overview, explanation, or result evidence?
- Would combining it with another panel obscure either task?
- Does it repeat information better handled in prose or a table?

Do not remove an optional figure solely because it is non-evidentiary. State its communication value and let the user decide.
