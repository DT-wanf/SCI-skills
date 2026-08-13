# Statistical Reporting

## Use for

Research design checks, Statistical Analysis sections, Results wording, p values, confidence intervals, sample sizes, replicates, multiple comparisons, figure legends, and reviewer statistics concerns.

## First questions

Separate:

1. What was measured?
2. What was the independent experimental or observational unit?
3. What unit entered the statistical model?
4. What inference is claimed?

Do not silently treat cells, images, fields of view, repeated readings, spectra, or model runs as independent samples.

## Required reporting

As applicable report:

- design and groups;
- independent `n`;
- biological versus technical replicates;
- randomization and blinding;
- inclusion, exclusion, and missing-data rules;
- test or model and why it fits;
- assumptions and diagnostics;
- multiple-comparison correction;
- exact effect estimate;
- uncertainty interval;
- exact p value or justified threshold;
- software and version.

## Results language

Prefer effect size, direction, uncertainty, and sample size over significance-only wording. Do not translate non-significance into equivalence or “no effect” without an appropriate design.

## Figures

Check error-bar definition, box/violin conventions, stars, exact tests, panel-level `n`, paired structure, and source data.

Do not permit a statistical or experimental result figure to be rendered from prose, manually typed summary values, or an image-generation model. Require real data or verified result files, declared transformations and tests, Python/R source, actual execution evidence, and input-to-pixel traceability. A written script without a verified run remains a plan, not a completed figure.

## Boundary

This capability audits and drafts reporting. Reanalyse data only when raw data and an explicit computation request are supplied. Use `AUTHOR_INPUT_NEEDED` for missing facts.
