---
stage_id: M2
paper_family: method_application
stage_name_en: Existing Methods and Competing Solutions
stage_name_zh: 现有方法与竞品方案分析
next_stage: M3
action_type_default: conditional_external
capability_candidates:
  - literature-search
  - paper-deep-reading
external_playbook: literature-database-export
---

# M2 - Existing Methods and Competing Solutions

## Purpose

Clarify the strengths, limitations, and improvement space of existing methods, tools, or solutions.

## Entry condition

Use this module only after the project has been routed to `method_application` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供问题定义、需求场景说明、现有痛点清单和评价目标。
    reply_format_zh: 上一阶段产出物：
  - id: existing_materials
    label_zh: 现有方法资料
    ask_zh: 请提供已有方法、论文、竞品、技术文档或测试材料。
    reply_format_zh: 现有方法资料：
```

## Optional fields

- 需要重点比较的指标
- 目标期刊或课程要求

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
现有方法资料：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Build a comparison table covering method, core idea, assumptions, conditions, performance, cost, usability, scalability, validation difficulty, strengths, limitations, and improvement opportunities.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Audit the user's comparison for unsupported claims, outdated information, incomparable metrics, and vague limitations. Identify the exact baseline or solution relative to which improvement is claimed.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 现有方法对比表
- 不足分析
- 改进方向
- 相关文献清单

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 能够明确本文相对谁改进
- 不足具体而非泛泛
- 改进方向与后续方案一致

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

- If passed: update the state card and move to `M3`.
- If partially passed or failed: remain in `M2`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
