
from flask import Flask, request, jsonify
import joblib
model = joblib.load('model/model.pkl')
app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict_post():
    data = request.get_json(silent=True) or {}
    features = data.get('features')
    if not isinstance(features, list) or len(features) != 2:
        return jsonify({'error': 'features must contain exactly 2 values'}), 400
    try: values = [float(value) for value in features]
    except (TypeError, ValueError): return jsonify({'error': 'features must be numeric'}), 400
    return jsonify({'prediction': float(model.predict([values])[0])})
@app.route('/predict/<f1>/<f2>', methods=['GET'])
def predict_get(f1, f2):
    try: values = [float(f1), float(f2)]
    except ValueError: return jsonify({'error': 'path values must be numeric'}), 400
    return jsonify({'prediction': float(model.predict([values])[0])})
if __name__ == '__main__': app.run(port=5000)
