import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Trader Analytics Dashboard", layout="wide")

st.title("Sentiment-Driven Trading Performance Analytics")
st.markdown("Analyzing how market sentiment influences trader behavior and performance")

# load data
@st.cache_data
def load_data():
    df = pd.read_csv("merged_data.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

# SIDEBAR FILTERS
st.sidebar.header("Filters")

sentiment_filter = st.sidebar.multiselect(
    "Sentiment",
    df['classification'].unique(),
    default=df['classification'].unique()
)

account_filter = st.sidebar.multiselect(
    "Select Traders (Optional)",
    df['account'].unique()
)

# apply filters
filtered_df = df[df['classification'].isin(sentiment_filter)]

if account_filter:
    filtered_df = filtered_df[filtered_df['account'].isin(account_filter)]

# KPI SECTION
st.subheader("Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Trades", len(filtered_df))
col2.metric("Avg PnL", round(filtered_df['pnl'].mean(), 2))
col3.metric("Win Rate", round(filtered_df['win'].mean(), 2))
col4.metric("Avg Trade Size", round(filtered_df['trade_size'].mean(), 2))

# TABS
tab1, tab2, tab3 = st.tabs(["Overview", "Time Analysis", "Advanced Insights"])

# 1: OVERVIEW
with tab1:

    st.subheader("PnL Distribution")
    fig, ax = plt.subplots()
    sns.boxplot(x='classification', y='pnl', data=filtered_df, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.subheader("Trade Size by Sentiment")
    st.bar_chart(filtered_df.groupby('classification')['trade_size'].mean())

    st.subheader("Win Rate by Sentiment")
    st.bar_chart(filtered_df.groupby('classification')['win'].mean())

# 2: TIME ANALYSIS
with tab2:

    st.subheader("PnL Over Time")

    pnl_time = filtered_df.groupby('date')['pnl'].sum()

    st.line_chart(pnl_time)

#  3: ADVANCED INSIGHTS
with tab3:

    st.subheader("Top Traders")

    top_traders = (
        filtered_df.groupby('account')['pnl']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(top_traders)

    st.subheader("Correlation Heatmap")

    corr = filtered_df[['pnl', 'trade_size', 'execution_price', 'win']].corr()

    fig2, ax2 = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax2)
    st.pyplot(fig2)

# DATA VIEW
st.subheader("Data Preview")
st.dataframe(filtered_df.head(100))