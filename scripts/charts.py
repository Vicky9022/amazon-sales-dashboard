import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

# ── Paths ─────────────────────────────────────────────────────
BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLEANED_PATH = os.path.join(BASE_DIR, 'output', 'cleaned_data', 'cleaned_orders.csv')
CHARTS_DIR  = os.path.join(BASE_DIR, 'output', 'charts')
os.makedirs(CHARTS_DIR, exist_ok=True)

# ── Load data ──────────────────────────────────────────────────
df = pd.read_csv(CLEANED_PATH)
df['date'] = pd.to_datetime(df['date'])

# ── Style ──────────────────────────────────────────────────────
plt.rcParams.update({
    'figure.facecolor' : '#0F1117',
    'axes.facecolor'   : '#0F1117',
    'axes.edgecolor'   : '#2a2d3e',
    'axes.labelcolor'  : '#c0c0c0',
    'text.color'       : '#c0c0c0',
    'xtick.color'      : '#c0c0c0',
    'ytick.color'      : '#c0c0c0',
    'grid.color'       : '#1e2130',
    'grid.linestyle'   : '--',
    'font.family'      : 'sans-serif',
    'font.size'        : 11,
})

ACCENT   = '#00D4FF'
ACCENT2  = '#FF6B6B'
ACCENT3  = '#FFD93D'
ACCENT4  = '#6BCB77'
BAR_GRAD = ['#00D4FF','#00B4E6','#0094CC','#0074B3','#005499',
            '#003480','#001466','#00044C','#000433','#00031A']

def save(name):
    path = os.path.join(CHARTS_DIR, name)
    plt.savefig(path, dpi=150, bbox_inches='tight',
                facecolor='#0F1117')
    print(f"✔ Saved → output/charts/{name}")
    plt.close()

print("=" * 50)
print("Building charts...")
print("=" * 50)

# ══ CHART 1 — Monthly Revenue Trend ══════════════════════
monthly = (df.groupby(['month_num','month'])['amount']
             .sum().reset_index().sort_values('month_num'))
monthly = monthly[monthly['month_num'] != 3]   # drop incomplete March

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(monthly['month'], monthly['amount']/1e6,
        color=ACCENT, linewidth=2.5, marker='o',
        markersize=8, markerfacecolor=ACCENT3)
ax.fill_between(monthly['month'], monthly['amount']/1e6,
                alpha=0.15, color=ACCENT)
for _, row in monthly.iterrows():
    ax.annotate(f"₹{row['amount']/1e6:.2f}M",
                (row['month'], row['amount']/1e6),
                textcoords="offset points", xytext=(0,12),
                ha='center', fontsize=10, color=ACCENT3)
ax.set_title('Monthly Revenue Trend (Apr–Jun 2022)',
             fontsize=14, color='white', pad=15)
ax.set_ylabel('Revenue (₹ Millions)')
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('₹%.1fM'))
ax.grid(True, axis='y')
ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
save('01_monthly_revenue_trend.png')

# ══ CHART 2 — Top 10 States ═══════════════════════════════
top_states = (df.groupby('ship_state')['amount']
                .sum().sort_values(ascending=False).head(10))

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(top_states.index[::-1],
               top_states.values[::-1]/1e6,
               color=BAR_GRAD[::-1], height=0.6)
for bar, val in zip(bars, top_states.values[::-1]):
    ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
            f'₹{val/1e6:.2f}M', va='center', fontsize=9, color='#c0c0c0')
ax.set_title('Top 10 States by Revenue', fontsize=14,
             color='white', pad=15)
ax.set_xlabel('Revenue (₹ Millions)')
ax.xaxis.set_major_formatter(mticker.FormatStrFormatter('₹%.1fM'))
ax.grid(True, axis='x')
ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
save('02_top10_states.png')

# ══ CHART 3 — Category Revenue ════════════════════════════
cat_rev = (df.groupby('category')['amount']
             .sum().sort_values(ascending=False))
