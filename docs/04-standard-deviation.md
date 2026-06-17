# Standard Deviation - Statistical Analysis

## Overview
Standard deviation measures the dispersion or spread of data points from the mean. It indicates how much the values deviate from the average.

## Formula
```
σ = √[ Σ(x - μ)² / n ]
```

Where:
- σ = Standard Deviation
- x = each value
- μ = mean
- n = number of values

## Results for Ethereum Dataset

| Variable | Standard Deviation |
|----------|-------------------|
| **Close** | 1,296.93 |
| **High** | 1,330.81 |
| **Low** | 1,260.40 |
| **Open** | 1,297.30 |
| **Volume** | 12,292,076,322.32 |
| **Daily_Return_Pct** | 4.49 |
| **Log_Return** | 0.0454 |
| **Price_Range** | 106.18 |
| **Body_Size** | 70.20 |
| **Upper_Shadow** | 30.06 |
| **Lower_Shadow** | 42.52 |
| **MA_7** | 1,293.97 |
| **MA_14** | 1,290.80 |
| **MA_21** | 1,287.52 |
| **MA_50** | 1,273.94 |
| **MA_100** | 1,250.89 |
| **MA_200** | 1,192.47 |
| **EMA_12** | 1,289.32 |
| **EMA_26** | 1,279.72 |
| **MACD** | 95.16 |
| **Signal_Line** | 90.03 |
| **MACD_Histogram** | 27.49 |
| **RSI_14** | 13.63 |
| **BB_Mid** | 1,287.99 |
| **BB_Std** | 105.96 |
| **BB_Upper** | 1,449.96 |
| **BB_Lower** | 1,142.49 |
| **BB_Width** | 423.84 |
| **Volume_MA_20** | 10,754,981,715.28 |
| **Volume_Change_Pct** | 35.08 |
| **Volatility_30d** | 1.61 |
| **Cumulative_Max** | 1,665.00 |
| **Drawdown_Pct** | 26.40 |

## Key Findings

1. **Price Volatility**: Standard deviation of Close price is ~$1,297, indicating high price variability
2. **Daily Returns**: Std Dev of 4.49% shows significant daily price fluctuations
3. **Volume Variability**: Extremely high std dev (~12.29B) shows varying trading activity
4. **RSI Stability**: Lower std dev (13.63) in RSI indicates relatively stable momentum

## Interpretation Guide

| Standard Deviation | Interpretation |
|-------------------|----------------|
| Low (< 10%) | Stable/Low volatility |
| Medium (10-25%) | Moderate volatility |
| High (> 25%) | High volatility |

### For this dataset:
- **Close Price**: High absolute std dev due to price scale
- **Daily_Return_Pct**: 4.49% - moderate volatility
- **Volatility_30d**: 1.61% - relatively stable 30-day volatility

## Coefficient of Variation (CV)

CV = (σ / μ) × 100

| Variable | Mean | Std Dev | CV (%) |
|----------|------|---------|--------|
| Close | 1,699.02 | 1,296.93 | 76.3% |
| Daily_Return_Pct | 0.17 | 4.49 | 2641% |
| RSI_14 | 51.39 | 13.63 | 26.5% |

High CV indicates high relative variability

## Visualization

See density plots in `/plots/density_*.png` to see spread of values

## Related Measures

- [Mean](01-mean.md)
- [Variance](05-variance.md)
- [Range](08-range.md)
