---
stage_id: T4
paper_family: theoretical
stage_name_en: Argument Framework and Chapter Design
stage_name_zh: 论证框架与章节结构设计
next_stage: T5
action_type_default: prompt
capability_candidates:
  - manuscript-writing
  - scientific-figures
external_playbook: null
---

# T4 - Argument Framework and Chapter Design

## Purpose

Decompose the central claim into a progressively advancing theoretical argument.

## Entry condition

Use this module only after the project has been routed to `theoretical` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供核心论点、理论缺口陈述、论证对象与反驳清单和修正后的题目。
    reply_format_zh: 上一阶段产出物：
  - id: outline
    label_zh: 已有提纲
    ask_zh: 请提供已有提纲或章节设想；没有可写“暂无”。
    reply_format_zh: 已有提纲：
```

## Optional fields

- 篇幅与结构要求

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
已有提纲：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Design each chapter around an explicit argumentative task, premises, concepts, source support, transition, counterargument, and contribution to the central claim.

Identify optional framework, relationship, or navigation figures and mark their intended manuscript locations. Explain the communication value and offer decomposition choices before rendering. The user may approve, revise, decline, defer, or provide a reference image; non-evidentiary communication value is a valid reason to propose a figure.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Audit for argumentative jumps, repeated chapters, concept drift, conclusion-first reasoning, and descriptive literature sections without theoretical work.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 详细论文提纲
- 章节论证任务表
- 关键概念安排表
- 可能反驳位置
- 理论图位建议、内容边界与用户选择记录（如适用）

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 每章有明确论证功能
- 章节顺序推动主论点
- 没有把文献介绍误当成理论论证
- 若制作理论图，图中没有把概念关系或作者主张伪装成已验证的实验机制

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

- If passed: update the state card and move to `T5`.
- If partially passed or failed: remain in `T4`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
