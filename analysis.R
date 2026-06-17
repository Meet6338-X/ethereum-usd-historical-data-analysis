# =============================================================================
# Ethereum USD Historical Dataset - Statistical Analysis
# =============================================================================
# This script performs comprehensive statistical analysis on the Ethereum USD
# historical dataset including:
# - Descriptive Statistics (Mean, Mode, Median, SD, Variance, Quartiles, IQR, Range)
# - Data Visualization (Histograms, Box Plots, Density Plots, etc.)
# - Hypothesis Testing
# =============================================================================

# Try to load required packages, if not available use base R
tryCatch({
  library(ggplot2)
  library(dplyr)
  library(tidyr)
  library(moments)
  has_packages <- TRUE
}, error = function(e) {
  has_packages <<- FALSE
  message("Additional packages not available. Using base R functions only.")
})

# Set working directory to the project root
setwd("C:/Users/shahm/Downloads/coding/etthurum datasest")

# Load the dataset
cat("Loading Ethereum USD Historical Dataset...\n")
data <- read.csv("ethereum_usd_historical_dataset.csv", stringsAsFactors = FALSE)

# Display basic information about the dataset
cat("\n=== DATASET OVERVIEW ===\n")
cat("Number of rows:", nrow(data), "\n")
cat("Number of columns:", ncol(data), "\n")
cat("\nColumn names:\n")
print(names(data))

# Identify numeric columns
numeric_cols <- names(data)[sapply(data, is.numeric)]
cat("\n=== NUMERIC COLUMNS IDENTIFIED ===\n")
cat("Total numeric columns:", length(numeric_cols), "\n")
print(numeric_cols)

# Remove non-meaningful numeric columns (like Year, Month, etc. that are identifiers)
# Keep actual data columns
meaningful_numeric_cols <- numeric_cols[!numeric_cols %in% c("Year", "Month", "Quarter", 
                                                               "Week_Number", "Day_of_Week")]
cat("\n=== MEANINGFUL NUMERIC COLUMNS FOR ANALYSIS ===\n")
print(meaningful_numeric_cols)

# =============================================================================
# FUNCTION DEFINITIONS
# =============================================================================

# Function to calculate mode
get_mode <- function(x) {
  x <- x[!is.na(x)]
  if (length(x) == 0) return(NA)
  ux <- unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}

# Function to calculate skewness using base R
skewness_base <- function(x) {
  x <- x[!is.na(x)]
  n <- length(x)
  if (n < 3) return(NA)
  m3 <- sum((x - mean(x))^3) / n
  m2 <- sum((x - mean(x))^2) / n
  return(m3 / (m2^(3/2)))
}

# Function to calculate kurtosis using base R
kurtosis_base <- function(x) {
  x <- x[!is.na(x)]
  n <- length(x)
  if (n < 4) return(NA)
  m4 <- sum((x - mean(x))^4) / n
  m2 <- sum((x - mean(x))^2) / n
  return(m4 / (m2^2) - 3)
}

# Function to calculate comprehensive statistics for a column
calculate_stats <- function(x, col_name) {
  x <- x[!is.na(x)]
  if (length(x) == 0) {
    return(data.frame(
      Column = col_name,
      Mean = NA,
      Median = NA,
      Mode = NA,
      Std_Dev = NA,
      Variance = NA,
      Q1 = NA,
      Q2 = NA,
      Q3 = NA,
      IQR = NA,
      Min = NA,
      Max = NA,
      Range = NA,
      Skewness = NA,
      Kurtosis = NA
    ))
  }
  
  # Calculate statistics
  mean_val <- mean(x)
  median_val <- median(x)
  mode_val <- get_mode(x)
  sd_val <- sd(x)
  var_val <- var(x)
  q1_val <- quantile(x, 0.25)
  q2_val <- quantile(x, 0.50)
  q3_val <- quantile(x, 0.75)
  iqr_val <- q3_val - q1_val
  min_val <- min(x)
  max_val <- max(x)
  range_val <- max_val - min_val
  skew_val <- skewness_base(x)
  kurt_val <- kurtosis_base(x)
  
  return(data.frame(
    Column = col_name,
    Mean = mean_val,
    Median = median_val,
    Mode = mode_val,
    Std_Dev = sd_val,
    Variance = var_val,
    Q1 = q1_val,
    Q2 = q2_val,
    Q3 = q3_val,
    IQR = iqr_val,
    Min = min_val,
    Max = max_val,
    Range = range_val,
    Skewness = skew_val,
    Kurtosis = kurt_val
  ))
}

