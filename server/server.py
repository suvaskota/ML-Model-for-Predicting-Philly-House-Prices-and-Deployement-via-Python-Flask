from flask import Flask, request, jsonify  
import util

app = Flask(__name__)


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    year =  float(request.form['year'])
    sqFt =  float(request.form['sqFt'])
    bathrooms = float(request.form['bathrooms'])
    bedrooms = float(request.form['bedrooms'])

    response = jsonify({
        'estimated_price': util.predict_price(year, sqFt, bathrooms, bedrooms)
    }) 

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    

if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction")
    util.load_saved_artifacts()
    app.run()