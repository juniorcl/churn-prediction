import joblib
import pandas as pd
from churn.Churn import Churn
from flask import Flask, request, Response

# loading model
model = joblib.load('../models/model_cycle3.joblib')

# initialize API
app = Flask(__name__)

@app.route('/churn/predict', methods=['POST'])
def churn_predict():
    test_json = request.get_json()
   
    if test_json: # there is data
        if isinstance(test_json, dict): # unique example
            test_raw = pd.DataFrame(test_json, index=[0])
            
        else: # multiple example
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
            
        # Instantiate Rossmann class
        pipeline = Churn()
        
        # data cleaning
        df1 = pipeline.data_cleaning(test_raw)
        
        # data preparation
        df2 = pipeline.data_preparation(df1)
        
        # prediction
        df_response = pipeline.get_prediction(model, test_raw, df2)
        
        return df_response
        
        
    else:
        return Reponse('{}', status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run('0.0.0.0')