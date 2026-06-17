# Range - Statistical Analysis

## Overview
The range is the difference between the maximum and minimum values in a dataset. It represents the total spread of data.

## Formula
```
Range = Maximum - Minimum
```

## Results for Ethereum Dataset

| Variable | Minimum | Maximum | Range |
|----------|---------|---------|-------|
| **Close** | 84.31 | 4,831.35 | 4,747.04 |
| **High** | 85.34 | 4,953.73 | 4,868.39 |
| **Low** | 82.83 | 4,718.04 | 4,635.21 |
| **Open** | 84.28 | 4,831.09 | 4,746.81 |
| **Volume** | 621,732,992 | 97,736,621,123 | 97,114,888,131 |
| **Daily_Return_Pct** | -42.35 | 26.46 | 68.80 |
| **Log_Return** | -0.551 | 0.235 | 0.785 |
| **Price_Range** | 1.22 | 1,485.48 | 1,484.26 |
| **Body_Size** | 0.00 | 921.98 | 921.98 |
| **Upper_Shadow** | 0.00 | 321.22 | 321.22 |
| **Lower_Shadow** | 0.00 | 708.80 | 708.80 |
| **MA_7** | 87.40 | 4,694.09 | 4,606.69 |
| **MA_14** | 91.55 | 4,626.70 | 4,535.15 |
| **MA_21** | 98.20 | 4,519.91 | 4,421.71 |
| **MA_50** | 118.23 | 4,407.52 | 4,289.29 |
| **MA_100** | 120.96 | 4,198.25 | 4,077.29 |
| **MA_200** | 143.35 | 3,671.87 | 3,528.52 |
| **EMA_12** | 92.60 | 4,597.79 | 4,505.19 |
| **EMA_26** | 107.81 | 4,444.10 | 4,336.29 |
| **MACD** | -323.65 | 454.41 | 778.06 |
| **Signal_Line** | -288.69 | 391.72 | 680.41 |
| **MACD_Histogram** | -228.00 | 104.36 | 332.36 |
| **RSI_14** | 15.69 | 90.33 | 74.64 |
| **BB_Mid** | 97.27 | 4,531.54 | 4,434.27 |
| **BB_Std** | 2.50 | 670.95 | 668.45 |
| **BB_Upper** | 118.07 | 5,022.10 | 4,904.03 |
| **BB_Lower** | 64.66 | 4,191.68 | 4,127.02 |
| **BB_Width** | 10.00 | 2,683.80 | 2,673.80 |
| **Volume_MA_20** | 1,118,925,837 | 54,730,579,179 | 53,611,653,342 |
| **Volume_Change_Pct** | -72.69 | 282.70 | 355.39 |
| **Volatility_30d** | 0.81 | 11.02 | 10.22 |
| **Cumulative_Max** | 320.88 | 4,831.35 | 4,510.47 |
| **Drawdown_Pct** | -93.96 | 0.00 | 93.96 |

## Key Findings

1. **Price Range**: Ethereum ranged from $84.31 to $4,831.35 (Range: $4,747.04)
2. **Daily Return Range**: From -42.35% to +26.46% (Range: 68.80%)
3. **Volume Range**: 621M to 97.7B (massive range in trading activity)
4. **RSI Range**: 15.69 to 90.33 (full range from oversold to overbought)

## Price Analysis

| Metric | Value |
|--------|-------|
| All-time Low | $84.31 |
| All-time High | $4,831.35 |
| Total Range | $4,747.04 |
| % Increase | 5,631% |

## Return Analysis

| Metric | Value |
|--------|-------|
| Worst Day | -42.35% |
| Best Day | +26.46% |
| Range | 68.80% |

## Volatility Analysis

| Metric | Daily Return | 30-day Volatility |
|--------|-------------|-------------------|
| Minimum | -42.35% | 0.81% |
| Maximum | +26.46% | 11.02% |
| Range | 68.80% | 10.22% |

## Limitations of Range

1. **Sensitive to Outliers**: Only uses two values (min/max)
- Example: One extreme day can vastly inflate the range

2. **Doesn't Show Distribution**: Doesn't tell us how data is spread

3. **Better Alternatives**:
- Interquartile Range (IQR) - middle 50%
- Standard Deviation - average deviation

## Comparison

| Measure | Price Range | Interpretation |
|---------|-------------|----------------|
| Range | $4,747.04 | Total spread |
| IQR | $2,366.83 | Middle 50% |
| Std Dev | $1,296.93 | Average deviation |

## Visualization

- Range is shown as whiskers in box plots: `/plots/boxplot_*.png`
- Min/Max visible in histograms: `/plots/histogram_*.png`

## Related Measures

- [Interquartile Range (IQR)](07-interquartile-range.md)
- [Standard Deviation](04-standard-deviation.md)
- [Quartiles](06-quartiles.md)
