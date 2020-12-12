import joblib

class Churn:
    
    def __init__(self):
        self.scaler = joblib.load('../parameters/minmaxscaler_cycle3.joblib')
        
    def data_cleaning(self, df1):
        new_columns = {'Age': 'age', 'Balance': 'balance', 'NumOfProducts': 'num_of_products'}
        df1.rename(columns=new_columns, inplace=True)
        df1 = df1[['age', 'balance', 'num_of_products']]
        
        return df1
    
    def data_preparation(self, df2):
        best_columns = ['age', 'balance', 'num_of_products']
        df2[best_columns] = self.scaler.transform(df2[best_columns])
        
        return df2
    
    def get_prediction(self, model, original_data, test_data):
        pred = model.predict(test_data)
        original_data['Prediction'] = pred
        
        return original_data.to_json(orient="records", date_format="iso")