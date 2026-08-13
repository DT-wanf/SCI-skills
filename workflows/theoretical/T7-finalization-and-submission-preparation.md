---
stage_id: T7
paper_family: theoretical
stage_name_en: Finalization and Submission Preparation
stage_name_zh: 终稿打磨与投稿准备
next_stage: END
action_type_default: conditional_external
capability_candidates:
  - academic-polishing
  - presubmission-review
  - reviewer-response
  - data-availability
  - paper-presentation
external_playbook: submission-platform
---

# T7 - Finalization and Submission Preparation

## Purpose

Prepare a clear, accurately cited, structurally complete theoretical manuscript for submission.

## Entry condition

Use this module only after the project has been routed to `theoretical` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供理论贡献表述、局限性说明、结论初稿和未来研究方向。
    reply_format_zh: 上一阶段产出物：
  - id: manuscript
    label_zh: 完整稿件
    ask_zh: 请上传或粘贴完整稿件。
    reply_format_zh: 完整稿件：
  - id: requirements
    label_zh: 目标要求
    ask_zh: 请提供期刊、课程、学校或答辩要求。
    reply_format_zh: 目标要求：
```

## Optional fields

- 审稿或导师意见

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
完整稿件：
目标要求：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Audit terminology, citations, original theoretical sources, abstract, argument continuity, formatting, submission package, and author claims.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Classify feedback into theoretical, structural, literature, and language issues, then create a line-item revision plan with source verification and manuscript locations.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 终稿
- 格式检查清单
- 投稿信/答辩说明
- 修改计划

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 术语统一
- 引用准确可查
- 摘要清楚表达问题、方法和贡献
- 审稿回复逐条对应

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
- Default external playbook: `references/action-playbooks/submission-platform.md`.

## Transition

- If passed: update the state card and move to `END`.
- If partially passed or failed: remain in `T7`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
