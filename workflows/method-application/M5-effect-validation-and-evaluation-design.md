---
stage_id: M5
paper_family: method_application
stage_name_en: Effect Validation and Evaluation Design
stage_name_zh: 效果验证与评估设计
next_stage: M6
action_type_default: conditional_external
capability_candidates:
  - statistical-reporting
  - scientific-figures
external_playbook: prototype-and-validation
---

# M5 - Effect Validation and Evaluation Design

## Purpose

Use experiments, cases, user tests, or metrics to show whether the method is effective.

## Entry condition

Use this module only after the project has been routed to `method_application` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供实施计划、原型功能清单、流程文档和测试准备材料。
    reply_format_zh: 上一阶段产出物：
  - id: method_goal
    label_zh: 方法与验证目标
    ask_zh: 请说明待验证的方法、核心主张和成功标准。
    reply_format_zh: 方法与验证目标：
  - id: validation_materials
    label_zh: 验证数据或结果
    ask_zh: 请提供数据、基线、实验设置、案例、用户测试或已有结果。
    reply_format_zh: 验证数据或结果：
```

## Optional fields

- 资源与伦理限制

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
方法与验证目标：
验证数据或结果：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Design baselines, metrics, ablations, experiments, cases, user tests, robustness checks, error analysis, and applicability evaluation that directly test the core claim.

Plan result figures, but render them only after the `RESULT` gate passes. Require real validation data or verified outputs, declared metrics/statistics, Python/R plotting source, actual execution evidence, and traceability. Do not use an image-generation model, invented values, or unexecuted code for final validation figures.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Interpret only supplied validation results. Separate strong evidence from supplementary evidence, identify missing baselines or controls, and flag conclusions that exceed the validation scope.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 验证方案
- 评价指标表
- 实验/案例结果
- 对比分析表
- 结果图Python/R源码、真实输入映射、运行证据与审核状态

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 验证方式与目标一致
- 有清楚基线或评价标准
- 结果能支撑核心主张
- 局限被说明
- 所有验证结果图由真实输入经Python/R实际运行生成并可追溯；没有AI生成或手工拼接的实验结论图

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
- Default external playbook: `references/action-playbooks/prototype-and-validation.md`.

## Transition

- If passed: update the state card and move to `M6`.
- If partially passed or failed: remain in `M5`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
