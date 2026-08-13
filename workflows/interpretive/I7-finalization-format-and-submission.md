---
stage_id: I7
paper_family: interpretive
stage_name_en: Finalization, Format, and Submission
stage_name_zh: 终稿打磨、格式规范与提交
next_stage: END
action_type_default: conditional_external
capability_candidates:
  - academic-polishing
  - presubmission-review
  - reviewer-response
  - paper-presentation
external_playbook: submission-platform
---

# I7 - Finalization, Format, and Submission

## Purpose

Unify language, citation, versions, annotations, and structure for final submission.

## Entry condition

Use this module only after the project has been routed to `interpretive` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供正文初稿、核心段落修改稿、证据与论点对应表、过渡句和章节结论。
    reply_format_zh: 上一阶段产出物：
  - id: requirements
    label_zh: 提交或格式要求
    ask_zh: 请提供导师、课程、学校或期刊要求。
    reply_format_zh: 提交或格式要求：
  - id: manuscript
    label_zh: 论文终稿或当前版本
    ask_zh: 请上传或粘贴当前完整稿件。
    reply_format_zh: 论文终稿或当前版本：
```

## Optional fields

- 导师或审稿意见

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
提交或格式要求：
论文终稿或当前版本：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Audit title, abstract, keywords, object, question, method, contribution, source versions, quotation locations, citations, notes, structure, and formatting.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Classify feedback into textual evidence, theory use, structure, language, and formatting, then create a line-item revision plan with locations and verification needs.

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
- 版本与引用检查清单
- 摘要与关键词
- 修改计划

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 文本版本和引用清楚
- 摘要说明对象、问题、方法和贡献
- 格式符合要求
- 没有明显证据缺口

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
- If partially passed or failed: remain in `I7`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
