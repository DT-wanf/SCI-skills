# Data Sufficiency Gate

Apply before loading any data-acquisition capability whenever the current stage depends on data, a corpus, records, or other research materials.

## Status

Set exactly one status:

- `UNKNOWN` — data is mentioned but the files, fields, sample, or documentation are insufficiently inspected;
- `SUFFICIENT` — available data can answer the current research question after reasonable cleaning, derivation, coding, or analysis;
- `INSUFFICIENT` — at least one critical evidence gap prevents the planned inference and cannot be repaired from the available data;
- `ABSENT` — no usable data or research material exists.

Do not infer insufficiency from untidy data alone.

## Audit criteria

Assess only what the research question requires:

1. unit of analysis and target population;
2. critical outcomes, exposures, constructs, labels, or textual evidence;
3. time, geography, language, group, and sample coverage;
4. identifiers needed for deduplication, longitudinal analysis, or authorized linkage;
5. provenance, permission, consent, license, and reproducibility;
6. analyzable record count and planned method compatibility;
7. whether defects can be handled by cleaning, coding, derivation, weighting, or sensitivity analysis.

## Routing rules

- `UNKNOWN`: ask for at most three missing items, such as a sample, field list, data dictionary, record count, labels, or provenance. Do not recommend sources or crawlers yet.
- `SUFFICIENT`: set acquisition to `NOT_NEEDED`, keep web-data acquisition inactive, and proceed to cleaning, coding, analysis, or the current task.
- `INSUFFICIENT`: name the exact critical gap, show why cleaning or derivation cannot fix it, and decide whether supplementation or replacement is needed.
- `ABSENT`: identify the required evidence and choose the appropriate collection family.

Activate academic web-data acquisition only for `INSUFFICIENT` or `ABSENT` when web evidence fits the research design. Route experiments, surveys, interviews, fieldwork, or non-web institutional data to their own playbooks.

An explicit request to “crawl,” “scrape,” or “find more data” does not bypass this gate. If existing data is sufficient, explain that further acquisition would add cost, bias, duplication, or rights risk and continue with the next analytical task.

## Crawler last-resort gate

Set `crawl_necessity` to `JUSTIFIED` only when all conditions pass:

1. data status is `ABSENT` or `INSUFFICIENT`;
2. web evidence is methodologically necessary or clearly preferable;
3. existing data, free official download/API, open repository, paid licensed data/API, and authorized manual export have been checked;
4. none of those routes adequately fills the critical gap;
5. the planned crawl is permitted and proportionate;
6. fields, sampling, stopping, provenance, pilot, and audit plans are ready.

Record why every non-crawl route failed. Otherwise set `crawl_necessity` to `BLOCKED` and do not generate or run crawler code.
