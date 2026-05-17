import mlflow
import pandas as pd


print("--- Starting Task 2: Model Search and Registration ---")

# The name of the experiment we used in Task 1
EXPERIMENT_NAME = "Tutorial_[YourName]"  # TODO: Replace with your experiment name

# TODO 2.1: Use mlflow.search_runs() to get all runs from your experiment.
# HINT: Pass the argument experiment_names=[EXPERIMENT_NAME]
# runs_df = ...


# TODO 2.2: Sort the dataframe to find the run with the highest accuracy.
# HINT: MLflow autolog saves the training accuracy as 'metrics.training_accuracy_score'.
# Use standard pandas sorting: sort_values(by="...", ascending=False)
# best_run = ...
# best_run_id = ...

# print(f"\nThe best model is from Run ID: {best_run_id}")


# TODO 2.3: Register the best model.
# HINT: The path to the model is usually f"runs:/{best_run_id}/model"
# Use mlflow.register_model(model_uri, "DiabetesPredictor")


print("\nTask 2 execution completed! Check the 'Models' tab in the MLflow UI.")