import pandas as pd
import numpy as np

class ModelComparison:
    def __init__(self):
        self.results = {}

    def add_model_results(
        self, model_name, food_names, actual_values, predicted_values
    ):
        """
        Adds a new set of model results to the comparison.
        :param model_name: Name of the model.
        :param food_names: List of food item names.
        :param actual_values: List of actual values.
        :param predicted_values: List of predicted values.
        """
        # Validate that the input arrays have the same shape
        if actual_values.shape != predicted_values.shape:
            raise ValueError("The shape of actual_values and predicted_values must match.")
        
        # Create a DataFrame for each set of actual vs predicted values
        data = {'Food Item': food_names}
        for i in range(actual_values.shape[1]):
            data[f'Actual Value - {i+1}'] = actual_values[:, i]
            data[f'Predicted Value - {i+1}'] = predicted_values[:, i]
            data[f'Absolute Error - {i+1}'] = np.abs(actual_values[:, i] - predicted_values[:, i])

        df = pd.DataFrame(data)
        self.results[model_name] = df

    def export_to_excel(self, file_path):
        """
        Exports the results to an Excel file.
        :param file_path: File path for the Excel file.
        """
        with pd.ExcelWriter(file_path) as writer:
            for model_name, df in self.results.items():
                df.to_excel(writer, sheet_name=model_name, index=False)
