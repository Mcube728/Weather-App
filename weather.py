from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def getCurrentWeather(city='Mumbai'):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weatherData = requests.get(request_url).json()
    return weatherData

if __name__ == '__main__':
    print('\n*** Get Current Weather Conditions *** ')
    city = input('Please Enter City Name: ')
    if not bool(city.strip()): 
        city = 'Mumbai'     # Check for empty strings
    weather = getCurrentWeather(city)
    print('\n')
    pprint(weather)