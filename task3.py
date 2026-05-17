import requests
import json

print("--- Starting Task 3: API Client ---")

# The endpoint where the MLflow model is listening
url = "http://127.0.0.1:5001/invocations"

headers = {
    "Content-Type": "application/json"
}

# Example patient data
# Columns: ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age']
patient_columns = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age"]
patient_values = [6, 148, 72, 35, 0, 33.6, 0.627, 50]

# TODO 3.1: Create the JSON payload.
# MLflow expects a very specific format called 'dataframe_split'.
# Structure: {"dataframe_split": {"columns": [...], "data": [[...]]}}
# payload = ...


# TODO 3.2: Send a POST request using the 'requests' library.
# HINT: requests.post(url=..., headers=..., json=...)
# response = ...


# TODO 3.3: Print the raw response text to see what the server returns.
# HINT: print(response.text)


# TODO 3.4: Parse the JSON response and extract just the prediction value.
# HINT: The response is usually a dictionary like {"predictions": [1]}
# Extract the list and print a clean message (e.g., "Prediction: [1]")