---
stage_id: E4
paper_family: empirical
stage_name_en: Research Design and Method Route
stage_name_zh: 研究设计与方法路线
next_stage: E5
action_type_default: prompt
capability_candidates:
  - web-data-acquisition
  - statistical-reporting
  - data-availability
external_playbook: null
---

# E4 - Research Design and Method Route

## Purpose

Design samples, variables, tools, and analysis paths that can answer the research question.

## Entry condition

Use this module only after the project has been routed to `empirical` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: core_question
    label_zh: 核心研究问题
    ask_zh: 请提供核心研究问题。
    reply_format_zh: 核心研究问题：
  - id: framework_hypotheses
    label_zh: 理论框架与研究假设
    ask_zh: 请提供已通过验收的理论框架与研究假设。
    reply_format_zh: 理论框架与研究假设：
  - id: research_object
    label_zh: 研究对象
    ask_zh: 请说明研究对象与样本边界。
    reply_format_zh: 研究对象：
  - id: resource_conditions
    label_zh: 数据、样本或设备条件
    ask_zh: 请说明实际可用的数据、样本、设备、软件或场地条件。
    reply_format_zh: 数据、样本或设备条件：
```

## Optional fields

- 时间、人力和伦理限制
- 拟采用的方法
- 数据获取预算、机构数据库权限和可使用账号

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
核心研究问题：
理论框架与研究假设：
研究对象：
数据、样本或设备条件：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.
- If data is listed, assess it with `data-sufficiency-gate.md` before selecting acquisition capabilities.

## CREATE mode

Choose an appropriate design, define sampling and inclusion criteria, operationalize variables, map each hypothesis to data and analysis, and specify robustness, ethics, and quality control.

First classify available data as `UNKNOWN`, `SUFFICIENT`, `INSUFFICIENT`, or `ABSENT`.

- For `UNKNOWN`, request the smallest missing evidence and do not recommend sources yet.
- For `SUFFICIENT`, do not load `web-data-acquisition.md`; specify how existing data will be cleaned, derived, coded, and analyzed.
- For `INSUFFICIENT` or `ABSENT`, activate acquisition only after stating the critical gap and deciding that web evidence is appropriate.

When acquisition is activated, load `web-data-acquisition.md`. Map constructs to observable fields and offer two or three ranked source plans. Prefer official downloads or APIs, include a paid licensed source when it is methodologically stronger, and permit crawling only after the last-resort gate is `JUSTIFIED`. Do not pass E4 until either the sufficient-data route is explicit or the activated acquisition route has a selected source, unit, fields, sampling rule, cost, permissions, and pilot plan.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Audit method-question fit, sample sufficiency, variable coverage, bias sources, omitted controls, robustness tests, and alternative explanations. Produce a safer revised route.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 研究设计方案
- 变量操作化表
- 数据收集计划
- 分析方法路线图
- 伦理与质量控制说明

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 方法能够回答研究问题并检验假设
- 数据来源和样本标准清楚
- 变量定义可操作且分析步骤可复现
- 主要偏差、混淆因素和伦理问题已识别
- 已有数据充足性已经基于字段、样本、范围、来源和研究问题完成判断
- 仅当数据为 `INSUFFICIENT` 或 `ABSENT` 时才设计新增数据方案
- 如计划爬取，已记录所有非爬虫路线不适用的理由并将 `crawl_necessity` 标为 `JUSTIFIED`

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
- This stage is Prompt-first, but still switch to MANUAL or HYBRID if a real external action is required.
- If the next action is web-data acquisition, keep the intellectual source selection in E4 and defer real download, payment, export, or crawl execution to E5.
- If data is `SUFFICIENT`, the next E5 action must begin with cleaning or analysis preparation, not source selection or crawling.

## Transition

- If passed: update the state card and move to `E5`.
- If partially passed or failed: remain in `E4`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
