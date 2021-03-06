# Dependencies
import sys

from flask import Flask, request, jsonify
import joblib
import traceback
import pandas as pd
import numpy as np
from flask_cors import CORS, cross_origin

# Your API definition
app = Flask(__name__)
CORS(app)




@app.route('/', methods=['GET'])
@cross_origin()
def get_prediction():
    print('Prediction')
    return ('prediction')

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(lr.predict(query))

            return jsonify({'Prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})

@app.after_request
def add_headers(response):
    response.headers.add('Content-Type', 'application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Expose-Headers', 'Content-Type,Content-Length,Authorization,X-Pagination')
    return response

if __name__ == '__main__':



    lr = joblib.load("model.pkl") # Load "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
    print ('Model columns loaded')

    #app.run(debug=True)