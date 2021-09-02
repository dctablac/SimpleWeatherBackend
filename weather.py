import requests
from decouple import config

API_KEY = config('API_KEY')

def weather_details(city: str)->dict:
    ''' Given a city, get the current weather and seven day forecast '''
    current_weather_details = _create_current_weather_details(city)
    seven_day_forecast_details = _create_seven_day_forecast(current_weather_details['lat'], current_weather_details['lon'])

    # # Return necessary information in one JSON
    city_weather_details = {
        'city': city,
        'current_weather': current_weather_details,
        'seven_day_forecast' : seven_day_forecast_details
    }
    return city_weather_details


def _create_current_weather_details(city: str)->dict:
    ''' Given a city, get the necessary current weather details provided by the OpenWeather API '''
    # Get current weather
    current_weather_api_base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    current_weather_api_url = '{0}q={1}&appid={2}'.format(current_weather_api_base_url, city, API_KEY)
    current_weather_response = requests.get(current_weather_api_url).json()

    # Compile necessary current temp details
    current_details = {
        'lat': current_weather_response['coord']['lat'],
        'lon': current_weather_response['coord']['lon'],
        'current_temp': current_weather_response['main']['temp'],
        'temp_min': current_weather_response['main']['temp_min'],
        'temp_max': current_weather_response['main']['temp_max'],
        'feels_like': current_weather_response['main']['feels_like'],
        'dt': current_weather_response['dt'],
        'weather_description': current_weather_response['weather'][0]
    }
    return current_details


def _create_seven_day_forecast(lat: str, lon: str)->dict:
    ''' Given the latitutde and longitude of a city center, get the necessary seven day forecast details
        provided by the OpenWeather API '''
    # Get forecast
    one_call_api_base_url = 'https://api.openweathermap.org/data/2.5/onecall?'
    one_call_api_url = '{0}lat={1}&lon={2}&exclude=current,minutely,hourly&appid={3}'.format(one_call_api_base_url, lat, lon, API_KEY)
    one_call_api_response = requests.get(one_call_api_url).json()

    # Compile necessary forecast details
    forecast_details = {}
    daily_forecasts = one_call_api_response['daily'][1:] # Only get forecast of days after today

    for days_after in range(len(daily_forecasts)):
        forecast_details[days_after + 1] = { # day = index + 1
            'dt': daily_forecasts[days_after]['dt'],
            'temp_min': daily_forecasts[days_after]['temp']['min'],
            'temp_max': daily_forecasts[days_after]['temp']['max'],
            'weather_description': daily_forecasts[days_after]['weather'][0]
        }
    return forecast_details