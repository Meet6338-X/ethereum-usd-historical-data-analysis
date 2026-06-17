# Quartiles - Statistical Analysis (Python)

## Overview

Quartiles divide a dataset into four equal parts, each containing 25% of the data.

## Types of Quartiles

| Quartile | Description                      | Symbol            |
| -------- | -------------------------------- | ----------------- |
| Q1       | 25th percentile (first quartile) | 25% of data below |
| Q2       | 50th percentile (median)         | 50% of data below |
| Q3       | 75th percentile (third quartile) | 75% of data below |

## Results for Ethereum Dataset

| Variable              | Q1 (25%) | Q2 (50%) | Q3 (75%) |
| --------------------- | -------- | -------- | -------- |
| **Close**             | 355.24   | 1,653.84 | 2,722.07 |
| **High**              | 367.37   | 1,687.24 | 2,797.74 |
| **Low**               | 348.14   | 1,622.91 | 2,622.19 |
| **Open**              | 354.16   | 1,652.97 | 2,721.93 |
| **Volume**            | 6.33B    | 12.17B   | 20.04B   |
| **Daily_Return_Pct**  | -1.88    | 0.06     | 2.16     |
| **Log_Return**        | -0.019   | 0.000632 | 0.021    |
| **Price_Range**       | 18.38    | 62.99    | 138.69   |
| **Body_Size**         | 5.85     | 21.24    | 65.00    |
| **Upper_Shadow**      | 2.09     | 9.68     | 28.23    |
| **Lower_Shadow**      | 2.55     | 10.86    | 32.92    |
| **MA_7**              | 356.96   | 1,657.06 | 2,692.44 |
| **MA_14**             | 363.59   | 1,646.15 | 2,715.40 |
| **MA_21**             | 362.50   | 1,653.72 | 2,749.34 |
| **MA_50**             | 368.06   | 1,660.70 | 2,812.57 |
| **MA_100**            | 335.63   | 1,712.16 | 2,768.53 |
| **MA_200**            | 313.95   | 1,777.46 | 2,815.70 |
| **EMA_12**            | 357.35   | 1,645.08 | 2,735.73 |
| **EMA_26**            | 360.60   | 1,645.42 | 2,795.52 |
| **MACD**              | -31.52   | 0.51     | 37.28    |
| **Signal_Line**       | -28.30   | 0.47     | 35.32    |
| **MACD_Histogram**    | -8.76    | 0.44     | 9.02     |
| **RSI_14**            | 41.71    | 50.09    | 60.56    |
| **BB_Mid**            | 362.51   | 1,649.79 | 2,741.02 |
| **BB_Std**            | 26.45    | 89.42    | 171.79   |
| **BB_Upper**          | 417.46   | 1,879.22 | 3,196.11 |
| **BB_Lower**          | 305.51   | 1,486.98 | 2,358.52 |
| **BB_Width**          | 105.80   | 357.68   | 687.16   |
| **Volume_MA_20**      | 6.71B    | 13.80B   | 20.09B   |
| **Volume_Change_Pct** | -14.68   | -0.52    | 17.04    |
| **Volatility_30d**    | 3.08     | 3.97     | 4.96     |
| **Cumulative_Max**    | 1,396.42 | 4,812.09 | 4,812.09 |
| **Drawdown_Pct**      | -75.58   | -59.75   | -34.81   |

## Key Findings

1. **Close Price Quartiles**:
   - Q1 ($355.24): 25% of days closed below this
   - Q2 ($1,653.84): Median price
   - Q3 ($2,722.07): 75% of days closed below this

2. **Daily Return Quartiles**:
   - Q1 (-1.88%): Bad days
   - Q2 (0.06%): Neutral
   - Q3 (2.16%): Good days

3. **RSI Quartiles**:
   - Q1 (41.71): Oversold territory
   - Q2 (50.09): Neutral
   - Q3 (60.56): Overbought territory

## Visualization

- Box plots show quartiles visually: `plots/boxplot_*.png`
- The box in box plot represents Q1 to Q3
- The line inside the box is Q2 (median)

## Related Measures

- [Median](03-median.md) (Q2)
- [Interquartile Range (IQR)](07-interquartile-range.md)
- [Range](08-range.md)
