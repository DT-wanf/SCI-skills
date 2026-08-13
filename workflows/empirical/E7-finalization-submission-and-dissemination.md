---
stage_id: E7
paper_family: empirical
stage_name_en: Finalization, Submission, and Dissemination
stage_name_zh: 终稿打磨、投稿与学术传播
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

# E7 - Finalization, Submission, and Dissemination

## Purpose

Convert the manuscript into a submission-ready, review-ready, and communicable final version.

## Entry condition

Use this module only after the project has been routed to `empirical` and this stage has been diagnosed as the earliest essential non-passed stage, or when the user explicitly requests a provisional task from this stage.

## Required fields

```yaml
  - id: manuscript
    label_zh: 完整论文初稿
    ask_zh: 请上传或粘贴完整论文初稿。
    reply_format_zh: 完整论文初稿：
  - id: requirements
    label_zh: 目标期刊或学校要求
    ask_zh: 请提供目标期刊、学校格式或投稿要求的原文或链接。
    reply_format_zh: 目标期刊或学校要求：
  - id: references_figures
    label_zh: 参考文献与图表清单
    ask_zh: 请提供参考文献、图表、附录和补充材料清单。
    reply_format_zh: 参考文献与图表清单：
```

## Optional fields

- 伦理声明
- 数据可获得性声明
- 审稿意见
- 稿件类型

## Active intake form

Ask only for unresolved required fields. Use this Chinese copyable format:

```text
完整论文初稿：
目标期刊或学校要求：
参考文献与图表清单：
```

Optional fields should be requested only after the required fields are usable. Allow `暂无` when appropriate.

## Field validation

- Confirm that each field is specific enough for the stage purpose.
- Reuse validated outputs from previous stages.
- Mark inferred values as `AI推断` and request confirmation.
- Exact sources, data, quotations, results, and external requirements are evidence-locked.

## CREATE mode

Create a submission checklist covering title, abstract, keywords, structure, figures, references, supplements, ethics, data availability, authorship, blind review, naming, and required files.

Generate source-aligned outputs. Explain the basis, intended use, and items requiring manual verification. Avoid generic suggestions.

## REFINE mode

Audit the manuscript and submission package against the supplied official requirements. Draft cover letters or reviewer responses without inventing funding, ethics IDs, links, or author contributions.

Always evaluate refinement along these four source-defined dimensions:

1. Alignment with the current stage goal.
2. Ability to support downstream stages.
3. Evidence insufficiency or conceptual ambiguity.
4. Additional material required.

Convert every major revision point into an executable task.

## PACKAGE mode

Consolidate the conversation and verified materials into the exact deliverables below. Make every deliverable usable as the next stage's input, and clearly mark manual-verification items.

## Source-defined deliverables

- 终稿文件
- 投稿前检查清单
- 投稿信或封面信
- 审稿回复框架
- 补充材料清单
- 传播版摘要或汇报提纲

## REVIEW mode

Apply the acceptance criteria below and use `templates/stage-review.md`.

### Acceptance criteria

- 格式符合目标要求
- 图表、引用、附录和声明齐全
- 审稿意见逐条回应且标明修改位置
- 终稿无明显错字、格式混乱或证据缺口
- 投稿材料与目标要求一致

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
- If partially passed or failed: remain in `E7`, list at most three critical gaps, and provide executable repair tasks.
- If this is a provisional downstream request: do not change earlier stage status.
