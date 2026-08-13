# Manuscript Writing

## Use for

Planning, drafting, restructuring, or packaging manuscript sections and first-submission materials.

## Evidence before prose

Before drafting, inventory:

- research question;
- approved contribution;
- supporting results or source materials;
- allowed causal strength;
- target audience and journal;
- missing evidence.

Do not fill missing results, citations, statistics, or journal rules with plausible prose.

## Section contract

For each requested section define:

- purpose;
- input evidence;
- allowed claims;
- forbidden claims;
- paragraph sequence;
- links to figures/tables;
- completion check.

## Figure-location proposals

While drafting or restructuring, actively identify locations where a result, explanatory, or enhancement figure could improve the paper. Do not silently add or suppress the figure.

At the exact location, insert `templates/figure-proposal-card.md` or its compact in-manuscript marker. State what will be shown, why it belongs there, how it should be decomposed, what materials are required, and whether the route is Python/R result plotting, code-native explanation, or reference-figure adaptation.

For complex algorithms or experiments, propose an overview plus module- or step-level panels instead of assuming one image can explain everything. Give the user split, merge, defer, decline, and reference-upload choices.

Do not render explanatory or enhancement figures before user approval. Do not accept or insert any rendered figure before the post-render review card is approved.

## Section logic

- Title: specific problem, object, and contribution without promotional wording.
- Abstract: problem, gap, method, evidence, result, bounded contribution.
- Introduction: context -> unresolved problem -> precise gap -> approach -> contribution.
- Related work: synthesis by problem or method, not one-paper-per-paragraph.
- Methods: reproducible decisions, data, modules, parameters, and validation route.
- Results: observations first; interpretation only where signposted.
- Discussion: explain meaning, compare with literature, limits, implications, and alternatives.
- Conclusion: answer the research question without adding new evidence.

## Chinese-to-English drafting

Preserve scientific commitment and terminology. Avoid upgrading:

- may -> demonstrates;
- associated with -> causes;
- internal validation -> generalizable performance;
- preliminary result -> established conclusion.

## Output

Return the requested draft plus:

- claim-evidence notes;
- placeholders requiring author input;
- terminology updates;
- reviewer-risk items;
- visible figure-location proposals and their approval status;
- the appropriate stage action card.
