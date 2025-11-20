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
Built and tested baseline models to study how model complexity and regularization affect generalization.
Added clear markdown explanations and inline comments for each modeling step.

**Key Experiments**

  - **Linear Models (Ridge, Lasso, ElasticNet):**
  Trained models across a range of alpha values to observe bias–variance behavior. Ridge gave the lowest RMSE (~0.12).

  - **Decision Tree:**
  Increased max_depth to show overfitting. Validation RMSE stabilized around depth 6–8.

  - **Random Forest:**
  Tested the effect of averaging more trees. Found stable results beyond 100 estimators.

  - **Neural Network (MLP):**
  Compared models with and without early stopping. Early stopping improved generalization (RMSE 0.19 vs 0.21).

  - **Curse of Dimensionality:**
  Added random noise features to test robustness. Ridge stayed stable, Random Forest worsened slightly, MLP degraded quickly.

  - **PCA (Dimensionality Reduction):**
  PCA reduced numeric dimensionality and improved generalization for Ridge and MLP. Tree models remained unaffected.

**Key Findings**

- Ridge regression is the most reliable model for this dataset.
- Regularization and early stopping reduce overfitting and improve validation performance.
- PCA effectively removes redundant numeric information without large information loss.
- Random Forests handle non-linearities well but are less data-efficient than Ridge.

## 2025-10-27
Tested the models from notebook 2 on the validation data and compared their accuracy.

**Key Findings**

  - **Ridge**
  performs the best with an average error of ~9% for each property.

  - **ElasticNet** and **Random Forest**
  are the follow ups with a higher average error of 9.9% and 10.2%

  - **Lasso**
  is less accurate then enet and rf because we left out less relevant feautres with this model (10.3%)

  - **MLP**
  is the lowest en shows more variation in its errors aswell, having an average error of 13.8%
