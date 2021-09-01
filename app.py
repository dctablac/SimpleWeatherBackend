from flask import Flask
from dotenv import dotenv_values
import requests

config = dotenv_values('.env')

app = Flask(__name__)

@app.route("/weather")
def get_weather():
    api_url = 'http://api.openweathermap.org/data/2.5/forecast?q='
    city = 'Irvine'
    api_string = api_url + city + '&appid=' + config["API_KEY"]
    return requests.get(api_string).json()

@app.route("/")
def hello_world():
    return "HELLO WORLD"