# Active Placeholder Intake

## Field classes

1. **Required** - execution must pause until supplied.
2. **Optional** - may be omitted, but the limitation must be reported.
3. **Derivable** - may be inferred from prior conversation or files, but requires confirmation.
4. **Defaultable** - use a safe default, such as three candidate versions.
5. **Evidence-locked** - must come from a real source or user material; never infer.

## Collection algorithm

1. Read the current stage module.
2. Build a field inventory from `required_fields`, `optional_fields`, and `evidence_locked_fields`.
3. Resolve fields from conversation and attachments.
4. Mark each field `verified`, `pending_verification`, `inferred`, or `missing`.
5. Ask only for missing required fields in the first round.
6. Ask for optional constraints only after the core fields are usable.
7. Validate scope, evidence form, and compatibility with stage goals.
8. Confirm inferred fields before running the stage task.

## Question quality

A good question:

- names one field;
- explains the expected granularity when necessary;
- provides a copyable reply label;
- permits `暂无` for optional fields;
- does not embed a suggested substantive answer that may bias the user.

## Broad-answer repair

When the answer is too broad, respond in Chinese:

```text
目前的“{field_value}”仍然过宽，暂时无法直接进入本阶段任务。请至少具体到{required_granularity}。
请按以下格式补充：
{field_label}：
```

## Evidence-locked examples

- Exact paper metadata and claims
- Dataset availability and fields
- Sample size and labels
- Statistical output and significance
- Text quotation and page number
- Ethics approval information
- Journal submission requirements
- Code execution output
