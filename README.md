# NSE_Banking_Analytics
Quantitative analysis of Tier-1 banking stocks on the Nairobi Securities Exchange (NSE), featuring weekly OHLCV data resampling and statistical modelling 

## Technical Indicators Used:

| Metric                                                        | Category                 | Purpose                                                                                                                                                            |
| ------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **VWAP (Volume Weighted Average Price)**                      | Price & Volume Indicator | Shows the average price traded throughout the day, weighted by volume. Used by traders to judge whether a stock is trading above or below its fair intraday price. |
| **Static Volatility (Historical Volatility)**                 | Risk Indicator           | Measures how much a stock's price has fluctuated over a past period.                                                                                               |
| **Dynamic Volatility (Realized/Implied/Adaptive Volatility)** | Risk Indicator           | Measures changing volatility over time, often updated continuously to reflect current market conditions.                                                           |
| **Beta (β)**                                                  | Market Risk Metric       | Measures a stock's sensitivity to movements in a benchmark index (e.g., S&P 500).                                                                                  |
| **MACD (Moving Average Convergence Divergence)**              | Momentum Indicator       | Identifies trend direction, momentum strength, and potential buy/sell signals.                                                                                     |

## Tools Used
 1. Pandas
 2. Matplotlib
 3. Seaborn
 4. mplfinance
