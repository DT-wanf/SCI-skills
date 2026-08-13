# Action Routing

## Capability check

Before producing the next action, answer:

1. Has existing data sufficiency been assessed as `UNKNOWN`, `SUFFICIENT`, `INSUFFICIENT`, or `ABSENT`?
2. Can the agent access the needed tool, source, file, or website?
3. Does the step require the user's account, institutional login, payment, consent, or identity?
4. Does it require a real experiment, interview, field observation, data collection, prototype run, or submission?
5. Can completion be verified from returned evidence?
6. Is an adequate official download, API, licensed dataset, or manual export available before crawling?
7. If payment is required, are current price, license, access duration, export limits, and research-use rights verified?
8. If a result figure is requested, are real inputs, Python/R source, and actual execution evidence available?
9. If an explanatory or enhancement figure is proposed, has its manuscript location, purpose, decomposition, and rendering route been shown to and approved by the user?

## Routes

### PROMPT

Use when the agent can perform the intellectual or file-based task after the user supplies missing inputs.

Output a next-stage Prompt after a passed review or a repair Prompt after a non-passed review.

### MANUAL

Use when the action must be performed by the user and no useful agent processing can begin until it is complete.

Output a manual action card with exact steps, completion evidence, and what to bring back. Do not invent a Prompt merely to satisfy the format.

### HYBRID

Use when the user must perform a bounded external action and the agent can continue after files or records are returned.

Output the manual steps followed by a return Prompt.

## Forbidden shortcuts

Never stop at:

- “自行检索”
- “去数据库下载CSV”
- “完成实验后再来”
- “按期刊要求修改”
- “上传系统投稿”

Name the platform or explain how it will be selected, provide the navigation path, inputs, filters, output format, file naming, completion standard, and return materials.

## Data-acquisition priority

Do not route to acquisition while data status is `UNKNOWN` or `SUFFICIENT`. For `INSUFFICIENT` or `ABSENT` web-obtained research data, prefer `download/API -> licensed paid source -> authorized export -> crawl`. Recommend a paid source when it is methodologically better, but disclose cost type, access conditions, research-use limits, and a free alternative. Use `web-data-collection.md` only after a source plan has been reviewed.

Do not route to crawling unless non-crawl routes are documented as inadequate and `crawl_necessity` is `JUSTIFIED`.

Do not treat crawler code as evidence of collection. Require a pilot result, run log or export record, data dictionary, provenance fields, and sample rows before accepting that acquisition occurred.

## Figure routing

- `NOT_READY`: request the smallest missing source material; do not render.
- `PLAN_READY`: produce a visible figure proposal or executable Python/R plan; do not claim a figure exists.
- `RENDER_READY`: render only through the approved class-specific route.
- `REVISION_READY`: audit the existing figure and its source context before editing.

For result figures, use `PROMPT` only when the agent can access the real inputs, run Python/R, inspect the output, and preserve execution evidence. Otherwise use `HYBRID`: provide executable code and require the returned script, console/log evidence, and rendered files. Never route a result figure through an image-generation model.

For explanatory or enhancement figures, use the proposal card before any rendering. User approval opens rendering but does not constitute final approval. Final insertion requires the figure review card and explicit acceptance.

## Stage-result interaction

- Passed + PROMPT: next-stage Prompt
- Partial/failed + PROMPT: current-stage repair Prompt
- Any result + MANUAL: manual action card; keep stage status unchanged
- Any result + HYBRID: hybrid card and return Prompt; keep stage status unchanged until evidence returns
