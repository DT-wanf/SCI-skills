---
stage_id: I3
paper_family: interpretive
stage_name_en: Theoretical Lens and Interpretive Path
stage_name_zh: 理论视角与阐释路径选择
next_stage: I4
action_type_default: prompt
capability_candidates:
  - paper-deep-reading
external_playbook: null
---

# I3 - Theoretical Lens and Interpretive Path

## Purpose

Choose an analytical lens that reveals the textual problem rather than mechanically imposing theory.

## Entry condition

Use this module only after the project has been routed to `interpretive` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供原始材料清单、文本摘录表、背景资料清单和已有研究简表。
    reply_format_zh: 上一阶段产出物：
  - id: object_question
    label_zh: 阐释对象与研究问题
    ask_zh: 请确认阐释对象和核心研究问题。
    reply_format_zh: 阐释对象与研究问题：
  - id: candidate_theory
    label_zh: 候选理论视角
    ask_zh: 你目前考虑使用什么理论视角？不确定可写“暂无”。
    reply_format_zh: 候选理论视角：
```

## Optional fields

- 导师、课程或期刊要求

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
阐释对象与研究问题：
候选理论视角：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Compare possible theoretical lenses by what each reveals, what evidence it requires, and how it may distort or flatten the text. Select the smallest adequate lens and map concept to detail to interpretation.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Audit whether the proposed theory genuinely fits the object and question. Build a theory-concept-text-detail-interpretive-conclusion map and identify signs of mechanical theory application.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 理论视角选择说明
- 核心理论概念
- 阐释路径图
- 理论与文本对应表

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 理论与问题高度匹配
- 理论概念有清楚定义
- 能够回到具体材料展开分析

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

- If passed: update the state card and move to `I4`.
- If partially passed or failed: remain in `I3`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
