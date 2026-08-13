# Literature Search and Verification

## Use for

Topic reconnaissance, benchmark-paper discovery, systematic search, citation verification, bibliography export, deduplication, research-gap support, and literature matrices.

## Intake

Determine:

- research question and scope;
- discipline and likely databases;
- date, language, document-type, population, or method limits;
- whether the user needs representative papers, a reproducible review search, or citation verification;
- accessible tools and institutional databases.

## Search workflow

1. Convert the research question into concept blocks.
2. Add controlled terms, synonyms, spelling variants, abbreviations, and cautious wildcards.
3. Build a broad discovery query and a narrower confirmation query.
4. Route to appropriate sources:
   - biomedical: PubMed and relevant registries;
   - multidisciplinary: Crossref, OpenAlex, Web of Science, or Scopus;
   - computing: IEEE Xplore, ACM Digital Library, arXiv as a preprint source;
   - Chinese literature: CNKI or appropriate Chinese databases;
   - target-journal evidence: the journal or publisher's official site.
5. Record database, platform, query, date, filters, and hit count.
6. Verify title, authors, year, venue, DOI, article status, and direct relevance.
7. Deduplicate by DOI, then normalized title, then author-year-title comparison.
8. Label relevance:
   - `精确同方向`
   - `同领域近似`
   - `仅作类型示例`
9. Separate verified findings from a proposed research gap.

## Output contract

Return as applicable:

- concept table and search strings;
- database and filter plan;
- verified core-paper table;
- deduplication summary;
- literature classification matrix;
- candidate gap statements with evidence strength;
- export-ready citation file guidance.

## Systematic-review boundary

Do not call a search systematic unless databases, dates, complete queries, filters, inclusion/exclusion rules, deduplication, and screening records are documented.

## Manual or hybrid switch

When institutional login or batch export is required, load `references/action-playbooks/literature-database-export.md`. Provide exact steps and a return Prompt. Never stop at “download CSV”.

## Integrity

Do not invent bibliographic fields. Distinguish peer-reviewed articles, preprints, conference papers, editorials, corrections, and retractions.
