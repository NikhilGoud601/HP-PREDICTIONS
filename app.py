from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("House_Price.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    # Numeric inputs
    bedrooms = float(request.form["bedrooms"])
    bathrooms = float(request.form["bathrooms"])
    sqft_living = float(request.form["sqft_living"])
    sqft_lot = float(request.form["sqft_lot"])
    floors = float(request.form["floors"])
    waterfront = int(request.form["waterfront"])
    view = int(request.form["view"])
    condition = int(request.form["condition"])
    sqft_above = float(request.form["sqft_above"])
    sqft_basement = float(request.form["sqft_basement"])
    yr_built = int(request.form["yr_built"])
    yr_renovated = int(request.form["yr_renovated"])
    city = int(request.form["city"])
    country = int(request.form["country"])
    year = int(request.form["year"])
    month = int(request.form["month"])
    day = int(request.form["day"])

    # Arrange features EXACT ORDER (17)
    features = np.array([[
        bedrooms, bathrooms, sqft_living, sqft_lot, floors,
        waterfront, view, condition, sqft_above, sqft_basement,
        yr_built, yr_renovated, city, country, year, month, day
    ]])

    prediction = model.predict(features)[0]

    return render_template(
        "index.html",
        prediction_text=f"₹ {prediction:,.2f}"
    )


if __name__ == "__main__":
    app.run(debug=True)
