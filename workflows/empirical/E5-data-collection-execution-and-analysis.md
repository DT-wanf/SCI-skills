---
stage_id: E5
paper_family: empirical
stage_name_en: Data Collection, Execution, and Analysis
stage_name_zh: 数据收集、实验执行与数据分析
next_stage: E6
action_type_default: conditional_external
capability_candidates:
  - web-data-acquisition
  - statistical-reporting
  - scientific-figures
  - data-availability
external_playbook: empirical-data-and-experiment
external_playbook_candidates:
  - empirical-data-and-experiment
  - web-data-collection
---

# E5 - Data Collection, Execution, and Analysis

## Purpose

Obtain reliable materials and convert them into evidence that can support conclusions.

## Entry condition

Use this module only after the project has been routed to `empirical` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: research_design
    label_zh: 研究设计方案
    ask_zh: 请提供已通过验收的研究设计方案。
    reply_format_zh: 研究设计方案：
  - id: operationalization
    label_zh: 变量操作化表
    ask_zh: 请提供变量操作化表或字段说明。
    reply_format_zh: 变量操作化表或字段说明：
  - id: raw_materials
    label_zh: 原始数据、实验记录或访谈文本
    ask_zh: 请上传或粘贴原始数据结构、实验记录、访谈文本或统计输出；如尚未获得数据，请提供已选定的数据源与采集方案。
    reply_format_zh: 原始数据、实验记录或访谈文本：
  - id: analysis_route
    label_zh: 研究假设与分析路线
    ask_zh: 请提供研究假设与分析方法路线。
    reply_format_zh: 研究假设与分析路线：
```

## Optional fields

- 数据字典
- 已有图表
- 软件环境与模型设定
- 数据源选择卡、网页数据采集方案、费用与许可说明
- 试采集文件、采集日志和用户审核结论

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
研究设计方案：
变量操作化表或字段说明：
原始数据、实验记录或访谈文本：
研究假设与分析路线：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.
- Do not interpret the presence of `raw_materials` as either sufficient or insufficient without checking fields, scope, sample, provenance, and method fit.

## CREATE mode

Use these ordered subgates:

1. `DATA_SUFFICIENCY_AUDIT` — classify available data as `UNKNOWN`, `SUFFICIENT`, `INSUFFICIENT`, or `ABSENT`;
2. `ACQUISITION_PLAN` — only for `INSUFFICIENT` or `ABSENT`; verify the source, fields, sampling, access, cost, permissions, and output schema;
3. `PILOT` — obtain and inspect a small sample before scale-up;
4. `FULL_COLLECTION` — preserve raw files, provenance, data dictionary, and logs;
5. `USER_AUDIT` — use `data-acquisition-review-card.md` and wait for explicit approval;
6. `CLEANING_AND_ANALYSIS` — create a processing copy, clean reproducibly, analyze, and map results to hypotheses.

Branch immediately after `DATA_SUFFICIENCY_AUDIT`:

- `UNKNOWN`: request the smallest missing evidence and stop; do not start acquisition.
- `SUFFICIENT`: skip `ACQUISITION_PLAN`, `PILOT`, `FULL_COLLECTION`, and `USER_AUDIT`; go directly to `CLEANING_AND_ANALYSIS`.
- `INSUFFICIENT` or `ABSENT`: name the critical gap, decide the appropriate collection family, and activate web acquisition only if web evidence fits.

When web acquisition is activated, load `web-data-acquisition.md` and choose `web-data-collection.md` instead of the general experiment playbook. Prefer download or API, recommend a paid licensed source when justified, and do not crawl until non-crawl routes are documented as inadequate and `crawl_necessity` is `JUSTIFIED`. After newly acquiring data, perform only non-destructive profiling and stop at `USER_AUDIT` until the user approves.

After approval, create a reproducible cleaning and analysis plan, address duplicates, missingness and outliers, encode variables, run descriptive and core analyses, specify robustness checks, and map every result to a hypothesis. Never overwrite raw data.

Before creating any core result figure, apply the `RESULT` figure gate. Require real cleaned data or verified analysis outputs, variable and metric definitions, declared transformations and statistics, Python/R plotting source, actual execution evidence, and input-to-pixel traceability. If the current environment cannot execute the source, provide a hybrid run-and-return procedure and keep the figure at `PLAN_READY`. Never generate a result figure from prose, manually typed metrics, simulated manuscript values, or an image-generation model.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Interpret only the supplied outputs. Separate result description from meaning, mark support status for each hypothesis, identify assumptions that require software verification, and flag overclaiming.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 原始数据与清洗后数据
- 数据字典或编码表
- 统计/编码/实验结果
- 核心图表
- 核心图表对应的Python/R源码、真实输入映射与运行证据
- 结果解释草稿
- 假设检验对应表

For web-obtained data also produce:

- 数据源与权限记录
- 试采集报告和全量采集日志
- 用户审核结论
- 数据清洗交接 Prompt

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 每个核心结论有数据或材料支撑
- 分析方法与研究设计一致
- 结果和图表清楚可读
- 没有将相关关系误写为因果关系
- 每个假设有明确结果对应
- 数据充足性结论与实际执行分支一致
- 新获取的网络数据在清洗前已完成来源、范围、字段、质量、偏差和权限审核，并获得用户明确通过
- 现有数据若被判定为 `SUFFICIENT`，没有误触发新增数据获取或爬虫
- 每张实验结论图均来自真实数据或已核实结果，经Python/R实际运行生成，并具有输入、源码、运行证据和输出之间的可追溯链
- 没有使用AI图片生成、手填数值或模拟数据制作正式实验结论图

A stage is `通过` only when all critical criteria are satisfied with traceable evidence. Otherwise return `部分通过` or `不通过`.

## User-facing output requirements

- Respond in Chinese unless the user requests otherwise.
- Preserve the source-defined deliverable names.
- Separate `已核实`, `待核实`, and `AI推断` where the distinction affects trust.
- Do not fabricate missing inputs.

## Next-action card contract

- After formal review, end with exactly one next-action card.
- If passed and the next task is agent-executable, generate the project-specific next-stage Prompt using `templates/next-stage-prompt-card.md`.
- If partially passed or failed, remain in this stage and generate a repair Prompt using `templates/repair-prompt-card.md`.
- Run the capability check before any external task. When the route is MANUAL or HYBRID, provide exact beginner steps, completion evidence, return materials, and a return Prompt where applicable.
- Default external playbook: `references/action-playbooks/empirical-data-and-experiment.md`.
- For web-obtained evidence, use `references/action-playbooks/web-data-collection.md`.
- Load that web playbook only for `INSUFFICIENT` or `ABSENT`; never load it for `UNKNOWN` or `SUFFICIENT`.
- After collection, end with `templates/data-acquisition-review-card.md`. If the user approves, remain in E5 and open data cleaning; if not, remain in the acquisition subgate.

## Transition

- If passed: update the state card and move to `E6`.
- If partially passed or failed: remain in `E5`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
- User approval of acquisition opens cleaning but does not by itself pass E5; E5 passes only after cleaning, analysis, and evidence review are complete.
