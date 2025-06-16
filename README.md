# runwei-opportunities-etl-pipeline
ETL pipeline from Azure Blob Storage to Azure SQL and mirrored to Power BI dashboards for real-time analytics of funding opportunities.
# Runwei Opportunities ETL Pipeline 

[![Azure](https://img.shields.io/badge/Cloud-Azure-0078D4.svg?style=flat&logo=microsoftazure)](https://azure.microsoft.com/) 
[![Power BI](https://img.shields.io/badge/Visualization-Power%20BI-F2C811.svg?style=flat&logo=powerbi)](https://powerbi.microsoft.com/)

This repository contains an ETL pipeline developed for Runwei™ to extract raw funding opportunity data from Azure Blob Storage, transform and cleanse the data, load it into Azure SQL Database, and mirror it to Power BI for dynamic analytics and visualization.

---

## 📌 **Pipeline Overview**

The pipeline automates the following:

- **Ingestion**: Scheduled daily data ingestion from Azure Blob Storage.
- **Cleaning and Transformation**: Data cleansing using Python scripts and Azure Data Factory transformations.
- **Loading and Modeling**: Structured data loaded into Azure SQL Database with normalized schemas.
- **Visualization**: Data mirrored and visualized via interactive dashboards in Power BI.

---

## 🔧 **Technology Stack**

- **Cloud Storage**: Azure Blob Storage
- **ETL Tool**: Azure Data Factory (ADF)
- **Database**: Azure SQL Database
- **Data Visualization**: Power BI
- **Programming Languages**: Python, SQL

---

## ⚙️ **Pipeline Workflow**

1. **Extract**:  
   - Automated daily extraction of latest JSON/CSV files.

2. **Transform**:  
   - Cleanse and standardize fields (Title, Deadline, AwardValue, etc.).
   - Convert datatypes and handle missing or invalid data.

3. **Load**:  
   - Load cleansed data into Azure SQL tables.
   - Apply indexing and constraints to optimize query performance.

4. **Mirror & Visualize**:  
   - Mirror SQL Database schema to Power BI model.
   - Develop dashboards showing real-time analytics and metrics.

---

## 📂 **Project Structure**

