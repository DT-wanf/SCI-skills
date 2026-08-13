---
stage_id: T5
paper_family: theoretical
stage_name_en: Conceptual Analysis and Theoretical Argument
stage_name_zh: 概念辨析与理论论证展开
next_stage: T6
action_type_default: prompt
capability_candidates:
  - manuscript-writing
  - academic-polishing
external_playbook: null
---

# T5 - Conceptual Analysis and Theoretical Argument

## Purpose

Complete the core argument through conceptual analysis, theoretical comparison, and logical reasoning.

## Entry condition

Use this module only after the project has been routed to `theoretical` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供详细论文提纲、章节论证任务表、关键概念安排表和可能反驳位置。
    reply_format_zh: 上一阶段产出物：
  - id: argument_text
    label_zh: 理论论证段落或材料
    ask_zh: 请粘贴需要分析或修改的理论论证段落及其引用来源。
    reply_format_zh: 理论论证段落或材料：
```

## Optional fields

- 目标章节论点

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
理论论证段落或材料：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Develop concept definitions, distinctions, comparative propositions, premise chains, objections, replies, and implications. Represent opposing theories charitably and accurately.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Check concept consistency, logical jumps, hidden premises, unfair criticism, unsupported attribution, and whether the response actually addresses the strongest objection.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 核心章节初稿
- 概念辨析段落
- 理论比较表
- 反驳与回应段落

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 每个判断有理论依据或文本依据
- 推理链条清楚
- 对被批判理论的呈现不过度简化

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

- If passed: update the state card and move to `T6`.
- If partially passed or failed: remain in `T5`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
