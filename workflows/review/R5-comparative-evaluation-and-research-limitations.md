---
stage_id: R5
paper_family: review
stage_name_en: Comparative Evaluation and Research Limitations
stage_name_zh: 比较评价与研究不足分析
next_stage: R6
action_type_default: prompt
capability_candidates:
  - paper-deep-reading
  - manuscript-writing
external_playbook: null
---

# R5 - Comparative Evaluation and Research Limitations

## Purpose

Evaluate contributions, limitations, contradictions, and unresolved problems in existing research.

## Entry condition

Use this module only after the project has been routed to `review` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供分类框架、研究脉络图、主题板块说明和发展阶段总结。
    reply_format_zh: 上一阶段产出物：
  - id: evaluation_materials
    label_zh: 评价材料
    ask_zh: 请提供需要评价的文献矩阵、分类结果或已有“研究不足”段落。
    reply_format_zh: 评价材料：
```

## Optional fields

- 质量评价标准

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
评价材料：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Compare theories, methods, samples, data, settings, results, quality, and limitations. Distinguish genuine gaps from normal scope limits and formulate researchable future questions.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Rewrite vague limitation claims into specific, evidence-based, verifiable problems. Identify contradictory findings, methodological trade-offs, and boundary conditions.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 研究评价表
- 主要不足清单
- 争议与矛盾总结
- 研究空白陈述

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 评价有依据而不泛泛
- 不足能够导向未来研究
- 没有贬低已有研究或过度概括

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

- If passed: update the state card and move to `R6`.
- If partially passed or failed: remain in `R5`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
