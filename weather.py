from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def getCurrentWeather(city='Mumbai'):
    api_key = os.getenv('API_KEY')
    api_endpoint = 'https://api.openweathermap.org/data/2.5/weather'
    forecast_params = {
        'appid': api_key,
        'q': city,
        'units': 'metric'
    }
    weatherData = requests.get(api_endpoint, params=forecast_params).json()
    return weatherData

def getCityForecast(city='Mumbai'):
    api_key = os.getenv('API_KEY')
    forecast_params = {
        'appid': api_key,
        'q': city,
        'units': 'metric'
    }
    api_forecast_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
    forecast_data = requests.get(api_forecast_endpoint, params=forecast_params).json()
    return forecast_data

if __name__ == '__main__':
    print('\n*** Get Current Weather Conditions *** ')
    city = input('Please Enter City Name: ')
    if not bool(city.strip()): 
        city = 'Mumbai'     # Check for empty strings
    weather = getCityForecast(city)
    print('\n')
    pprint(weather)