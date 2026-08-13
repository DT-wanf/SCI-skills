---
stage_id: I1
paper_family: interpretive
stage_name_en: Interpretive Object and Research Question Definition
stage_name_zh: 阐释对象与研究问题确定
next_stage: I2
action_type_default: prompt
capability_candidates:
  - literature-search
external_playbook: null
---

# I1 - Interpretive Object and Research Question Definition

## Purpose

Transform a text, work, historical material, event, or cultural phenomenon into a specific academic interpretive question.

## Entry condition

Use this module only after the project has been routed to `interpretive` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: initial_object
    label_zh: 初步对象
    ask_zh: 你想研究哪个文本、作品、事件、历史材料或文化现象？
    reply_format_zh: 初步对象：
  - id: core_detail
    label_zh: 核心细节或矛盾
    ask_zh: 其中哪个细节、矛盾、叙事结构、意象或历史语境最值得重新解释？
    reply_format_zh: 核心细节或矛盾：
  - id: primary_materials
    label_zh: 可获得的原始材料
    ask_zh: 你目前可以获得哪些原始文本、版本、译本或档案材料？
    reply_format_zh: 可获得的原始材料：
```

## Optional fields

- 可使用的理论视角
- 目标期刊、课程或学校要求

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
初步对象：
核心细节或矛盾：
可获得的原始材料：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Generate at least three interpretive paper questions. For each, define the object, core problem, possible materials, theoretical lens, expected novelty, and the textual or contextual details required to support it.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Rewrite an overbroad object into three writable question versions. Evaluate alignment with the stage goal, downstream support, evidence sufficiency, conceptual clarity, and missing materials, then convert revisions into executable tasks.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 阐释对象说明
- 核心研究问题
- 材料范围
- 题目版本

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 问题具体且可通过材料分析回答
- 研究对象边界清楚
- 不是简单主题赏析或读后感

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

- If passed: update the state card and move to `I2`.
- If partially passed or failed: remain in `I1`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
