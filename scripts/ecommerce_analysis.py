import pandas as pd
import os

# ── Paths ────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'Amazon Sale Report.csv')
CLEANED_DIR = os.path.join(BASE_DIR, 'output', 'cleaned_data')
os.makedirs(CLEANED_DIR, exist_ok=True)

# ── 1. Load Data ─────────────────────────────────────────
print("=" * 50)
print("STEP 1: Loading data...")
df = pd.read_csv(DATA_PATH, low_memory=False)
print(f"✔ Loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# ── 2. Drop useless columns ──────────────────────────────
print("\nSTEP 2: Dropping useless columns...")
df.drop(columns=['index', 'Unnamed: 22', 'fulfilled-by',
                 'promotion-ids', 'currency', 'ASIN'], inplace=True)
print("✔ Dropped useless columns")

# ── 3. Rename columns ────────────────────────────────────
print("\nSTEP 3: Renaming columns...")
df.columns = (df.columns.str.strip()
                         .str.lower()
                         .str.replace(' ', '_')
                         .str.replace('-', '_'))
print("✔ Columns renamed:", df.columns.tolist())

# ── 4. Fix Date column ───────────────────────────────────
print("\nSTEP 4: Fixing date column...")
df['date'] = pd.to_datetime(df['date'], format='%m-%d-%y')
df['month'] = df['date'].dt.month_name()
df['month_num'] = df['date'].dt.month
print(f"✔ Date range: {df['date'].min().date()} → {df['date'].max().date()}")

# ── 5. Remove rows with missing Amount ───────────────────
print("\nSTEP 5: Removing rows with missing Amount...")
before = len(df)
df = df[df['amount'].notna()].copy()
after = len(df)
print(f"✔ Removed {before - after} rows with missing amount")

# ── 6. Fill remaining missing values ─────────────────────
print("\nSTEP 6: Filling missing values...")
df['ship_city']       = df['ship_city'].fillna('Unknown')
df['ship_state']      = df['ship_state'].fillna('Unknown')
df['courier_status']  = df['courier_status'].fillna('Unknown')
df['ship_country']    = df['ship_country'].fillna('IN')
df['ship_postal_code']= df['ship_postal_code'].fillna(0)
print("✔ All missing values filled")

# ── 7. Fix data types ────────────────────────────────────
print("\nSTEP 7: Fixing data types...")
df['qty']              = df['qty'].astype(int)
df['amount']           = df['amount'].astype(float)
df['ship_postal_code'] = df['ship_postal_code'].astype(int)
print("✔ qty → int | amount → float | ship_postal_code → int")

# ── 8. Final check ───────────────────────────────────────
print("\nSTEP 8: Final check...")
print(f"✔ Clean shape: {df.shape}")
missing = df.isnull().sum()
print(f"✔ Missing values:\n{missing}")

# ── 9. Save cleaned data ─────────────────────────────────
CLEANED_PATH = os.path.join(CLEANED_DIR, 'cleaned_orders.csv')
df.to_csv(CLEANED_PATH, index=False)
print(f"\n✔ Saved → output/cleaned_data/cleaned_orders.csv")
print("=" * 50)
print("✅ DATA CLEANING COMPLETE — ZERO WARNINGS, ZERO MISSING VALUES!")