# Model Complexity and Generalization

This project explores how machine learning models balance complexity and generalization. Using the Ames Housing dataset, we predict house prices and study how different techniques reduce overfitting and improve robustness.

The project is divided into several notebooks:

    1. **0_data_exploration.ipynb**
    Exploratory Data Analysis (EDA). Examines data distributions, correlations, and outliers.

    2. **1_data_preprocessing_and_baseline.ipynb**
    Data preprocessing pipeline. Imputation, normalization, and baseline regression models such as Ridge, Lasso, and ElasticNet.

    3. **2_bias_variance_dimensionality_reduction.ipynb**
    Experiments on the bias–variance trade-off, regularization, early stopping, and PCA. Comparison between linear, tree-based, and neural models.

    4. **3_model_testing.ipynb**
    Exports and tests the trained models on the official test set. Evaluates performance using RMSE, MAE, and percentage errors.

**Key Findings**

- Ridge (L2 regularization) provided the best balance between accuracy and generalization.
- Early stopping improved neural network performance and reduced overfitting.
- PCA reduced redundancy and improved robustness by filtering noise.
- Simple architectures offered better interpretability, which is crucial for medical and audio-related projects.

**Project Goal**
The goal of this research is to strengthen our understanding of how model complexity, regularization, and dimensionality reduction influence generalization. The insights gained here help us design more stable and interpretable models for real-world applications such as sound classification, ECG signal analysis, image recognition and so on. The goal was to get a better understanding of these concepts, not necessairly in a regression context. But more so an overall context, how can we apply this knowledge onto our other projects? Is the main goal.