# Sector-wise-Analysis-for-Indian-States

## 📌 Project Overview
This project analyzes district-wise sectoral economic performance across Indian states using SQL. The dataset contains economic contributions from Primary, Secondary, and Tertiary sectors at both constant and current prices.

The analysis helps identify:
- Sector-wise growth
- Economic trends
- District performance
- State comparisons
- Time-series insights

---

## 🎯 Objectives
- Perform SQL-based economic analysis
- Identify sector growth trends
- Compare district and state performance
- Generate business insights
- Practice advanced SQL concepts

---

## 🛠 Tools & Technologies
- SQL
- MySQL / PostgreSQL
- DBeaver
- Power BI
- GitHub

---
```sql
SELECT State_Name,
       SUM(Tertiary_Sector)
FROM sector_data
GROUP BY State_Name;
```

## 📂 Repository Structure

```bash
Sector-wise-Analysis-for-Indian-States
│
├── Dataset
│   └── SectoralAnalysis.csv
│
├── SQL Queries
│   └── all_queries.sql
│
├── Query Outputs
│   ├── Q1.csv
│   └── Q2.csv
│
├── Reports
│   └── PGDM_Project_Report.pdf
│
└── README.md
```

---

## 📊 SQL Concepts Used
- Filtering
- Aggregation
- Window Functions
- Ranking
- Subqueries
- Joins
- Group By
- Time-Series Analysis

---

## 📈 Key Insights
- Urban districts show stronger tertiary sector growth
- Some districts remain dependent on the primary sector
- Economic contribution differs significantly across states
- Per capita contribution is higher in developed districts

---

## 🚀 Future Improvements
- Interactive Power BI dashboards
- Predictive analytics using Python
- Automated reports
- Advanced visualizations
