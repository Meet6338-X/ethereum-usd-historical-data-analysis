# =============================================================================
# Ethereum USD Historical Dataset - Statistical Analysis (Python Version)
# =============================================================================
# This script performs comprehensive statistical analysis on the Ethereum USD
# historical dataset including:
# - Descriptive Statistics (Mean, Mode, Median, SD, Variance, Quartiles, IQR, Range)
# - Data Visualization (Histograms, Box Plots, Density Plots, etc.)
# - Hypothesis Testing
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

# Set the style for plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Create output directory for plots
os.makedirs('plots', exist_ok=True)

# Load the dataset
print("Loading Ethereum USD Historical Dataset...")
data = pd.read_csv('../ethereum_usd_historical_dataset.csv')

# Display basic information about the dataset
print("\n=== DATASET OVERVIEW ===")
print(f"Number of rows: {len(data)}")
print(f"Number of columns: {len(data.columns)}")
print("\nColumn names:")
print(list(data.columns))

# Identify numeric columns
numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
print(f"\n=== NUMERIC COLUMNS IDENTIFIED ===")
print(f"Total numeric columns: {len(numeric_cols)}")
print(numeric_cols)

# Remove non-meaningful numeric columns (like Year, Month, etc. that are identifiers)
# Keep actual data columns
meaningless_cols = ['Year', 'Month', 'Quarter', 'Week_Number', 'Day_of_Week']
meaningful_numeric_cols = [col for col in numeric_cols if col not in meaningless_cols]
print(f"\n=== MEANINGFUL NUMERIC COLUMNS FOR ANALYSIS ===")
print(meaningful_numeric_cols)

# =============================================================================
# FUNCTION DEFINITIONS
# =============================================================================

def get_mode(x):
    """Calculate mode of a series, handling NaN values"""
    x_clean = x.dropna()
    if len(x_clean) == 0:
        return np.nan
    mode_result = x_clean.mode()
    return mode_result.iloc[0] if not mode_result.empty else np.nan

def skewness_base(x):
    """Calculate skewness using base Python (similar to R's moments package)"""
    x_clean = x.dropna()
    if len(x_clean) < 3:
        return np.nan
    m3 = np.sum((x_clean - np.mean(x_clean))**3) / len(x_clean)
    m2 = np.sum((x_clean - np.mean(x_clean))**2) / len(x_clean)
    return m3 / (m2**(3/2)) if m2 != 0 else 0

def kurtosis_base(x):
    """Calculate kurtosis using base Python"""
    x_clean = x.dropna()
    if len(x_clean) < 4:
        return np.nan
    m4 = np.sum((x_clean - np.mean(x_clean))**4) / len(x_clean)
    m2 = np.sum((x_clean - np.mean(x_clean))**2) / len(x_clean)
    return m4 / (m2**2) - 3 if m2 != 0 else -3

def calculate_stats(series, col_name):
    """Calculate comprehensive statistics for a column"""
    x = series.dropna()
    if len(x) == 0:
        return pd.DataFrame({
            'Column': [col_name],
            'Mean': [np.nan],
            'Median': [np.nan],
            'Mode': [np.nan],
            'Std_Dev': [np.nan],
            'Variance': [np.nan],
            'Q1': [np.nan],
            'Q2': [np.nan],
            'Q3': [np.nan],
            'IQR': [np.nan],
            'Min': [np.nan],
            'Max': [np.nan],
            'Range': [np.nan],
            'Skewness': [np.nan],
            'Kurtosis': [np.nan]
        })
    
    # Calculate statistics
    mean_val = np.mean(x)
    median_val = np.median(x)
    mode_val = get_mode(x)
    sd_val = np.std(x, ddof=1)  # Sample standard deviation
    var_val = np.var(x, ddof=1)  # Sample variance
    q1_val = np.percentile(x, 25)
    q2_val = np.percentile(x, 50)
    q3_val = np.percentile(x, 75)
    iqr_val = q3_val - q1_val
    min_val = np.min(x)
    max_val = np.max(x)
    range_val = max_val - min_val
    skew_val = skewness_base(x)
    kurt_val = kurtosis_base(x)
    
    return pd.DataFrame({
        'Column': [col_name],
        'Mean': [mean_val],
        'Median': [median_val],
        'Mode': [mode_val],
        'Std_Dev': [sd_val],
        'Variance': [var_val],
        'Q1': [q1_val],
        'Q2': [q2_val],
        'Q3': [q3_val],
        'IQR': [iqr_val],
        'Min': [min_val],
        'Max': [max_val],
        'Range': [range_val],
        'Skewness': [skew_val],
        'Kurtosis': [kurt_val]
    })

