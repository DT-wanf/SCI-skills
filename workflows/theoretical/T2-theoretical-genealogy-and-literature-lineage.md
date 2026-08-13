---
stage_id: T2
paper_family: theoretical
stage_name_en: Theoretical Genealogy and Literature Lineage
stage_name_zh: 理论谱系与文献脉络梳理
next_stage: T3
action_type_default: conditional_external
capability_candidates:
  - literature-search
  - paper-deep-reading
external_playbook: literature-database-export
---

# T2 - Theoretical Genealogy and Literature Lineage

## Purpose

Establish the academic origin, major divisions, and development of the theoretical problem.

## Entry condition

Use this module only after the project has been routed to `theoretical` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: previous_outputs
    label_zh: 上一阶段产出物
    ask_zh: 请提供理论问题表述、核心概念清单、初步论点版本和研究边界说明。
    reply_format_zh: 上一阶段产出物：
  - id: literature
    label_zh: 理论文献与原典
    ask_zh: 请提供理论原典、代表文献或文献清单。
    reply_format_zh: 理论文献与原典：
```

## Optional fields

- 需要重点梳理的学派或争议

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
上一阶段产出物：
理论文献与原典：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Organize the genealogy by representative thinker, proposition, contribution, limitation, school, concept use, dispute, and relation to the paper's problem.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Check source accuracy, classification consistency, missing positions, and whether the proposed theoretical gap follows from the actual literature rather than from a simplified summary.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 理论谱系表
- 核心文献分类表
- 主要争议清单
- 可进入的理论缺口

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 能够说明理论问题从哪里来
- 不同理论立场之间差异清楚
- 文献综述服务于后续论证

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
- Default external playbook: `references/action-playbooks/literature-database-export.md`.

## Transition

- If passed: update the state card and move to `T3`.
- If partially passed or failed: remain in `T2`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
