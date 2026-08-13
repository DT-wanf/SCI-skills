---
stage_id: I6
paper_family: interpretive
stage_name_en: Drafting and Interpretive Deepening
stage_name_zh: 正文写作与阐释深化
next_stage: I7
action_type_default: prompt
capability_candidates:
  - manuscript-writing
  - academic-polishing
external_playbook: null
---

# I6 - Drafting and Interpretive Deepening

## Purpose

Write a coherent academic argument that integrates textual evidence, theoretical lens, and central thesis.

## Entry condition

Use this module only after the project has been routed to `interpretive` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供中心论点、详细提纲、章节材料分配表和题目修订版。
    reply_format_zh: 上一阶段产出物：
  - id: draft_or_evidence
    label_zh: 正文、章节论点或证据
    ask_zh: 请粘贴需要写作或修改的段落、章节论点和对应文本证据。
    reply_format_zh: 正文、章节论点或证据：
```

## Optional fields

- 篇幅与格式要求

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
正文、章节论点或证据：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Draft paragraphs with claim, textual evidence, close analysis, theoretical clarification, counter-reading where needed, and a local conclusion connected to the chapter thesis.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Check for vague judgment, weak evidence, mechanical theory use, logical jumps, and subjective feeling presented as a scholarly conclusion. Preserve the user's core interpretation.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 正文初稿
- 核心段落修改稿
- 证据与论点对应表
- 过渡句和章节结论

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 文本证据和解释紧密对应
- 理论使用适度
- 章节之间有递进关系
- 没有把主观感受当作学术结论

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

- If passed: update the state card and move to `I7`.
- If partially passed or failed: remain in `I6`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
