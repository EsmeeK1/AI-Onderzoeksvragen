## 2025-10-21 — EDA & Data Cleaning Notes (House Prices)

**Summary**
Completed the initial Exploratory Data Analysis (EDA) for the Ames Housing dataset.
Added detailed inline comments explaining each analysis step (missing values, distributions, correlations, outliers, etc.).

**Key Findings**
- The target variable `SalePrice` is right-skewed; a log-transform (`SalePriceLog`) produces a more normal distribution.
- Strongest correlations with price: `OverallQual`, `GrLivArea`, `GarageCars`, `TotalBsmtSF`, `1stFlrSF`, and `YearBuilt`.
- High-missing columns: `PoolQC`, `MiscFeature`, `Alley`, `Fence`, and `FireplaceQu` — these indicate absence rather than missing data.
- Neighborhood and quality features explain a large share of price variance.

**Data Cleaning**
- Identified two clear outliers: **rows 523 and 1298** (both located in *Edwards*).
  - These houses are of relatively high quality but were sold for under \$200,000 — inconsistent with the rest of the dataset.
  - To improve generalization and reduce noise, these rows were removed.

**Next Steps**
- Build a preprocessing pipeline (numeric/categorical split, imputation, encoding, scaling).
- Prepare feature-target matrices (`X`, `y`) for baseline modeling experiments.

## 2025-10-22