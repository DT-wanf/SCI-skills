---
stage_id: E6
paper_family: empirical
stage_name_en: Paper Writing and Structural Optimization
stage_name_zh: 论文写作与结构优化
next_stage: E7
action_type_default: prompt
capability_candidates:
  - manuscript-writing
  - academic-polishing
  - scientific-figures
external_playbook: null
---

# E6 - Paper Writing and Structural Optimization

## Purpose

Organize the research process and findings into a coherent academic narrative.

## Entry condition

Use this module only after the project has been routed to `empirical` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: core_question
    label_zh: 核心研究问题
    ask_zh: 请提供核心研究问题。
    reply_format_zh: 核心研究问题：
  - id: review_framework
    label_zh: 文献综述框架
    ask_zh: 请提供文献综述框架和研究空白。
    reply_format_zh: 文献综述框架与研究空白：
  - id: framework_method
    label_zh: 理论框架与研究方法
    ask_zh: 请提供理论框架、假设和研究方法。
    reply_format_zh: 理论框架与研究方法：
  - id: results
    label_zh: 核心结果与图表
    ask_zh: 请提供核心结果、图表和结果解释草稿。
    reply_format_zh: 核心结果与图表：
```

## Optional fields

- 目标期刊结构要求
- 已有正文或提纲

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
核心研究问题：
文献综述框架与研究空白：
理论框架与研究方法：
核心结果与图表：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Build the outline around introduction, literature, framework, method, results, discussion, and conclusion. Define each section question, claim, evidence, transition, and writing risk.

Create a manuscript-level figure map. At each useful location, visibly propose the figure class, purpose, content, split/merge options, required materials, and rendering route. Use the figure proposal card and let the user approve, revise, decline, defer, or upload a reference image. Do not silently render explanatory or enhancement figures or insert unapproved drafts.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Revise existing text for academic logic, transitions, terminology consistency, evidence support, restrained conclusions, and language while preserving the user's validated meaning.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 完整论文提纲
- 各章节初稿
- 图表与结果说明
- 修改记录或问题清单
- 章节衔接检查表
- 论文图位建议与用户选择记录

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 引言问题在结论中得到回应
- 方法、结果和讨论逻辑闭合
- 语言规范且不夸大贡献
- 引用、图表和附录相互对应
- 所有核心结论来自真实文献、数据和结果
- 实验结论图通过真实输入与Python/R运行证据审核；解释性和增强图均在制作前确认图位与拆图方案

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

- If passed: update the state card and move to `E7`.
- If partially passed or failed: remain in `E6`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
