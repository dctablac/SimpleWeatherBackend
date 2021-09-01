from flask import Flask
import requests
import os


app = Flask(__name__)

@app.route("/weather")
def get_weather():
    api_url = 'http://api.openweathermap.org/data/2.5/forecast?q='
    city = 'Irvine'
    api_string = api_url + city + '&appid=' + os.environ["API_KEY"]
    return requests.get(api_string).json()

@app.route("/")
def hello_world():
    return "HELLO WORLD"