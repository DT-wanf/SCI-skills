# Figure Visual QA

Run this after rendering and before final insertion or packaging.

## Source and execution

- Confirm the source file exists and uses the approved route.
- For result figures, confirm real input readers, declared transformations, Python/R execution evidence, and input-to-output traceability.
- Flag embedded result arrays, unreported manual values, simulated data, or image-generation provenance.
- Preserve raw inputs, processing code, seeds, environment notes, and generated-file timestamps or hashes when available.

## Scientific content

- Match axes, units, groups, sample sizes, metrics, and panel claims to the source.
- Define center, spread, intervals, tests, corrections, and significance notation.
- Show paired, repeated, hierarchical, temporal, or censored structure honestly.
- Make missing, excluded, interpolated, normalized, or transformed values explicit.
- Verify that explanatory diagrams do not overstate mechanisms or causal relations.

## Visual inspection at final size

- Read every label and panel letter at the intended manuscript dimensions.
- Check clipping, overlap, whitespace, alignment, legend placement, scale bars, and image crops.
- Confirm consistent group, method, and module mappings across panels and figures.
- Test color plus redundant encodings and inspect a grayscale rendering when relevant.
- Confirm that overview and module panels remain distinguishable and that no panel carries excessive explanatory load.

## Export inspection

- Prefer editable SVG/PDF for plots and diagrams.
- Use high-resolution TIFF/PNG for raster images or required submission files.
- Verify dimensions, effective DPI, page size, transparency, and font behavior where the format permits.
- Open the delivered files rather than trusting successful save calls.

Use `scripts/validate_figure_source.py` and `scripts/inspect_figure_output.py` where supported. Automated checks are preflight aids, not proof of scientific correctness.

## User review

Use `templates/figure-review-card.md` after QA. Keep final manuscript insertion blocked until the user explicitly approves the rendered figure.
