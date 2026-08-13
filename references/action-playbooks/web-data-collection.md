# Academic Web Data Collection Action Guide

Use only after data status is `ABSENT` or `INSUFFICIENT`, web evidence is appropriate, and the research-to-data mapping, source choice, fields, sampling rule, and permissions have been reviewed. Prefer acquisition without crawling.

## Contents

1. Preconditions
2. Route selection
3. Paid-source guidance
4. Crawl escalation
5. Pilot
6. Full collection
7. User audit and cleaning handoff

## Preconditions

Confirm:

- the data-sufficiency result and exact critical gap;
- why cleaning, derivation, coding, or existing authorized linkage cannot repair that gap;
- research question and intended analysis;
- unit of analysis and field schema;
- inclusion, exclusion, time, geographic, language, and stopping rules;
- expected volume and output format;
- source ownership, access route, cost, license, platform terms, privacy, ethics, and copyright status;
- raw-data directory, logs, and provenance fields.

If these are not usable, return to the source-choice capability. Do not begin with crawler code.

If data status is `UNKNOWN` or `SUFFICIENT`, stop this playbook. Request sufficiency evidence or proceed to cleaning and analysis.

## Route selection

### 1. Official download or API

Use this route first. Verify the current official interface and provide the exact dataset, table, filters, date range, fields, file format, documentation, and access date. Preserve the original download unchanged with its documentation and license.

### 2. Paid licensed data

Recommend a paid route when it offers materially better construct fit, coverage, metadata, stable identifiers, reproducibility, or permission clarity. Explain:

- why the paid source is better for this study;
- subscription, one-time purchase, usage-based, or institutional-access model;
- current official price or `待核实` status;
- included records, fields, export/API limits, access duration, and update frequency;
- research, quotation, redistribution, and publication permissions;
- cancellation or continued-access implications;
- free or lower-cost alternative and its methodological tradeoff.

Payment requires user authorization. Use `MANUAL` or `HYBRID`; never purchase automatically or infer that access grants extraction rights.

### 3. Authorized manual export

Use when the source requires an institutional login, personal account, consent, or an export button. Give exact filters, columns, export format, naming, screenshots or logs to retain, and materials to return.

### 4. Public-page crawl

Use only when earlier routes are documented as inadequate, `crawl_necessity` is `JUSTIFIED`, and the planned access is permitted. Select the least complex method that works:

1. discover sources or URLs;
2. fetch a known page;
3. map a site or section;
4. crawl a bounded URL set or section;
5. use browser interaction only for permitted rendering, scrolling, or pagination.

Use static HTTP and HTML parsing for server-rendered pages, a browser-capable or open-source crawler for permitted JavaScript pages, and official APIs or authorized platform adapters for platform-specific data. Do not require a commercial vendor. If no compatible tool is available, provide runnable code or a hybrid guide rather than claiming collection occurred.

## Reconnaissance before crawling

Check the official access documentation, terms, robots instructions, sitemap, page structure, structured metadata, hidden public API only when its use is permitted, pagination, stable IDs, rate limits, and likely failure modes. Record the check date and unresolved permission questions.

Do not bypass login, paywalls, CAPTCHAs, rate limits, access controls, or explicit anti-automation restrictions. Do not use personal data merely because it is visible.

If any adequate download, API, licensed dataset, or authorized export becomes available, stop the crawler route and use it instead.

## Pilot

Collect 1-3 pages or approximately 10-50 records. Produce:

- pilot raw file;
- sample table;
- field-availability report;
- missingness and duplicate summary;
- pagination and stopping-rule check;
- provenance and timestamp check;
- mismatch list between planned and observed fields;
- recommendation: proceed, revise, change source, or stop.

Do not scale until critical fields and permissions pass. Keep the stage open when the pilot is incomplete.

## Full collection

Use bounded concurrency and respectful pacing. Save:

```text
project/
  raw/
  metadata/
  scripts/
  logs/
  pilot/
```

Never overwrite raw data. Record source, URL or record ID, query, filters, collection time, page or cursor, tool and version, failures, retries, exclusions, and final record count. Separate acquisition from cleaning.

## User audit and cleaning handoff

After collection, summarize the source, route, dates, requested versus collected scope, fields, sample rows, missingness, duplicates, exclusions, failures, rights, and known biases. Use `templates/data-acquisition-review-card.md` and ask the user to choose:

- approve and enter data cleaning;
- revise fields or exclusions;
- supplement the sample or change the source.

Do not clean, transform, deduplicate, impute, translate, or analyze before the user approves, except for non-destructive profiling needed for the audit. After approval, preserve the raw files, create a processing copy, and generate a project-specific cleaning Prompt covering schema validation, duplicates, missingness, type conversion, text normalization, outliers, derived variables, and a reproducible cleaning log.

## Completion evidence

Require the raw files or verified export, data dictionary, provenance record, pilot report, collection log, sample rows, rights or access notes, known-deviation list, and explicit user review decision.
