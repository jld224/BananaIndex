# Project README

## Introduction

This project focuses on developing a comprehensive analysis and predictive modeling framework to evaluate the environmental impact of food production through the lens of the Banana Index. Utilizing core Python libraries for data manipulation and visualization, along with advanced machine learning and deep learning techniques, the project aims to predict the Banana Index values for different food items, enabling a better understanding of their environmental footprints.

### Core Libraries Used:

- `pandas` for data manipulation
- `numpy` for numerical computations
- `matplotlib` and `seaborn` for data visualization
- `joblib` for model serialization

### Machine Learning and Model Evaluation:

- `sklearn` for preprocessing, model evaluation, pipeline creation, and ensemble methods like RandomForestRegressor and GradientBoostingRegressor.
- `tensorflow` and `keras` for building deep learning models.

### Hyperparameter Optimization:

- `hyperopt` for optimizing the neural network architecture and parameters.

### Custom Functions:

- Ensure `model_funcs.py` and `ModelComparison.py` files are available for wrapping models and evaluating performance.

## Getting Started

1. **Environment Setup:** Make sure you have Python 3.6+ installed. It's recommended to use a virtual environment.

2. **Dependency Installation:** Install all required libraries using `pip install -r requirements.txt` (ensure you have a requirements file created).

3. **Data Preparation:** Load and preprocess the dataset. Apply label encoding to categorical variables, impute missing values, and scale the features.

4. **Model Training and Evaluation:** Train different models including Linear Regression, RandomForest, and Neural Networks. Evaluate their performance using metrics like R-squared and Mean Squared Error (MSE).

5. **Hyperparameter Tuning:** Use GridSearchCV for model tuning and HyperOpt for optimizing neural network parameters.

6. **Visualization:** Visualize the distribution of Banana Index across different food categories and the feature importance for RandomForestRegressor.

7. **Custom Analysis:** Implement custom functions to calculate the Nutritional Footprint Index (NFI) and visualize the results.

## Key Files and Folders

- `bananaindex_with_categories.csv`: The dataset file.
- `model_funcs.py`: Contains utility functions for model training and evaluation.
- `ModelComparison.py`: A script for comparing different models' performances.
- `requirements.txt`: List all dependencies for the project.

## Running the Project

1. Prepare your data and environment as described in the Getting Started section.
2. Execute the analysis scripts in a sequential manner, starting from data preprocessing to model training and evaluation.
3. Use the custom functions provided for in-depth analysis and visualization of results.

## Results

The project includes detailed exploration of data, training of multiple machine learning and deep learning models, and a comparison of their performance. Additionally, it introduces the concept of the Nutritional Footprint Index (NFI) to evaluate food items based on their environmental and nutritional impact.

## Conclusion

This framework offers a robust approach to understanding and predicting the environmental impact of food production. Through detailed analysis and predictive modeling, it supports the development of more sustainable food consumption patterns.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
