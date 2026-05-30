import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Retail ETL Analytics Dashboard",
    layout="wide"
)

# --------------------------------------------------
# Database Connection
# --------------------------------------------------
engine = create_engine("sqlite:///../retail.db")

# Load Data
df = pd.read_sql("SELECT * FROM sales", engine)

# --------------------------------------------------
# Dashboard Title
# --------------------------------------------------
st.title("📊 Retail ETL Analytics Dashboard")
st.markdown("Enterprise Retail Data Engineering Pipeline Analysis")

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------
st.sidebar.header("Filters")

regions = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

categories = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

years = st.sidebar.multiselect(
    "Select Year",
    options=sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

# --------------------------------------------------
# Apply Filters
# --------------------------------------------------
filtered_df = df[
    (df["Region"].isin(regions))
    & (df["Category"].isin(categories))
    & (df["Year"].isin(years))
]

# --------------------------------------------------
# KPI Section
# --------------------------------------------------
st.subheader("📈 Key Performance Indicators")

total_revenue = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order_ID"].nunique()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Revenue",
        f"${total_revenue:,.2f}"
    )

with col2:
    st.metric(
        "Total Profit",
        f"${total_profit:,.2f}"
    )

with col3:
    st.metric(
        "Total Orders",
        total_orders
    )

st.markdown("---")

# --------------------------------------------------
# Charts Row
# --------------------------------------------------
col1, col2 = st.columns(2)

# Region-wise Sales
with col1:

    st.subheader("Region-wise Sales")

    region_sales = (
        filtered_df
        .groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    fig1, ax1 = plt.subplots(figsize=(5, 3))

    region_sales.plot(
        kind="bar",
        ax=ax1
    )

    ax1.set_ylabel("Sales")
    ax1.set_xlabel("Region")

    plt.tight_layout()

    st.pyplot(fig1)

# Monthly Revenue Trend
with col2:

    st.subheader("Monthly Revenue Trend")

    monthly_sales = (
        filtered_df
        .groupby("Month")["Sales"]
        .sum()
    )

    fig2, ax2 = plt.subplots(figsize=(5, 3))

    monthly_sales.plot(
        marker="o",
        ax=ax2
    )

    ax2.set_ylabel("Revenue")
    ax2.set_xlabel("Month")

    plt.tight_layout()

    st.pyplot(fig2)

st.markdown("---")

# --------------------------------------------------
# Category Profit Pie Chart
# --------------------------------------------------
st.subheader("Category-wise Profit Distribution")

category_profit = (
    filtered_df
    .groupby("Category")["Profit"]
    .sum()
)

fig3, ax3 = plt.subplots(figsize=(3, 3))

category_profit.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax3
)

ax3.set_ylabel("")

plt.tight_layout()

st.pyplot(fig3)
# --------------------------------------------------
# Top Products Table
# --------------------------------------------------
st.subheader("🏆 Top 10 Selling Products")

top_products = (
    filtered_df
    .groupby("Product_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

st.dataframe(
    top_products,
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# Dataset Preview
# --------------------------------------------------
st.subheader("📄 Dataset Preview")

st.dataframe(
    filtered_df.head(100),
    use_container_width=True
)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption(
    "Retail ETL Analytics Pipeline | Python • SQL • SQLite • Streamlit"
)