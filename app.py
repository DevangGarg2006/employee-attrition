from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model/attrition_model.pkl")
columns = joblib.load("model/columns.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    probability = None

    if request.method == "POST":
        # Create empty input with all features
        input_data = dict.fromkeys(columns, 0)

        # Fill form values
        input_data["Age"] = int(request.form["Age"])
        input_data["DailyRate"] = int(request.form["DailyRate"])
        input_data["DistanceFromHome"] = int(request.form["DistanceFromHome"])
        input_data["Education"] = int(request.form["Education"])
        input_data["MonthlyIncome"] = int(request.form["MonthlyIncome"])
        input_data["NumCompaniesWorked"] = int(request.form["NumCompaniesWorked"])
        input_data["PercentSalaryHike"] = int(request.form["PercentSalaryHike"])
        input_data["TotalWorkingYears"] = int(request.form["TotalWorkingYears"])
        input_data["YearsAtCompany"] = int(request.form["YearsAtCompany"])

        input_df = pd.DataFrame([input_data])

        pred = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1]

        prediction = "High Attrition Risk" if pred == 1 else "Low Attrition Risk"
        probability = round(prob * 100, 2)

    return render_template("index.html", prediction=prediction, probability=probability)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)