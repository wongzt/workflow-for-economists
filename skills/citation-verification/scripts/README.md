# Citation Verification Scripts

These scripts provide a lightweight DOI-first verification path for economics references.

## Included Scripts

- `verify-citations.py`: verify BibTeX entries against Crossref or OpenAlex metadata
- `api-clients.py`: small client layer for metadata lookup
- `format-checker.py`: format checks for BibTeX and LaTeX references

## Intended Use

- batch cleanup of a bibliography
- cross-checking title, author, year, and DOI fields
- identifying likely version mismatches

## Main Principle

The scripts are helpers. Final citation judgment still belongs to the economics workflow in `citation-verification` and `paper-writing`.