# =============================================================================
# DESCRIPTIVE STATISTICS CALCULATION
# =============================================================================

cat("\n\n")
cat("################################################################################\n")
cat("#                     DESCRIPTIVE STATISTICS ANALYSIS                          #\n")
cat("################################################################################\n\n")

# Calculate statistics for all meaningful numeric columns
all_stats <- data.frame()
for (col in meaningful_numeric_cols) {
  if (col %in% names(data)) {
    stats <- calculate_stats(data[[col]], col)
    all_stats <- rbind(all_stats, stats)
  }
}

# Display statistics
cat("=== MEAN ===\n")
print(all_stats[, c("Column", "Mean")])

cat("\n=== MODE ===\n")
print(all_stats[, c("Column", "Mode")])

cat("\n=== MEDIAN ===\n")
print(all_stats[, c("Column", "Median")])

cat("\n=== STANDARD DEVIATION ===\n")
print(all_stats[, c("Column", "Std_Dev")])

cat("\n=== VARIANCE ===\n")
print(all_stats[, c("Column", "Variance")])

cat("\n=== QUARTILES ===\n")
print(all_stats[, c("Column", "Q1", "Q2", "Q3")])

cat("\n=== INTERQUARTILE RANGE (IQR) ===\n")
print(all_stats[, c("Column", "IQR")])

cat("\n=== RANGE ===\n")
print(all_stats[, c("Column", "Min", "Max", "Range")])

# Save statistics to CSV
write.csv(all_stats, "descriptive_statistics.csv", row.names = FALSE)
cat("\nDescriptive statistics saved to 'descriptive_statistics.csv'\n")

# Print full statistics table
cat("\n=== COMPLETE STATISTICS TABLE ===\n")
print(all_stats)

# =============================================================================
# DATA VISUALIZATION
# =============================================================================

cat("\n\n")
cat("################################################################################\n")
cat("#                           DATA VISUALIZATION                                 #\n")
cat("################################################################################\n\n")

# Create output directory for plots
dir.create("plots", showWarnings = FALSE)

# Select key fields for visualization
key_fields <- c("Close", "High", "Low", "Open", "Volume", "Daily_Return_Pct", 
                 "Log_Return", "Volatility_30d", "RSI_14", "MACD")
key_fields <- key_fields[key_fields %in% meaningful_numeric_cols]

# 1. HISTOGRAMS
cat("Creating Histograms...\n")
for (field in key_fields) {
  if (field %in% names(data)) {
    png(filename = paste0("plots/histogram_", field, ".png"), width = 800, height = 600)
    hist(data[[field]], 
         main = paste("Histogram of", field),
         xlab = field,
         col = "steelblue",
         border = "white",
         breaks = 30,
         probability = TRUE)
    lines(density(data[[field]], na.rm = TRUE), col = "red", lwd = 2)
    abline(v = mean(data[[field]], na.rm = TRUE), col = "green", lty = 2, lwd = 2)
    abline(v = median(data[[field]], na.rm = TRUE), col = "orange", lty = 2, lwd = 2)
    legend("topright", legend = c("Density", "Mean", "Median"), 
           col = c("red", "green", "orange"), lty = c(1, 2, 2))
    dev.off()
  }
}

# 2. BOX PLOTS
cat("Creating Box Plots...\n")
for (field in key_fields) {
  if (field %in% names(data)) {
    png(filename = paste0("plots/boxplot_", field, ".png"), width = 800, height = 600)
    boxplot(data[[field]], 
            main = paste("Box Plot of", field),
            ylab = field,
            col = "steelblue",
            border = "black",
            horizontal = FALSE)
    # Add mean point
    points(mean(data[[field]], na.rm = TRUE), col = "red", pch = 18, cex = 2)
    legend("topright", legend = "Mean", col = "red", pch = 18)
    dev.off()
  }
}

