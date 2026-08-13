---
stage_id: R2
paper_family: review
stage_name_en: Search Strategy and Literature Screening
stage_name_zh: 检索策略与文献筛选
next_stage: R3
action_type_default: conditional_external
capability_candidates:
  - literature-search
external_playbook: literature-database-export
---

# R2 - Search Strategy and Literature Screening

## Purpose

Establish a transparent and reproducible literature search and screening process.

## Entry condition

Use this module only after the project has been routed to `review` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供综述主题、范围说明、综述类型判断和核心综述问题。
    reply_format_zh: 上一阶段产出物：
  - id: search_materials
    label_zh: 已有检索材料
    ask_zh: 请提供已有关键词、检索式、数据库、检索结果摘要或文献清单。
    reply_format_zh: 已有检索材料：
```

## Optional fields

- 课程、导师或期刊要求

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
已有检索材料：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Design Chinese and English keywords, Boolean search strings, database coverage, time range, inclusion and exclusion criteria, deduplication, screening stages, and a screening record.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Review actual search results and classify records as must include, possibly include, or exclude with reasons. Never generate fictional studies to fill a category.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 检索式
- 数据库清单
- 纳入/排除标准
- 筛选记录表

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 检索过程可复述
- 筛选标准前后一致
- 最终文献来源真实可查

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
- Default external playbook: `references/action-playbooks/literature-database-export.md`.

## Transition

- If passed: update the state card and move to `R3`.
- If partially passed or failed: remain in `R2`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