# =============================================================================
# DESCRIPTIVE STATISTICS CALCULATION
# =============================================================================

print("\n\n")
print("################################################################################")
print("#                     DESCRIPTIVE STATISTICS ANALYSIS                          #")
print("################################################################################\n")

# Calculate statistics for all meaningful numeric columns
all_stats = pd.DataFrame()
for col in meaningful_numeric_cols:
    if col in data.columns:
        col_stats = calculate_stats(data[col], col)
        all_stats = pd.concat([all_stats, col_stats], ignore_index=True)

# Display statistics
print("=== MEAN ===")
print(all_stats[['Column', 'Mean']].to_string(index=False))

print("\n=== MODE ===")
print(all_stats[['Column', 'Mode']].to_string(index=False))

print("\n=== MEDIAN ===")
print(all_stats[['Column', 'Median']].to_string(index=False))

print("\n=== STANDARD DEVIATION ===")
print(all_stats[['Column', 'Std_Dev']].to_string(index=False))

print("\n=== VARIANCE ===")
print(all_stats[['Column', 'Variance']].to_string(index=False))

print("\n=== QUARTILES ===")
print(all_stats[['Column', 'Q1', 'Q2', 'Q3']].to_string(index=False))

print("\n=== INTERQUARTILE RANGE (IQR) ===")
print(all_stats[['Column', 'IQR']].to_string(index=False))

print("\n=== RANGE ===")
print(all_stats[['Column', 'Min', 'Max', 'Range']].to_string(index=False))

# Save statistics to CSV
all_stats.to_csv('descriptive_statistics.csv', index=False)
print("\nDescriptive statistics saved to 'descriptive_statistics.csv'")

# Print full statistics table
print("\n=== COMPLETE STATISTICS TABLE ===")
print(all_stats.to_string(index=False))

# =============================================================================
# DATA VISUALIZATION
# =============================================================================

print("\n\n")
print("################################################################################")
print("#                           DATA VISUALIZATION                                 #")
print("################################################################################\n")

# Select key fields for visualization
key_fields = ["Close", "High", "Low", "Open", "Volume", "Daily_Return_Pct", 
              "Log_Return", "Volatility_30d", "RSI_14", "MACD"]
key_fields = [field for field in key_fields if field in meaningful_numeric_cols]

# 1. HISTOGRAMS
print("Creating Histograms...")
for field in key_fields:
    if field in data.columns:
        plt.figure(figsize=(10, 8))
        plt.hist(data[field].dropna(), bins=30, alpha=0.7, color='steelblue', edgecolor='white', density=True)
        plt.title(f'Histogram of {field}')
        plt.xlabel(field)
        plt.ylabel('Density')
        
        # Add density curve
        from scipy.stats import gaussian_kde
        data_clean = data[field].dropna()
        if len(data_clean) > 1:
            kde = gaussian_kde(data_clean)
            x_range = np.linspace(data_clean.min(), data_clean.max(), 1000)
            plt.plot(x_range, kde(x_range), 'r-', linewidth=2, label='Density')
            
            # Add mean and median lines
            plt.axvline(np.mean(data_clean), color='green', linestyle='--', linewidth=2, label='Mean')
            plt.axvline(np.median(data_clean), color='orange', linestyle='--', linewidth=2, label='Median')
        
        plt.legend()
        plt.tight_layout()
        plt.savefig(f'plots/histogram_{field}.png', dpi=300, bbox_inches='tight')
        plt.close()

# 2. BOX PLOTS
print("Creating Box Plots...")
for field in key_fields:
    if field in data.columns:
        plt.figure(figsize=(10, 8))
        box_plot = plt.boxplot(data[field].dropna(), patch_artist=True)
        box_plot['boxes'][0].set_facecolor('steelblue')
        box_plot['boxes'][0].set_edgecolor('black')
        plt.title(f'Box Plot of {field}')
        plt.ylabel(field)
        
        # Add mean point
        mean_val = np.mean(data[field].dropna())
        plt.scatter([1], [mean_val], color='red', s=100, zorder=3, label='Mean')
        plt.legend()
        plt.tight_layout()
        plt.savefig(f'plots/boxplot_{field}.png', dpi=300, bbox_inches='tight')
        plt.close()

# Combined box plot for multiple fields
plt.figure(figsize=(14, 10))
data_key = data[key_fields].dropna()
box_plot = plt.boxplot([data_key[col] for col in key_fields], patch_artist=True, tick_labels=key_fields)
colors = plt.cm.rainbow(np.linspace(0, 1, len(key_fields)))
for patch, color in zip(box_plot['boxes'], colors):
    patch.set_facecolor(color)
