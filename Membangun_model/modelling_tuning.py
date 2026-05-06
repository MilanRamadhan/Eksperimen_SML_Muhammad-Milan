import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv(
    'dataset/dataset_clean.csv',
    nrows=1000,
    low_memory=False
)

# Target
TARGET = 'Survived'

# Features dan target
X = df.drop(columns=[TARGET])
y = df[TARGET]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model sederhana (lebih ringan dari RandomForest)
model = DecisionTreeClassifier(max_depth=3)

with mlflow.start_run(run_name='simple_tuning'):

    # Training
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Logging MLflow
    mlflow.log_param("max_depth", 3)
    mlflow.log_metric("accuracy", accuracy)

    # Save model
    mlflow.sklearn.log_model(model, "model")

    print("Accuracy:", accuracy)