---
stage_id: T1
paper_family: theoretical
stage_name_en: Theoretical Problem and Core Concept Definition
stage_name_zh: 理论问题与核心概念界定
next_stage: T2
action_type_default: prompt
capability_candidates:
  - literature-search
external_playbook: null
---

# T1 - Theoretical Problem and Core Concept Definition

## Purpose

Turn a broad intellectual interest into a problem requiring conceptual clarification, theoretical correction, or framework construction.

## Entry condition

Use this module only after the project has been routed to `theoretical` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: initial_problem
    label_zh: 初步理论问题或思想兴趣
    ask_zh: 你准备讨论什么理论问题、思想兴趣或现实中的概念困难？
    reply_format_zh: 初步理论问题或思想兴趣：
  - id: core_concept
    label_zh: 核心概念或理论对象
    ask_zh: 涉及哪些核心概念、理论对象或命题？
    reply_format_zh: 核心概念或理论对象：
  - id: core_sources
    label_zh: 经典文本或核心文献
    ask_zh: 你目前有哪些经典文本、理论原文或核心文献？
    reply_format_zh: 经典文本或核心文献：
  - id: existing_dispute
    label_zh: 已有争议或解释不足
    ask_zh: 现有理论在哪些地方存在争议或解释不足？
    reply_format_zh: 已有争议或解释不足：
```

## Optional fields

- 目标期刊、课程或学校要求

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
初步理论问题或思想兴趣：
核心概念或理论对象：
经典文本或核心文献：
已有争议或解释不足：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Generate multiple theoretical topics and identify the dispute, concepts, critical object, possible contribution, and minimum writable version. Define concept source, dispute, explanatory limitation, position, and contribution.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Audit whether the initial idea is a theoretical problem rather than a general opinion. Narrow concepts, identify what must be defined first, and convert conceptual ambiguity into tasks.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 理论问题表述
- 核心概念清单
- 初步论点版本
- 研究边界说明

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 问题指向理论争议或概念困难
- 核心概念有明确边界
- 能够说明本文不是简单介绍而是提出判断

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

- If passed: update the state card and move to `T2`.
- If partially passed or failed: remain in `T1`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
