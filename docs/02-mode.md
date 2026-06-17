# Mode - Statistical Analysis

## Overview
The mode is the value that appears most frequently in a dataset. It represents the most common or popular value.

## Formula
```
Mode = Value with highest frequency
```

## Results for Ethereum Dataset

| Variable | Mode Value |
|----------|------------|
| **Close** | 480.36 |
| **High** | 229.86 |
| **Low** | 429.51 |
| **Open** | 360.31 |
| **Volume** | 893,249,984 |
| **Daily_Return_Pct** | 0.44 |
| **Log_Return** | 0.004432 |
| **Price_Range** | 20.08 |
| **Body_Size** | 3.34 |
| **Upper_Shadow** | 0.00 |
| **Lower_Shadow** | 0.00 |
| **MA_7** | 206.36 |
| **MA_14** | 398.20 |
| **MA_21** | 500.95 |
| **MA_50** | 214.09 |
| **MA_100** | 212.80 |
| **MA_200** | 172.46 |
| **EMA_12** | 597.02 |
| **EMA_26** | 548.50 |
| **MACD** | 8.58 |
| **Signal_Line** | 57.86 |
| **MACD_Histogram** | 1.95 |
| **RSI_14** | 45.54 |
| **BB_Mid** | 460.78 |
| **BB_Std** | 9.23 |
| **BB_Upper** | 748.21 |
| **BB_Lower** | 178.26 |
| **BB_Width** | 36.92 |
| **Volume_MA_20** | 1,118,925,837 |
| **Volume_Change_Pct** | -10.41 |
| **Volatility_30d** | 4.59 |
| **Cumulative_Max** | 4,812.09 |
| **Drawdown_Pct** | 0.00 |

## Key Findings

1. **Most Common Close Price**: $480.36 appeared most frequently
2. **Zero Shadows**: Upper and Lower Shadow both have mode of 0, indicating many doji candles
3. **Most Common Drawdown**: 0% (no drawdown) is most frequent
4. **Volume Mode**: ~893 million was the most common daily volume

## Interpretation

- The mode values often differ significantly from mean/median, especially in skewed distributions
- Zero values for shadows indicate frequent doji or pin bar candlestick patterns
- The 0% drawdown mode shows many days with no drawdown from peak
- Continuous variables like prices rarely repeat, so mode shows snapshot values

## Observations

- For continuous data like prices, mode is less informative than mean/median
- The mode is more meaningful for discrete or categorical data
- In financial data, repeated values often indicate support/resistance levels

## Visualization

See histogram visualizations in `/plots/histogram_*.png` to see frequency distributions

## Related Measures

- [Mean](01-mean.md)
- [Median](03-median.md)
- [Range](08-range.md)
