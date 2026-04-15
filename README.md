# Sentiment-Driven Trading Performance Analytics

##  Overview
This project analyzes how market sentiment (Fear vs Greed) influences trader behavior and performance using Hyperliquid trading data.  
The goal is to uncover actionable insights that can improve trading strategies.

---

##  Datasets
- **Bitcoin Market Sentiment Dataset**
  - Contains daily Fear/Greed classification

- **Historical Trader Data (Hyperliquid)**
  - Includes execution price, trade size, side, PnL, account, and timestamps

---

##  Methodology
- Data cleaning and preprocessing  
- Timestamp conversion and alignment at daily level  
- Feature engineering:
  - Profit & Loss (PnL)
  - Win rate
  - Trade size
  - Trade frequency  
- Sentiment-based comparative analysis  
- Trader segmentation using clustering  
- Predictive modeling using Random Forest  

---

##  Key Insights
- **Trade size strongly impacts profitability** (~10x difference observed between low and high-size trades)  
- **Greed amplifies both profits and losses**, increasing market risk  
- **Frequent trading does not guarantee higher returns**, indicating overtrading inefficiency  
- **Extreme Greed periods show highest profitability**, driven by strong market momentum  
- **Trading behavior (execution & sizing) has stronger influence than sentiment alone**

---

##  Strategy Recommendations
- Increase position sizes selectively during strong bullish sentiment (Extreme Greed)  
- Reduce risk exposure during Greed phases for inconsistent traders  
- Avoid overtrading and focus on high-quality trades  

---

##  Bonus Work
- **Trader Clustering:** Identified behavioral archetypes (risk-tolerant, balanced, high-risk inefficient traders)  
- **Predictive Modeling:** Random Forest model achieved ~82% accuracy in predicting trade profitability  
- **Interactive Dashboard:** Built using Streamlit for real-time exploration  

---

## Live Dashboard
https://trader-sentiment-analysis18.streamlit.app/

---

##  How to Run Locally

```bash
# Clone repository
git clone https://github.com/Yanshuptl18/trader-sentiment-analysis.git

# Navigate to project
cd trader-sentiment-analysis

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run src/app.py
```

##  Project Structure

```
trader-sentiment-analysis/
│
├── src/
│   ├── app.py
│   └── merged_data.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│
├── README.md
├── summary.md
└── requirements.txt
```
---

## Tools & Technologies

- Python (Pandas, NumPy)
- Matplotlib, Seaborn
- Scikit-learn
- Streamlit

---

## Conclusion

The analysis demonstrates that while market sentiment influences trading environments, **trader behavior and execution decisions play a more critical role in determining profitability**.  

Effective risk management, position sizing, and disciplined trading strategies are key to consistent performance.
