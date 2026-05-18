# MLOps Tutorial: From Script to Production API with MLflow

Welcome to the MLflow tutorial! Today, you will take a standard Machine Learning training script, track its experiments, version the models, and finally deploy the best one as a REST API.

## Setup Instructions

1. **Clone this repository** to your local machine and open the folder in your terminal.
2. **Create a Virtual Environment:**
   `python -m venv venv`
3. **Activate the Virtual Environment:**
   * **Windows (Command Prompt):** `venv\Scripts\activate`
   * **Windows (PowerShell):** `.\venv\Scripts\activate`
   * **macOS / Linux:** `source venv/bin/activate`
   *(You should now see `(venv)` at the beginning of your terminal line).*
4. **Install all required packages:**
   `pip install mlflow uvicorn scikit-learn pandas matplotlib requests psutil`
5. **Start the MLflow Tracking Server:**
   `mlflow ui`
   Go to `http://localhost:5000` in your browser. **Keep this terminal running in the background!**

---

## 📝 Tasks & Grading

Save your screenshots in an `evidence` folder in your repository or show to us during the class.

### 🟢 Task 1: Autologging, Parameter Sweep & Signatures (5 points)
**Goal:** Automate experiment tracking across multiple model configurations and compare them visually.

1. Open `task1.py`.
2. Import `mlflow` and `infer_signature` (from `mlflow.models`).
3. Set your experiment name using `mlflow.set_experiment("Tutorial_[YourName]")` and enable `mlflow.autolog()`.
4. Wrap the training code in a `for` loop to test the provided `param_combinations`.
5. Inside the loop, isolate each run using `with mlflow.start_run(run_name=...):`.
6. Inside the loop, immediately after opening the run context, add a custom tag using `mlflow.set_tag("student_id", "YOUR_INDEX_NUMBER")`.
7. After predicting, generate a model signature using `infer_signature(X_train, predictions)`.
8. At the end of the loop, log the generated Matplotlib plot as an artifact.
9. Open a **new terminal tab**, activate your environment again (`venv\Scripts\activate`), and run your script: `python task1.py`.
10. **Go to the MLflow UI** (`http://localhost:5000`), select your experiment, and check the boxes next to your 3 new runs.
11. Click the blue **"Compare"** button. Scroll down to the Scatter Plot, set the X-axis to `max_depth` and the Y-axis to `training_accuracy_score`.
* **Proof of completion:** Take a screenshot of the MLflow Compare screen showing the Scatter Plot with your 3 runs plotted. Save as `task1.png`.

### 🟡 Task 2: Automated Model Registry (10 points)
**Goal:** Learn how to query your experiment logs programmatically and register the best model without touching the UI.

1. Open the `task2.py` file.
2. Use `mlflow.search_runs()` to retrieve a pandas DataFrame of all runs in your experiment.
3. Sort the DataFrame to find the run with the highest `metrics.training_accuracy_score`.
4. Extract the `run_id` of the best model.
5. Construct the model URI (format: `runs:/<run_id>/model`) and register it using `mlflow.register_model()` with the name `"DiabetesPredictor"`.
6. Run your script: `python task2.py`.
* **Proof of completion:** Take a screenshot of the **"Models"** tab in the MLflow UI (`http://localhost:5000`) showing your successfully registered `DiabetesPredictor` model. Save it as `task2.png`.

### 🔴 Task 3: Model Serving & REST API Client (15 points)
**Goal:** Deploy your registered model as a live microservice and write a Python client to query it.

1. **Start the MLflow Server:** Open a **NEW** terminal window. 
2. **IMPORTANT:** You must activate your virtual environment in this new terminal first!
3. Run the following command to serve your registered `DiabetesPredictor` model on port 5001:
   `mlflow models serve -m "models:/DiabetesPredictor/1" -p 5001 --env-manager local`
   *(Wait until the terminal says: `Listening at: http://127.0.0.1:5001`)*
4. Open the `task3.py` file.
5. Construct the correct JSON payload. MLflow expects pandas DataFrames to be sent in the `dataframe_split` format.
6. Send a `POST` request to the server's `/invocations` endpoint.
7. Extract and print the prediction from the server's response.
8. Open one more terminal tab, activate the environment, and run your script: `python task3.py`.
* **Proof of completion:** Take a screenshot of your terminal showing the successfully parsed prediction from the API (e.g., `The patient is classified as: POSITIVE (1) for Diabetes.`). Save it as `task3.png`.

---

### 🟣 Task 4: Model Promotion & Aliases (15 points)
**Goal:** Use the `MlflowClient` to programmatically document a specific model version and assign a deployment alias (like "champion"), making it easy for production systems to fetch the right version.

1. Create and open a new file named `task4.py`.
2. Copy the template code provided below into the file.
3. Complete the `TODO` sections to instantiate the client, update the specific model version's description, and set the alias.
4. Open your terminal, activate your environment, and run the script: `python task4.py`.
5. **Go to the MLflow UI** (`http://localhost:5000`), click on the **"Models"** tab, click `DiabetesPredictor`, and then click on **Version 1**.
* **Proof of completion:** Take a screenshot of the `DiabetesPredictor` Version 1 page showing your new description and the `@champion` alias. Save it as `task4.png`.