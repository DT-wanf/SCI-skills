---
stage_id: I4
paper_family: interpretive
stage_name_en: Close Reading, Coding, and Material Analysis
stage_name_zh: 细读、编码与材料分析
next_stage: I5
action_type_default: conditional_external
capability_candidates:
  - paper-deep-reading
external_playbook: text-and-archive-collection
---

# I4 - Close Reading, Coding, and Material Analysis

## Purpose

Connect textual details to interpretive claims through close reading and structured analysis.

## Entry condition

Use this module only after the project has been routed to `interpretive` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供理论视角选择说明、核心理论概念、阐释路径图和理论与文本对应表。
    reply_format_zh: 上一阶段产出物：
  - id: text_segments
    label_zh: 文本片段或材料
    ask_zh: 请粘贴或上传要分析的具体文本片段、页码和版本信息。
    reply_format_zh: 文本片段或材料：
```

## Optional fields

- 编码维度
- 需要重点分析的问题

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
文本片段或材料：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Perform close reading across lexical choice, imagery, narrative structure, voice, character, space, rhetoric, and context. Trace detail to pattern to tension to interpretation.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Transform supplied materials into a table of textual detail, supported interpretation, missing evidence, and possible counter-reading. Reject claims that cannot be traced to the text.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 文本细读笔记
- 材料分析表
- 关键证据链
- 初步阐释判断

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 每个解释都有具体材料支撑
- 细读不是摘抄而有分析推进
- 能够呈现文本复杂性或矛盾

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
- Default external playbook: `references/action-playbooks/text-and-archive-collection.md`.

## Transition

- If passed: update the state card and move to `I5`.
- If partially passed or failed: remain in `I4`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
