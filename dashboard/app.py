import sys
from pathlib import Path
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# ----------------------------------------------------------
# Add /src to path
# ----------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "src"))
from config import DB_URL

engine = create_engine(DB_URL)

st.set_page_config(page_title="Real-Time Retail KPIs", layout="wide")
st.title("📊 Real-Time Retail KPI Dashboard")

# ----------------------------------------------------------
# Simple, stable auto-refresh (no infinite loops)
# ----------------------------------------------------------
refresh_sec = st.slider("Refresh interval (seconds)", 30, 60, 300)

# Trigger rerun using Streamlit's built-in refresh pattern
st.write(f"🔄 Auto-refresh every **{refresh_sec}s**")
st.markdown(
    f"<meta http-equiv='refresh' content='{refresh_sec}'>",
    unsafe_allow_html=True
)

# ----------------------------------------------------------
# Always re-read DB
# ----------------------------------------------------------
with engine.connect() as conn:
    df = pd.read_sql(text("SELECT * FROM sales"), conn)
    row_count = conn.execute(text("SELECT COUNT(*) FROM sales")).scalar()

st.caption(f"DB in use: `{DB_URL}`")
st.metric("Rows currently in DB", row_count)

if df.empty:
    st.warning("No sales data yet. Keep generator + pipeline running.")
    st.stop()

df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${df['total'].sum():,.2f}")
col2.metric("Total Orders", len(df))
col3.metric("Avg Order Value", f"${df['total'].mean():.2f}")

# Top Products
st.subheader("🏆 Top Products by Revenue")
top_products = df.groupby("product")["total"].sum().sort_values(ascending=False)
st.bar_chart(top_products)

# Top Categories
st.subheader("📦 Top Categories by Revenue")
top_categories = df.groupby("category")["total"].sum().sort_values(ascending=False)
st.bar_chart(top_categories)

# Trend
st.subheader("⏱️ Sales Trend (Live)")
st.line_chart(df.set_index("timestamp")["total"])

st.subheader("🧾 Latest Sales")
st.dataframe(df.tail(20), use_container_width=True)
