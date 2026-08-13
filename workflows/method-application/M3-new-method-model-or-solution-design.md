---
stage_id: M3
paper_family: method_application
stage_name_en: New Method, Model, or Solution Design
stage_name_zh: 新方法、模型或方案设计
next_stage: M4
action_type_default: prompt
capability_candidates:
  - scientific-figures
  - manuscript-writing
external_playbook: null
---

# M3 - New Method, Model, or Solution Design

## Purpose

Propose a clear, executable, and explainable method or application solution.

## Entry condition

Use this module only after the project has been routed to `method_application` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供现有方法对比表、不足分析、改进方向和相关文献清单。
    reply_format_zh: 上一阶段产出物：
  - id: problem_and_gap
    label_zh: 问题与现有不足
    ask_zh: 请确认要解决的问题以及现有方法的具体不足。
    reply_format_zh: 问题与现有不足：
```

## Optional fields

- 已有方案草稿
- 资源限制

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
问题与现有不足：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Design the overall framework, modules, process, inputs, outputs, key parameters, resources, innovation points, assumptions, and applicability limits.

Propose a method-figure architecture before rendering. For a non-trivial algorithm or system, offer at least a multi-panel overview option and an overview-plus-module-figures option. Mark the intended manuscript location, explain each panel's communication task, and let the user approve, split, merge, decline, or upload a reference image.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Check the proposed solution for logical breaks, unclear steps, unavailable resources, unverifiable metrics, and unclear innovation. Revise it into a minimum executable architecture.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 方法框架图文字版
- 方法图位、全览与模块拆图建议及用户选择记录
- 模块说明
- 操作流程
- 资源与条件清单

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 方案结构清楚
- 每个模块有明确功能
- 能够说明相对现有方法的改进点
- 具备实施条件
- 复杂方法没有被强行压缩成单张拥挤图片；若制作图件，已先获得用户对图位和拆图方案的确认

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

- If passed: update the state card and move to `M4`.
- If partially passed or failed: remain in `M3`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
