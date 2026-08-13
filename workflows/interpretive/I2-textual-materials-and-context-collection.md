---
stage_id: I2
paper_family: interpretive
stage_name_en: Textual Materials and Context Collection
stage_name_zh: 文本材料与背景资料收集
next_stage: I3
action_type_default: conditional_external
capability_candidates:
  - web-data-acquisition
  - literature-search
  - paper-deep-reading
external_playbook: text-and-archive-collection
external_playbook_candidates:
  - text-and-archive-collection
  - web-data-collection
---

# I2 - Textual Materials and Context Collection

## Purpose

Build the textual evidence, historical context, and research material required for interpretation.

## Entry condition

Use this module only after the project has been routed to `interpretive` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供上一阶段通过验收的阐释对象说明、核心研究问题、材料范围和题目版本。
    reply_format_zh: 上一阶段产出物：
  - id: materials
    label_zh: 已有文本与资料
    ask_zh: 请上传或列出原始文本、版本、摘录、档案、背景资料和已有研究。
    reply_format_zh: 已有文本与资料：
```

## Optional fields

- 需要宝宝巴士重点检查或生成的内容
- 导师、课程或期刊要求
- 网络材料的时间、平台、语言、地区、预算和访问条件

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
已有文本与资料：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.
- Assess the sufficiency of existing texts and materials before proposing any new collection.

## CREATE mode

Specify the primary texts, versions, historical background, theory, and prior research needed. Build a source table that records location, page, paragraph, keyword, and intended analytical use.

Classify existing materials first. For `UNKNOWN`, request a source list, sample, version, coverage, or locator evidence. For `SUFFICIENT`, do not load `web-data-acquisition.md`; organize and prepare the existing corpus. Only for `INSUFFICIENT` or `ABSENT`, state the critical textual or contextual gap and activate web acquisition when online evidence is appropriate.

When activated for born-digital or web-accessed materials, compare official or archival downloads, licensed paid collections, authorized exports, and permitted crawling. Define the document or post as a research unit, preserve version and provenance fields, pilot the corpus, and require user review before cleaning, OCR correction, deduplication, excerpt coding, or close reading. Permit crawling only when `crawl_necessity` is `JUSTIFIED`.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Classify the user-provided excerpts by imagery, narrative, character, space, rhetoric, and historical context. Identify which details actually support the question and which materials are missing.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 原始材料清单
- 文本摘录表
- 背景资料清单
- 已有研究简表

For web-obtained corpora also produce a source-choice record, acquisition log, provenance table, and user audit decision.

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 材料能直接支撑阐释问题
- 文本证据有出处和页码
- 背景资料没有喧宾夺主
- 现有材料充足性已先行判断，充分时没有误触发新增采集
- 新获取的网络材料，其范围、版本、权限、缺失和选择偏差已经说明并经用户审核

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
- Default external playbook: `references/action-playbooks/text-and-archive-collection.md`.
- Use `references/action-playbooks/web-data-collection.md` when materials require online download, export, or permitted crawling.
- Load the web playbook only after a result of `INSUFFICIENT` or `ABSENT`; do not load it for `UNKNOWN` or `SUFFICIENT`.
- Do not enter corpus cleaning or I4 close reading until the user approves `templates/data-acquisition-review-card.md`.

## Transition

- If passed: update the state card and move to `I3`.
- If partially passed or failed: remain in `I2`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
