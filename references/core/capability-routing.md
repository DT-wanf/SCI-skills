# Capability Routing

Select capabilities from `manifest.yaml` by task, not by brand name.

## Rules

- Load the current stage before selecting capabilities.
- Load no more than two primary capabilities by default.
- Treat a third capability as support only when the deliverable would otherwise be incomplete.
- Do not expose capability filenames to beginners.
- Prefer the most specific capability: reviewer response over general writing, statistics over general polishing for statistical claims, data availability over general writing for repository statements.

## Common combinations

- Literature stage: literature search + paper deep reading
- Analysis stage: statistical reporting + scientific figures
- Writing stage: manuscript writing + academic polishing
- Submission stage: pre-submission review + one of data availability, response, or presentation
- Missing/insufficient web evidence: web data acquisition + one of statistics or paper deep reading
- Figure planning or rendering: scientific figures + one of statistics, manuscript writing, or paper deep reading according to the figure class

Before loading `web-data-acquisition.md`, apply `data-sufficiency-gate.md`. Load it only for `ABSENT` or `INSUFFICIENT` data when web evidence is appropriate. If data is `SUFFICIENT`, select cleaning, statistics, coding, or deep-reading capabilities instead. Do not load a vendor-specific crawler skill as a permanent dependency.

Before rendering any figure, apply `figure-readiness-gate.md`. Result figures require real inputs and verified Python/R execution. Explanatory and enhancement figures require a visible manuscript proposal and user approval. Figure planning may occur earlier, but planning never counts as rendering or final insertion.
