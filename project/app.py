from pathlib import Path

import joblib
from flask import Flask, jsonify, request


MODEL_PATH = Path(__file__).resolve().parent / "model" / "model.pkl"
model = joblib.load(MODEL_PATH) if MODEL_PATH.exists() else None
app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok", "model_loaded": model is not None})


@app.post("/predict")
def predict():
    if model is None:
        return jsonify({"error": "model is not available"}), 503
    data = request.get_json(silent=True) or {}
    features = data.get("features")
    if not isinstance(features, list) or len(features) != 4:
        return jsonify({"error": "features must be a list of exactly 4 numbers"}), 400
    try:
        values = [float(value) for value in features]
    except (TypeError, ValueError):
        return jsonify({"error": "all features must be numeric"}), 400
    prediction = float(model.predict([values])[0])
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(port=5000)
