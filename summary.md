# Summary: Trader Performance vs Market Sentiment

## Objective
The objective of this project is to analyze how market sentiment (Fear vs Greed) influences trader behavior and performance using Hyperliquid trading data. The goal is to uncover actionable insights that can inform smarter trading strategies.

---

## Methodology
- Loaded and cleaned both datasets (trader data and sentiment data)  
- Handled missing values and ensured data consistency  
- Converted timestamps and aligned datasets at a daily level  
- Engineered key metrics:
  - Profit & Loss (PnL)
  - Win rate
  - Trade size
  - Trade frequency  
- Merged datasets to associate each trade with market sentiment  
- Performed comparative analysis across sentiment regimes  
- Segmented traders based on:
  - Trade size (high vs low)
  - Trade frequency (frequent vs infrequent)
  - Performance (winners vs losers)  
- Applied K-Means clustering to identify trader archetypes  
- Built a Random Forest model to predict trade profitability  
- Developed a Jupyter Notebook (`analysis.ipynb`) for step-by-step analysis and visualization  
- Built and deployed a Streamlit dashboard for interactive exploration  

---

## Key Insights

### 1. Trade Size Strongly Impacts Profitability
High-size trades generate significantly higher PnL compared to low-size trades across all sentiment conditions.  
For example, during Extreme Greed, high-size trades produce ~10x higher returns.

Additionally, traders tend to increase trade sizes during Greed and Extreme Greed periods, indicating higher risk-taking behavior in bullish markets.

---

### 2. Greed Amplifies Both Profit and Loss
During Greed phases, trader outcomes become highly polarized:
- Profitable traders achieve strong returns  
- Underperforming traders incur significantly larger losses  

This suggests that Greed increases both opportunity and risk.

---

### 3. Frequent Trading Does Not Guarantee Better Performance
Frequent traders do not consistently outperform others.  
This indicates that overtrading reduces efficiency and may lead to unnecessary losses.

---

### 4. Extreme Greed Offers Highest Profit Potential
Extreme Greed periods show the highest average profitability across trader segments, likely due to strong market momentum.

---

### 5. Trading Behavior Matters More Than Sentiment Alone
Predictive modeling shows:
- Execution price (~60%) and trade size (~38%) dominate prediction  
- Market sentiment contributes very little (~1%)  

This highlights that **trader decisions and execution strategy are more important than sentiment alone**.

---

## Trader Segmentation (Clustering)

Traders were grouped into three behavioral archetypes:

- **Risk-tolerant traders:** High profitability with larger trades but lower win rates  
- **Balanced traders:** Moderate profitability with consistent performance  
- **High-risk inefficient traders:** Very large trades but relatively low returns  

This demonstrates that increasing trade size alone does not ensure profitability.

---

## Predictive Modeling

A Random Forest classifier was trained to predict trade profitability:

- Accuracy: ~82%  
- Better at identifying loss-making trades (risk-aware behavior)  
- Feature importance:
  - Execution price → most important  
  - Trade size → significant impact  
  - Sentiment → minimal direct effect  

This suggests the model captures behavioral patterns more than market sentiment signals.

---

## Strategy Recommendations

### 1. Position Sizing Strategy
Increase position sizes selectively during strong bullish sentiment (Extreme Greed), as larger trades are associated with higher returns.

### 2. Risk Management Strategy
Reduce leverage and avoid aggressive trading during Greed phases, especially for inconsistent traders, as losses are amplified.

### 3. Trade Optimization Strategy
Avoid overtrading and focus on high-quality trades rather than increasing trade frequency.

---

## Conclusion

This analysis demonstrates that while market sentiment influences trading environments, **trader behavior, execution quality, and position sizing are the primary drivers of profitability**.  

Successful trading strategies should prioritize disciplined decision-making, risk management, and efficient capital allocation.

---

## Deliverables

- Jupyter Notebook: `analysis.ipynb`  
- Cleaned and processed dataset  
- Visualizations and charts  
- Streamlit dashboard (deployed)  
- GitHub repository with full project structure  
