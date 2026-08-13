---
stage_id: R4
paper_family: review
stage_name_en: Classification Framework and Research Trajectory
stage_name_zh: 分类框架与研究脉络提炼
next_stage: R5
action_type_default: prompt
capability_candidates:
  - paper-deep-reading
  - scientific-figures
external_playbook: null
---

# R4 - Classification Framework and Research Trajectory

## Purpose

Extract field structure, development stages, and major branches from the literature matrix.

## Entry condition

Use this module only after the project has been routed to `review` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供文献编码表、核心文献摘要、主题标签和资料矩阵。
    reply_format_zh: 上一阶段产出物：
  - id: review_question
    label_zh: 核心综述问题
    ask_zh: 请确认核心综述问题。
    reply_format_zh: 核心综述问题：
```

## Optional fields

- 已有分类结果

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
核心综述问题：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Construct a classification framework by research problem, theory, method, data, application, mechanism, or other justified dimensions. Explain transitions, branches, and turning points.

Propose the research-trajectory or classification figure at its manuscript location before rendering. Explain what structure the figure clarifies, offer overview-versus-detail options, and let the user approve or provide a reference figure. Quantitative bibliometric panels remain result figures and require real data plus verified Python/R execution.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Check that categories are mutually intelligible, evidence-supported, and analytically useful. Replace chronological listing with an explanatory research trajectory.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 分类框架
- 研究脉络图
- 主题板块说明
- 发展阶段总结
- 研究脉络/分类图位方案与用户选择记录

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 分类标准明确且不重叠
- 能够解释领域发展逻辑
- 不是简单按年份罗列
- 定量脉络图来自真实文献矩阵和Python/R运行证据；解释性脉络图的图位与结构已经用户确认

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

- If passed: update the state card and move to `R5`.
- If partially passed or failed: remain in `R4`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
