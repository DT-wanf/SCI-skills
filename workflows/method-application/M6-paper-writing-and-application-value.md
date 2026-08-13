---
stage_id: M6
paper_family: method_application
stage_name_en: Paper Writing and Application Value
stage_name_zh: 论文写作与应用价值表达
next_stage: M7
action_type_default: prompt
capability_candidates:
  - manuscript-writing
  - academic-polishing
external_playbook: null
---

# M6 - Paper Writing and Application Value

## Purpose

Organize the problem, solution, implementation, and validation into a method/application paper.

## Entry condition

Use this module only after the project has been routed to `method_application` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供验证方案、评价指标表、实验或案例结果和对比分析表。
    reply_format_zh: 上一阶段产出物：
  - id: problem_solution_results
    label_zh: 问题、方案与结果
    ask_zh: 请提供问题定义、方法方案、实现过程和核心结果。
    reply_format_zh: 问题、方案与结果：
```

## Optional fields

- 已有提纲或正文
- 目标期刊结构

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
问题、方案与结果：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Create a paper structure that makes the chain problem -> existing limitation -> solution -> implementation -> validation -> application value explicit and reproducible.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Check the method description for missing steps, conceptual inconsistency, vague novelty, insufficient validation, overstated application value, and undefined applicability boundaries.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 论文提纲
- 方法章节初稿
- 验证结果说明
- 应用价值段落

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 方法描述足以让他人理解和复现
- 验证结果对应核心问题
- 贡献具体而非只说有价值
- 局限和适用范围明确

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

- If passed: update the state card and move to `M7`.
- If partially passed or failed: remain in `M6`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
