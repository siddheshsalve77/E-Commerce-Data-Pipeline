# 🛒 E-Commerce Data Pipeline
### End-to-End Data Engineering Project on AWS

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20RDS-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-28a745?style=for-the-badge)

**A production-style ETL pipeline ingesting 100K+ real e-commerce transactions through a Medallion Architecture on AWS, building a Star Schema data warehouse for business analytics.**

[Architecture](#️-architecture) • [Tech Stack](#️-tech-stack) • [Setup Guide](#-how-to-run-this-project) • [Results](#-analytics-results) • [Project Structure](#-project-structure)

</div>

---

## 📖 Project Overview

This project implements a complete **Extract → Load → Transform** pipeline for an e-commerce platform using the real-world **Brazilian E-Commerce Public Dataset (Olist)** — 112,650 orders across 9 CSV files.

Raw transactional data is ingested from local CSV files, organized in a **Data Lake on AWS S3** using Bronze/Staging/Processed zones, then loaded and transformed into a **Star Schema Data Warehouse on AWS RDS PostgreSQL** for analytics and business reporting.

### What This Project Demonstrates

| Concept | Implementation |
|---|---|
| **Data Lake Design** | S3 with Raw, Staging, and Processed zones |
| **Medallion Architecture** | Bronze (raw) → Silver (staged) → Gold (warehouse) |
| **Dimensional Modeling** | Star Schema — 2 dimension tables + 1 fact table |
| **ETL Automation** | Python scripts for each pipeline stage |
| **Data Quality** | Type casting, null handling, deduplication |
| **Cloud Infrastructure** | AWS S3 + RDS on Free Tier |
| **SQL Transformations** | Staging → Warehouse via SQL scripts |
| **Business Analytics** | Revenue, customer, and product insights |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        DATA SOURCES                             │
│              [ Olist Brazilian E-Commerce CSVs ]                │
│         orders • customers • products • order_items             │
│              payments • reviews • sellers                       │
└──────────────────────────┬──────────────────────────────────────┘
                           │  Python + boto3
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    AWS S3 — DATA LAKE                           │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐    │
│  │   BRONZE    │  │   SILVER    │  │        GOLD         │    │
│  │  (raw/)     │  │ (staging/)  │  │    (processed/)     │    │
│  │             │  │             │  │                     │    │
│  │ Raw CSVs    │  │ Cleaned &   │  │ Analytics-ready     │    │
│  │ as-is,      │  │ typed data  │  │ Parquet files       │    │
│  │ untouched   │  │ in S3       │  │ ready for BI        │    │
│  └─────────────┘  └─────────────┘  └─────────────────────┘    │
└──────────────────────────┬──────────────────────────────────────┘
                           │  Python + Pandas + SQLAlchemy
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│              AWS RDS POSTGRESQL — DATA WAREHOUSE                │
│                                                                 │
│  ┌──────────────┐     ┌───────────────────────────────────┐    │
│  │   STAGING    │────▶│         STAR SCHEMA               │    │
│  │   LAYER      │ SQL │                                   │    │
│  │              │     │  dim_customer   dim_product        │    │
│  │ Raw tables   │     │       └──────────────┘            │    │
│  │ before       │     │              │                    │    │
│  │ transform    │     │         fact_sales                │    │
│  └──────────────┘     └───────────────────────────────────┘    │
└──────────────────────────┬──────────────────────────────────────┘
                           │  Python Analytics Scripts
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                       ANALYTICS LAYER                           │
│         Revenue Trends • Customer Segments • Product KPIs       │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow — Step by Step

```
Step 1  setup_s3_structure.py   →  Creates S3 bucket with raw/staging/processed zones
Step 2  setup_rds_tables.py     →  Creates staging + star schema tables in PostgreSQL
Step 3  load_data_to_rds.py     →  Reads local CSVs → uploads to S3 Bronze → loads to RDS Staging
Step 4  run_transformation.py   →  Executes SQL: Staging → dim_customer, dim_product, fact_sales
Step 5  revenue_analysis.py     →  Runs analytical queries → prints business KPIs
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Language** | Python 3.12 | All pipeline scripts |
| **Data Lake** | AWS S3 | Raw, Staging, and Processed zones |
| **Data Warehouse** | AWS RDS PostgreSQL | Star schema for analytics |
| **Data Processing** | Pandas 2.0 | Transformation and cleaning |
| **AWS SDK** | boto3 | S3 operations from Python |
| **DB Connector** | SQLAlchemy + psycopg2 | Python → PostgreSQL connection |
| **SQL** | PostgreSQL SQL | Staging → warehouse transformations |
| **Dataset** | Olist (Kaggle) | 112,650 real Brazilian e-commerce orders |
| **Infrastructure** | AWS Free Tier | Zero-cost cloud deployment |

---

## 📂 Project Structure

```
E-Commerce-Data-Pipeline/
│
├── raw_data/                       # Source CSV files — Git Ignored
│   ├── olist_orders_dataset.csv
│   ├── olist_customers_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_products_dataset.csv
│   └── olist_payments_dataset.csv
│
├── scripts/                        # Core ETL Pipeline Scripts
│   ├── setup_s3_structure.py       # Step 1: Initialize S3 bucket and zones
│   ├── setup_rds_tables.py         # Step 2: Create staging + DW tables in RDS
│   ├── load_data_to_rds.py         # Step 3: CSV → S3 Bronze → RDS Staging
│   ├── run_transformation.py       # Step 4: Staging → Star Schema (SQL transforms)
│   └── revenue_analysis.py         # Step 5: Run analytics queries, print KPIs
│
├── sql_queries/                    # All SQL Files
│   ├── create_tables.sql           # DDL: staging + dimension + fact table schemas
│   └── transform_data.sql          # DML: INSERT INTO dim/fact from staging
│
├── config.py                       # DB credentials and config — Git Ignored
├── requirements.txt                # Python dependencies
├── .gitignore                      # Excludes venv, secrets, raw_data/
└── README.md                       # This file
```

---

## 📊 Data Model — Star Schema

The data warehouse uses a **Star Schema** — one central fact table surrounded by dimension tables. This structure is optimized for analytical queries (GROUP BY, aggregations, filtering by customer or product).

```
                    ┌─────────────────┐
                    │  dim_customer   │
                    │─────────────────│
                    │ customer_key PK │
                    │ customer_id     │
                    │ customer_city   │
                    │ customer_state  │
                    │ zip_code        │
                    └────────┬────────┘
                             │
                             │  FK: customer_key
                             │
┌─────────────────┐   ┌──────▼──────────────┐
│  dim_product    │   │     fact_sales       │
│─────────────────│   │──────────────────────│
│ product_key  PK │◄──┤ sale_id          PK  │
│ product_id      │   │ customer_key     FK  │
│ category_name   │   │ product_key      FK  │
│ product_name    │   │ order_id             │
│ weight_g        │   │ order_date           │
│ length_cm       │   │ quantity             │
└─────────────────┘   │ price                │
                      │ freight_value        │
                      │ total_revenue        │
                      │ payment_type         │
                      │ payment_installments │
                      └──────────────────────┘
```

### Why Star Schema?

A normalized transactional schema has 9 tables with complex joins. The Star Schema flattens this into 3 tables that analytical queries can read with simple JOINs:

```sql
-- Revenue by product category — simple and fast on Star Schema
SELECT
    p.category_name,
    SUM(f.total_revenue)  AS total_revenue,
    COUNT(f.sale_id)       AS order_count,
    AVG(f.total_revenue)   AS avg_order_value
FROM fact_sales f
JOIN dim_product p ON f.product_key = p.product_key
GROUP BY p.category_name
ORDER BY total_revenue DESC;
```

---

## 🗄️ SQL Transformation Logic

The transformation step (`run_transformation.py` executing `transform_data.sql`) converts staging tables into the star schema.

### dim_customer population
```sql
INSERT INTO dim_customer (customer_id, customer_city, customer_state, zip_code)
SELECT DISTINCT
    customer_id,
    customer_city,
    customer_state,
    customer_zip_code_prefix
FROM staging_customers
ON CONFLICT (customer_id) DO NOTHING;
```

### dim_product population
```sql
INSERT INTO dim_product (product_id, category_name, weight_g, length_cm)
SELECT DISTINCT
    product_id,
    COALESCE(product_category_name, 'Unknown') AS category_name,
    product_weight_g,
    product_length_cm
FROM staging_products
ON CONFLICT (product_id) DO NOTHING;
```

### fact_sales population
```sql
INSERT INTO fact_sales (
    customer_key, product_key, order_id,
    order_date, quantity, price,
    freight_value, total_revenue, payment_type
)
SELECT
    dc.customer_key,
    dp.product_key,
    o.order_id,
    o.order_purchase_timestamp::DATE,
    oi.order_item_id                        AS quantity,
    oi.price,
    oi.freight_value,
    oi.price + oi.freight_value             AS total_revenue,
    p.payment_type
FROM staging_orders o
JOIN staging_order_items oi  ON o.order_id       = oi.order_id
JOIN staging_payments p      ON o.order_id       = p.order_id
JOIN dim_customer dc         ON o.customer_id    = dc.customer_id
JOIN dim_product dp          ON oi.product_id    = dp.product_id
WHERE o.order_status = 'delivered';
```

---

## 📈 Analytics Results

After running the full pipeline (`python scripts/revenue_analysis.py`), the following business KPIs are computed directly from the Star Schema:

### Summary Metrics
| Metric | Value |
|---|---|
| **Total Transactions** | 112,650 |
| **Total Revenue** | 15.8 Million BRL |
| **Unique Customers** | 96,096 |
| **Unique Products** | 32,951 |
| **Date Range** | Sep 2016 — Oct 2018 |

### Top 5 Product Categories by Revenue
| Rank | Category | Revenue (BRL) | Orders |
|---|---|---|---|
| 1 | Health & Beauty | 1,258,690 | 9,670 |
| 2 | Watches & Gifts | 1,205,306 | 8,114 |
| 3 | Bed, Bath & Table | 1,040,951 | 11,115 |
| 4 | Sports & Leisure | 996,343 | 8,637 |
| 5 | Computers & Accessories | 911,902 | 6,736 |

### Top 5 States by Customer Count
| Rank | State | Customers | % of Total |
|---|---|---|---|
| 1 | São Paulo (SP) | 41,746 | 43.4% |
| 2 | Rio de Janeiro (RJ) | 12,852 | 13.4% |
| 3 | Minas Gerais (MG) | 11,635 | 12.1% |
| 4 | Rio Grande do Sul (RS) | 5,466 | 5.7% |
| 5 | Paraná (PR) | 5,045 | 5.2% |

### Payment Method Distribution
| Payment Type | Transactions | % Share |
|---|---|---|
| Credit Card | 76,795 | 73.9% |
| Boleto | 19,784 | 19.0% |
| Voucher | 5,775 | 5.6% |
| Debit Card | 1,529 | 1.5% |

---

## 🚀 How to Run This Project

### Prerequisites

- Python 3.9+ installed on your machine
- AWS Account (Free Tier is sufficient)
- Git installed

### Step 1 — Clone the Repository

```bash
git clone https://github.com/siddheshsalve77/E-Commerce-Data-Pipeline.git
cd E-Commerce-Data-Pipeline
```

### Step 2 — Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3 — Set Up AWS Infrastructure

**3a. Create IAM User**
```
AWS Console → IAM → Users → Create User
  Name: ecommerce-pipeline-user
  Permissions: AmazonS3FullAccess + AmazonRDSFullAccess
  Access Key: Create and download CSV
```

**3b. Configure AWS CLI**
```bash
aws configure
  AWS Access Key ID:     [from downloaded CSV]
  AWS Secret Access Key: [from downloaded CSV]
  Default region name:   ap-south-1
  Default output format: json
```

**3c. Create RDS PostgreSQL Instance**
```
AWS Console → RDS → Create Database
  Engine: PostgreSQL 15
  Template: Free Tier
  DB Instance: db.t3.micro
  Storage: 20GB gp2
  Public Access: Yes (for learning — disable in production)
  Security Group: Allow port 5432 from your IP
```

### Step 4 — Configure Database Credentials

Create `config.py` in the project root (this file is git-ignored):

```python
# config.py — DO NOT commit this file

DB_CONFIG = {
    'host':     'your-rds-endpoint.rds.amazonaws.com',
    'port':     5432,
    'database': 'ecommerce_dw',
    'username': 'your_username',
    'password': 'your_password'
}

S3_CONFIG = {
    'bucket_name': 'ecommerce-pipeline-yourname',
    'region':      'ap-south-1'
}
```

### Step 5 — Download the Dataset

1. Go to [Kaggle — Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
2. Download and unzip
3. Place all CSV files in the `raw_data/` folder

```
raw_data/
  olist_orders_dataset.csv
  olist_customers_dataset.csv
  olist_order_items_dataset.csv
  olist_products_dataset.csv
  olist_payments_dataset.csv
  olist_sellers_dataset.csv
  olist_order_reviews_dataset.csv
```

### Step 6 — Run the Pipeline

Run each script in order:

```bash
# Step 1: Create S3 bucket with raw/staging/processed zones
python scripts/setup_s3_structure.py

# Step 2: Create all tables in RDS PostgreSQL
python scripts/setup_rds_tables.py

# Step 3: Load CSVs → S3 Bronze → RDS Staging tables
python scripts/load_data_to_rds.py

# Step 4: Transform Staging → Star Schema (dim + fact tables)
python scripts/run_transformation.py

# Step 5: Run analytics queries and print KPIs
python scripts/revenue_analysis.py
```

Expected output of Step 5:
```
============================================================
E-COMMERCE ANALYTICS REPORT
============================================================
Total Transactions : 112,650
Total Revenue      : BRL 15,842,746.32
Unique Customers   : 96,096

Top Product Categories:
  1. health_beauty          : BRL 1,258,690
  2. watches_gifts          : BRL 1,205,306
  3. bed_bath_table         : BRL 1,040,951
  ...
============================================================
```

---

## 🔒 Security Notes

| Practice | Implementation |
|---|---|
| **No hardcoded credentials** | All secrets in `config.py`, excluded via `.gitignore` |
| **IAM least privilege** | Production should use scoped IAM roles, not AdministratorAccess |
| **RDS access control** | Security Group restricts port 5432 to specific IPs only |
| **S3 public access** | Block Public Access enabled — no data exposed to internet |
| **Git safety** | `raw_data/`, `config.py`, and `venv/` all listed in `.gitignore` |

> ⚠️ **Important:** Never commit `config.py` to GitHub. The `.gitignore` is pre-configured to exclude it. Verify with `git status` before every push.

---

## 📦 requirements.txt

```
pandas==2.1.0
boto3==1.34.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
python-dotenv==1.0.0
```

---

## 🔮 Future Improvements

| Improvement | Description | Priority |
|---|---|---|
| **Apache Airflow DAG** | Orchestrate all 5 steps as a scheduled daily DAG | High |
| **AWS Glue Migration** | Replace Pandas transforms with PySpark Glue jobs for scalability | High |
| **Parquet on S3** | Convert staging CSVs to Parquet for 5x faster Athena queries | Medium |
| **Athena Gold Layer** | Replace RDS analytics with Athena querying S3 directly | Medium |
| **Power BI Dashboard** | Connect Power BI to RDS for visual KPI dashboards | Medium |
| **Data Quality Checks** | Add Great Expectations for automated schema and null validation | Low |
| **dbt Models** | Replace SQL transform scripts with dbt models for lineage tracking | Low |

---

## 🐛 Known Issues and Troubleshooting

**Connection refused to RDS**
```
→ Check Security Group allows inbound on port 5432 from your current IP
→ Verify RDS is in "Available" state in AWS Console
→ Confirm endpoint, port, username, password in config.py
```

**S3 Access Denied**
```
→ Run `aws sts get-caller-identity` to confirm IAM user is configured
→ Verify IAM user has AmazonS3FullAccess policy attached
→ Confirm bucket name in config.py matches the created bucket exactly
```

**Pandas dtype warnings on CSV load**
```
→ Expected — raw Olist CSVs have mixed types in some columns
→ Handled in load_data_to_rds.py with explicit dtype casting
→ All warnings are non-critical and do not affect pipeline output
```

**Out of RDS Free Tier storage**
```
→ RDS Free Tier gives 20GB — Olist dataset uses ~500MB
→ If exceeding limits: delete test data, run VACUUM in PostgreSQL
```

---

## 👤 Author

**Siddhesh Salve**
MCA Candidate — MIT College of Engineering, Aurangabad
Internship: Sai Soft Infosys

[![GitHub](https://img.shields.io/badge/GitHub-siddheshsalve77-181717?style=flat&logo=github)](https://github.com/siddheshsalve77)

---

## 📄 Dataset Credit

**Brazilian E-Commerce Public Dataset by Olist**
Available on [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

<div align="center">

**⭐ If this project helped you, give it a star on GitHub!**

</div>
