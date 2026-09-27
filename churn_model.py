import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("data/player_data.csv")

features = [
    "matches_played",
    "avg_session_minutes",
    "days_since_last_login",
    "avg_kills",
    "win_rate"
]

X = data[features]
y = data["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model, "churn_model.pkl")

print("Churn model trained successfully!")
print("Accuracy:", model.score(X_test, y_test))