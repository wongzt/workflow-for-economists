# Stata Workflow

Suggested do-file order:

1. `00_globals_and_paths.do`
2. `01_raw_import_and_cleaning.do`
3. `02_merge_and_sample_construction.do`
4. `03_variable_construction.do`
5. `04_descriptives_and_balance.do`
6. `05_main_results.do`
7. `06_robustness.do`
8. `07_heterogeneity_and_mechanisms.do`
9. `08_export_tables_and_figures.do`

For each step, keep:

- a log file
- clear input and output datasets
- notes on destructive versus reversible steps
