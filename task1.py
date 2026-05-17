import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# TODO 1.1: Import 'mlflow' and 'infer_signature' from 'mlflow.models'


print("Loading data...")
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
columns = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv(url, names=columns)

X = df.drop('class', axis=1)
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TODO 1.2: Set experiment name to "Tutorial_[YourName]" and enable autologging.


# We want to test 3 different configurations of our Random Forest
param_combinations = [(10, 3), (50, 5), (100, 10)]

# TODO 1.3: Start a 'for' loop iterating over 'param_combinations' (n_est, depth)
# for ... in ...:

    # TODO 1.4: Open an MLflow run context using 'with mlflow.start_run(run_name=...):'
    # with ...:

        # TODO 1.4b: Add a custom tag with your index number
        # mlflow.set_tag("student_id", "123456")
        
        # --- Make sure all code below is indented correctly inside the 'with' block! ---
        # print(f"\nTraining model with n_estimators={n_est}, max_depth={depth}...")
        
        # model = RandomForestClassifier(n_estimators=n_est, max_depth=depth, random_state=42)
        # model.fit(X_train, y_train)

        # predictions = model.predict(X_test)
        # acc = accuracy_score(y_test, predictions)
        # print(f"Accuracy: {acc:.4f}")

        # TODO 1.5: Infer the model signature using 'infer_signature(X_train, predictions)'
        # signature = ...

        # Generate a Feature Importance plot
        # plt.figure(figsize=(8, 5))
        # plt.bar(X.columns, model.feature_importances_, color='skyblue')
        # plt.title(f"Feature Importances (n={n_est}, depth={depth})")
        # plt.xlabel("Features")
        # plt.ylabel("Importance")
        # plot_filename = f"feature_importance_n{n_est}_d{depth}.png"
        # plt.savefig(plot_filename)
        # plt.close()

        # TODO 1.6: Log the saved plot image (plot_filename) as an artifact in MLflow
        

print("\nTask 1 execution completed! Check the MLflow UI.")

