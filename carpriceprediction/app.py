from flask import Flask,request,jsonify
import pandas as pd
import numpy as np
import pickle
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "LinearRegressionModel.pkl")

model = pickle.load(open(model_path, 'rb'))
csv_path = os.path.join(BASE_DIR, "Cleaned Car.csv")
car = pd.read_csv(csv_path)

@app.route('/')
def index():
    return "Car Prediction"


@app.route('/get-predict-data', methods=['GET'])
def get_data():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()

     # Convert NumPy int64 values to standard Python int
    companies = [str(c) for c in companies]
    car_models = [str(model) for model in car_models]
    year = [int(y) for y in year]

    data = {
        'companies': companies,
        'car_models': car_models,
        'years': year,
        'fuel_types': list(fuel_type)
    }
    return jsonify(data)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    company = data.get('company')
    year = data.get('year')
    car_model = data.get('car_model')
    fuel_type = data.get('fuel_type')
    kms_driven = data.get('kilo_driven')
 
    prediction = model.predict(pd.DataFrame([[car_model,company,year,kms_driven,fuel_type]], columns=['name','company','year','kms_driven','fuel_type']))
    return jsonify({'prediction': float(np.round(prediction[0], 2))})
    


if __name__=="__main__":
    app.run(debug=True)