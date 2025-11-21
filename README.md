
# 📊 Real-Time Retail KPI Streaming Dashboard

### **A Data Analyst + Data Engineering Project (End-to-End Streaming Pipeline)**

This project simulates a **real-time retail sales monitoring system**—from data generation to storage, ETL, and a live-updating analytics dashboard.

It is designed to demonstrate practical **data analyst + data engineering** skills using Python, SQL, Streamlit, and real-time data flows.



# 🚀 Features

### ✅ **Real-Time Data Generator**

* Continuously simulates incoming sales every few seconds
* Generates realistic products, categories, prices, and timestamps

### ✅ **Streaming ETL Pipeline**

* Loads new records incrementally into a SQLite/PostgreSQL database
* Cleans data and preserves schema
* Runs continuously for real-time ingestion

### ✅ **Live Analytics Dashboard (Streamlit)**

* Auto-refreshes every 5 minutes
* Displays key retail KPIs:

  * Total Sales
  * Total Orders
  * Average Order Value
  * Top Products
  * Top Categories
  * Real-time sales trend
  * Latest 20 transactions

### ✅ **Tech Stack**

* **Python**
* **Pandas**
* **Streamlit**
* **SQLAlchemy**
* **SQLite / PostgreSQL**
* **dotenv**



# 🏗️ Architecture Overview

```
                  +-------------------------+
                  | Real-Time Data Generator |
                  | (generate_stream.py)     |
                  +------------+-------------+
                               |
                               v
                   +------------------------+
                   |  Streaming CSV Buffer  |
                   |     (data/stream.csv)  |
                   +------------+-----------+
                                |
                                v
                   +-------------------------+
                   |   Real-Time ETL Loader  |
                   |     (pipeline.py)       |
                   +------------+------------+
                                |
                                v
               +------------------------------------+
               |     SQLite / PostgreSQL Database    |
               +------------------------------------+
                                |
                                v
                 +--------------------------------+
                 |   Live Streamlit Dashboard      |
                 |    (dashboard/app.py)           |
                 +--------------------------------+
```



# 🛠️ Installation & Setup

## 1️⃣ **Clone the Repo**

```bash
git clone https://github.com/Pravya425/retail-kpi-streaming.git
cd retail-kpi-streaming
```

## 2️⃣ **(Optional) Create Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

## 4️⃣ **Create a `.env` File**

Create a `.env` in project root:

```
DB_URL=sqlite:///retail.db
STREAM_DELAY=3
```



# 🔄 Running the System (3 Terminals)

## **Terminal 1 — Start Real-Time Generator**

```bash
python3 src/generate_stream.py
```

## **Terminal 2 — Start Real-Time ETL Loader**

```bash
python3 src/pipeline.py
```

## **Terminal 3 — Start Dashboard**

```bash
streamlit run dashboard/app.py
```

Dashboard will open automatically at:

```
http://localhost:8501
```



# 📈 Dashboard Preview

### 🏆 KPIs

* Total Sales
* Total Orders
* Live Average Order Value

### 📦 Product & Category Insights

* Top revenue-generating products
* Top earning categories

### 📉 Real-Time Trend

* Time-series line chart of total sales
* Auto-refresh every 5 minutes

### 🧾 Latest Transactions

* Last 20 sales displayed in a dynamic table



# 📁 Project Structure

```
retail-kpi-streaming/
│
├── src/
│   ├── generate_stream.py      # Real-time data generator
│   ├── pipeline.py             # Incremental ETL loader
│   ├── config.py               # Environment setup
│
├── dashboard/
│   ├── app.py                  # Streamlit dashboard
│
├── data/
│   └── stream.csv              # Streaming buffer (ignored in git)
│
├── .gitignore
├── requirements.txt
├── README.md
└── .env (ignored)
```



# 🚀 Use Cases / Interview Highlights

This project demonstrates:

### ✔️ Real-time data pipelines

### ✔️ KPI dashboarding

### ✔️ ETL development

### ✔️ SQL + Python analytics

### ✔️ Data modeling & time-series trends

### ✔️ Auto-refreshing dashboards

Perfect to showcase in:

* **Data Analyst**
* **Data Engineer**
* **Data Scientist (Analytics)**
* **Business Analyst**
* **BI / Reporting Analyst**

Interviewer-friendly & resume-ready.


# ⭐ Future Enhancements

* Add forecasting model (Prophet or LSTM)
* Add anomaly detection on sales
* Convert pipeline to Airflow / Prefect DAG
* Add user login + filtering
* Deploy dashboard to cloud (Railway, Streamlit Cloud, Render)



# 🎉 Author

**Pranay Reddy Tatiparti**
Data Analyst | Data Engineer | Python | SQL | Cloud | Streamlit

