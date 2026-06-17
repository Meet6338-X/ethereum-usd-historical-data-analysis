# Median - Statistical Analysis (Python)

## Overview

The median is the middle value when data is sorted in ascending order. It divides the dataset into two equal halves.

## Formula

```
If n is odd: Median = (n+1)/2 th value
If n is even: Median = Average of n/2 and (n/2 + 1) th values
```

## Results for Ethereum Dataset

| Variable              | Median Value   |
| --------------------- | -------------- |
| **Close**             | 1,653.84       |
| **High**              | 1,687.24       |
| **Low**               | 1,622.91       |
| **Open**              | 1,652.97       |
| **Volume**            | 12,166,684,523 |
| **Daily_Return_Pct**  | 0.06           |
| **Log_Return**        | 0.000632       |
| **Price_Range**       | 62.99          |
| **Body_Size**         | 21.24          |
| **Upper_Shadow**      | 9.68           |
| **Lower_Shadow**      | 10.86          |
| **MA_7**              | 1,657.06       |
| **MA_14**             | 1,646.15       |
| **MA_21**             | 1,653.72       |
| **MA_50**             | 1,660.70       |
| **MA_100**            | 1,712.16       |
| **MA_200**            | 1,777.46       |
| **EMA_12**            | 1,645.08       |
| **EMA_26**            | 1,645.42       |
| **MACD**              | 0.51           |
| **Signal_Line**       | 0.47           |
| **MACD_Histogram**    | 0.44           |
| **RSI_14**            | 50.09          |
| **BB_Mid**            | 1,649.79       |
| **BB_Std**            | 89.42          |
| **BB_Upper**          | 1,879.22       |
| **BB_Lower**          | 1,486.98       |
| **BB_Width**          | 357.68         |
| **Volume_MA_20**      | 13,798,765,959 |
| **Volume_Change_Pct** | -0.52          |
| **Volatility_30d**    | 3.97           |
| **Cumulative_Max**    | 4,812.09       |
| **Drawdown_Pct**      | -59.75         |

## Key Findings

1. **Median Close Price**: $1,653.84 (50% of days below, 50% above)
2. **Median Daily Return**: 0.06% (slightly positive)
3. **Median Volume**: ~12.17 billion
4. **Median RSI**: 50.09 (neutral momentum)

## Comparison: Mean vs Median

| Variable         | Mean     | Median   | Difference |
| ---------------- | -------- | -------- | ---------- |
| Close            | 1,699.02 | 1,653.84 | +45.18     |
| High             | 1,744.37 | 1,687.24 | +57.13     |
| Low              | 1,648.30 | 1,622.91 | +25.39     |
| Daily_Return_Pct | 0.17     | 0.06     | +0.11      |

## Interpretation

- For symmetric distributions, mean ≈ median
- Here, mean > median for most price variables, indicating **right-skewed distribution**
- The difference between mean and median shows the presence of high outliers (price spikes)
- Median is more robust to outliers than mean

## Visualization

See box plot visualizations in `plots/boxplot_*.png` to see median lines

## Related Measures

- [Mean](01-mean.md)
- [Mode](02-mode.md)
- [Quartiles](06-quartiles.md)