plt.title('Box Plots of Key Ethereum Metrics')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('plots/boxplot_combined.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. DENSITY PLOTS
print("Creating Density Plots...")
for field in key_fields:
    if field in data.columns:
        plt.figure(figsize=(10, 8))
        data_clean = data[field].dropna()
        if len(data_clean) > 1:
            from scipy.stats import gaussian_kde
            kde = gaussian_kde(data_clean)
            x_range = np.linspace(data_clean.min(), data_clean.max(), 1000)
            plt.plot(x_range, kde(x_range), 'b-', linewidth=2)
            plt.fill_between(x_range, kde(x_range), alpha=0.3, color='steelblue')
            plt.title(f'Density Plot of {field}')
            plt.xlabel(field)
            plt.ylabel('Density')
        plt.tight_layout()
        plt.savefig(f'plots/density_{field}.png', dpi=300, bbox_inches='tight')
        plt.close()

# 4. BAR CHARTS (for categorical summaries)
print("Creating Bar Charts...")

# Monthly average close price
if 'Month' in data.columns and 'Close' in data.columns:
    monthly_avg = data.groupby('Month')['Close'].mean().reset_index()
    plt.figure(figsize=(10, 8))
    plt.bar(monthly_avg['Month'], monthly_avg['Close'], color='steelblue', edgecolor='white')
    plt.title('Average Close Price by Month')
    plt.xlabel('Month')
    plt.ylabel('Average Close Price')
    plt.tight_layout()
    plt.savefig('plots/bar_monthly_avg_close.png', dpi=300, bbox_inches='tight')
    plt.close()

# Yearly average close price
if 'Year' in data.columns and 'Close' in data.columns:
    yearly_avg = data.groupby('Year')['Close'].mean().reset_index()
    plt.figure(figsize=(10, 8))
    plt.bar(yearly_avg['Year'], yearly_avg['Close'], color='coral', edgecolor='white')
    plt.title('Average Close Price by Year')
    plt.xlabel('Year')
    plt.ylabel('Average Close Price')
    plt.tight_layout()
    plt.savefig('plots/bar_yearly_avg_close.png', dpi=300, bbox_inches='tight')
    plt.close()

# 5. SCATTER PLOTS
print("Creating Scatter Plots...")

# Close vs Volume
if 'Close' in data.columns and 'Volume' in data.columns:
    plt.figure(figsize=(10, 8))
    plt.scatter(data['Close'], data['Volume'], alpha=0.5, color='steelblue', s=20)
    plt.title('Close Price vs Volume')
    plt.xlabel('Close Price')
    plt.ylabel('Volume')
    
    # Add trend line
    z = np.polyfit(data['Close'].dropna(), data['Volume'].dropna(), 1)
    p = np.poly1d(z)
    plt.plot(data['Close'], p(data['Close']), "r--", alpha=0.8, linewidth=2)
    plt.tight_layout()
    plt.savefig('plots/scatter_close_volume.png', dpi=300, bbox_inches='tight')
    plt.close()

# Close vs Daily Return
if 'Close' in data.columns and 'Daily_Return_Pct' in data.columns:
    valid_idx = data['Close'].notna() & data['Daily_Return_Pct'].notna()
    plt.figure(figsize=(10, 8))
    plt.scatter(data.loc[valid_idx, 'Close'], data.loc[valid_idx, 'Daily_Return_Pct'], 
                alpha=0.7, color='coral', s=20)
    plt.title('Close Price vs Daily Return')
    plt.xlabel('Close Price')
    plt.ylabel('Daily Return (%)')
    
    # Add trend line
    z = np.polyfit(data.loc[valid_idx, 'Close'], data.loc[valid_idx, 'Daily_Return_Pct'], 1)
    p = np.poly1d(z)
    plt.plot(data.loc[valid_idx, 'Close'], p(data.loc[valid_idx, 'Close']), "b--", alpha=0.8, linewidth=2)
    plt.tight_layout()
    plt.savefig('plots/scatter_close_daily_return.png', dpi=300, bbox_inches='tight')
    plt.close()

# 6. CORRELATION MATRIX HEATMAP
print("Creating Correlation Heatmap...")
plt.figure(figsize=(12, 10))
cor_matrix = data[key_fields].corr()
sns.heatmap(cor_matrix, annot=True, cmap='coolwarm', center=0, square=True, linewidths=0.5)
plt.title('Correlation Matrix of Key Ethereum Metrics')
plt.tight_layout()
plt.savefig('plots/correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# Save correlation matrix
cor_matrix.to_csv('correlation_matrix.csv')
print("Correlation matrix saved to 'correlation_matrix.csv'")

# 7. Q-Q PLOTS for key fields
print("Creating Q-Q Plots...")
for field in ["Close", "Daily_Return_Pct", "Volume"]:
    if field in data.columns:
        plt.figure(figsize=(10, 8))
        data_clean = data[field].dropna()
        if len(data_clean) > 0:
            from scipy import stats as sp_stats
            sp_stats.probplot(data_clean, dist="norm", plot=plt)
            plt.title(f'Q-Q Plot of {field}')
        plt.tight_layout()
        plt.savefig(f'plots/qqplot_{field}.png', dpi=300, bbox_inches='tight')
        plt.close()

print("\nAll visualizations saved to 'plots/' directory")

# =============================================================================
# HYPOTHESIS TESTING
# =============================================================================

print("\n\n")
print("################################################################################")
print("#                        HYPOTHESIS TESTING                                    #")
print("################################################################################\n")

# Test 1: One-sample t-test - Is the mean daily return significantly different from 0?
print("\n=== HYPOTHESIS TEST 1: One-Sample T-Test ===")
print("Question: Is the mean daily return significantly different from 0?\n")
print("H0: Mean daily return = 0")
print("H1: Mean daily return != 0\n")

daily_return = data['Daily_Return_Pct'].dropna()
t_test_result = stats.ttest_1samp(daily_return, 0)
print("Test Results:")
print(f"t-statistic: {t_test_result.statistic:.6f}")
print(f"p-value: {t_test_result.pvalue:.6f}")
print(f"degrees of freedom: {len(daily_return)-1}")

if t_test_result.pvalue < 0.05:
    print("\nConclusion: At 5% significance level, we REJECT the null hypothesis.")
    print("The mean daily return is significantly different from 0.")
else:
    print("\nConclusion: At 5% significance level, we FAIL TO REJECT the null hypothesis.")
    print("There is no significant evidence that the mean daily return is different from 0.")

# Test 2: Two-sample t-test - Is there a significant difference between Close prices in different years?
print("\n\n=== HYPOTHESIS TEST 2: Two-Sample T-Test ===")
print("Question: Is there a significant difference in Close prices between 2021 and 2022?\n")

close_2021 = data[data['Year'] == 2021]['Close'].dropna()
close_2022 = data[data['Year'] == 2022]['Close'].dropna()

print("H0: Mean Close price in 2021 = Mean Close price in 2022")
print("H1: Mean Close price in 2021 != Mean Close price in 2022\n")
print("Sample sizes:")
print(f"2021: {len(close_2021)}")
print(f"2022: {len(close_2022)}\n")

t_test_2 = stats.ttest_ind(close_2021, close_2022, equal_var=False)
print("Test Results:")
print(f"t-statistic: {t_test_2.statistic:.6f}")
print(f"p-value: {t_test_2.pvalue:.6f}")
print(f"degrees of freedom: {t_test_2.df:.2f}")

if t_test_2.pvalue < 0.05:
    print("\nConclusion: At 5% significance level, we REJECT the null hypothesis.")
    print("There is a significant difference in Close prices between 2021 and 2022.")
else:
    print("\nConclusion: At 5% significance level, we FAIL TO REJECT the null hypothesis.")
    print("There is no significant difference in Close prices between 2021 and 2022.")

# Test 3: Correlation Test - Is there a significant correlation between Close price and Volume?
print("\n\n=== HYPOTHESIS TEST 3: Correlation Test ===")
print("Question: Is there a significant correlation between Close price and Volume?\n")

valid_corr = data[['Close', 'Volume']].dropna()
close_corr = valid_corr['Close']
volume_corr = valid_corr['Volume']

print("H0: Correlation between Close and Volume = 0")
print("H1: Correlation between Close and Volume != 0\n")

cor_test_result = stats.pearsonr(close_corr, volume_corr)
print("Test Results:")
print(f"Correlation coefficient: {cor_test_result[0]:.6f}")
print(f"p-value: {cor_test_result[1]:.6f}")

if cor_test_result[1] < 0.05:
    print("\nConclusion: At 5% significance level, we REJECT the null hypothesis.")
    print("There is a significant correlation between Close price and Volume.")
else:
    print("\nConclusion: At 5% significance level, we FAIL TO REJECT the null hypothesis.")
    print("There is no significant correlation between Close price and Volume.")

# Test 4: Paired t-test - Is there a significant difference between High and Low prices?
print("\n\n=== HYPOTHESIS TEST 4: Paired T-Test ===")
print("Question: Is there a significant difference between High and Low prices?\n")

print("H0: Mean High price = Mean Low price")
print("H1: Mean High price != Mean Low price\n")

paired_test = stats.ttest_rel(data['High'].dropna(), data['Low'].dropna())
print("Test Results:")
print(f"t-statistic: {paired_test.statistic:.6f}")
print(f"p-value: {paired_test.pvalue:.6f}")
print(f"degrees of freedom: {len(data)-1}")

if paired_test.pvalue < 0.05:
    print("\nConclusion: At 5% significance level, we REJECT the null hypothesis.")
    print("There is a significant difference between High and Low prices.")
else:
    print("\nConclusion: At 5% significance level, we FAIL TO REJECT the null hypothesis.")
    print("There is no significant difference between High and Low prices.")

# Test 5: Chi-Square Test - Is there a relationship between Day of Week and Price Movement?
print("\n\n=== HYPOTHESIS TEST 5: Chi-Square Test ===")
print("Question: Is there a significant relationship between Day of Week and Price Movement direction?\n")

# Create price movement categories (only for non-NA values)
valid_idx = data['Daily_Return_Pct'].notna()
price_movement = np.where(data.loc[valid_idx, 'Daily_Return_Pct'] > 0, "Up",
                         np.where(data.loc[valid_idx, 'Daily_Return_Pct'] < 0, "Down", "Neutral"))
day_of_week = data.loc[valid_idx, 'Day_of_Week']

# Create contingency table
contingency_table = pd.crosstab(day_of_week, price_movement)
print("Contingency Table:")
print(contingency_table)

print("\nH0: Day of Week and Price Movement are independent")
print("H1: Day of Week and Price Movement are not independent\n")

chi_square_result = stats.chi2_contingency(contingency_table)
print("Test Results:")
print(f"Chi-square statistic: {chi_square_result[0]:.6f}")
print(f"p-value: {chi_square_result[1]:.6f}")
print(f"degrees of freedom: {chi_square_result[2]}")

if chi_square_result[1] < 0.05:
    print("\nConclusion: At 5% significance level, we REJECT the null hypothesis.")
    print("There is a significant relationship between Day of Week and Price Movement.")
else:
    print("\nConclusion: At 5% significance level, we FAIL TO REJECT the null hypothesis.")
    print("Day of Week and Price Movement appear to be independent.")

# Save hypothesis test results
with open('hypothesis_test_results.txt', 'w', encoding='utf-8') as f:
    f.write("HYPOTHESIS TEST RESULTS\n")
    f.write("======================\n\n")
    
    f.write("Test 1: One-Sample T-Test (Daily Return)\n")
    f.write("---------------------------------------\n")
    f.write(f"t-statistic: {t_test_result.statistic:.6f}\n")
    f.write(f"p-value: {t_test_result.pvalue:.6f}\n")
    f.write(f"df: {len(daily_return)-1}\n")
    f.write("\n")
    
    f.write("Test 2: Two-Sample T-Test (2021 vs 2022 Close Prices)\n")
    f.write("-------------------------------------------------------\n")
    f.write(f"t-statistic: {t_test_2.statistic:.6f}\n")
    f.write(f"p-value: {t_test_2.pvalue:.6f}\n")
    f.write(f"df: {t_test_2.df:.2f}\n")
    f.write("\n")
    
    f.write("Test 3: Correlation Test (Close vs Volume)\n")
    f.write("-----------------------------------------\n")
    f.write(f"Correlation coefficient: {cor_test_result[0]:.6f}\n")
    f.write(f"p-value: {cor_test_result[1]:.6f}\n")
    f.write("\n")
    
    f.write("Test 4: Paired T-Test (High vs Low)\n")
    f.write("-----------------------------------\n")
    f.write(f"t-statistic: {paired_test.statistic:.6f}\n")
    f.write(f"p-value: {paired_test.pvalue:.6f}\n")
    f.write(f"df: {len(data)-1}\n")
    f.write("\n")
    
    f.write("Test 5: Chi-Square Test (Day of Week vs Price Movement)\n")
    f.write("---------------------------------------------------------\n")
    f.write(f"Chi-square statistic: {chi_square_result[0]:.6f}\n")
    f.write(f"p-value: {chi_square_result[1]:.6f}\n")
    f.write(f"df: {chi_square_result[2]}\n")

print("\nHypothesis test results saved to 'hypothesis_test_results.txt'")
print("\nAnalysis complete!")
