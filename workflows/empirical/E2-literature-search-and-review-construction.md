---
stage_id: E2
paper_family: empirical
stage_name_en: Literature Search and Review Construction
stage_name_zh: 文献检索与综述构建
next_stage: E3
action_type_default: conditional_external
capability_candidates:
  - literature-search
  - paper-deep-reading
external_playbook: literature-database-export
---

# E2 - Literature Search and Review Construction

## Purpose

Use systematic search and classification to establish the research base and locate a specific gap.

## Entry condition

Use this module only after the project has been routed to `empirical` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: core_question
    label_zh: 核心研究问题
    ask_zh: 请提供上一阶段通过验收的核心研究问题。
    reply_format_zh: 核心研究问题：
  - id: working_title
    label_zh: 初步题目
    ask_zh: 请提供当前初步题目。
    reply_format_zh: 初步题目：
  - id: scope
    label_zh: 研究对象与边界
    ask_zh: 请提供研究对象、时间范围和场景边界。
    reply_format_zh: 研究对象与边界：
  - id: existing_literature
    label_zh: 已有文献或关键词
    ask_zh: 请提供已有文献、摘要、笔记或关键词；没有可写“暂无”。
    reply_format_zh: 已有文献或关键词：
```

## Optional fields

- 目标数据库
- 时间范围
- 目标期刊或学校要求

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
核心研究问题：
初步题目：
研究对象与边界：
已有文献或关键词：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Design Chinese and English keywords, database-specific search strings, inclusion and exclusion rules, and a literature matrix covering theme, theory, object, data, method, finding, limitation, and transferable insight.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Classify the user-provided real literature, test whether the proposed gap is specific and verifiable, and reorganize the review around questions rather than paper-by-paper summaries.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 关键词与检索式
- 核心文献清单
- 文献分类矩阵
- 研究空白初步陈述
- 文献综述结构框架

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 能够说明研究所依托的文献基础
- 综述按问题组织而不是逐篇堆砌
- 研究空白直接连接后续假设、理论框架或方法
- 核心文献真实且可核查

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

- If passed: update the state card and move to `E3`.
- If partially passed or failed: remain in `E2`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
