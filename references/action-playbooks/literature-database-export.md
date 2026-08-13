# Literature Database Search and Export

Use when the user must access an authenticated database, execute a reproducible search, or export records for later processing.

## Select the database

Choose from the user's discipline and access:

- PubMed for biomedical literature;
- Web of Science Core Collection or Scopus for multidisciplinary citation-indexed literature;
- IEEE Xplore or ACM Digital Library for engineering and computing;
- CNKI for Chinese literature;
- a field-specific database when justified.

If the user does not know which database to use, recommend one primary and one backup with reasons. Do not ask them to choose from an unexplained list.

## Before the user clicks

Generate:

- concept blocks;
- copyable database-specific query;
- field choice such as topic/title/abstract/keyword;
- date, language, document-type, and subject filters;
- inclusion/exclusion draft;
- planned export fields.

## Step-by-step guide

When current web access is available, verify the database's official current interface before naming buttons.

Then tell the user:

1. Open the exact database landing page or institutional library entry.
2. Sign in through the permitted institutional or personal route.
3. Open basic or advanced search and explain which to use.
4. Select the specified field.
5. Paste the exact query.
6. Apply each filter separately and record it.
7. Run the search and record the total hit count.
8. Inspect a small sample to test relevance before bulk export.
9. Adjust the query only with a documented reason.
10. Export all eligible records in supported batches.

## Required record

Ask the user to save:

```text
数据库：
检索日期：
完整检索式：
检索字段：
筛选条件：
检索结果总数：
导出批次：
```

## Export

Prefer CSV, RIS, BibTeX, NBIB, or the database's complete-record format. Request title, authors, year, abstract, keywords, DOI, journal/source, affiliations, document type, cited references, and citation count when available and allowed.

For batch limits use:

```text
DATABASE_TOPIC_YYYYMMDD_batch01.csv
DATABASE_TOPIC_YYYYMMDD_batch02.csv
```

Never ask the user to copy thousands of records into chat.

## Completion evidence

- search record;
- hit count before and after filters;
- all exported files;
- screenshot only when the interface or error needs diagnosis.

## Common failures

- Login loop: return to the institutional library entry and confirm the licensed database.
- Query syntax error: test concept blocks separately and escape platform-specific operators.
- Too many results: narrow one concept or field, not arbitrary year trimming.
- Too few results: remove the most restrictive concept, check synonyms, and inspect spelling.
- Export limit: split consecutive ranges without overlap and record batch boundaries.

## Return

Ask the user to upload every batch and send the return Prompt from `templates/return-to-agent-prompt.md`. Continue with merge, deduplication, screening, coding, and stage review.
