---
stage_id: T3
paper_family: theoretical
stage_name_en: Theoretical Gap and Author Position
stage_name_zh: 理论缺口与本文立场形成
next_stage: T4
action_type_default: prompt
capability_candidates:
  - paper-deep-reading
  - manuscript-writing
external_playbook: null
---

# T3 - Theoretical Gap and Author Position

## Purpose

Develop a defensible judgment, correction, or integration from existing theoretical tensions.

## Entry condition

Use this module only after the project has been routed to `theoretical` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供理论谱系表、核心文献分类表、主要争议清单和可进入的理论缺口。
    reply_format_zh: 上一阶段产出物：
  - id: proposed_position
    label_zh: 初步论点或立场
    ask_zh: 请写出你目前想提出的核心判断；不成熟也可以。
    reply_format_zh: 初步论点或立场：
```

## Optional fields

- 主要反对观点

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
初步论点或立场：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Form the paper's position by specifying the target theory, precise gap, proposed correction or integration, expected contribution, counterarguments, and minimum defensible claim.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Evaluate conceptual consistency, originality, argument difficulty, refutation risk, and writability. Revise claims that are obvious, unbounded, or unsupported.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 核心论点
- 理论缺口陈述
- 论证对象与反驳清单
- 修正后的题目

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 本文立场明确且可争论
- 论点不是常识判断
- 论点能被后续章节层层支撑

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

## Transition

- If passed: update the state card and move to `T4`.
- If partially passed or failed: remain in `T3`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
