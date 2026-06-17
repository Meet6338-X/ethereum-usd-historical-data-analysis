# Variance - Statistical Analysis

## Overview
Variance measures the average squared deviation of each number from the mean. It quantifies the spread of data points.

## Formula
```
Variance = Σ(x - μ)² / n
```

Where:
- x = each value
- μ = mean
- n = number of values

## Results for Ethereum Dataset

| Variable | Variance |
|----------|----------|
| **Close** | 1,682,018.26 |
| **High** | 1,771,064.46 |
| **Low** | 1,588,608.35 |
| **Open** | 1,682,986.80 |
| **Volume** | 151,095,140,313,757,000,000 |
| **Daily_Return_Pct** | 20.16 |
| **Log_Return** | 0.00206 |
| **Price_Range** | 11,274.91 |
| **Body_Size** | 4,928.33 |
| **Upper_Shadow** | 903.55 |
| **Lower_Shadow** | 1,808.10 |
| **MA_7** | 1,674,356.01 |
| **MA_14** | 1,666,153.39 |
| **MA_21** | 1,657,718.56 |
| **MA_50** | 1,622,926.96 |
| **MA_100** | 1,564,727.24 |
| **MA_200** | 1,421,995.04 |
| **EMA_12** | 1,662,339.18 |
| **EMA_26** | 1,637,673.60 |
| **MACD** | 9,054.75 |
| **Signal_Line** | 8,105.57 |
| **MACD_Histogram** | 755.82 |
| **RSI_14** | 185.82 |
| **BB_Mid** | 1,658,921.76 |
| **BB_Std** | 11,227.61 |
| **BB_Upper** | 2,102,376.47 |
| **BB_Lower** | 1,305,287.94 |
| **BB_Width** | 179,641.76 |
| **Volume_MA_20** | 115,669,631,696,050,000,000 |
| **Volume_Change_Pct** | 1,230.67 |
| **Volatility_30d** | 2.60 |
| **Cumulative_Max** | 2,772,232.64 |
| **Drawdown_Pct** | 697.08 |

## Key Findings

1. **Price Variance**: Close price variance of ~1.68 million shows high price dispersion
2. **Daily Returns**: Variance of 20.16 indicates significant daily price movement
3. **Volume Variance**: Extremely high variance due to large scale
4. **RSI Variance**: 185.82 shows moderate spread in momentum values

## Relationship: Variance vs Standard Deviation

Variance is the square of standard deviation:

```
Variance = Standard Deviation²
```

| Variable | Std Dev | Variance | Verification |
|----------|---------|----------|--------------|
| Close | 1,296.93 | 1,682,018.26 | ✓ (1,296.93² ≈ 1,682,018) |
| Daily_Return_Pct | 4.49 | 20.16 | ✓ (4.49² ≈ 20.16) |
| RSI_14 | 13.63 | 185.82 | ✓ (13.63² ≈ 185.82) |

## Interpretation

- **High Variance**: Data points are widely spread from the mean
- **Low Variance**: Data points are clustered near the mean
- Variance is always non-negative (≥ 0)

## Use Cases

1. **Risk Assessment**: Higher variance = higher risk in financial data
2. **Portfolio Theory**: Variance used to calculate volatility
3. **Quality Control**: Lower variance indicates more consistent processes

## Visualization

See histogram and density plots to visualize spread:
- `/plots/histogram_*.png`
- `/plots/density_*.png`

## Related Measures

- [Standard Deviation](04-standard-deviation.md)
- [Mean](01-mean.md)
- [Range](08-range.md)
