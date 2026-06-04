---
name: citation-verification
description: Use when the user needs to verify citations for an empirical economics paper, distinguish working-paper and published versions, check journal metadata, confirm DOI information, or prevent invented references.
tags: [Economics, Citation, Verification, Journals, Working Papers]
version: 0.3.0
---

# Citation Verification for Empirical Economics

Use this skill to verify citations for economics papers, referee responses, and appendices.

## Default Source Hierarchy

Prefer sources in this order unless the user asks otherwise:

1. publisher page or DOI landing page
2. `AEA`, `Econometrica`, `QJE`, `JPE`, `ReStud`, `EJ`, `JPubE`, `JHR`, `AEJ`, and field-journal websites
3. `NBER`, `RePEc`, `IDEAS`, `IZA`, `CEPR`, `SSRN`
4. `Google Scholar` as a search aid
5. a preprint source only as a clearly marked fallback

## What To Verify

- the paper exists
- title, authors, year, and venue match
- working-paper versus published version is correctly identified
- DOI or stable URL is available
- the cited claim is actually supported by the cited source when the paper relies on a specific result

## Working-Paper Rules

- cite the published version when it exists and is the version the argument relies on
- mention the working-paper series when the discussion is explicitly about the working-paper stage or the published version does not exist
- do not collapse `NBER`, `IZA`, `CEPR`, `SSRN`, and journal metadata into one record

## Failure Handling

If verification fails:

- do not guess
- mark the citation as unresolved
- explain whether the problem is missing paper, conflicting metadata, or unclear versioning

## Integration

This skill supports:

- `paper-writing`
- `review-response`
- `paper-self-review`
- `qa-paper`
- `qa-response`
