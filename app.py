from flask import Flask, render_template, url_for, request
import pickle

app = Flask(__name__)

model = pickle.load(open('savedmodel.sav', 'rb'))

@app.route('/')
def index():
    result = ''
    return render_template("index.html", **locals())

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    temperature = float(request.form['temperature'])
    humidity_1 = float(request.form['humidity_1'])
    humidity_2 = float(request.form['humidity_2'])
    rainfall = float(request.form['rainfall'])
    soil_moisture_1 = float(request.form['soil_moisture_1'])
    soil_moisture_2 = float(request.form['soil_moisture_2'])
    valve = float(request.form['valve'])
    result = model.predict([[temperature, humidity_1, humidity_2, rainfall, soil_moisture_1, soil_moisture_2, valve]])[0]
    return render_template("index.html", **locals())
     

if __name__ == "__main__":
    app.run(debug = True)
