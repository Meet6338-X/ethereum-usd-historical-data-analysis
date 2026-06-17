# Ethereum USD Statistical Analysis Project

A comprehensive statistical analysis of Ethereum USD historical price data using R programming language.

## 📊 Project Overview

This project performs complete statistical analysis on the Ethereum USD historical dataset, covering all required statistical measures and hypothesis testing.

## 📁 Project Structure

```
ethereum_usd_historical_dataset/
├── README.md                     # This file
├── analysis.R                    # Main R script for analysis
├── ethereum_statistics.Rproj     # R Project file
├── dashboard.html                # Modern HTML/CSS dashboard
├── descriptive_statistics.csv    # All statistical measures
├── correlation_matrix.csv        # Correlation analysis
├── hypothesis_test_results.txt   # Hypothesis test results
├── plots/                       # All visualization files
│   ├── histogram_*.png           # 10 histogram charts
│   ├── boxplot_*.png            # 11 box plot charts
│   ├── density_*.png            # 10 density charts
│   ├── scatter_*.png            # 2 scatter plots
│   ├── bar_*.png                # 2 bar charts
│   ├── qqplot_*.png             # 3 Q-Q plots
│   └── correlation_heatmap.png  # Correlation heatmap
└── docs/                        # Documentation files
    ├── 01-mean.md
    ├── 02-mode.md
    ├── 03-median.md
    ├── 04-standard-deviation.md
    ├── 05-variance.md
    ├── 06-quartiles.md
    ├── 07-interquartile-range.md
    ├── 08-range.md
    ├── 09-charts.md
    ├── 10-hypothesis-testing.md
    └── r-machine-learning-book.md  # Complete R & ML Tutorial
```

## 📈 Statistical Measures Calculated

| # | Measure | Description | File |
|---|---------|-------------|------|
| 1 | **Mean** | Average value across all data points | [docs/01-mean.md](docs/01-mean.md) |
| 2 | **Mode** | Most frequently occurring value | [docs/02-mode.md](docs/02-mode.md) |
| 3 | **Median** | Middle value in sorted data | [docs/03-median.md](docs/03-median.md) |
| 4 | **Standard Deviation** | Measure of data spread | [docs/04-standard-deviation.md](docs/04-standard-deviation.md) |
| 5 | **Variance** | Squared deviation from mean | [docs/05-variance.md](docs/05-variance.md) |
| 6 | **Quartiles** | Q1, Q2 (Median), Q3 | [docs/06-quartiles.md](docs/06-quartiles.md) |
| 7 | **Interquartile Range (IQR)** | Q3 - Q1 | [docs/07-interquartile-range.md](docs/07-interquartile-range.md) |
| 8 | **Range** | Max - Min | [docs/08-range.md](docs/08-range.md) |
| 9 | **Charts** | 40+ visualizations | [docs/09-charts.md](docs/09-charts.md) |
| 10 | **Hypothesis Testing** | 5 statistical tests | [docs/10-hypothesis-testing.md](docs/10-hypothesis-testing.md) |
| 11 | **R & ML Tutorial** | Complete learning guide | [docs/r-machine-learning-book.md](docs/r-machine-learning-book.md) |

## 📊 Dataset Information

- **Source**: ethereum_usd_historical_dataset.csv
- **Records**: 3,006 data points
- **Variables**: 39 columns (33 numeric analyzed)
- **Time Period**: 2017-2024

### Key Variables Analyzed

| Variable | Description |
|----------|-------------|
| Close | Closing price |
| High | Highest price |
| Low | Lowest price |
| Open | Opening price |
| Volume | Trading volume |
| Daily_Return_Pct | Daily return percentage |
| Log_Return | Logarithmic return |
| RSI_14 | 14-day Relative Strength Index |
| MACD | Moving Average Convergence Divergence |
| Volatility_30d | 30-day volatility |

## 🔬 Hypothesis Tests Performed

1. **One-Sample T-Test**: Mean daily return ≠ 0
2. **Two-Sample T-Test**: 2021 vs 2022 Close prices
3. **Correlation Test**: Close price vs Volume correlation
4. **Paired T-Test**: High vs Low prices
5. **Chi-Square Test**: Day of Week vs Price Movement

## 📚 R & Machine Learning Tutorial

A comprehensive guide to learning R programming and Machine Learning is available in [docs/r-machine-learning-book.md](docs/r-machine-learning-book.md).

### Tutorial Covers:
- ✅ R programming basics
- ✅ Data types and structures  
- ✅ Statistical analysis
- ✅ Data visualization (ggplot2)
- ✅ Machine learning fundamentals
- ✅ Supervised learning (Regression, Classification)
- ✅ Unsupervised learning (Clustering, PCA)
- ✅ Model evaluation
- ✅ Real-world projects

---

## 🚀 How to Run

### Using RStudio
1. Open `ethereum_statistics.Rproj` in RStudio
2. Open `analysis.R`
3. Click "Source" or press Ctrl+Shift+Enter

### Using Command Line
```bash
Rscript analysis.R
```

## 📊 Dashboard

Open `dashboard.html` in any web browser to view the beautiful interactive dashboard with all statistics and visualizations.

## 📝 Output Files

- `descriptive_statistics.csv` - Complete statistics table
- `correlation_matrix.csv` - Variable correlations
- `hypothesis_test_results.txt` - Test results
- `plots/` - All visualization images

## 🛠 Technologies Used

- **R** - Statistical computing
- **HTML/CSS** - Dashboard design
- **Base R Graphics** - Chart generation

## 📄 License

This project is for educational purposes.

## 👤 Author

Statistical Analysis Project - Ethereum USD Dataset
