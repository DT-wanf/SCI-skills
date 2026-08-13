# Academic Web Data Acquisition

Use this capability only after `references/core/data-sufficiency-gate.md` records `ABSENT` or `INSUFFICIENT` and confirms that web evidence is methodologically appropriate. Design the evidence route before selecting tools or writing crawler code.

## Strict activation gate

Do not activate for `UNKNOWN` or `SUFFICIENT` data status. Do not activate merely because data is messy, incomplete in non-critical fields, or needs cleaning, coding, derivation, weighting, or authorized linkage.

If the user already has data, first verify the critical gap. State exactly which required variable, outcome, unit, population, time range, label, document, or provenance element is absent and why the gap cannot be repaired from existing materials. If no critical gap remains, stop this capability and return to cleaning or analysis.

An explicit request for a crawler does not override the gate.

## Intake

Reuse known project facts. Ask no more than three critical questions per round.

First round:

1. What must the study describe, compare, explain, or predict?
2. What is the unit of analysis: person, post, comment, document, event, organization, job, place, or another record?
3. What time, geographic, language, and population boundaries apply?

Second round only when unresolved:

1. Which constructs or variables need observable web signals?
2. What inclusion, exclusion, sampling, and stopping rules are defensible?
3. What budget, institutional access, account, deadline, computing, privacy, or ethics constraints apply?

Accept `暂无`. Convert uncertainty into source options or verification tasks instead of guessing.

## Research-to-data mapping

Map every research construct through this chain:

```text
research question -> construct -> observable signal -> unit -> field -> source -> analysis use
```

Reject fields that are convenient to collect but do not support the research question. Keep content fields separate from provenance, sampling, and audit fields.

## Source-first ladder

Evaluate routes in this order and stop at the first adequate, lawful, and feasible option:

1. existing user-held data;
2. official free download, open API, or public portal;
3. open repository or institutional archive;
4. paid licensed dataset, database, or official API;
5. authorized manual export;
6. permitted public-page crawling.

Do not recommend crawling when a download or API provides equivalent or better coverage. Read `references/web-source-families.md` when the user does not know where to obtain the data.

Before proposing the sixth route, record the result of checking routes 1-5. Set `crawl_necessity: JUSTIFIED` only when none adequately fills the verified critical gap. Otherwise set it to `BLOCKED` and do not produce crawler code.

## Source choices

When no source is selected, present two or three ranked plans with `templates/data-source-choice-card.md`. For every plan provide:

- source and official access page;
- evidence and variables it can support;
- coverage, unit, time span, and likely fields;
- access route and output format;
- free, paid, institutional, or mixed access status;
- price model, license, export limit, and research-use rights when applicable;
- methodological fit, known bias, technical difficulty, and reproducibility;
- a free or lower-cost alternative when one exists.

Verify current access and pricing from official sources. If not verified, label them `待核实`; never invent prices or licensing rights.

## Acquisition plan

After the user chooses a source, populate `schemas/web-data-collection-plan.yaml`. Define the output schema before collection. Include stable identifiers, source URL, collection timestamp, query or filter, page or cursor, and raw-record reference whenever available.

Select the route:

- `DOWNLOAD_OR_API` for official exports, APIs, and licensed datasets;
- `MANUAL_EXPORT` for authenticated interfaces or bounded user actions;
- `STATIC_SCRAPE` for permitted server-rendered pages;
- `DYNAMIC_BROWSER` for permitted rendering, scrolling, or pagination;
- `PLATFORM_ADAPTER` for an official API or authorized prebuilt collector;
- `NOT_FEASIBLE` when access, ethics, rights, cost, or sampling validity is unacceptable.

Use `references/action-playbooks/web-data-collection.md` for execution. Keep the workflow provider-neutral; use an available compliant tool, or give a manual/hybrid guide when execution is unavailable.

## Pilot and audit gates

Require a pilot of 1-3 pages or approximately 10-50 records before full collection. Check field availability, parsing accuracy, duplicates, missingness, time coverage, sampling bias, identifiers, rate limits, and raw-data preservation.

After full collection, do not start cleaning automatically. Summarize the returned evidence and use `templates/data-acquisition-review-card.md`. Require explicit user approval of the source, scope, fields, sample rows, exclusions, rights, missingness, duplicates, and bias. Only an approved audit can open the data-cleaning handoff.

## Required outputs

- 现有数据充足性结论与关键缺口（仅 `ABSENT` 或 `INSUFFICIENT` 可继续）
- 研究问题—数据映射表
- 数据源候选方案与推荐顺序
- 付费与免费方案比较（适用时）
- 字段表与来源追踪字段
- 采样、范围和停止规则
- 采集方式与试采集计划
- 权限、伦理、隐私和版权检查
- 采集后用户审核卡
- 审核通过后的数据清洗交接 Prompt
- 爬虫必要性结论及非爬虫路线排除理由（仅计划爬取时）

## Boundaries

Do not bypass authentication, paywalls, CAPTCHAs, access controls, explicit prohibitions, or technical protections. Do not collect unnecessary personal or sensitive data. Public visibility and paid access do not by themselves authorize bulk collection, redistribution, quotation, or publication.
