from flask import Flask, render_template, request
import pandas as pd
import joblib


# ==========================================
# CREATE FLASK APP
# ==========================================

app = Flask(__name__)


# ==========================================
# LOAD MODELS
# ==========================================

classification_model = joblib.load(
    "models/classification_model.pkl"
)

clustering_model = joblib.load(
    "models/clustering_model.pkl"
)

scaler = joblib.load(
    "models/scaler.pkl"
)

encoders = joblib.load(
    "models/encoders.pkl"
)


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    return render_template(
        "index.html",
        prediction=None,
        probability=None,
        cluster=None
    )


# ==========================================
# PREDICTION
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get values from HTML form

        airline = request.form["airline"]
        origin = request.form["origin"]
        destination = request.form["destination"]

        distance = float(
            request.form["distance"]
        )

        departure_hour = int(
            request.form["departure_hour"]
        )

        weather = request.form["weather"]

        previous_delay = float(
            request.form["previous_delay"]
        )


        # ==================================
        # ENCODE INPUT
        # ==================================

        airline_encoded = encoders["airline"].transform(
            [airline]
        )[0]

        origin_encoded = encoders["origin"].transform(
            [origin]
        )[0]

        destination_encoded = encoders["destination"].transform(
            [destination]
        )[0]

        weather_encoded = encoders["weather"].transform(
            [weather]
        )[0]


        # ==================================
        # CREATE INPUT DATA
        # ==================================

        input_data = pd.DataFrame(
            [[
                airline_encoded,
                origin_encoded,
                destination_encoded,
                distance,
                departure_hour,
                weather_encoded,
                previous_delay
            ]],
            columns=[
                "airline",
                "origin",
                "destination",
                "distance",
                "departure_hour",
                "weather",
                "previous_delay"
            ]
        )


        # ==================================
        # CLASSIFICATION PREDICTION
        # ==================================

        prediction = classification_model.predict(
            input_data
        )[0]


        # Probability

        probability = classification_model.predict_proba(
            input_data
        )[0][1] * 100


        if prediction == 1:

            prediction_text = "Delayed"

        else:

            prediction_text = "Not Delayed"


        # ==================================
        # CLUSTERING
        # ==================================

        cluster_data = pd.DataFrame(
            [[
                distance,
                departure_hour,
                previous_delay
            ]],
            columns=[
                "distance",
                "departure_hour",
                "previous_delay"
            ]
        )


        scaled_cluster_data = scaler.transform(
            cluster_data
        )


        cluster = clustering_model.predict(
            scaled_cluster_data
        )[0]


        return render_template(
            "index.html",
            prediction=prediction_text,
            probability=round(probability, 2),
            cluster=cluster
        )


    except Exception as e:

        return render_template(
            "index.html",
            prediction="Error: " + str(e),
            probability=None,
            cluster=None
        )


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )