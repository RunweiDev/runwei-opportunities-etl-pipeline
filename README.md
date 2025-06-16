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

```
runwei-opportunities-etl-pipeline/
├── src/
│   ├── data_ingestion.py         # ADF ingestion scripts
│   ├── data_cleaning.SQL         # SQL scripts for data cleansing
│   └── database_schema.sql       # Azure SQL schema scripts
├── docs/
│   ├── architecture.png          # ETL architecture diagram
│   └── Fabric_powerbi            # Power BI screenshots
├── .gitignore                    # Python & Azure gitignore
├── README.md                     # This document
└── requirements.txt              # Python dependencies
```

---

## 🚀 **Setup Instructions**
### 1. Clone the Repository

```bash
git clone https://github.com/Cloudpeng121/runwei-opportunities-etl-pipeline.git
cd runwei-opportunities-etl-pipeline
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Azure

- Set up Azure Blob Storage & Azure Data Factory.
- Deploy Azure SQL Database schema using provided scripts.

### 4. Connect Power BI

- Link Azure SQL Database to Power BI Desktop.
- Develop visualizations from mirrored data.

---

## 📊 Sample Visualizations

*(Insert your Power BI visualizations screenshots here.)*

---

## ✅ Contributions

- **Automated Data Processing:** Achieved 80% reduction in manual tasks.
- **Improved Data Quality:** Ensured data accuracy and standardization >95%.
- **Real-time Analytics:** Enabled interactive dashboards for rapid decision-making.

---

## 📝 Future Enhancements

- Implement incremental loading strategies.
- Integrate real-time monitoring and alerting.
- Develop predictive analytics features for opportunities.

---

## 🤝 License

Distributed under the MIT License. See `LICENSE` file for details.

---

## 📞 Contact

- **Yunpeng Wang**
  - 📧 [yunpeng.wyp@gmail.com](mailto:yunpeng.wyp@gmail.com)
  - 🌐 [LinkedIn](https://www.linkedin.com/in/yunpeng-wang-a33215247/)

