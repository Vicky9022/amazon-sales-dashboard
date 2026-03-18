import pandas as pd
import os

# ── Paths ────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLEANED_PATH = os.path.join(BASE_DIR, 'output', 'cleaned_data', 'cleaned_orders.csv')

# ── Load cleaned data ────────────────────────────────────
df = pd.read_csv(CLEANED_PATH)
df['date'] = pd.to_datetime(df['date'])

print("=" * 55)
print("         AMAZON SALES — KPI REPORT")
print("=" * 55)

# ── KPI 1: Total Revenue ─────────────────────────────────
total_revenue = df['amount'].sum()
total_orders  = df['order_id'].nunique()
avg_order_val = total_revenue / total_orders
print(f"\n📦 KPI 1 — OVERALL SUMMARY")
print(f"   Total Revenue    : ₹{total_revenue:,.2f}")
print(f"   Total Orders     : {total_orders:,}")
print(f"   Avg Order Value  : ₹{avg_order_val:,.2f}")

# ── KPI 2: Monthly Revenue Trend ─────────────────────────
monthly = (df.groupby(['month_num', 'month'])['amount']
             .sum()
             .reset_index()
             .sort_values('month_num'))
print(f"\n📅 KPI 2 — MONTHLY REVENUE TREND")
for _, row in monthly.iterrows():
    bar = '█' * int(row['amount'] / monthly['amount'].max() * 20)
    print(f"   {row['month']:<12} ₹{row['amount']:>15,.2f}  {bar}")

# ── KPI 3: Top 10 States by Revenue ──────────────────────
top_states = (df.groupby('ship_state')['amount']
                .sum()
                .sort_values(ascending=False)
                .head(10))
print(f"\n🗺️  KPI 3 — TOP 10 STATES BY REVENUE")
for state, rev in top_states.items():
    print(f"   {state:<30} ₹{rev:>12,.2f}")

# ── KPI 4: Top Categories by Sales ───────────────────────
top_cats = (df.groupby('category')
              .agg(revenue=('amount','sum'), orders=('order_id','count'))
              .sort_values('revenue', ascending=False))
print(f"\n🛍️  KPI 4 — CATEGORY PERFORMANCE")
for cat, row in top_cats.iterrows():
    print(f"   {cat:<20} Revenue: ₹{row['revenue']:>12,.2f}  Orders: {row['orders']:>6,}")

# ── KPI 5: Order Status Breakdown ────────────────────────
status_counts = df['status'].value_counts()
status_pct    = (status_counts / len(df) * 100).round(2)
print(f"\n📋 KPI 5 — ORDER STATUS BREAKDOWN")
for status, count in status_counts.items():
    print(f"   {status:<30} {count:>6,}  ({status_pct[status]}%)")

# ── KPI 6: B2B vs B2C ────────────────────────────────────
b2b = df.groupby('b2b')['amount'].sum()
b2b_orders = df.groupby('b2b')['order_id'].count()
print(f"\n🏢 KPI 6 — B2B vs B2C")
for key in b2b.index:
    label = 'B2B' if key else 'B2C'
    print(f"   {label}  Revenue: ₹{b2b[key]:>14,.2f}  Orders: {b2b_orders[key]:>6,}")

print("\n" + "=" * 55)
print("✅ KPI ANALYSIS COMPLETE!")
print("=" * 55)