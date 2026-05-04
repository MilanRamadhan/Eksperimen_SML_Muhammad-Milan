import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# set experiment
mlflow.set_experiment("Titanic CI")

# load dataset
df = pd.read_csv("dataset/dataset_clean.csv")

X = df.drop("survived", axis=1)
y = df["survived"]

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# autolog
mlflow.sklearn.autolog()

# 🚨 HAPUS start_run()
model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

# log manual metric (optional, karena autolog sudah handle)
mlflow.log_metric("accuracy_manual", acc)

print("Accuracy:", acc)