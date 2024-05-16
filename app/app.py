 
from flask import Flask, request, jsonify
import joblib
from src.data_preprocessing import preprocess_data

app = Flask(__name__)

# Load your model here
model = joblib.load('path/to/your/model.pkl')

@app.route('/')
def home():
    return "Retail Price Optimization API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Add your prediction logic here
    return jsonify({'prediction': 'result'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