# Combined box plot for multiple fields
png(filename = "plots/boxplot_combined.png", width = 1200, height = 800)
boxplot(data[key_fields],
        main = "Box Plots of Key Ethereum Metrics",
        col = rainbow(length(key_fields)),
        border = "black",
        notch = TRUE)
dev.off()

# 3. DENSITY PLOTS
cat("Creating Density Plots...\n")
for (field in key_fields) {
  if (field %in% names(data)) {
    png(filename = paste0("plots/density_", field, ".png"), width = 800, height = 600)
    plot(density(data[[field]], na.rm = TRUE),
         main = paste("Density Plot of", field),
         xlab = field,
         col = "steelblue",
         lwd = 2)
    polygon(density(data[[field]], na.rm = TRUE), col = "steelblue", alpha = 0.3)
    dev.off()
  }
}

# 4. BAR CHARTS (for categorical summaries)
cat("Creating Bar Charts...\n")

# Monthly average close price
monthly_avg <- aggregate(data$Close, by = list(Month = data$Month), FUN = mean, na.rm = TRUE)
png(filename = "plots/bar_monthly_avg_close.png", width = 800, height = 600)
barplot(monthly_avg$x, 
        names.arg = monthly_avg$Month,
        main = "Average Close Price by Month",
        xlab = "Month",
        ylab = "Average Close Price",
        col = "steelblue",
        border = "white")
dev.off()

# Yearly average close price
yearly_avg <- aggregate(data$Close, by = list(Year = data$Year), FUN = mean, na.rm = TRUE)
png(filename = "plots/bar_yearly_avg_close.png", width = 800, height = 600)
barplot(yearly_avg$x, 
        names.arg = yearly_avg$Year,
        main = "Average Close Price by Year",
        xlab = "Year",
        ylab = "Average Close Price",
        col = "coral",
        border = "white")
dev.off()

# 5. SCATTER PLOTS
cat("Creating Scatter Plots...\n")

# Close vs Volume
png(filename = "plots/scatter_close_volume.png", width = 800, height = 600)
plot(data$Close, data$Volume,
     main = "Close Price vs Volume",
     xlab = "Close Price",
     ylab = "Volume",
     col = "steelblue",
     pch = 16, alpha = 0.5)
abline(lm(data$Volume ~ data$Close), col = "red", lwd = 2)
dev.off()

# Close vs Daily Return
valid_idx <- !is.na(data$Close) & !is.na(data$Daily_Return_Pct)
png(filename = "plots/scatter_close_daily_return.png", width = 800, height = 600)
plot(data$Close[valid_idx], data$Daily_Return_Pct[valid_idx],
     main = "Close Price vs Daily Return",
     xlab = "Close Price",
     ylab = "Daily Return (%)",
     col = "coral",
     pch = 16)
abline(lm(data$Daily_Return_Pct[valid_idx] ~ data$Close[valid_idx]), col = "blue", lwd = 2)
dev.off()

# 6. CORRELATION MATRIX HEATMAP
cat("Creating Correlation Heatmap...\n")
png(filename = "plots/correlation_heatmap.png", width = 1000, height = 800)
cor_matrix <- cor(data[key_fields], use = "complete.obs")
# Simple correlation plot
plot.new()
text(0.5, 0.9, "Correlation Matrix", cex = 2, font = 2)
text(0.5, 0.5, "See correlation_matrix.csv for values", cex = 1.5)
dev.off()

# Save correlation matrix
write.csv(cor_matrix, "correlation_matrix.csv", row.names = TRUE)

