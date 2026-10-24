import pandas as pd
from pathlib import Path

path = Path("data/retail_sales_sample.csv")
df = pd.read_csv(path, parse_dates=["Order_Date"])
checks = {
    "records": len(df) == 1000,
    "unique_order_ids": df["Order_ID"].is_unique,
    "no_missing_values": not df.isna().any().any(),
    "valid_dates": df["Order_Date"].notna().all(),
    "nonnegative_quantity": (df["Quantity"] >= 0).all(),
    "sales_and_profit_present": df[["Sales_Revenue", "Profit"]].notna().all().all(),
}
for name, passed in checks.items():
    print(f"{name}: {'PASS' if passed else 'FAIL'}")
if not all(checks.values()):
    raise SystemExit("Dataset validation failed")
print("All dataset validation checks passed.")
