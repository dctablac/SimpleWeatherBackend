from flask import Flask, make_response
from flask_cors import cross_origin
from weather import weather_details

app = Flask(__name__)

@app.route('/weather/<city>', methods=['GET'])
@cross_origin(origins=['http://localhost:8080', 'https://dctablac-simple-weather.herokuapp.com/'])
def get_weather(city):
    return make_response(weather_details(city))

@app.route('/')
def hello_world():
    return 'Make requests to this url /weather/<city>'