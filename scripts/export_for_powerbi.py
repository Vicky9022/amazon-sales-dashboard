import pandas as pd
import os

# ── Paths ────────────────────────────────────────────────
BASE_DIR     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLEANED_PATH = os.path.join(BASE_DIR, 'output', 'cleaned_data', 'cleaned_orders.csv')
EXPORT_DIR   = os.path.join(BASE_DIR, 'output', 'cleaned_data')

# ── Load cleaned data ────────────────────────────────────
df = pd.read_csv(CLEANED_PATH)
df['date'] = pd.to_datetime(df['date'])

# ── Build summary tables for Power BI ───────────────────
monthly = (df.groupby(['month_num', 'month'])
             .agg(revenue=('amount','sum'), orders=('order_id','count'))
             .reset_index().sort_values('month_num'))

state_rev = (df.groupby('ship_state')
               .agg(revenue=('amount','sum'), orders=('order_id','count'))
               .reset_index().sort_values('revenue', ascending=False))

category = (df.groupby('category')
              .agg(revenue=('amount','sum'), orders=('order_id','count'))
              .reset_index().sort_values('revenue', ascending=False))

status = (df.groupby('status')
            .agg(orders=('order_id','count'))
            .reset_index().sort_values('orders', ascending=False))

city_rev = (df.groupby('ship_city')
              .agg(revenue=('amount','sum'), orders=('order_id','count'))
              .reset_index().sort_values('revenue', ascending=False).head(20))

# ── Export to Excel with multiple sheets ────────────────
EXCEL_PATH = os.path.join(EXPORT_DIR, 'powerbi_data.xlsx')

print("=" * 50)
print("Exporting data for Power BI...")

with pd.ExcelWriter(EXCEL_PATH, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='All Orders', index=False)
    monthly.to_excel(writer, sheet_name='Monthly Revenue', index=False)
    state_rev.to_excel(writer, sheet_name='State Revenue', index=False)
    category.to_excel(writer, sheet_name='Category Revenue', index=False)
    status.to_excel(writer, sheet_name='Order Status', index=False)
    city_rev.to_excel(writer, sheet_name='Top 20 Cities', index=False)

print(f"✔ Excel file saved → output/cleaned_data/powerbi_data.xlsx")
print(f"✔ Sheets created:")
print(f"   - All Orders ({len(df):,} rows)")
print(f"   - Monthly Revenue ({len(monthly)} rows)")
print(f"   - State Revenue ({len(state_rev)} rows)")
print(f"   - Category Revenue ({len(category)} rows)")
print(f"   - Order Status ({len(status)} rows)")
print(f"   - Top 20 Cities ({len(city_rev)} rows)")
print("=" * 50)
print("✅ EXPORT COMPLETE — Ready for Power BI!")