# Stage 13 Homework - Prediction API

This API loads a saved regression model and returns predictions from two numeric inputs.

## Running it

    python app.py

## POST /predict

    curl http://127.0.0.1:5000/predict

Invalid values return a JSON error with HTTP status 400.
