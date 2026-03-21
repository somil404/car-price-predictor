from flask import Flask, render_template, request, redirect
from flask_cors import CORS,cross_origin
import numpy as np
import pandas as pd
import pickle
import os

app = Flask(__name__)

cors = CORS(app)

car = pd.read_csv(os.path.join(os.path.dirname(__file__), "new_df.csv"))
model = pickle.load(open(os.path.join(os.path.dirname(__file__), 'model.pkl'), 'rb'))

@app.route('/', methods = ['GET', 'POST'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(),reverse=True)
    fuel_type = car['fuel_type'].unique()
    companies.insert(0,'Select Company')
    return render_template('index.html', companies = companies, car_models = car_models, years = year, fuel_types = fuel_type)

@app.route('/predict', methods = ['POST'])
@cross_origin()
def predict():
    try:
        company = request.form.get('company')
        car_models = request.form.get('car_models')
        year = int(request.form.get('year'))
        fuel_type = request.form.get('fuel_type')
        kilo_driven = int(request.form.get('kilo_driven'))

        prediction = model.predict(pd.DataFrame(
            [[car_models, company, int(year), int(kilo_driven), fuel_type]],
            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
        ))
        print(prediction)
        return str(np.round(np.exp(prediction[0])))

    except:
        return "Error in input"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)