# Charts and Visualizations (Python)

## Overview

This project includes 40+ different charts and visualizations to help understand the Ethereum USD dataset.

## Types of Charts Created

### 1. Histograms (10 charts)

Histograms show the frequency distribution of data.

| Chart          | File                             | Description                     |
| -------------- | -------------------------------- | ------------------------------- |
| Close Price    | `histogram_Close.png`            | Distribution of closing prices  |
| High Price     | `histogram_High.png`             | Distribution of daily highs     |
| Low Price      | `histogram_Low.png`              | Distribution of daily lows      |
| Open Price     | `histogram_Open.png`             | Distribution of opening prices  |
| Volume         | `histogram_Volume.png`           | Trading volume distribution     |
| Daily Return   | `histogram_Daily_Return_Pct.png` | Daily return distribution       |
| Log Return     | `histogram_Log_Return.png`       | Logarithmic return distribution |
| RSI-14         | `histogram_RSI_14.png`           | RSI momentum distribution       |
| MACD           | `histogram_MACD.png`             | MACD indicator distribution     |
| Volatility-30d | `histogram_Volatility_30d.png`   | 30-day volatility distribution  |

### 2. Box Plots (11 charts)

Box plots show quartiles, median, and outliers.

| Chart          | File                           | Description                |
| -------------- | ------------------------------ | -------------------------- |
| Close Price    | `boxplot_Close.png`            | Close price quartiles      |
| High Price     | `boxplot_High.png`             | High price quartiles       |
| Low Price      | `boxplot_Low.png`              | Low price quartiles        |
| Open Price     | `boxplot_Open.png`             | Open price quartiles       |
| Volume         | `boxplot_Volume.png`           | Volume distribution        |
| Daily Return   | `boxplot_Daily_Return_Pct.png` | Daily return distribution  |
| Log Return     | `boxplot_Log_Return.png`       | Log return distribution    |
| RSI-14         | `boxplot_RSI_14.png`           | RSI distribution           |
| MACD           | `boxplot_MACD.png`             | MACD distribution          |
| Volatility-30d | `boxplot_Volatility_30d.png`   | Volatility distribution    |
| Combined       | `boxplot_combined.png`         | All key metrics comparison |

### 3. Density Plots (10 charts)

Density plots show the probability density function.

| Chart          | File                           |
| -------------- | ------------------------------ |
| Close Price    | `density_Close.png`            |
| High Price     | `density_High.png`             |
| Low Price      | `density_Low.png`              |
| Open Price     | `density_Open.png`             |
| Volume         | `density_Volume.png`           |
| Daily Return   | `density_Daily_Return_Pct.png` |
| Log Return     | `density_Log_Return.png`       |
| RSI-14         | `density_RSI_14.png`           |
| MACD           | `density_MACD.png`             |
| Volatility-30d | `density_Volatility_30d.png`   |

### 4. Scatter Plots (2 charts)

Scatter plots show relationships between two variables.

| Chart                 | File                             | Description                  |
| --------------------- | -------------------------------- | ---------------------------- |
| Close vs Volume       | `scatter_close_volume.png`       | Price vs Volume relationship |
| Close vs Daily Return | `scatter_close_daily_return.png` | Price vs Return relationship |

### 5. Bar Charts (2 charts)

Bar charts show categorical comparisons.

| Chart           | File                        | Description            |
| --------------- | --------------------------- | ---------------------- |
| Yearly Average  | `bar_yearly_avg_close.png`  | Average close by year  |
| Monthly Average | `bar_monthly_avg_close.png` | Average close by month |

### 6. Q-Q Plots (3 charts)

Q-Q plots assess normality of distributions.

| Chart        | File                          |
| ------------ | ----------------------------- |
| Close        | `qqplot_Close.png`            |
| Daily Return | `qqplot_Daily_Return_Pct.png` |
| Volume       | `qqplot_Volume.png`           |

### 7. Other Charts

| Chart               | File                      | Description           |
| ------------------- | ------------------------- | --------------------- |
| Correlation Heatmap | `correlation_heatmap.png` | Variable correlations |

## Chart Interpretation

### Histogram Reading

- **X-axis**: Value ranges
- **Y-axis**: Frequency/count
- Shows shape: symmetric, skewed left, skewed right

### Box Plot Reading

- **Box**: IQR (Q1 to Q3)
- **Line in box**: Median (Q2)
- **Whiskers**: Min and Max (within 1.5×IQR)
- **Dots**: Outliers

### Density Plot Reading

- Shows probability density
- Area under curve = 1
- Peaks indicate most common values

### Scatter Plot Reading

- Points show individual observations
- Trend line shows relationship
- Clustering indicates correlation

## Key Visual Insights

### 1. Price Distribution

- Right-skewed distribution (long tail to high prices)
- Most common prices around $300-$500

### 2. Return Distribution

- Approximately normal with fat tails
- Extreme values (outliers) present

### 3. Volume Distribution

- Highly right-skewed
- Most days have moderate volume

### 4. RSI Distribution

- Fairly uniform distribution
- Centered around 50

### 5. Correlation Insights

- Close price correlates with Volume (0.58)
- Technical indicators show expected patterns

## File Location

All charts are stored in: `plots/`

## Dashboard Integration

All charts are integrated into the HTML dashboard: `dashboard.html`

## Related Measures

- [Mean](01-mean.md)
- [Median](03-median.md)
- [Standard Deviation](04-standard-deviation.md)
- [Quartiles](06-quartiles.md)
- [Range](08-range.md)
