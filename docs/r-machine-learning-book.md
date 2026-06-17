# Complete R Programming & Machine Learning Guide

## A Professional Tutorial for Data Science

---

# Table of Contents

1. [Introduction to R](#introduction)
2. [R Basics](#r-basics)
3. [Data Types and Structures](#data-types)
4. [Statistical Analysis](#statistics)
5. [Data Visualization](#visualization)
6. [Machine Learning Fundamentals](#ml-fundamentals)
7. [Supervised Learning](#supervised)
8. [Unsupervised Learning](#unsupervised)
9. [Model Evaluation](#evaluation)
10. [Real-World Projects](#projects)

---

# Chapter 1: Introduction to R

## What is R?

R is a programming language and software environment for statistical computing and graphics. It's widely used by:
- Data Scientists
- Statisticians
- Machine Learning Engineers
- Academic Researchers

## Why Learn R?

| Feature | Benefit |
|---------|---------|
| Open Source | Free to use and modify |
| Rich Packages | 18,000+ packages on CRAN |
| Statistical Focus | Built specifically for statistics |
| Visualization | Powerful graphics with ggplot2 |
| Community | Large, supportive community |

## Installing R and RStudio

```r
# Install R from: https://cran.r-project.org/
# Install RStudio from: https://www.rstudio.com/

# Verify installation
R.version
```

## Your First R Script

```r
# This is a comment
print("Hello, R!")

# Basic arithmetic
2 + 2    # Addition
10 - 5   # Subtraction
3 * 4    # Multiplication
8 / 2    # Division
2 ^ 3    # Exponentiation

# Store values in variables
x <- 5          # Assignment operator
y = 10          # Alternative assignment
total <- x + y  # Use variables
print(total)
```

## Working Directory

```r
# Get current working directory
getwd()

# Set working directory
setwd("C:/Users/YourName/Documents")

# List files in directory
list.files()
```

---

# Chapter 2: R Basics

## Variables and Data Types

### Numeric
```r
# Integer
age <- 25

# Decimal/Float
price <- 19.99

# Check type
is.numeric(age)
```

### Character (String)
```r
name <- "Ethereum"
symbol <- 'ETH'

# Check type
is.character(name)
```

### Logical (Boolean)
```r
is_active <- TRUE
is_deleted <- FALSE

# Check type
is.logical(is_active)
```

## Operators

### Arithmetic Operators
```r
+   # Addition
-   # Subtraction
*   # Multiplication
/   # Division
^   # Exponentiation
%%  # Modulus (remainder)
%/% # Integer division
```

### Comparison Operators
```r
==  # Equal to
!=  # Not equal to
<   # Less than
>   # Greater than
<=  # Less than or equal
>=  # Greater than or equal
```

### Logical Operators
```r
&   # AND (element-wise)
|   # OR (element-wise)
!   # NOT
&&  # AND (short-circuit)
||  # OR (short-circuit)
```

## Basic Functions

```r
# Print output
print("Hello")
cat("Hello", "World")

# Get help
?mean
help("sum")

# Round numbers
round(3.14159, 2)  # 3.14

# Absolute value
abs(-5)  # 5

# Square root
sqrt(16)  # 4
```

---

# Chapter 3: Data Types and Structures

## Vectors

A vector is the most basic data structure in R.

### Creating Vectors
```r
# Numeric vector
prices <- c(100, 200, 300, 400, 500)

# Character vector
coins <- c("Bitcoin", "Ethereum", "Cardano")

# Logical vector
is_crypto <- c(TRUE, TRUE, FALSE)

# Sequence
1:10              # 1 to 10
seq(1, 10, 2)    # 1, 3, 5, 7, 9
rep(1, 5)        # 1, 1, 1, 1, 1
```

### Vector Operations
```r
prices <- c(100, 200, 300, 400)

# Arithmetic with vectors
prices * 2        # Multiply each by 2
prices + 10        # Add 10 to each
prices ^ 2         # Square each

# Vector functions
sum(prices)       # Sum all
mean(prices)      # Average
median(prices)    # Median
min(prices)       # Minimum
max(prices)       # Maximum
length(prices)    # Number of elements
```

### Vector Indexing
```r
prices <- c(100, 200, 300, 400, 500)

# Get first element
prices[1]         # 100

# Get multiple elements
prices[c(1, 3)]   # 100, 300

# Get range
prices[1:3]        # 100, 200, 300

# Negative indexing (exclude)
prices[-1]         # 200, 300, 400, 500

# Logical indexing
prices[prices > 250]  # 300, 400, 500
```

## Matrices

A matrix is a 2-dimensional array of the same type.

### Creating Matrices
```r
# Create matrix
m <- matrix(1:9, nrow = 3, ncol = 3)
m <- matrix(1:9, nrow = 3, byrow = TRUE)

# Bind columns/rows
cbind(1:3, 4:6)   # Column bind
rbind(1:3, 4:6)   # Row bind
```

### Matrix Operations
```r
m1 <- matrix(1:4, nrow = 2)
m2 <- matrix(5:8, nrow = 2)

m1 + m2           # Addition
m1 %*% m2         # Matrix multiplication
t(m1)             # Transpose
solve(m1)         # Inverse (if square)
```

## Data Frames

Data frames are the most important data structure for data analysis - like spreadsheets.

### Creating Data Frames
```r
# Create data frame
df <- data.frame(
  name = c("Bitcoin", "Ethereum", "Cardano"),
  symbol = c("BTC", "ETH", "ADA"),
  price = c(50000, 3000, 1.5),
  market_cap = c(1e12, 350e9, 50e9)
)

# View structure
str(df)
```

### Accessing Data Frames
```r
# Column access
df$price
df[["price"]]
df[, "price"]

# Row access
df[1, ]
df[1:3, ]

# Cell access
df[1, "price"]
```

### Useful Data Frame Functions
```r
head(df)          # First 6 rows
tail(df)          # Last 6 rows
nrow(df)          # Number of rows
ncol(df)          # Number of columns
names(df)         # Column names
summary(df)       # Summary statistics
```

## Lists

Lists can contain different types of objects.

```r
# Create list
my_list <- list(
  name = "Ethereum",
  prices = c(100, 200, 300),
  data = data.frame(x = 1:3, y = 4:6)
)

# Access list elements
my_list$name
my_list[[1]]
my_list[["prices"]]
```

---

# Chapter 4: Statistical Analysis

## Descriptive Statistics

### Central Tendency

```r
# Sample data
returns <- c(1.2, -0.5, 2.1, 0.8, -1.3, 0.3, 1.5, -0.2)

# Mean (average)
mean(returns)

# Median (middle value)
median(returns)

# Mode (most frequent)
get_mode <- function(x) {
  ux <- unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}
get_mode(returns)
```

### Spread/Dispersion

```r
# Variance
var(returns)

# Standard Deviation
sd(returns)

# Range (max - min)
max(returns) - min(returns)

# Interquartile Range (IQR)
IQR(returns)

# Quantiles
quantile(returns, probs = c(0.25, 0.5, 0.75))
```

### Complete Summary

```r
# Summary statistics
summary(returns)

# More detailed
install.packages("psych")
library(psych)
describe(returns)
```

## Probability Distributions

### Normal Distribution

```r
# Generate random normal values
rnorm(n = 1000, mean = 0, sd = 1)

# Density function
dnorm(x = 0, mean = 0, sd = 1)

# Cumulative distribution
pnorm(q = 1.96, mean = 0, sd = 1)

# Quantile function
qnorm(p = 0.975, mean = 0, sd = 1)
```

### Other Distributions

```r
# Binomial
rbinom(n = 10, size = 5, prob = 0.5)

# Poisson
rpois(n = 10, lambda = 3)

# Exponential
rexp(n = 10, rate = 1)

# t-distribution
rt(n = 10, df = 5)
```

---

# Chapter 5: Data Visualization

## Base R Graphics

```r
# Simple plot
plot(1:10, 1:10)

# Line plot
plot(1:10, 1:10, type = "l")

# Scatter plot with options
plot(x, y, 
     main = "Title",
     xlab = "X Axis",
     ylab = "Y Axis",
     col = "blue",
     pch = 16)

# Histogram
hist(data, 
     breaks = 30,
     col = "steelblue",
     border = "white")

# Box plot
boxplot(data ~ group,
        data = df,
        col = "lightblue")
```

## ggplot2 (Advanced Visualization)

ggplot2 is R's most popular visualization package.

### Basic ggplot2 Syntax

```r
# Install and load
install.packages("ggplot2")
library(ggplot2)

# Basic scatter plot
ggplot(df, aes(x = price, y = volume)) +
  geom_point()

# Add layers
ggplot(df, aes(x = price, y = volume)) +
  geom_point(color = "blue", alpha = 0.5) +
  labs(title = "Price vs Volume",
       x = "Price (USD)",
       y = "Volume") +
  theme_minimal()
```

### Common ggplot2 Geometries

```r
# Scatter plot
ggplot(df, aes(x, y)) + geom_point()

# Line plot
ggplot(df, aes(x, y)) + geom_line()

# Bar plot
ggplot(df, aes(x)) + geom_bar()

# Histogram
ggplot(df, aes(x)) + geom_histogram()

# Box plot
ggplot(df, aes(x = group, y = value)) + geom_boxplot()

# Density plot
ggplot(df, aes(x = value)) + geom_density()

# Area plot
ggplot(df, aes(x, y)) + geom_area()
```

### Customizing ggplot2

```r
# Colors and fills
ggplot(df, aes(x, y, color = category)) + geom_point()
ggplot(df, aes(x, fill = category)) + geom_bar()

# Facets (multiple plots)
ggplot(df, aes(x, y)) + 
  geom_point() +
  facet_wrap(~category)

# Themes
ggplot(df, aes(x, y)) +
  geom_point() +
  theme_minimal()
ggplot(df, aes(x, y)) +
  geom_point() +
  theme_dark()
```

---

# Chapter 6: Machine Learning Fundamentals

## What is Machine Learning?

Machine Learning (ML) is a subset of artificial intelligence that enables computers to learn from data without being explicitly programmed.

### Types of Machine Learning

| Type | Description | Examples |
|------|-------------|----------|
| **Supervised** | Learn from labeled data | Classification, Regression |
| **Unsupervised** | Find patterns in unlabeled data | Clustering, Dimensionality Reduction |
| **Reinforcement** | Learn from feedback | Game AI, Robotics |

## Data Preprocessing

### Handling Missing Values

```r
# Check for missing values
is.na(df)
colSums(is.na(df))

# Remove rows with missing values
na.omit(df)
df_complete <- na.omit(df)

# Impute missing values
df$column[is.na(df$column)] <- mean(df$column, na.rm = TRUE)

# Using tidyr
library(tidyr)
df %>% drop_na()
df %>% fill(column, .direction = "down")
```

### Feature Scaling

```r
# Min-Max Normalization
normalize <- function(x) {
  (x - min(x)) / (max(x) - min(x))
}

# Standardization (Z-score)
standardize <- function(x) {
  (x - mean(x)) / sd(x)
}

# Using scale()
scaled_data <- scale(data)
```

### Train-Test Split

```r
# Simple split
set.seed(42)
n <- nrow(df)
train_index <- sample(1:n, 0.8 * n)
train <- df[train_index, ]
test <- df[-train_index, ]

# Using caret
library(caret)
trainIndex <- createDataPartition(df$target, p = 0.8, list = FALSE)
train <- df[trainIndex, ]
test <- df[-trainIndex, ]
```

---

# Chapter 7: Supervised Learning

## Regression

Regression predicts continuous numerical values.

### Linear Regression

```r
# Simple Linear Regression
model <- lm(price ~ volume, data = train_data)

# Summary
summary(model)

# Predictions
predictions <- predict(model, test_data)

# Multiple Linear Regression
model <- lm(price ~ volume + market_cap + age, data = train_data)
```

### Model Evaluation (Regression)

```r
# Mean Squared Error
mse <- mean((actual - predicted)^2)

# Root Mean Squared Error
rmse <- sqrt(mse)

# Mean Absolute Error
mae <- mean(abs(actual - predicted))

# R-squared
rsq <- 1 - (sum((actual - predicted)^2) / 
            sum((actual - mean(actual))^2))
```

### Polynomial Regression

```r
# Polynomial regression
model <- lm(price ~ poly(volume, 2), data = train_data)
model <- lm(price ~ poly(volume, 3), data = train_data)
```

## Classification

Classification predicts categorical labels.

### Logistic Regression

```r
# Logistic regression (binary)
model <- glm(target ~ features, 
             data = train_data, 
             family = "binomial")

# Predictions
predictions <- predict(model, test_data, type = "response")
predicted_class <- ifelse(predictions > 0.5, 1, 0)
```

### Decision Trees

```r
# Install package
install.packages("rpart")
library(rpart)

# Create model
model <- rpart(target ~ features, 
               data = train_data,
               method = "class")

# Predictions
predictions <- predict(model, test_data, type = "class")
```

### Random Forest

```r
# Install package
install.packages("randomForest")
library(randomForest)

# Create model
model <- randomForest(target ~ features,
                      data = train_data,
                      ntree = 100,
                      mtry = sqrt(ncol(train_data) - 1))

# Predictions
predictions <- predict(model, test_data)
```

### Support Vector Machine (SVM)

```r
# Install package
install.packages("e1071")
library(e1071)

# Create model
model <- svm(target ~ features,
              data = train_data,
              kernel = "radial")

# Predictions
predictions <- predict(model, test_data)
```

---

# Chapter 8: Unsupervised Learning

## Clustering

### K-Means Clustering

```r
# K-Means
set.seed(42)
model <- kmeans(data, centers = 3, nstart = 10)

# Results
model$cluster
model$centers
model$size

# Visualize
library(factoextra)
fviz_cluster(model, data = data)
```

### Hierarchical Clustering

```r
# Distance matrix
dist_matrix <- dist(data)

# Hierarchical clustering
hc <- hclust(dist_matrix, method = "ward.D2")

# Cut tree into clusters
clusters <- cutree(hc, k = 3)

# Visualize
plot(hc)
rect.hclust(hc, k = 3, border = "red")
```

## Dimensionality Reduction

### Principal Component Analysis (PCA)

```r
# PCA
pca <- prcomp(data, scale = TRUE)

# Summary
summary(pca)

# Get principal components
pca$x

# Variance explained
pca$sdev^2
var_explained <- pca$sdev^2 / sum(pca$sdev^2)

# Visualize variance
plot(var_explained, type = "b")
cumsum(var_explained)

# Biplot
biplot(pca)
```

---

# Chapter 9: Model Evaluation

## Classification Metrics

### Confusion Matrix

```r
library(caret)
confusionMatrix(predicted, actual)
```

### Key Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **Accuracy** | (TP + TN) / Total | Overall correctness |
| **Precision** | TP / (TP + FP) | Positive predictions accuracy |
| **Recall** | TP / (TP + FN) | Actual positives found |
| **F1-Score** | 2 × (Precision × Recall) / (Precision + Recall) | Harmonic mean |
| **AUC-ROC** | Area under ROC curve | Discrimination ability |

### ROC Curve

```r
library(ROCR)
pred <- prediction(predictions, actual)
perf <- performance(pred, "tpr", "fpr")
plot(perf)

# AUC
auc <- performance(pred, "auc")
auc@y.values[[1]]
```

## Cross-Validation

```r
# K-Fold Cross-Validation
library(caret)
train_control <- trainControl(method = "cv", number = 10)

model <- train(target ~ features,
               data = data,
               trControl = train_control,
               method = "glm")

# Results
print(model)
```

---

# Chapter 10: Real-World Projects

## Project 1: Stock Price Prediction

```r
# Load data
data <- read.csv("ethereum_usd_historical_dataset.csv")

# Explore
head(data)
str(data)
summary(data)

# Check for missing values
colSums(is.na(data))

# Select numeric columns
numeric_cols <- sapply(data, is.numeric)

# Calculate correlations
cor_matrix <- cor(data[, numeric_cols])

# Visualize
library(corrplot)
corrplot(cor_matrix, method = "color")

# Build model
model <- lm(Close ~ Volume + Daily_Return_Pct, data = data)
summary(model)

# Predictions
predictions <- predict(model)
```

## Project 2: Customer Segmentation

```r
# Load customer data
customer_data <- read.csv("customer_data.csv")

# Select features
features <- customer_data[, c("age", "income", "spending_score")]

# Scale data
scaled_data <- scale(features)

# Determine optimal clusters
library(factoextra)
fviz_nbclust(scaled_data, kmeans, method = "wss")

# K-Means clustering
set.seed(42)
kmeans_model <- kmeans(scaled_data, centers = 4)

# Add cluster to data
customer_data$cluster <- kmeans_model$cluster

# Analyze clusters
aggregate(customer_data[, c("age", "income", "spending_score")], 
          by = list(cluster = customer_data$cluster), 
          FUN = mean)
```

## Project 3: Email Spam Detection

```r
# Load data
data <- read.csv("spam_data.csv")

# Text preprocessing
library(tm)
corpus <- VCorpus(VectorSource(data$text))
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removeWords, stopwords())

# Create document term matrix
dtm <- DocumentTermMatrix(corpus)

# Train-test split
set.seed(42)
train_index <- sample(nrow(data), 0.8 * nrow(data))
train <- dtm[train_index, ]
test <- dtm[-train_index, ]

# Naive Bayes
library(e1071)
model <- naiveBayes(train, data$label[train_index])

# Predictions
predictions <- predict(model, test)
```

---

# Appendix: Useful R Packages

## Data Manipulation
```r
install.packages(c("dplyr", "tidyr", "readr", "data.table"))
```

## Visualization
```r
install.packages(c("ggplot2", "plotly", "ggpubr", "corrplot"))
```

## Machine Learning
```r
install.packages(c("caret", "randomForest", "e1071", "rpart", 
                  "nnet", "glmnet", "xgboost"))
```

## Statistics
```r
install.packages(c("psych", "moments", "httr", "jsonlite"))
```

---

# Conclusion

Congratulations! You have completed the R Programming and Machine Learning guide.

## What You've Learned:

✅ R programming basics  
✅ Data types and structures  
✅ Statistical analysis  
✅ Data visualization with ggplot2  
✅ Machine learning fundamentals  
✅ Supervised and unsupervised learning  
✅ Model evaluation techniques  
✅ Real-world projects  

## Next Steps:

1. Practice with real datasets
2. Participate in Kaggle competitions
3. Build your own ML projects
4. Explore advanced topics (Deep Learning, NLP)
5. Contribute to open source

## Resources:

- [R Documentation](https://www.rdocumentation.org)
- [RStudio Cheat Sheets](https://www.rstudio.com/resources/cheatsheets)
- [Kaggle](https://www.kaggle.com)
- [Coursera R Programming](https://www.coursera.org)

---

**Author**: Ethereum Statistical Analysis Project  
**Date**: 2024  
**License**: Educational Use
