# Enterprise Retail ETL Analytics Pipeline

## Project Overview

This project is an enterprise-style Retail ETL Analytics Pipeline developed using Python, SQL, SQLite, and Streamlit. The system automates the extraction, transformation, loading, validation, and analysis of retail sales data while providing interactive business insights through a dashboard.

The project simulates real-world data engineering workflows used in enterprise environments for processing transactional data and generating actionable business intelligence.

---

## Key Features

### ETL Pipeline
- Extracts retail sales data from CSV files
- Cleans and transforms raw data
- Loads processed data into a SQLite database

### Incremental Data Loading
- Loads only new records into the database
- Prevents duplicate data ingestion
- Improves pipeline efficiency

### Data Validation
- Removes duplicate records
- Handles missing values
- Validates sales and quantity data
- Standardizes data formats

### SQL Analytics
- Region-wise sales analysis
- Monthly revenue trends
- Category-wise profit analysis
- Top-selling products analysis

### Interactive Dashboard
- Dynamic KPI monitoring
- Region filters
- Category filters
- Year filters
- Interactive visualizations

### Logging System
- Tracks ETL execution status
- Records pipeline activities
- Supports monitoring and debugging

---

## Technology Stack

| Category | Technologies |
|-----------|-------------|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Database | SQLite |
| Database Connectivity | SQLAlchemy |
| Dashboard | Streamlit |
| Visualization | Matplotlib |
| Version Control | Git, GitHub |

---

## Project Architecture

```text
Retail Sales Dataset
         ↓
      Extract
         ↓
     Transform
         ↓
 Data Validation
         ↓
 Incremental ETL
         ↓
 SQLite Database
         ↓
   SQL Analytics
         ↓
 Interactive Dashboard
```

---

## Folder Structure

```text
retail-etl-pipeline/
│
├── data/
├── scripts/
├── dashboard/
├── logs/
├── screenshots/
├── retail.db
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Dashboard KPIs

The dashboard provides the following business metrics:

- Total Revenue
- Total Profit
- Total Orders
- Region-wise Sales
- Monthly Revenue Trend
- Category Profit Distribution
- Top 10 Selling Products

---

## Business Insights Generated

- Identify top-performing regions
- Analyze monthly sales trends
- Monitor category profitability
- Track overall business performance
- Discover best-selling products

---

## Incremental Loading Logic

The pipeline implements incremental ETL processing by comparing incoming Order IDs with existing database records.

Benefits:
- Prevents duplicate records
- Reduces processing time
- Simulates enterprise-grade data ingestion workflows

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Execute ETL Pipeline

```bash
python scripts/run_pipeline.py
```

### Run Analytics Queries

```bash
python scripts/run_queries.py
```

### Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Sample Workflow

1. Load raw retail dataset
2. Clean and validate records
3. Generate derived metrics
4. Perform incremental loading
5. Store processed data in SQLite
6. Execute SQL analytics
7. Visualize KPIs in Streamlit dashboard

---

## Future Enhancements

- PostgreSQL Integration
- Apache Airflow Scheduling
- Cloud Deployment
- Automated Data Quality Monitoring
- Real-Time Data Processing
- Advanced Business Intelligence Reporting

---

## Resume Highlights

- Developed an enterprise-style Retail ETL Analytics Pipeline using Python, SQL, SQLite, and Streamlit.
- Implemented incremental data loading with duplicate detection and automated logging.
- Built interactive KPI dashboards and business analytics reports.
- Designed modular ETL workflows for scalable retail data processing.

---

## Author

Vinodini B

Computer Science Engineering (AI & ML)

Passionate about Data Engineering, Artificial Intelligence, and Analytics.
