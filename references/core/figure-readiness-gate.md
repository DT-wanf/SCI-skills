# Figure Readiness Gate

Apply this gate before any scientific-figure rendering, adaptation, or final insertion.

## 1. Classify the figure

- `RESULT`: displays evidence from experiments, observations, models, coding, statistics, or material analysis.
- `EXPLANATORY`: explains an algorithm, module, workflow, method, theory, mechanism, or process.
- `ENHANCEMENT`: improves navigation or synthesis, such as a graphical abstract or study overview.

If a figure mixes classes, apply the strictest relevant rule to each panel. Any result-bearing panel remains a `RESULT` panel even when surrounded by explanatory graphics.

## 2. Set readiness

| Status | Meaning | Allowed action |
|---|---|---|
| `NOT_READY` | Purpose or essential source material is unknown | Ask for the smallest missing information |
| `PLAN_READY` | Location, purpose, and intended content are known | Propose, decompose, or write executable code only |
| `RENDER_READY` | All class-specific prerequisites pass | Render through the approved route |
| `REVISION_READY` | Existing figure and source context are available | Audit and revise without inventing missing evidence |

## 3. Result-figure execution gate

Set `RESULT` to `RENDER_READY` only when all are true:

1. `real_inputs_available = true` — real data or verified result files exist;
2. `semantics_defined = true` — variables, groups, units, metrics, sample structure, and uncertainty are defined;
3. `transformations_declared = true` — filters, exclusions, missingness, normalization, aggregation, and tests are recorded;
4. `backend in [python, r]`;
5. `plotting_source_available = true` — source reads the real input rather than embedding invented result values;
6. `execution_verified = true` — the source was actually run and evidence of the run is available;
7. `traceability_verified = true` — displayed values and layers trace to the real input and declared transformations.

Keep `RESULT` at `PLAN_READY` or `NOT_READY` when any of the following is true:

- only a textual conclusion is available;
- metrics or p values were manually typed without a verified source file;
- only a screenshot is available and reconstruction would require invented data;
- simulated, random, or example values would be used as manuscript results;
- an image-generation model would create result pixels;
- a script has been written but not run;
- an output exists but its input or transformation chain is unknown.

If the current environment cannot run Python/R, produce the source and a hybrid return contract. Require the returned source, command, console/log evidence, and rendered files. Do not claim completion before verification.

## 4. Explanatory and enhancement consent gate

Set `EXPLANATORY` or `ENHANCEMENT` to `RENDER_READY` only when all are true:

1. `manuscript_location_proposed = true`;
2. `communication_purpose_disclosed = true`;
3. `content_boundary_disclosed = true`;
4. `decomposition_options_disclosed = true` when complexity warrants them;
5. `required_materials_disclosed = true`;
6. `generation_route_disclosed = true`;
7. `user_rendering_approval = true`.

Communication value is sufficient grounds to propose the figure. Do not require empirical evidence for a genuine explanatory or enhancement figure. However, do not imply measured results, verified mechanisms, or causal certainty that the manuscript does not support.

## 5. Final insertion gate

Rendering approval and final approval are separate.

Set `manuscript_insertion_status = allowed` only when:

- the rendered output exists;
- source and output QA have passed or documented exceptions are accepted;
- the legend and manuscript callout match the actual figure;
- result panels have full input-to-pixel traceability;
- reference adaptation and attribution requirements are resolved;
- `user_final_approval = true`.

Otherwise keep final insertion blocked and use the figure review card.
