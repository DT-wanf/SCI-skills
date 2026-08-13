---
stage_id: T6
paper_family: theoretical
stage_name_en: Theoretical Contribution, Limits, and Conclusion
stage_name_zh: 理论贡献、局限与结论提升
next_stage: T7
action_type_default: prompt
capability_candidates:
  - manuscript-writing
  - academic-polishing
external_playbook: null
---

# T6 - Theoretical Contribution, Limits, and Conclusion

## Purpose

Clarify the paper's conceptual or theoretical contribution and its boundaries.

## Entry condition

Use this module only after the project has been routed to `theoretical` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供核心章节初稿、概念辨析段落、理论比较表和反驳与回应段落。
    reply_format_zh: 上一阶段产出物：
  - id: conclusion
    label_zh: 结论或章节结论
    ask_zh: 请提供主论点、各章结论和当前结论段。
    reply_format_zh: 结论或章节结论：
```

## Optional fields

- 目标期刊定位

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
结论或章节结论：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Synthesize the argument, state exact conceptual clarification, theoretical correction, integration, or framework contribution, and define scope conditions and unresolved problems.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Check for inflated contribution, concept non-recovery, mismatch with the body, vague future work, and limitations that either hide risks or invalidate the main claim.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 理论贡献表述
- 局限性说明
- 结论初稿
- 未来研究方向

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 结论回答引言问题
- 贡献表述具体而克制
- 局限说明不削弱核心论点

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

- If passed: update the state card and move to `T7`.
- If partially passed or failed: remain in `T6`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
