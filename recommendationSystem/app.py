from flask import Flask, request, jsonify
import contentBasedModel as CBM

app = Flask(__name__)

@app.route('/')
def home():
    return "Machine Learning Model API"

@app.route('/predict/contentBased', methods=['GET'])
def predict():
    data = request.get_json(force=True)
    model = CBM.contentBasedModel(data["input"][0])
    prediction = model.get_recommendation()
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)