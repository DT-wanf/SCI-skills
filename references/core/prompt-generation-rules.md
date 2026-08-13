# Prompt Generation Rules

## Prompt contract

Generate a Prompt that a beginner can copy as one block.

Include:

1. Agent role
2. Current stage and task
3. Verified project context
4. Missing fields shown as `【字段：填写说明】`
5. Uploaded or required materials
6. Named deliverables
7. Evidence labels and prohibited invention
8. Acceptance criteria
9. Required stage-review format
10. Transition rule

## Personalization

Fill all verified values directly. Do not turn known facts back into placeholders.

Use `【】` only for:

- missing required fields;
- choices that require the user;
- evidence-locked facts the agent cannot verify.

Allow `暂无`, but instruct the agent to mark the resulting limitation.

## Passed-stage Prompt

Target the next stage and include the approved outputs from the current stage as inputs.

## Repair Prompt

Remain in the current stage. List only the critical gaps found in review. Ask for another formal review after correction.

## Formatting

Place the Prompt in one fenced text block. Do not insert commentary inside the block. Keep the instruction explicit enough for a new conversation.
