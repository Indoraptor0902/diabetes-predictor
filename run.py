from flask import Flask, request, render_template
from diabetes_prediction import DiabetesPredictor

app = Flask(__name__)

#Press Ctrl + C to exit


@app.route("/", methods=["GET", "POST"])
def home():
    statement = ""
    
    if request.method == "POST":
        pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age = request.form["pregnancies"], request.form["glucose"], request.form["bloodpressure"], request.form["skinthickness"], request.form["insulin"], request.form["bmi"], request.form["diabetespedigreefunction"], request.form["age"]
        predictor = DiabetesPredictor()
        prediction = predictor.has_diabetes([pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age])
        statement = "You are at risk of diabetes." if prediction else "You are not at risk of diabetes."

    return render_template("index.html", statement=statement)


if __name__ == "__main__":
    app.run(debug=True)