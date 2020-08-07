import json
import pickle
import pandas as pd 
import numpy as np

__data_columns = None
__model = None

def predict_price(year, sqFt, bathrooms, bedrooms):
    data = {'yearBuilt' : [year], 'finished \n(SqFt)': [sqFt], ' bathrooms ': [bathrooms], ' bedrooms ': [bedrooms]}
    prediction = pd.DataFrame.from_dict(data)
    return round(__model.predict(prediction)[0])
     

def load_saved_artifacts():
    print("loading saved artifacts")
    global __data_columns
    global __model

    with open("server/artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']

    with open("server/artifacts/philly_housing_model.pickle", 'rb') as f:
        __model =  pickle.load(f)

    print ("done loading artifacts")

if __name__ == "__main__":
    load_saved_artifacts()
    print(predict_price(2005, 4000, 3, 5))
    
