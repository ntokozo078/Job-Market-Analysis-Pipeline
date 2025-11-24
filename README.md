# 📊 Job Market Analysis Pipeline

A full-stack data engineering pipeline that extracts job market data, stores it in a structured database, and visualizes skill demand trends in real-time.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Status](https://img.shields.io/badge/Status-Active-success)

## 🚀 Overview
This project automates the process of market research by:
1.  **Scraping** job listings from a target portal (simulated using *Real Python Fake Jobs*).
2.  **Cleaning & Structuring** data (extracting key tech skills from unstructured text).
3.  **Storing** historical data in a local **SQLite** database.
4.  **Visualizing** insights via an interactive **Streamlit** dashboard.

## 🏗️ Architecture
**ETL Pipeline:**
`Web Source` ➡️ `Python Scraper (BS4)` ➡️ `SQLite Database` ➡️ `Pandas Transformation` ➡️ `Streamlit Dashboard`

## 🌟 Key Features
* **Live Web Scraping:** Fetches real-time data upon request.
* **Keyword Extraction:** Parses job descriptions to find high-demand skills (e.g., Python, AWS, SQL).
* **Data Persistence:** Prevents data loss using SQLite.
* **Export Capabilities:** Allows users to download datasets in **CSV** and **Excel** formats.
* **Interactive Visualization:** Dynamic bar charts built with **Seaborn**.

## 🛠️ Tech Stack
* **Core:** Python 3.x
* **ETL & Scraping:** `BeautifulSoup4`, `Requests`
* **Data Processing:** `Pandas`, `NumPy`
* **Database:** `SQLite`
* **Visualization:** `Streamlit`, `Seaborn`, `Matplotlib`

## 💻 Installation & Usage

### 1. Clone the repository
```bash
git clone [https://github.com/ntokoz078/job-market-analysis.git](https://github.com/ntokozo078/job-market-analysis.git)
cd job-market-analysis
