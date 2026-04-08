import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Déposez votre code à partir d'ici :

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/paris')
def paris():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 48.8566,
        "longitude": 2.3522,
        "hourly": "temperature_2m",
        "forecast_days": 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    result = {
        "time": data["hourly"]["time"],
        "temperature_2m": data["hourly"]["temperature_2m"]
    }
    return jsonify(result)

@app.route('/rapport')
def rapport():
    return render_template('graphique.html')

@app.route('/histogramme')
def histogramme():
    return render_template('histogramme.html')

@app.route('/atelier')
def atelier():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 48.8566,
        "longitude": 2.3522,
        "hourly": ["windspeed_10m", "precipitation"],
        "forecast_days": 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    result = {
        "time": data["hourly"]["time"],
        "windspeed_10m": data["hourly"]["windspeed_10m"],
        "precipitation": data["hourly"]["precipitation"]
    }
    return jsonify(result)

# Ne rien mettre après ce commentaire

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