colors  = [ACCENT, ACCENT2, ACCENT3, ACCENT4,
           '#A78BFA','#F97316','#EC4899','#14B8A6','#F59E0B']

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(cat_rev.index, cat_rev.values/1e6,
              color=colors[:len(cat_rev)], width=0.6)
for bar, val in zip(bars, cat_rev.values):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.3,
            f'₹{val/1e6:.1f}M', ha='center',
            fontsize=9, color='#c0c0c0')
ax.set_title('Revenue by Category', fontsize=14,
             color='white', pad=15)
ax.set_ylabel('Revenue (₹ Millions)')
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('₹%.0fM'))
plt.xticks(rotation=30, ha='right')
ax.grid(True, axis='y')
ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
save('03_category_revenue.png')

# ══ CHART 4 — Order Status Donut ══════════════════════════
status = df['status'].value_counts()
top5   = status.head(5)
other  = pd.Series({'Other': status.iloc[5:].sum()})
pie_data = pd.concat([top5, other])
pie_colors = [ACCENT, ACCENT4, ACCENT2, ACCENT3,
              '#A78BFA','#94A3B8']

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    pie_data.values,
    labels=pie_data.index,
    colors=pie_colors,
    autopct='%1.1f%%',
    pctdistance=0.75,
    wedgeprops=dict(width=0.55, edgecolor='#0F1117', linewidth=2),
    startangle=90)
for t in texts:
    t.set_color('#c0c0c0')
    t.set_fontsize(10)
for at in autotexts:
    at.set_color('white')
    at.set_fontsize(9)
    at.set_fontweight('bold')
ax.text(0, 0, f'{len(df):,}\nOrders', ha='center',
        va='center', fontsize=13, color='white', fontweight='bold')
ax.set_title('Order Status Breakdown', fontsize=14,
             color='white', pad=20)
fig.tight_layout()
save('04_order_status_donut.png')

# ══ CHART 5 — B2B vs B2C ══════════════════════════════════
b2b_rev = df.groupby('b2b')['amount'].sum()
labels  = ['B2C', 'B2B']
values  = [b2b_rev[False], b2b_rev[True]]
clrs    = [ACCENT, ACCENT2]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
# Revenue pie
ax1.pie(values, labels=labels, colors=clrs,
        autopct='%1.1f%%', startangle=90,
        wedgeprops=dict(edgecolor='#0F1117', linewidth=2))
ax1.set_title('Revenue Split', color='white')

# Orders bar
b2b_orders = df.groupby('b2b')['order_id'].count()
ax2.bar(labels, [b2b_orders[False], b2b_orders[True]],
        color=clrs, width=0.4)
ax2.set_title('Order Count Split', color='white')
ax2.set_ylabel('Number of Orders')
ax2.yaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
ax2.grid(True, axis='y')
ax2.spines[['top','right']].set_visible(False)
fig.suptitle('B2B vs B2C Analysis', fontsize=14,
             color='white', y=1.01)
fig.tight_layout()
save('05_b2b_vs_b2c.png')

# ══ CHART 6 — Top 10 Cities ═══════════════════════════════
top_cities = (df.groupby('ship_city')['amount']
                .sum().sort_values(ascending=False).head(10))

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(top_cities.index[::-1],
               top_cities.values[::-1]/1e6,
               color=ACCENT4, height=0.6)
for bar, val in zip(bars, top_cities.values[::-1]):
    ax.text(bar.get_width() + 0.02,
            bar.get_y() + bar.get_height()/2,
            f'₹{val/1e6:.2f}M', va='center',
            fontsize=9, color='#c0c0c0')
ax.set_title('Top 10 Cities by Revenue', fontsize=14,
             color='white', pad=15)
ax.set_xlabel('Revenue (₹ Millions)')
ax.xaxis.set_major_formatter(
    mticker.FormatStrFormatter('₹%.1fM'))
ax.grid(True, axis='x')
ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
save('06_top10_cities.png')

print("=" * 50)
print("✅ ALL 6 CHARTS SAVED TO output/charts/")
print("=" * 50)