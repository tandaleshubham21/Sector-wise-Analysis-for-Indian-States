# Sector-wise-Analysis-for-Indian-States

<div align="center">

# 📊 District-wise Sectoral Economic Analysis of Indian States

**Advanced SQL + Tableau Project**

[![CI](https://github.com/tandaleshubham21/Sector-wise-Analysis-for-Indian-States/actions/workflows/ci.yml/badge.svg)](https://github.com/tandaleshubham21/Sector-wise-Analysis-for-Indian-States/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with SQL](https://img.shields.io/badge/Made%20with-SQL-blue?logo=sqlite)](https://www.sqlite.org/)
[![Tableau](https://img.shields.io/badge/Tableau-Dashboard-orange?logo=tableau)](https://www.tableau.com/)

**Analyze • Visualize • Insight**

</div>

---

## 📌 Project Overview

This project performs **comprehensive district-level sectoral analysis** across multiple Indian states using advanced SQL techniques. It examines the contribution of **Primary, Secondary, and Tertiary** sectors using both constant and current prices.

### What makes this project special?
- Deep district-level granularity across 20+ states
- Time-series analysis from 2007–2013
- Rich visualization through interactive Tableau dashboard
- Real-world economic insights with practical business value

---

## 📊 Interactive Tableau Dashboard

<div align="center">

![District-wise sectoral analysis Dashboard](Dashboard.png)

**Click to explore the full interactive experience →** `sectoral analysis_v2025.3.twbx`

</div>

### Dashboard Highlights
| Feature                    | Description                                      |
|---------------------------|--------------------------------------------------|
| **Time Series Analysis**  | Track Primary, Secondary & Tertiary growth over years |
| **Map Visualization**     | Geographic view of economic performance across India    |
| **Sector Comparison**     | Bar charts comparing districts and states               |
| **Per Capita Analysis**   | Income trends and disparities visualization             |

> **Tip:** Open the `.twbx` file in **Tableau Desktop** or **Tableau Public** to interact with filters, drill-downs, and dynamic charts.

---

## 🎯 Project Objectives

- Perform advanced **SQL-based economic analysis** at district level
- Identify **sectoral growth trends** and performance leaders
- Compare **state-wise and district-wise** economic contributions
- Generate **actionable business & policy insights**
- Master advanced SQL concepts (Window Functions, Ranking, Time-Series)

---

## 🛠 Tools & Technologies

| Category           | Tools Used                          |
|--------------------|-------------------------------------|
| **Data Analysis**  | SQL (MySQL / PostgreSQL)            |
| **Visualization**  | **Tableau**                         |
| **Automation**     | **GitHub Actions** (CI/CD)          |
| **Database Tool**  | DBeaver                             |
| **Version Control**| Git + GitHub                        |

---

## 📂 Repository Structure

```bash
Sector-wise-Analysis-for-Indian-States/
├── .github/workflows/
│   ├── ci.yml                    # Project validation CI
│   └── update-readme.yml         # Auto-updates this README
├── Dataset/
│   └── Sectorial Analysis        # Source data
├── Query Outputs/                # 20 pre-computed query results (Q1–Q20)
├── SQL Queries/                  # All analysis queries
├── project code.sql              # Main working queries
├── sectoral analysis_v2025.3.twbx # Tableau Dashboard
├── Dashboard.png                 # Dashboard preview image
├── Reports/
│   └── Sectorial Analysis Report.docx
├── LICENSE
├── .gitignore
└── README.md
```

---

## 📊 Advanced SQL Concepts Mastered

- ✅ Filtering, Aggregation & GROUP BY
- ✅ **Window Functions** (RANK(), LAG(), Cumulative SUM)
- ✅ Subqueries & Complex Joins
- ✅ **Time-Series Analysis**
- ✅ Ranking & Ordering with PARTITION BY

---

## 📈 Key Insights & Findings

| Insight | Details |
|---------|---------|
| **Tertiary Sector Dominance** | Strong in developed districts like **Thane, Pune, Nagpur** |
| **Primary Sector Dependence** | Higher in districts like **Osmanabad, Beed, Parbhani** |
| **Top Performers**            | **Pune** and **Thane** consistently lead in total economic contribution |
| **Per Capita Variation**      | Significant differences across Maharashtra districts |

---

## ⚙️ Automation with GitHub Actions

This repository uses **GitHub Actions** for continuous quality assurance and maintenance:

- ✅ Validates all Query Output files and core project files
- ✅ Ensures Tableau dashboard file is present
- ✅ **Auto-updates this README** with the last successful validation time
- ✅ Runs automatically on push & pull requests
- ✅ Supports manual triggering from the Actions tab

**Last Automated Validation:** <!-- LAST_VALIDATED: -->**2026-07-16 08:08:20 UTC** <!-- /LAST_VALIDATED -->

**→ [View Workflow Runs](https://github.com/tandaleshubham21/Sector-wise-Analysis-for-Indian-States/actions)**

---

## 🚀 Future Roadmap

- [ ] Publish interactive dashboard to **Tableau Public**
- [ ] Add **Python predictive analytics** layer
- [ ] Create **Power BI** version of dashboard
- [ ] Build automated reporting pipeline
- [ ] Expand GitHub Actions for dynamic query regeneration

---

## 📬 Contact & Credits

**Project Author:** Shubham Kailas Tandale  
**Built with ❤️ using SQL + Tableau**

---

<div align="center">

**⭐ If you found this project helpful, consider giving it a star!**

</div>