---
stage_id: M1
paper_family: method_application
stage_name_en: Application Problem and Need Definition
stage_name_zh: 应用问题与需求场景定义
next_stage: M2
action_type_default: prompt
capability_candidates:
  - literature-search
external_playbook: null
---

# M1 - Application Problem and Need Definition

## Purpose

Transform a real pain point, technical bottleneck, or practical need into a solvable and testable paper problem.

## Entry condition

Use this module only after the project has been routed to `method_application` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: application_problem
    label_zh: 应用场景或技术问题
    ask_zh: 你准备解决什么具体应用场景或技术问题？
    reply_format_zh: 应用场景或技术问题：
  - id: pain_point
    label_zh: 真实需求或痛点
    ask_zh: 这个场景中的真实需求、痛点或约束是什么？
    reply_format_zh: 真实需求或痛点：
  - id: resources
    label_zh: 可用数据、工具或资源
    ask_zh: 你可以使用哪些数据、设备、软件、代码、案例或团队资源？
    reply_format_zh: 可用数据、工具或资源：
  - id: existing_solutions
    label_zh: 现有方法或方案
    ask_zh: 目前有哪些方法、工具或竞品方案？不了解可写“暂无”。
    reply_format_zh: 现有方法或方案：
```

## Optional fields

- 目标期刊、课程或学校要求

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
应用场景或技术问题：
真实需求或痛点：
可用数据、工具或资源：
现有方法或方案：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Generate multiple method/application topics. For each, state the real pain point, existing-method limitation, proposed method direction, validation approach, and minimum viable version.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Rewrite the initial problem through scenario need, existing limitation, method entry point, validation indicator, and application value. Convert ambiguity and missing evidence into tasks.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 问题定义
- 需求场景说明
- 现有痛点清单
- 评价目标

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 问题真实具体
- 应用场景清楚
- 评价标准初步明确

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

- If passed: update the state card and move to `M2`.
- If partially passed or failed: remain in `M1`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
