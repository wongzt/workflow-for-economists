# AGENTS.project.md - Private Empirical Project Guide

This is a private research project. Treat the public workflow repository as the reusable method layer and this directory as the project-specific research space.

## Workflow Source

Public workflow repository:

```text
{{WORKFLOW_REPO_PATH}}
```

Read the public workflow `AGENTS.md` first, then apply the project-specific rules below.

## Project Rules

- Keep all project-specific inputs, code, logs, outputs, memos, and drafts inside this private project directory.
- Do not write real research data, confidential outputs, or manuscript drafts back into the public workflow repository.
- Use relative paths inside this project whenever possible.
- Save all numerical-result evidence under `logs/` or `output/tables/`.
- Do not state coefficients, standard errors, sample sizes, descriptive statistics, or p-values without a current log or output table.
- Write new Stata comments in Chinese unless the user asks otherwise.
- Use Good Question Cards before empirical work when the research question is still broad, gap-based, proposal-shaped, or competing with other ideas.
- Record major research-design decisions under `quality_reports/decisions/`.
- For manuscript-facing work, maintain claim provenance under `quality_reports/passports/`.

## Recommended Session Order

1. Good Question Card.
2. Requirements spec, if the task is ambiguous.
3. Data audit and codebook notes.
4. Analysis plan and regression-spec matrix.
5. Stata do-file execution.
6. Log verification.
7. Results analysis and theory/story diagnostics.
8. Paper writing, QA, or response work.
