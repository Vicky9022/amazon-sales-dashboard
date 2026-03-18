# 📊 Amazon E-Commerce Sales Dashboard

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green?style=flat&logo=pandas)
![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?style=flat&logo=powerbi)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat)

> **End-to-end data analytics project** analyzing **1,21,180 Amazon orders** worth **₹7.8 Crore** using Python and Power BI — built as part of a Data Analytics Portfolio.

---

## 🎯 Project Summary

| Detail | Info |
|--------|------|
| 📦 Dataset | Amazon Sales Report (India) |
| 📅 Time Period | April – June 2022 |
| 🔢 Total Records | 1,21,180 cleaned orders |
| 💰 Total Revenue | ₹7,85,92,678 (₹7.8 Crore) |
| 🛠️ Tools Used | Python, Pandas, Matplotlib, Seaborn, Power BI |
| 📁 Output | Interactive Dashboard + 6 Charts + KPI Report |

---

## 📌 Problem Statement

A fashion e-commerce business on Amazon India needed clarity on:

- Is revenue **growing or declining** month over month?
- Which **states and cities** drive the most revenue?
- Which **product categories** are most profitable?
- How big is the **cancellation and return problem**?
- What is the **B2B vs B2C** revenue split?

The raw data had **1,28,975 messy records** with missing values, wrong data types, and no analysis structure. This project builds a complete analytics pipeline to answer all of the above.

---

## 💡 Key Business Insights

### 📉 Insight 1 — Revenue is Declining
> Revenue dropped **19% in just 3 months**
> - April 2022 → ₹2.88 Crore (peak)
> - May 2022 → ₹2.62 Crore (-9%)
> - June 2022 → ₹2.34 Crore (-11%)

### 🗺️ Insight 2 — Geographic Concentration Risk
> **Top 3 states drive 39% of all revenue**
> - Maharashtra → ₹1.33 Crore (17%)
> - Karnataka → ₹1.05 Crore (13%)
> - Telangana → ₹0.69 Crore (9%)

### 🛍️ Insight 3 — Category Dependency Risk
> **Just 2 categories = 77% of revenue**
> - "Set" → ₹3.92 Crore (50%)
> - "Kurta" → ₹2.13 Crore (27%)

### ⚠️ Insight 4 — Cancellation is a Major Problem
> **10.49% of all orders never complete**
> - Cancellation rate → 8.88% (10,766 orders)
> - Return rate → 1.61% (1,950 orders)
> - Estimated lost revenue → ₹82 Lakhs+

### 🏢 Insight 5 — B2B Untapped Opportunity
> B2B is only **0.75% of revenue** (₹5.91 Lakhs)
> Huge potential for wholesale and bulk sales expansion

---

## 📊 Dashboard Preview

The Power BI dashboard includes:

| Visual | Description |
|--------|-------------|
| 💳 KPI Card 1 | Total Revenue — ₹78.59M |
| 💳 KPI Card 2 | Total Orders — 1,13,030 |
| 💳 KPI Card 3 | Avg Order Value — ₹648 |
| 💳 KPI Card 4 | Cancelled Orders — 11K |
| 📈 Line Chart | Monthly Revenue Trend (Apr–Jun) |
| 📊 Bar Chart | Top 10 States by Revenue |
| 📊 Bar Chart | Revenue by Category |
| 🍩 Donut Chart | Order Status Breakdown |
| 📊 Bar Chart | Top 10 Cities by Revenue |

---

## 📁 Folder Structure

```
amazon-sales-dashboard/
│
├── README.md                             ← You are here
├── case_study.html                       ← Full project case study
│
├── data/
│   └── Amazon Sale Report.csv           ← Raw dataset (1,28,975 rows)
│
├── scripts/
│   ├── ecommerce_analysis.py            ← Step 1: Data cleaning
│   ├── kpi_analysis.py                  ← Step 2: KPI calculations
│   ├── charts.py                        ← Step 3: Chart generation
│   └── export_for_powerbi.py            ← Step 4: Power BI export
│
├── output/
│   ├── charts/
│   │   ├── 01_monthly_revenue_trend.png
│   │   ├── 02_top10_states.png
│   │   ├── 03_category_revenue.png
│   │   ├── 04_order_status_donut.png
│   │   ├── 05_b2b_vs_b2c.png
│   │   └── 06_top10_cities.png
│   │
│   └── cleaned_data/
│       ├── cleaned_orders.csv           ← Cleaned dataset (1,21,180 rows)
│       └── powerbi_data.xlsx            ← Power BI ready Excel file
│
└── dashboard/
    └── Amazon_Sales_Dashboard.pbix      ← Final Power BI dashboard
```

