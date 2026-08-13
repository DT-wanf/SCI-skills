---
stage_id: R3
paper_family: review
stage_name_en: Literature Reading, Coding, and Evidence Matrix
stage_name_zh: 文献阅读、编码与资料矩阵
next_stage: R4
action_type_default: conditional_external
capability_candidates:
  - literature-search
  - paper-deep-reading
external_playbook: literature-database-export
---

# R3 - Literature Reading, Coding, and Evidence Matrix

## Purpose

Convert a large literature set into comparable and analyzable structured material.

## Entry condition

Use this module only after the project has been routed to `review` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供检索式、数据库清单、纳入/排除标准和筛选记录表。
    reply_format_zh: 上一阶段产出物：
  - id: literature_materials
    label_zh: 文献摘要或全文材料
    ask_zh: 请提供真实文献摘要、全文、笔记或已有编码表。
    reply_format_zh: 文献摘要或全文材料：
```

## Optional fields

- 核心综述问题

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
文献摘要或全文材料：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Build coding fields for bibliographic details, topic, theory, method, sample, data, finding, limitation, quality, and relevance to the review question.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Audit an existing coding table for missing fields, inconsistent coding, incomparable categories, unsupported summaries, and whether the matrix can support later classification and evaluation.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 文献编码表
- 核心文献摘要
- 主题标签
- 资料矩阵

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 每篇文献信息完整
- 编码字段能够支持综述问题
- 可以横向比较不同文献

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

- If passed: update the state card and move to `R4`.
- If partially passed or failed: remain in `R3`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
