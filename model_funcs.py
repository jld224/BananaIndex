from sklearn.multioutput import MultiOutputRegressor
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

def model_wrap(model_input, X_train, y_train, X_test):
    multi_output_model = MultiOutputRegressor(model_input)
    multi_output_model.fit(X_train, y_train)
    return multi_output_model.predict(X_test)

def evaluate(y_test, y_pred, model_name=None):
    # Evaluate the model
    for r in range(y_test.shape[1]):
        r2 = r2_score(y_test[:, r], y_pred[:, r])
        print(f'R-squared for the {r + 1} target: {r2}')

    plt.figure(figsize=(14, 4))

    for i in range(y_test.shape[1]):
        plt.subplot(1, y_test.shape[1], i+1)
        plt.scatter(y_test[:, i], y_pred[:, i], color='blue', label='Actual vs Predicted')
        plt.title(f'Target {i+1}')
        plt.xlabel('Actual Values')
        plt.ylabel('Predicted Values')

        min_val = min(y_test[:, i].min(), y_pred[:, i].min())
        max_val = max(y_test[:, i].max(), y_pred[:, i].max())
        plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', lw=2)
        plt.legend()
        plt.grid(True)

    plt.tight_layout()

    # Set the overall title
    if model_name:
        plt.suptitle(f'Evaluation of {model_name}', fontsize=16, y=1.05)

    plt.show()