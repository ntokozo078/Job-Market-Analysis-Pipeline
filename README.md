
# 📊 Job Market Analysis Pipeline

A full-stack data engineering pipeline that scrapes job listings, processes and stores the data, and visualizes real-time skill-demand insights.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🚀 Live Dashboard

👉 **View the real-time dashboard here:**
**[https://ntokozo078-job-market-analysis-pipeline-dashboard-6xn1cy.streamlit.app/](https://ntokozo078-job-market-analysis-pipeline-dashboard-6xn1cy.streamlit.app/)**

---

## 🚀 Overview

This project automates job-market analysis through a complete ETL workflow:

1. **Scrapes** job listings from a public test dataset (*Real Python Fake Jobs*).
2. **Extracts skills** from unstructured job descriptions.
3. **Stores** processed records in an **SQLite** database.
4. **Visualizes** skill demand trends using **Streamlit**.

---

## 🏗️ Architecture

```
Web Source
   ➜ Python Scraper (BeautifulSoup + Requests)
   ➜ SQLite Database
   ➜ Pandas Transformation
   ➜ Streamlit Dashboard
```

---

## 🌟 Key Features

* **On-Demand Web Scraping** – Fetch fresh job listings instantly.
* **Skill Extraction Engine** – Detects popular tools (Python, SQL, AWS, etc.).
* **Historical Storage** – SQLite maintains accumulated job data.
* **Data Export** – Download CSV/Excel datasets.
* **Interactive Visuals** – Seaborn/Matplotlib bar charts and trends.

---

## 🛠️ Tech Stack

| Component     | Tools                          |
| ------------- | ------------------------------ |
| Core          | Python 3.x                     |
| Scraping      | BeautifulSoup4, Requests       |
| Processing    | Pandas, NumPy                  |
| Database      | SQLite                         |
| Visualization | Streamlit, Seaborn, Matplotlib |

---

## 💻 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ntokozo078/Job-Market-Analysis-Pipeline.git
cd Job-Market-Analysis-Pipeline
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit Dashboard

```bash
streamlit run dashboard.py
```

---

## 📈 Sample Visualization

![Sample Chart](https://github.com/ntokozo078/Job-Market-Analysis-Pipeline/blob/main/Figure_1.png?raw=true)

---

## 🔮 Future Improvements

* Add scheduling (Airflow or Cron) for automatic daily scraping.
* Deploy to cloud platforms (Streamlit Cloud, Azure, AWS).
* Enhance skill extraction using NLP (spaCy, transformers, embeddings).






