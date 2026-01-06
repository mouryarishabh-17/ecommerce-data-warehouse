# 🛒 E-Commerce Batch Data Warehouse & Analytics

## 📌 Project Overview
This project demonstrates an **end-to-end batch ETL pipeline** for an e-commerce business.  
It ingests raw data, applies transformations and data quality checks, and loads analytics-ready data into a PostgreSQL data warehouse for reporting and visualization.

The project is designed to reflect **real-world data engineering practices** including:
- Reproducible ETL pipelines
- Data quality enforcement
- Warehouse modeling
- SQL analytics
- BI visualization 
- Clean GitHub repository structure

---

## 🎯 Project Goals
- Build a batch ETL pipeline using Python
- Enforce data quality and referential integrity
- Design an analytics-ready data warehouse
- Perform business analytics using SQL
- Enable BI dashboards Power BI 
- Maintain professional logging and documentation

---

## 🏗️ Project Structure

```
ecommerce-data-warehouse/
│
├── data/
│ ├── raw/        # Generated raw data (ignored in Git)
│ ├── processed/  # Processed data outputs (ignored in Git)
│ └── sample/     # Small sample CSVs for schema demonstration
│
├── etl/
│ ├── read_customers.py
│ ├── etl_customers_orders.py
│ ├── data_quality.py
│ ├── etl_pipeline.py
│ └── etl_pipeline.log
│
├── warehouse/
│ └── schema.sql
│
├── analytics/
│ └── queries.sql
│
├── dashboard/
│ └── powerbi.pbix
│
├── .gitignore
└── README.md 
```

---

## 🔄 ETL Pipeline Flow
```
                                                             Raw Data
                                                                ↓
                                                            Extraction
                                                                ↓
                                                           Transformation
                                                                ↓
                                                         Data Quality Checks
                                                                ↓
                                                      Analytics-Ready Fact Table
                                                                ↓
                                                              Dashboard
```

---

## 🧩 ETL Stages Explained

### 1️⃣ Extraction
- Reads raw CSV files for customers, orders, products, and order items
- Validates schema consistency
- Prepares data for transformation

### 2️⃣ Transformation
- Joins customers and orders
- Calculates order totals using:
```
product.price × quantity
```
- Enriches records with derived attributes

### 3️⃣ Data Quality
- Validates primary keys
- Enforces foreign key relationships
- Removes invalid records
- Ensures numeric and date integrity

### 4️⃣ Loading
- Writes clean, validated data to processed files
- Loads final tables into PostgreSQL

---

## 🗄️ Data Warehouse Design

The warehouse follows a **star-schema-inspired design**.

### Dimension Table
- `dim_customers`
- Contains descriptive customer attributes

### Fact Table
- `fact_orders`
- Stores transactional order metrics
- Includes computed `total_amount`

This design supports efficient analytical queries and BI reporting.

---

## 📊 Analytics & KPIs

SQL analytics include:
- Total revenue
- Revenue by customer
- Average order value
- Order volume analysis

All SQL queries are stored in:


`analytics/queries.sql`


---

## 📈 Dashboard
Business metrics are visualized using a BI tool Power BI connected directly to PostgreSQL.

Dashboards include:
- Revenue trends
- Customer distribution
- Order performance metrics

---

## 🪵 Logging
Basic logging is implemented to track pipeline execution:
- Pipeline start
- Stage-level completion
- Successful pipeline finish

Logs are written to:


`etl/etl_pipeline.log`


---

## 📂 Data Strategy (Important)
- Full raw and processed datasets are **generated locally** and excluded from GitHub.
- The repository includes **small sample CSV files** under `data/sample/` to demonstrate:
  - Schema
  - Relationships

---

## ⚠️ Challenges & Decisions
- Detected and handled invalid foreign key relationships
- Enforced data quality before analytics
- Chose reproducibility over manual data edits
- Logging added after pipeline stabilization
- Orchestration tools explored but not executed due to OS limitations

---

## 🚀 Future Improvements
- Add workflow orchestration using Airflow in a Linux/cloud environment
- Improve data realism and volume
- Add additional dimensions (products, dates)
- Deploy warehouse and dashboards to the cloud
- Extend logging and monitoring

---

## 🧠 Key Learnings
- End-to-end batch ETL design
- Importance of data quality checks
- Warehouse schema modeling
- SQL-based analytics
- BI integration
- GitHub best practices for data projects

---
