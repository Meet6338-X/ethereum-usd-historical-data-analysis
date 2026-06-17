# Mean - Statistical Analysis (Python)

## Overview

The mean (average) is the sum of all values divided by the count of values. It represents the central tendency of the data.

## Formula

```
Mean = Σx / n
```

## Results for Ethereum Dataset

| Variable              | Mean Value        |
| --------------------- | ----------------- |
| **Close**             | 1,699.02          |
| **High**              | 1,744.37          |
| **Low**               | 1,648.30          |
| **Open**              | 1,698.45          |
| **Volume**            | 15,005,101,859.69 |
| **Daily_Return_Pct**  | 0.17              |
| **Log_Return**        | 0.000676          |
| **Price_Range**       | 96.07             |
| **Body_Size**         | 49.18             |
| **Upper_Shadow**      | 21.04             |
| **Lower_Shadow**      | 25.85             |
| **MA_7**              | 1,699.37          |
| **MA_14**             | 1,699.54          |
| **MA_21**             | 1,699.46          |
| **MA_50**             | 1,698.57          |
| **MA_100**            | 1,694.29          |
| **MA_200**            | 1,673.82          |
| **EMA_12**            | 1,694.36          |
| **EMA_26**            | 1,687.99          |
| **MACD**              | 6.37              |
| **Signal_Line**       | 6.44              |
| **MACD_Histogram**    | -0.07             |
| **RSI_14**            | 51.39             |
| **BB_Mid**            | 1,699.49          |
| **BB_Std**            | 114.22            |
| **BB_Upper**          | 1,927.93          |
| **BB_Lower**          | 1,471.04          |
| **BB_Width**          | 456.89            |
| **Volume_MA_20**      | 15,004,914,415.80 |
| **Volume_Change_Pct** | 5.01              |
| **Volatility_30d**    | 4.17              |
| **Cumulative_Max**    | 3,333.09          |
| **Drawdown_Pct**      | -54.28            |

## Key Findings

1. **Average Close Price**: The mean closing price of Ethereum is approximately **$1,699.02**
2. **Average Daily Return**: Mean daily return is **0.17%** (positive trend)
3. **Average Volume**: Trading volume averages around **15 billion** daily
4. **30-day Volatility**: Average volatility is **4.17%**

## Interpretation

- The positive mean daily return (0.17%) indicates an overall upward trend in Ethereum prices during the analyzed period
- The mean prices (Close, High, Low, Open) are all around $1,648-$1,744, showing consistency
- Moving averages (MA_7, MA_14, MA_21) are very close to each other (~1,699), indicating stable price periods

## Visualization

See histogram visualizations in `plots/histogram_*.png`

## Related Measures

- [Mode](02-mode.md)
- [Median](03-median.md)
- [Standard Deviation](04-standard-deviation.md)
