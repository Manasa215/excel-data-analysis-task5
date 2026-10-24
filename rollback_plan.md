# Rollback / Recovery Evidence

## Recovery objective
Restore the last known good workbook without altering the source dataset.

## Baseline artifacts
- Source CSV: `data/retail_sales_sample.csv`
- Workbook: `Excel_Data_Analysis_Task5.xlsx`
- Git baseline: the first commit containing these files

## Rollback steps
1. If the workbook is corrupted or formulas are overwritten, do not overwrite the source CSV.
2. In GitHub, open the repository history and restore/download the last known good version of `Excel_Data_Analysis_Task5.xlsx`, or locally run `git checkout <known-good-commit> -- Excel_Data_Analysis_Task5.xlsx`.
3. If no valid workbook remains, rebuild the workbook from the preserved source CSV using the documented sheet structure and formulas.
4. Open the restored workbook in Excel and check the KPI cards, five summary tables, and charts.
5. Commit the recovered workbook with a message such as `Restore validated Excel workbook`.

## Evidence status
This file documents the rollback procedure and identifies the preserved baseline artifacts. It is not a screenshot of an executed rollback test. To provide actual execution evidence, make a copy of the workbook, change a harmless cell, restore the original from Git, and capture screenshots of the before/after state and Git history.
