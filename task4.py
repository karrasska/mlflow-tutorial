from mlflow.client import MlflowClient

print("--- Starting Task 4: Model Promotion & Aliases ---")

model_name = "DiabetesPredictor"
model_version = "1"
alias_name = "champion"

# TODO 4.1: Instantiate the MLflow Tracking Client.
# client = ...


# TODO 4.2: Update the specific model version with a description.
# HINT: client.update_model_version(name=..., version=..., description=...)
# print("Updating model version description...")


# TODO 4.3: Assign the "champion" alias to version 1 of your model.
# HINT: client.set_registered_model_alias(name=..., alias=..., version=...)
# print(f"Assigning alias '{alias_name}' to {model_name} v{model_version}...")


print(f"Success! Refresh the MLflow UI -> Models -> {model_name} -> Version {model_version} to see the changes.")