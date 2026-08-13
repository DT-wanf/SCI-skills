---
stage_id: I5
paper_family: interpretive
stage_name_en: Interpretive Thesis and Chapter Structure
stage_name_zh: 阐释论点与章节结构形成
next_stage: I6
action_type_default: prompt
capability_candidates:
  - manuscript-writing
external_playbook: null
---

# I5 - Interpretive Thesis and Chapter Structure

## Purpose

Organize dispersed textual details into a central interpretation and layered argument structure.

## Entry condition

Use this module only after the project has been routed to `interpretive` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供文本细读笔记、材料分析表、关键证据链和初步阐释判断。
    reply_format_zh: 上一阶段产出物：
  - id: notes_or_outline
    label_zh: 已有笔记或提纲
    ask_zh: 请提供已有论点、笔记或提纲；没有可写“暂无”。
    reply_format_zh: 已有笔记或提纲：
```

## Optional fields

- 目标篇幅或章节要求

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
已有笔记或提纲：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Form a central interpretive thesis, subordinate claims, chapter sequence, and evidence allocation. Ensure each chapter advances rather than repeats the main claim.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Check the outline for an unclear thesis, repeated evidence, theory substitution, or disordered chapters. Reassign evidence and revise the title to match the argument.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 中心论点
- 详细提纲
- 章节材料分配表
- 题目修订版

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 中心论点清晰且可争论
- 各章节共同服务主论点
- 材料分配不重复、不空泛

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

- If passed: update the state card and move to `I6`.
- If partially passed or failed: remain in `I5`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
