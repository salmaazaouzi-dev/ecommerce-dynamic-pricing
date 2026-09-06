# 📈 Automated E-Commerce Dynamic Pricing & Market Benchmark Engine

An end-to-end Data Engineering and Analytics pipeline designed to optimize e-commerce pricing strategies through automated competitor web scraping, anomaly detection algorithms, and NLP-driven customer sentiment analysis.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29-red)
![CI/CD](https://img.shields.io/badge/GitHub_Actions-Automated-green)
![Database](https://img.shields.io/badge/SQLite-Database-lightgrey)

---

## 🎯 Business Problem

E-commerce businesses operate in hyper-competitive markets where pricing strategies directly impact profit margins and market share. Manually tracking competitor prices across thousands of SKUs is inefficient and error-prone. Furthermore, price changes without context (e.g., brand perception or product ratings) can harm sales volume.

**Key Objective:** Automate daily competitor pricing acquisition, flag pricing anomalies, analyze customer product sentiment, and generate optimal dynamic price recommendations.

---

## 🛠️ Tech Stack & Architecture

- **Data Ingestion & Scraping:** `Playwright`, `BeautifulSoup4`
- **Data Pipeline & Storage:** Python ETL routines, `SQLite` database
- **Analytics & Anomaly Detection:** `NumPy`, `Pandas` (Z-score calculation)
- **Natural Language Processing (NLP):** Sentiment Analysis Engine
- **Visualization & Dashboarding:** `Streamlit`, `Plotly`
- **Automation & CI/CD:** `GitHub Actions` (Scheduled daily cron job execution)

```text
ecommerce-dynamic-pricing/
├── .github/workflows/       # GitHub Actions CI/CD workflows
├── app/                     # Streamlit dashboard interface
├── config/                  # Project configuration settings
├── database/                # SQL Schema and database manager scripts
├── src/
│   ├── analytics/           # Pricing engine & anomaly detection algorithms
│   ├── nlp/                 # Customer review sentiment analysis
│   └── scrapers/            # Web scraping extraction modules
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
