---
stage_id: E1
paper_family: empirical
stage_name_en: Research Topic and Problem Definition
stage_name_zh: 科研选题与问题定义
next_stage: E2
action_type_default: prompt
capability_candidates:
  - literature-search
external_playbook: null
---

# E1 - Research Topic and Problem Definition

## Purpose

Compress a broad interest into a researchable, verifiable, and writable core problem.

## Entry condition

Use this module only after the project has been routed to `empirical` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: initial_direction
    label_zh: 初步研究方向或现实问题
    ask_zh: 你目前感兴趣的研究方向或想解决的现实问题是什么？
    reply_format_zh: 初步研究方向或现实问题：
  - id: discipline_context
    label_zh: 研究领域或学科背景
    ask_zh: 这个问题属于什么研究领域或学科背景？
    reply_format_zh: 研究领域或学科背景：
  - id: available_resources
    label_zh: 已有经验与资源条件
    ask_zh: 你目前有哪些经验、数据渠道、样本、实验、访谈或团队资源？
    reply_format_zh: 已有经验与资源条件：
  - id: evidence_access
    label_zh: 可获得证据条件
    ask_zh: 你实际能够获得哪些数据、样本、实验或访谈材料？
    reply_format_zh: 可获得证据条件：
```

## Optional fields

- 目标期刊、学校要求或完成时限

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
初步研究方向或现实问题：
研究领域或学科背景：
已有经验与资源条件：
可获得证据条件：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Generate multiple candidate empirical questions, score them on scientific value, novelty, evidence availability, method feasibility, and writability, then narrow the best options into explicit objects, boundaries, relationships, mechanisms, or effects.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Rewrite an existing broad direction through background trend, key contradiction, researchable question, variable relationship, and verifiable contribution. Identify concepts and boundaries that remain vague.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 候选选题清单
- 核心研究问题表述
- 研究对象与边界说明
- 初步题目 3 个版本

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 研究问题可转化为变量、对象、关系、机制或效果
- 研究对象、时间范围和场景边界清楚
- 能够说明使用何种证据回答问题
- 至少一个题目具备三个月内完成最小可行版本的可能

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

- If passed: update the state card and move to `E2`.
- If partially passed or failed: remain in `E1`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
