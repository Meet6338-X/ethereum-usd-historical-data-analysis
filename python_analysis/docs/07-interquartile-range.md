# Interquartile Range (IQR) - Statistical Analysis (Python)

## Overview

The Interquartile Range (IQR) is the difference between the third quartile (Q3) and first quartile (Q1). It measures the middle 50% spread of data.

## Formula

```
IQR = Q3 - Q1
```

## Results for Ethereum Dataset

| Variable              | IQR Value         |
| --------------------- | ----------------- |
| **Close**             | 2,366.83          |
| **High**              | 2,430.38          |
| **Low**               | 2,274.06          |
| **Open**              | 2,367.77          |
| **Volume**            | 13,716,683,851.75 |
| **Daily_Return_Pct**  | 4.04              |
| **Log_Return**        | 0.0404            |
| **Price_Range**       | 120.31            |
| **Body_Size**         | 59.15             |
| **Upper_Shadow**      | 26.14             |
| **Lower_Shadow**      | 30.37             |
| **MA_7**              | 2,335.48          |
| **MA_14**             | 2,351.81          |
| **MA_21**             | 2,386.83          |
| **MA_50**             | 2,444.51          |
| **MA_100**            | 2,432.90          |
| **MA_200**            | 2,501.75          |
| **EMA_12**            | 2,378.38          |
| **EMA_26**            | 2,434.92          |
| **MACD**              | 68.80             |
| **Signal_Line**       | 63.63             |
| **MACD_Histogram**    | 17.79             |
| **RSI_14**            | 18.85             |
| **BB_Mid**            | 2,378.51          |
| **BB_Std**            | 145.34            |
| **BB_Upper**          | 2,778.66          |
| **BB_Lower**          | 2,053.01          |
| **BB_Width**          | 581.36            |
| **Volume_MA_20**      | 13,376,462,536.00 |
| **Volume_Change_Pct** | 31.72             |
| **Volatility_30d**    | 1.88              |
| **Cumulative_Max**    | 3,415.67          |
| **Drawdown_Pct**      | 40.76             |

## Key Findings

1. **Close Price IQR**: $2,366.83 - middle 50% of prices span this range
2. **Daily Return IQR**: 4.04% - typical daily movement range
3. **RSI IQR**: 18.85 - spread of momentum values
4. **Volatility IQR**: 1.88% - typical 30-day volatility range

## How to Use IQR for Outlier Detection

### Method: 1.5 × IQR Rule

```
Lower Fence = Q1 - 1.5 × IQR
Upper Fence = Q3 + 1.5 × IQR
```

Values outside these fences are considered outliers.

### Example: Close Price

```
Q1 = 355.24
Q3 = 2,722.07
IQR = 2,366.83

Lower Fence = 355.24 - (1.5 × 2,366.83) = -3,195.01 (impossible)
Upper Fence = 2,722.07 + (1.5 × 2,366.83) = 6,272.32

Prices above $6,272.32 are outliers
```

## Comparison: IQR vs Range

| Metric        | Close Price | Daily Return % |
| ------------- | ----------- | -------------- |
| **Range**     | 4,747.04    | 68.80          |
| **IQR**       | 2,366.83    | 4.04           |
| **IQR/Range** | 49.9%       | 5.9%           |

- IQR is more robust to outliers than range
- IQR focuses on the middle 50% of data

## Interpretation

- **High IQR**: Large spread in middle 50% of data
- **Low IQR**: Data is clustered in the middle
- IQR is used in box plots (the "box" represents IQR)

## Visualization

- Box plots: `plots/boxplot_*.png`
- The box in box plot = IQR

## Related Measures

- [Quartiles](06-quartiles.md)
- [Range](08-range.md)
- [Standard Deviation](04-standard-deviation.md)