---

## 🔧 How to Run This Project

### Prerequisites
```bash
pip install pandas matplotlib seaborn openpyxl
```

### Step 1 — Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/amazon-sales-dashboard.git
cd amazon-sales-dashboard
```

### Step 2 — Clean the data
```bash
python scripts/ecommerce_analysis.py
```
Output: `output/cleaned_data/cleaned_orders.csv`

### Step 3 — Run KPI analysis
```bash
python scripts/kpi_analysis.py
```
Output: Full KPI report printed in terminal

### Step 4 — Generate charts
```bash
python scripts/charts.py
```
Output: 6 PNG charts saved in `output/charts/`

### Step 5 — Export for Power BI
```bash
python scripts/export_for_powerbi.py
```
Output: `output/cleaned_data/powerbi_data.xlsx`

### Step 6 — Open the dashboard
```
Open dashboard/Amazon_Sales_Dashboard.pbix in Power BI Desktop
```

---

## 📈 KPI Report Output

```
==================================================
         AMAZON SALES — KPI REPORT
==================================================

📦 KPI 1 — OVERALL SUMMARY
   Total Revenue    : ₹78,592,678.30
   Total Orders     : 113,030
   Avg Order Value  : ₹695.33

📅 KPI 2 — MONTHLY REVENUE TREND
   April        ₹  28,838,708.32  ████████████████████
   May          ₹  26,226,476.75  ██████████████████
   June         ₹  23,425,809.38  ████████████████

🗺️  KPI 3 — TOP 10 STATES BY REVENUE
   MAHARASHTRA                    ₹13,335,534.14
   KARNATAKA                      ₹10,481,114.37
   TELANGANA                      ₹ 6,916,615.65
   UTTAR PRADESH                  ₹ 6,816,642.08
   TAMIL NADU                     ₹ 6,515,650.11

🛍️  KPI 4 — CATEGORY PERFORMANCE
   Set           Revenue: ₹39,204,124   Orders: 47,042
   Kurta         Revenue: ₹21,299,546   Orders: 46,717
   Western Dress Revenue: ₹11,216,072   Orders: 14,704
   Top           Revenue: ₹ 5,347,792   Orders: 10,165

📋 KPI 5 — ORDER STATUS
   Shipped                        77,596  (64.03%)
   Shipped - Delivered to Buyer   28,761  (23.73%)
   Cancelled                      10,766  ( 8.88%)
   Shipped - Returned to Seller    1,950  ( 1.61%)

🏢 KPI 6 — B2B vs B2C
   B2C  Revenue: ₹78,001,457   Orders: 1,20,337
   B2B  Revenue: ₹   591,220   Orders:      843
==================================================
```

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| Python 3.x | Core programming language |
| Pandas | Data cleaning and analysis |
| Matplotlib | Chart generation |
| Seaborn | Chart styling |
| OpenPyXL | Excel file export |
| Power BI Desktop | Interactive dashboard |

---

## 📄 Resume Bullet Points

Copy and paste these directly on your resume:

- Built end-to-end Amazon Sales Analytics dashboard analyzing **1,21,180 orders worth ₹7.8 Crore** using Python and Power BI
- Cleaned and processed raw dataset of **1,28,975 records** — removed duplicates, fixed data types, handled missing values achieving zero data quality issues
- Identified **19% month-over-month revenue decline** from April to June 2022 using Python trend analysis
- Discovered **8.88% cancellation rate** representing ₹82L+ in potential lost revenue — flagged as critical business risk
- Revealed geographic concentration risk — **top 3 states drive 39%** of all revenue across 69 states
- Built interactive Power BI dashboard with **5 visualizations and 4 KPI cards** for business stakeholders
- Automated full data pipeline: raw CSV → data cleaning → KPI analysis → charts → Power BI using Python scripts

---

## 🔗 Connect With Me

- 💼 LinkedIn: [Your LinkedIn URL here]
- 📧 Email: [Your Email here]
- 🐙 GitHub: [Your GitHub URL here]

---

⭐ **If you found this project helpful, please give it a star!**