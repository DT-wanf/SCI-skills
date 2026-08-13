# Stage Module Schema

Each stage module must contain:

- Stage identifier and family
- English internal title and Chinese user-facing title
- Purpose
- Entry condition
- Default action type: `prompt` or `conditional_external`
- Candidate capability modules
- Optional external action playbook
- Optional alternate external playbooks selected by source type
- Required, optional, defaultable, and evidence-locked fields
- Chinese active-intake form
- `CREATE`, `REFINE`, `PACKAGE`, and `REVIEW` instructions
- Source-defined deliverables
- Acceptance criteria
- Academic boundaries
- Next-action card contract
- Next-stage transition

The module should be loaded only after paper-family and stage routing.

## Action fields

```yaml
action_type_default: prompt | conditional_external
capability_candidates: []
external_playbook: null
external_playbook_candidates: []
```

At runtime, convert `conditional_external` into `PROMPT`, `MANUAL`, or `HYBRID` after checking tools, files, accounts, real-world operations, and return evidence.

When multiple external playbooks are declared, keep `external_playbook` as the default and select one item from `external_playbook_candidates` after identifying the actual evidence source.

Every stage must end with:

- a next-stage Prompt after passage;
- a repair Prompt after partial passage or failure;
- or a manual/hybrid action guide when external evidence is required.
