---
stage_id: R6
paper_family: review
stage_name_en: Review Writing and Knowledge Map Presentation
stage_name_zh: 综述正文写作与知识地图呈现
next_stage: R7
action_type_default: prompt
capability_candidates:
  - manuscript-writing
  - academic-polishing
  - scientific-figures
external_playbook: null
---

# R6 - Review Writing and Knowledge Map Presentation

## Purpose

Write the classification, trajectory, and evaluation as a coherent review paper.

## Entry condition

Use this module only after the project has been routed to `review` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供研究评价表、主要不足清单、争议与矛盾总结和研究空白陈述。
    reply_format_zh: 上一阶段产出物：
  - id: framework_materials
    label_zh: 分类框架与资料矩阵
    ask_zh: 请提供分类框架、文献矩阵、研究脉络和图表材料。
    reply_format_zh: 分类框架与资料矩阵：
```

## Optional fields

- 已有综述正文
- 目标期刊结构

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
分类框架与资料矩阵：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Design a problem-oriented outline and integrate classification, trajectory, comparison, limitations, and future directions. Use tables and maps to expose structure rather than decorate the paper.

Actively propose evidence, explanatory, and enhancement figures at visible manuscript locations. State why each figure helps, how it should be split, and what materials it needs; let the user decide whether to create it. Any quantitative map or plot must use the real literature matrix and verified Python/R execution.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Check draft paragraphs for citation stacking, unclear categories, weak evaluation, poor transitions, and future directions unsupported by the synthesis.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 综述论文提纲
- 正文初稿
- 文献分类表
- 研究脉络图/未来方向图
- 全文图件地图、图位建议与用户审核状态

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 正文按问题组织
- 图表帮助理解领域结构
- 评价与未来方向相互对应
- 所有定量图可追溯到真实文献矩阵和Python/R运行；所有解释性或增强图均经过制作前图位确认和制作后用户审核

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

- If passed: update the state card and move to `R7`.
- If partially passed or failed: remain in `R6`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
