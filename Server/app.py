from flask import Flask, request, jsonify
from utils import *

app = Flask(__name__)

# Khoi tao model
model = random_forest_model()

@app.route('/api/predict', methods=['POST'])
def predict():
    # Nhan data tu input
    input = request.get_json()
    # Tien xu ly data
    data = preprocess_data_input(input)
    # Make predictions using your model
    predictions = get_class_value(model.predict([data]))
    # Format predictions as JSON response
    response = {
        'predictions': predictions,
        'input': input
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
