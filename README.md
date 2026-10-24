# Excel Data Analysis — Veda Technology Task 5

## Project overview
This repository contains an end-to-end Excel retail sales analysis example using a generated sample dataset of 1,000 orders. It demonstrates raw-data preservation, formula-based analysis, KPI reporting, business summaries, sorting/filtering, and visualizations.

> **Data note:** The dataset is synthetic and generated for practice. Findings are illustrative, not claims about a real company.

## Repository contents
- `Excel_Data_Analysis_Task5.xlsx` — workbook with `Raw_Data`, `Working_Analysis`, and `Summary` tabs.
- `data/retail_sales_sample.csv` — source dataset in CSV format.
- `FINDINGS_SUMMARY.md` — one-paragraph findings summary.
- `evidence/quality_report.json` — dataset quality checks.
- `evidence/rollback_plan.md` — rollback and recovery evidence/steps.
- `deployment/deployment_config.yml` — lightweight project configuration and validation checklist.
- `requirements.txt` — optional Python packages for regenerating/checking the sample data.

## Workbook guide
1. **Raw_Data:** original source rows, formatted as an Excel Table (`RetailRawData`); do not edit this tab during analysis.
2. **Working_Analysis:** formula-linked fields plus `Month`, `Profit_Margin`, and `Average_Order_Value`. It uses Excel formulas so the analysis can be traced to the raw tab.
3. **Summary:** KPI cards and five formula-driven business summary tables: sales by category, region, month, customer segment, and sales channel, with charts.

The summary tables are pivot-style summaries built with `SUMIF`/`COUNTIF` formulas for compatibility. If your reviewer specifically requires native Excel PivotTables, create them in Excel using **Insert → PivotTable** from the `RetailRawData` table; suggested layouts are listed below.

## Business questions answered
- Which product category contributes the most sales and profit?
- Which region has the highest sales?
- How do sales change month by month?
- Which customer segment contributes the most revenue?
- Which sales channel contributes the most revenue?

## Excel formulas demonstrated
- `SUMIF`/`COUNTIF` for grouped summaries (the same approach extends to `SUMIFS`/`COUNTIFS` for multiple criteria).
- `AVERAGE`, `COUNTA`, `IFERROR`, and `TEXT`.
- Calculated fields: profit margin and month.

## Suggested native PivotTables (if required)
Use `Raw_Data` or `Working_Analysis` as the source:
1. **Category performance:** Rows = Category; Values = Sum of Sales_Revenue, Sum of Profit, Count of Order_ID.
2. **Regional performance:** Rows = Region; Values = Sum of Sales_Revenue, Sum of Profit.
3. **Monthly trend:** Rows = Order_Date (group by Months) or Month; Values = Sum of Sales_Revenue.
4. **Customer segment:** Rows = Customer_Segment; Values = Sum of Sales_Revenue.
5. **Sales channel:** Rows = Sales_Channel; Values = Sum of Sales_Revenue, Count of Order_ID.

The source data is formatted as an Excel Table so added rows can be included in PivotTables created from that table. After adding records, use **Data → Refresh All**.

## Run / verify
Open `Excel_Data_Analysis_Task5.xlsx` in Microsoft Excel or upload it to Google Sheets. Excel formulas and charts may recalculate when opened. Review the KPI cards and grouped summaries.

Optional CSV validation:
```bash
pip install -r requirements.txt
python validate_dataset.py
```

## Rollback and recovery
The raw source is separately preserved as `data/retail_sales_sample.csv` and `Raw_Data` in the workbook. If a working formula or summary is accidentally changed, restore the workbook from the last committed Git version or rebuild the workbook from the CSV. See `evidence/rollback_plan.md`.

## Limitations
- The grouped summary tables are formula-driven summaries, not embedded native Excel PivotTable objects.
- Results describe the generated sample dataset only.
