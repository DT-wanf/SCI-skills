---
stage_id: E3
paper_family: empirical
stage_name_en: Theoretical Framework and Research Hypotheses
stage_name_zh: 理论框架与研究假设
next_stage: E4
action_type_default: prompt
capability_candidates:
  - paper-deep-reading
  - scientific-figures
external_playbook: null
---

# E3 - Theoretical Framework and Research Hypotheses

## Purpose

Convert explanatory logic from the literature into a testable framework and hypotheses.

## Entry condition

Use this module only after the project has been routed to `empirical` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: core_question
    label_zh: 核心研究问题
    ask_zh: 请提供核心研究问题。
    reply_format_zh: 核心研究问题：
  - id: research_gap
    label_zh: 研究空白
    ask_zh: 请提供已通过验收的研究空白陈述。
    reply_format_zh: 研究空白：
  - id: core_theory
    label_zh: 核心理论或关键文献
    ask_zh: 请提供可核查的核心理论或关键文献。
    reply_format_zh: 核心理论或关键文献：
  - id: candidate_variables
    label_zh: 可能变量或概念
    ask_zh: 请列出目前考虑的变量或核心概念；不确定可写“暂无”。
    reply_format_zh: 可能变量或概念：
```

## Optional fields

- 研究对象与边界
- 已有理论框架或假设草稿

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
核心研究问题：
研究空白：
核心理论或关键文献：
可能变量或概念：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Build a theory-to-mechanism-to-variable-to-testable-proposition chain. Define independent, dependent, mediator, moderator, control, and confounding variables only when justified.

Prepare a theoretical-framework figure proposal at its intended manuscript location. Explain why a figure would help, what relationships it will show, and what it will not establish. Use the figure proposal card and wait for approval before rendering; a verified text framework remains sufficient if the user declines the figure.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Check conceptual clarity, theory support, measurability, causal direction, testability, confounding, and alignment with the research gap. Revise each hypothesis and name the evidence required.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 理论框架图或文字版框架
- 变量关系说明
- 研究假设列表
- 核心概念定义
- 变量与假设对应表

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 每个假设有明确理论依据
- 变量原则上可测量、编码或通过材料识别
- 理论框架能够指导研究设计
- 假设与研究空白直接对应
- 若制作理论框架图，图位和关系边界已由用户确认，且图中没有把假设关系冒充为已验证因果机制

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

- If passed: update the state card and move to `E4`.
- If partially passed or failed: remain in `E3`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
