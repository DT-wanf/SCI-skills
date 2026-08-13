---
stage_id: M4
paper_family: method_application
stage_name_en: Implementation Route and Prototype Construction
stage_name_zh: 实施路径与原型构建
next_stage: M5
action_type_default: conditional_external
capability_candidates:
  - scientific-figures
  - data-availability
external_playbook: prototype-and-validation
---

# M4 - Implementation Route and Prototype Construction

## Purpose

Translate the solution into a runnable, testable, or simulatable prototype and execution plan.

## Entry condition

Use this module only after the project has been routed to `method_application` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供方法框架、模块说明、操作流程和资源条件清单。
    reply_format_zh: 上一阶段产出物：
  - id: prototype_goal
    label_zh: 最小可行原型目标
    ask_zh: 你希望最小可行原型实现什么核心功能？
    reply_format_zh: 最小可行原型目标：
  - id: implementation_resources
    label_zh: 实施资源
    ask_zh: 请说明可用数据、代码、设备、平台、人员和时间。
    reply_format_zh: 实施资源：
```

## Optional fields

- 当前实现进度
- 备选方案

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
最小可行原型目标：
实施资源：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Break the method into milestones, modules, interfaces, data preparation, testing sequence, documentation, acceptance criteria, risks, and fallback plans.

Where an implementation or experiment flow would improve comprehension, insert a figure proposal rather than drawing immediately. Invite the user to upload a reference workflow or algorithm figure; adapt its structure or style to the user's own content under the reference-figure rules.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Audit the proposed MVP for scope, dependency, resource availability, testability, and whether the prototype can generate evidence for the core claim.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 实施计划
- 原型功能清单
- 流程文档
- 测试准备材料
- 实施/实验流程图建议、对标图适配方案与用户选择记录（如适用）

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 实施步骤可执行
- 资源需求明确
- 原型能支撑验证目标
- 风险有备选方案
- 若制作流程图，步骤、模块和输入输出均来自已确认方案，并在制作前完成图位与用户确认

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

- If passed: update the state card and move to `M5`.
- If partially passed or failed: remain in `M4`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
