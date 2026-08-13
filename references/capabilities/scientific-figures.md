# Scientific Figures

## Purpose

Plan, create, adapt, audit, and package manuscript figures without confusing a proposed image, an explanatory schematic, or an unexecuted script with experimental evidence.

Read `references/core/figure-readiness-gate.md` before rendering. Load the other figure references only when their route applies:

- `references/figure-planning-and-consent.md` for manuscript placement and user choice;
- `references/figure-decomposition.md` for complex algorithms, systems, or workflows;
- `references/reference-figure-adaptation.md` when the user supplies a reference image;
- `references/figure-visual-qa.md` after rendering and before final delivery.

## Classify the figure

Assign exactly one primary class:

- `RESULT`: experimental, observational, coded-material, statistical, model, comparison, ablation, robustness, or interpretation results;
- `EXPLANATORY`: algorithm overview, module architecture, experimental workflow, method route, theoretical framework, mechanism, or process explanation;
- `ENHANCEMENT`: graphical abstract, paper overview, chapter navigation, visual synthesis, or optional communication aid.

A multi-panel figure may contain more than one class, but every result-bearing panel must pass the `RESULT` gate independently.

## Set readiness

- `NOT_READY`: purpose, inputs, or source meaning is missing;
- `PLAN_READY`: a useful proposal or executable plan can be made, but rendering prerequisites are incomplete;
- `RENDER_READY`: class-specific prerequisites are satisfied;
- `REVISION_READY`: an existing figure plus sufficient source context is available for audit or revision.

Never convert `PLAN_READY` into `RENDER_READY` merely because a plausible design or script can be written.

## Result-figure hard gate

Treat this as an absolute constraint.

Before rendering any result-bearing panel, require:

1. real data or verified result files;
2. variable, group, unit, metric, and sample definitions;
3. declared filtering, transformation, normalization, aggregation, missing-data, and statistical rules;
4. a selected Python or R plotting backend;
5. plotting source that reads the real input instead of embedding invented result values;
6. actual execution evidence such as a successful run record, console output, generated-file metadata, or a locally verified run;
7. traceability from every displayed value or image layer to the input and transformation chain.

Block rendering when only a textual conclusion, manually typed metric, screenshot without source data, simulated example, or image-generation request is available. Never use an image-generation model for result pixels, axes, heatmaps, ROC curves, confusion matrices, survival curves, significance plots, microscopy measurements, or other evidence panels.

Demo data may be used only in an explicitly labeled tutorial artifact that cannot be confused with the manuscript figure. Never include it in the final result bundle.

If Python/R cannot be run in the current environment, provide an executable script and exact instructions, then request the returned script, console or log evidence, and rendered files. Keep status as `PLAN_READY` and do not claim completion until the run is verified.

## Explanatory and enhancement consent gate

Communication value is a valid reason to propose a figure. Do not silently suppress a useful overview, workflow, module diagram, graphical abstract, or visual synthesis merely because it is not an empirical evidence panel.

Before rendering:

1. insert a conspicuous proposal at the exact manuscript or outline location;
2. state the figure class and working title;
3. explain why it improves comprehension;
4. describe what the figure will and will not communicate;
5. propose an overview and module-level decomposition where complexity requires it;
6. list source materials, labels, and reference images needed;
7. state the generation route and verification burden;
8. use `templates/figure-proposal-card.md` and wait for the user's choice.

The user may approve, revise, split, merge, defer, decline, or upload a reference image. Approval to render is not approval for final insertion.

## Figure architecture

Start from the paper's communication problem, not a favorite template. Create a manuscript-level figure map when more than one figure is involved.

For algorithms, models, or complex experiments, normally consider:

- overview: inputs, major stages, information flow, outputs;
- modules: internal operations of scientifically important components;
- training or execution: loss, optimization, intervention, sampling, or experimental sequence;
- evaluation: datasets, baselines, metrics, and validation route;
- results: main findings, ablations, robustness, errors, and interpretation.

Do not presume one image can explain the entire method. Offer at least two architectures, such as one multi-panel figure versus an overview figure plus a separate module figure. Explain readability, journal-space, and production tradeoffs, then let the user decide.

## Data profile and chart choice

For result plots, inspect the actual data before choosing a chart. When useful, run `scripts/profile_figure_data.py` on CSV or TSV input.

Check:

- variable types, units, and identifiers;
- group and sample sizes;
- paired, repeated, hierarchical, temporal, or censored structure;
- missingness, exclusions, outliers, skew, and cross-scale values;
- biological versus technical replicates;
- estimator, uncertainty, test, and multiplicity correction;
- whether raw observations should remain visible.

Give one recommended chart, one or two alternatives, and any actively discouraged chart with a concise reason. Do not obey a requested chart when it would materially misrepresent the data without first warning the user and offering a better encoding.

## Reference-figure route

When the user supplies a reference image, inspect it before proposing a redraw. Separate:

- information flow and panel hierarchy;
- reusable layout or visual grammar;
- source-specific results, labels, icons, artwork, and branding;
- the user's replacement content and evidence.

Offer `structural`, `stylistic`, or `close-redraw` adaptation. Use `close-redraw` only for user-owned or clearly licensed material. Otherwise rebuild an original figure from the user's content and record whether attribution such as “adapted from” is needed.

## Backend and execution

Honor an explicit Python or R choice. Otherwise use the existing code/data workflow or the saved preference in `schemas/user-style-profile.yaml`; ask once only when no reasonable backend is established.

- Python: matplotlib, seaborn, and appropriate scientific packages;
- R: ggplot2, patchwork, ComplexHeatmap, and appropriate domain packages.

Use the selected backend for plotting, previews, exports, and visual QA. A different language may prepare non-visual data, but it must not silently substitute the requested rendering route.

## Style and consistency

- User-facing planning and QA: Chinese unless requested otherwise.
- Manuscript annotations: English unless the manuscript or journal requires another language.
- Reuse stable group, method, and module colors across the whole paper.
- Use colorblind-aware palettes plus redundant encodings where needed.
- Avoid deceptive axes, unsupported smoothing, decorative 3D, rainbow maps, and hidden missingness.
- Preserve raw inputs and record all exclusions or transformations.
- Verify current target-journal requirements instead of treating a preset as guaranteed compliance.

## Render and QA loop

After rendering:

1. run `scripts/validate_figure_source.py` for result-figure source checks;
2. run `scripts/inspect_figure_output.py` for supported output metadata checks;
3. inspect the rendered preview at final manuscript size;
4. check labels, units, panel letters, legends, statistics, colors, typography, clipping, alignment, and traceability;
5. revise and rerender until deterministic and visual checks pass;
6. use `templates/figure-review-card.md` and wait for the user's final decision.

Do not insert the figure into the final manuscript or mark it accepted until the user chooses approval.

## Delivery bundle

As applicable deliver:

- plotting or diagram source;
- source data or a stable source-data mapping;
- execution evidence;
- editable SVG/PDF;
- TIFF/PNG preview or submission raster;
- figure legend draft;
- transformation, statistics, and exclusion notes;
- reference-adaptation and attribution note;
- QA report;
- user approval status.

For result figures, absence of real input, Python/R source, execution evidence, or traceability keeps the deliverable incomplete regardless of visual quality.
