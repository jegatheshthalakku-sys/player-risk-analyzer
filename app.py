from flask import Flask, render_template, request
import joblib
from toxicity import detect_toxicity

app = Flask(__name__)

model = joblib.load("churn_model.pkl")

player_data = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    player_id = request.form["player_id"]

    matches = float(request.form["matches"])
    session = float(request.form["session"])
    days = float(request.form["days"])
    kills = float(request.form["kills"])
    winrate = float(request.form["winrate"])

    features = [[matches, session, days, kills, winrate]]

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    result = "High Churn Risk" if prediction == 1 else "Low Churn Risk"

    player_data[player_id] = {
        "churn_probability": round(probability * 100, 2),
        "churn_result": result
    }

    return render_template(
        "index.html",
        churn_result=result,
        churn_probability=round(probability * 100, 2),
        player_id=player_id
    )


@app.route("/toxicity", methods=["POST"])
def toxicity():

    player_id = request.form["player_id"]
    message = request.form["message"]

    result = detect_toxicity(message)

    player_info = player_data.get(player_id)

    combined_risk = None

    if player_info:

        churn_probability = player_info["churn_probability"]

        toxicity_score = 100 if result["toxic"] else 0

        combined_risk = round(
            (churn_probability * 0.7) +
            (toxicity_score * 0.3),
            2
        )

    return render_template(
        "index.html",
        toxicity_result=result,
        combined_risk=combined_risk,
        player_id=player_id
    )


if __name__ == "__main__":
    app.run(debug=True)