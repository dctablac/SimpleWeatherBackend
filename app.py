from flask import Flask, json
from weather import weather_details


app = Flask(__name__)

@app.route('/weather/<city>',methods=['GET'])
def get_weather(city):
    return weather_details(city)

@app.route('/')
def hello_world():
    return 'Make requests to this url /weather/<city>'