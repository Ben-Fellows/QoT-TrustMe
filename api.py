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
@cross_origin(origin='*')
def get_prediction():
    print('Prediction')
    print('Prediction')
    return ('prediction')

@app.route('/predict', methods=['POST'])
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


if __name__ == '__main__':



    lr = joblib.load("model.pkl") # Load "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
    print ('Model columns loaded')

    #app.run(debug=True)