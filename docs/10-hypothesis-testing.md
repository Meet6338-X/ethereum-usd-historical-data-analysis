# Hypothesis Testing - Statistical Analysis

## Overview
Hypothesis testing is a statistical method used to make decisions about a population based on sample data.

## Hypothesis Testing Steps

1. **State Null Hypothesis (H₀)**: The default assumption
2. **State Alternative Hypothesis (H₁)**: What we're trying to prove
3. **Set Significance Level (α)**: Usually 0.05 (5%)
4. **Calculate Test Statistic**: From sample data
5. **Find p-value**: Probability of observing results
6. **Make Decision**: Reject or fail to reject H₀

## Tests Performed

---

### Test 1: One-Sample T-Test

**Question**: Is the mean daily return significantly different from 0?

**Hypotheses**:
- H₀: μ = 0 (Mean daily return equals zero)
- H₁: μ ≠ 0 (Mean daily return is different from zero)

**Results**:
| Statistic | Value |
|-----------|-------|
| t-statistic | 2.0697 |
| p-value | 0.0386 |
| Degrees of Freedom | 3,004 |
| Sample Mean | 0.1695% |
| 95% CI | [0.009, 0.330] |

**Decision**: **REJECT H₀** (p < 0.05)

**Conclusion**: At 5% significance level, there is sufficient evidence that the mean daily return is significantly different from zero. Ethereum shows a statistically significant positive average daily return.

---

### Test 2: Two-Sample T-Test

**Question**: Is there a significant difference in Close prices between 2021 and 2022?

**Hypotheses**:
- H₀: μ₂₀₂₁ = μ₂₀₂₂ (Mean prices are equal)
- H₁: μ₂₀₂₁ ≠ μ₂₀₂₂ (Mean prices are different)

**Results**:
| Statistic | Value |
|-----------|-------|
| t-statistic | 11.769 |
| p-value | < 2.2e-16 |
| Mean 2021 | $2,778.35 |
| Mean 2022 | $1,987.39 |
| 95% CI | [659.00, 922.92] |

**Decision**: **REJECT H₀** (p < 0.05)

**Conclusion**: There is a statistically significant difference in Ethereum prices between 2021 and 2022. The average price in 2021 was significantly higher than in 2022.

---

### Test 3: Correlation Test (Pearson)

**Question**: Is there a significant correlation between Close price and Volume?

**Hypotheses**:
- H₀: ρ = 0 (No correlation)
- H₁: ρ ≠ 0 (Correlation exists)

**Results**:
| Statistic | Value |
|-----------|-------|
| Pearson r | 0.5775 |
| t-statistic | 38.766 |
| p-value | < 2.2e-16 |
| 95% CI | [0.553, 0.601] |

**Decision**: **REJECT H₀** (p < 0.05)

**Conclusion**: There is a statistically significant moderate positive correlation (r = 0.58) between Close price and Volume. Higher prices tend to have higher trading volume.

---

### Test 4: Paired T-Test

**Question**: Is there a significant difference between High and Low prices?

**Hypotheses**:
- H₀: μ_High = μ_Low (No difference)
- H₁: μ_High ≠ μ_Low (Difference exists)

**Results**:
| Statistic | Value |
|-----------|-------|
| t-statistic | 49.605 |
| p-value | < 2.2e-16 |
| Mean Difference | $96.07 |
| 95% CI | [92.27, 99.87] |

**Decision**: **REJECT H₀** (p < 0.05)

**Conclusion**: There is a statistically significant difference between High and Low prices. On average, the daily high is $96.07 higher than the daily low.

---

### Test 5: Chi-Square Test

**Question**: Is there a significant relationship between Day of Week and Price Movement direction?

**Hypotheses**:
- H₀: Day and Movement are independent
- H₁: Day and Movement are not independent

**Results**:
| Statistic | Value |
|-----------|-------|
| Chi² statistic | 19.336 |
| p-value | 0.0807 |
| Degrees of Freedom | 12 |

**Decision**: **FAIL TO REJECT H₀** (p > 0.05)

**Conclusion**: At 5% significance level, there is no statistically significant relationship between the day of the week and price movement direction. Price movements appear to be independent of the day.

---

## Summary Table

| Test | Question | p-value | Significant? |
|------|----------|---------|--------------|
| One-Sample T-Test | Mean return = 0? | 0.0386 | ✓ Yes |
| Two-Sample T-Test | 2021 = 2022 prices? | < 2.2e-16 | ✓ Yes |
| Correlation Test | Correlation exists? | < 2.2e-16 | ✓ Yes |
| Paired T-Test | High = Low? | < 2.2e-16 | ✓ Yes |
| Chi-Square Test | Day affects movement? | 0.0807 | ✗ No |

## Key Takeaways

1. **Positive Returns**: Ethereum shows statistically significant positive average daily returns
2. **Year Difference**: 2021 had significantly higher prices than 2022
3. **Price-Volume Correlation**: Higher prices correlate with higher volume
4. **Daily Range**: Significant difference between daily high and low prices
5. **Day Independence**: Day of week does not significantly affect price movement

## Statistical Significance vs Practical Significance

- **Statistical significance**: p < 0.05 (results unlikely due to chance)
- **Practical significance**: Whether the difference matters in real-world applications

## Files

- Test results: `hypothesis_test_results.txt`
- Dashboard: `dashboard.html`

## Related Measures

- [Mean](01-mean.md)
- [Standard Deviation](04-standard-deviation.md)
- [Quartiles](06-quartiles.md)
