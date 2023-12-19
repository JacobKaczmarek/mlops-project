from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from pathlib import Path
from mlops_project.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    input_data = request.form.to_dict()
    input_data = pd.DataFrame(input_data, index=[0])
    input_data = input_data.astype(np.float64)

    prediction_pipeline = PredictionPipeline()
    prediction = prediction_pipeline.predict(input_data)

    return render_template("result.html", prediction="{:10.2f}".format(prediction[0]))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)