# 7. Q-Q PLOTS for key fields
cat("Creating Q-Q Plots...\n")
for (field in c("Close", "Daily_Return_Pct", "Volume")) {
  if (field %in% names(data)) {
    png(filename = paste0("plots/qqplot_", field, ".png"), width = 800, height = 600)
    qqnorm(data[[field]], main = paste("Q-Q Plot of", field))
    qqline(data[[field]], col = "red", lwd = 2)
    dev.off()
  }
}

cat("\nAll visualizations saved to 'plots/' directory\n")

# =============================================================================
# HYPOTHESIS TESTING
# =============================================================================

cat("\n\n")
cat("################################################################################\n")
cat("#                        HYPOTHESIS TESTING                                    #\n")
cat("################################################################################\n\n")

# Test 1: One-sample t-test - Is the mean daily return significantly different from 0?
cat("\n=== HYPOTHESIS TEST 1: One-Sample T-Test ===\n")
cat("Question: Is the mean daily return significantly different from 0?\n\n")
cat("H0: Mean daily return = 0\n")
cat("H1: Mean daily return ≠ 0\n\n")

daily_return <- data$Daily_Return_Pct[!is.na(data$Daily_Return_Pct)]
t_test_result <- t.test(daily_return, mu = 0)
cat("Test Results:\n")
print(t_test_result)

if (t_test_result$p.value < 0.05) {
  cat("\nConclusion: At 5% significance level, we REJECT the null hypothesis.\n")
  cat("The mean daily return is significantly different from 0.\n")
} else {
  cat("\nConclusion: At 5% significance level, we FAIL TO REJECT the null hypothesis.\n")
  cat("There is no significant evidence that the mean daily return is different from 0.\n")
}

# Test 2: Two-sample t-test - Is there a significant difference between Close prices in different years?
cat("\n\n=== HYPOTHESIS TEST 2: Two-Sample T-Test ===\n")
cat("Question: Is there a significant difference in Close prices between 2021 and 2022?\n\n")

close_2021 <- data$Close[data$Year == 2021]
close_2022 <- data$Close[data$Year == 2022]

cat("H0: Mean Close price in 2021 = Mean Close price in 2022\n")
cat("H1: Mean Close price in 2021 ≠ Mean Close price in 2022\n\n")
cat("Sample sizes:\n")
cat("2021:", length(close_2021), "\n")
cat("2022:", length(close_2022), "\n\n")

t_test_2 <- t.test(close_2021, close_2022, var.equal = FALSE)
print(t_test_2)

if (t_test_2$p.value < 0.05) {
  cat("\nConclusion: At 5% significance level, we REJECT the null hypothesis.\n")
  cat("There is a significant difference in Close prices between 2021 and 2022.\n")
} else {
  cat("\nConclusion: At 5% significance level, we FAIL TO REJECT the null hypothesis.\n")
  cat("There is no significant difference in Close prices between 2021 and 2022.\n")
}

# Test 3: Correlation Test - Is there a significant correlation between Close price and Volume?
cat("\n\n=== HYPOTHESIS TEST 3: Correlation Test ===\n")
cat("Question: Is there a significant correlation between Close price and Volume?\n\n")

valid_corr <- complete.cases(data$Close, data$Volume)
close_corr <- data$Close[valid_corr]
volume_corr <- data$Volume[valid_corr]

cat("H0: Correlation between Close and Volume = 0\n")
cat("H1: Correlation between Close and Volume ≠ 0\n\n")

cor_test_result <- cor.test(close_corr, volume_corr)
print(cor_test_result)

if (cor_test_result$p.value < 0.05) {
  cat("\nConclusion: At 5% significance level, we REJECT the null hypothesis.\n")
  cat("There is a significant correlation between Close price and Volume.\n")
} else {
  cat("\nConclusion: At 5% significance level, we FAIL TO REJECT the null hypothesis.\n")
  cat("There is no significant correlation between Close price and Volume.\n")
}

# Test 4: Paired t-test - Is there a significant difference between High and Low prices?
cat("\n\n=== HYPOTHESIS TEST 4: Paired T-Test ===\n")
cat("Question: Is there a significant difference between High and Low prices?\n\n")

cat("H0: Mean High price = Mean Low price\n")
cat("H1: Mean High price ≠ Mean Low price\n\n")

paired_test <- t.test(data$High, data$Low, paired = TRUE)
print(paired_test)

if (paired_test$p.value < 0.05) {
  cat("\nConclusion: At 5% significance level, we REJECT the null hypothesis.\n")
  cat("There is a significant difference between High and Low prices.\n")
} else {
  cat("\nConclusion: At 5% significance level, we FAIL TO REJECT the null hypothesis.\n")
  cat("There is no significant difference between High and Low prices.\n")
}

# Test 5: Chi-Square Test - Is there a relationship between Day of Week and Price Movement?
cat("\n\n=== HYPOTHESIS TEST 5: Chi-Square Test ===\n")
cat("Question: Is there a significant relationship between Day of Week and Price Movement direction?\n\n")

# Create price movement categories (only for non-NA values)
valid_idx <- !is.na(data$Daily_Return_Pct)
price_movement <- ifelse(data$Daily_Return_Pct[valid_idx] > 0, "Up", 
                          ifelse(data$Daily_Return_Pct[valid_idx] < 0, "Down", "Neutral"))
day_of_week <- data$Day_of_Week[valid_idx]

# Create contingency table
contingency_table <- table(day_of_week, price_movement)
cat("Contingency Table:\n")
print(contingency_table)

cat("\nH0: Day of Week and Price Movement are independent\n")
cat("H1: Day of Week and Price Movement are not independent\n\n")

chi_square_result <- chisq.test(contingency_table)
print(chi_square_result)

if (chi_square_result$p.value < 0.05) {
  cat("\nConclusion: At 5% significance level, we REJECT the null hypothesis.\n")
  cat("There is a significant relationship between Day of Week and Price Movement.\n")
} else {
  cat("\nConclusion: At 5% significance level, we FAIL TO REJECT the null hypothesis.\n")
  cat("Day of Week and Price Movement appear to be independent.\n")
}

# Save hypothesis test results
sink("hypothesis_test_results.txt")
cat("HYPOTHESIS TEST RESULTS\n")
cat("======================\n\n")

cat("Test 1: One-Sample T-Test (Daily Return)\n")
cat("---------------------------------------\n")
print(t_test_result)
cat("\n")

cat("Test 2: Two-Sample T-Test (2021 vs 2022 Close Prices)\n")
cat("-------------------------------------------------------\n")
print(t_test_2)
cat("\n")

cat("Test 3: Correlation Test (Close vs Volume)\n")
cat("-----------------------------------------\n")
print(cor_test_result)
cat("\n")

cat("Test 4: Paired T-Test (High vs Low)\n")
cat("-----------------------------------\n")
print(paired_test)
cat("\n")

cat("Test 5: Chi-Square Test (Day of Week vs Price Movement)\n")
cat("---------------------------------------------------------\n")
print(chi_square_result)
sink()

cat("\nHypothesis test results saved to 'hypothesis_test_results.txt'\n")

# =============================================================================
# SUMMARY
# =============================================================================

cat("\n\n")
cat("################################################################################\n")
cat("#                              ANALYSIS COMPLETE                               #\n")
cat("################################################################################\n\n")

cat("Files Generated:\n")
cat("1. descriptive_statistics.csv - All statistical measures\n")
cat("2. correlation_matrix.csv - Correlation matrix of key fields\n")
cat("3. hypothesis_test_results.txt - Results of hypothesis tests\n")
cat("4. plots/ directory - All visualizations\n")
cat("   - histograms for each key field\n")
cat("   - box plots for each key field\n")
cat("   - density plots\n")
cat("   - bar charts (monthly/yearly averages)\n")
cat("   - scatter plots\n")
cat("   - Q-Q plots\n")

cat("\nStatistical Analysis Summary:\n")
cat("----------------------------\n")
cat("Total numeric fields analyzed:", length(meaningful_numeric_cols), "\n")
cat("Key fields for visualization:", length(key_fields), "\n")
cat("Hypothesis tests performed: 5\n")

cat("\nAnalysis completed successfully!\n")
