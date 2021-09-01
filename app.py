from flask import Flask

app = Flask(__name__)

@app.route("/weather")
def get_weather():
    return 'GOT YOUR WEATHER'

@app.route("/")
def hello_world():
    return "HELLO WORLD"