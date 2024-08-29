from flask import Flask, render_template, request
from weather import getCurrentWeather, getCityForecast
from waitress import serve
import werkzeug.serving
import datetime

app = Flask(__name__)

@app.route('/')     # Homepage
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def getWeather():
    city = request.args.get('city')
    if not bool(city.strip()): city = 'Mumbai'     # Check for empty strings
    weather_data = getCurrentWeather(city)
    if not weather_data['cod'] == 200: return render_template('citynotfound.html')     # Check status code
    today = datetime.datetime.now()
    current_date = today.strftime("%A, %B %d")
    
    # Simple City Weather Conditions
    city = weather_data['name']
    status = weather_data['weather'][0]['main']
    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    min_temp = weather_data['main']['temp_min']
    max_temp = weather_data['main']['temp_max']
    wind_speed = weather_data['wind']['speed']
    icons = {
        'clear':'fa-sun',
        'clouds':'fa-cloud',
        'drizzle':'fa=cloud-rain',
        'fog':'fa-smog',
        'haze':'fa-smog',
        'mist':'fa-smog',
        'smoke':'fa-smog',
        'snow':'fa-snowflake',
        'tornado':'fa-tornado',
        'thunderstorm':'fa-cloud-bolt',
        'rain':'fa-cloud-showers-heavy',
        'wind':'fa-wind',
    }
    weather_icon = icons[weather_data["weather"][0]["main"].lower()]

    # 5 day weather forecast
    weather_forecast = getCityForecast(city)
    five_day_unformatted = [today, today + datetime.timedelta(days=1), today + datetime.timedelta(days=2), today + datetime.timedelta(days=3), today + datetime.timedelta(days=4)]
    five_day_dates_list = [date.strftime("%a") for date in five_day_unformatted]
    five_day_temp_list = [round(item['main']['temp']) for item in weather_forecast['list'] if '12:00:00' in item['dt_txt']]     # 5 day temperature list
    five_day_weather_list = [item['weather'][0]['main'] for item in weather_forecast['list']
                             if '12:00:00' in item['dt_txt']]   # 5 day weather list
    
    five_day_weather_icons = [icons[i.lower()] for i in five_day_weather_list]

    return render_template(
        'weather.html',
        city=city,
        status=status,
        weather_icon = weather_icon,
        current_date=current_date,
        temp=temp,
        feels_like=feels_like,
        min_temp=min_temp, 
        max_temp=max_temp,
        wind_speed=wind_speed,
        five_day_temp_list=five_day_temp_list, 
        five_day_weather_list=five_day_weather_list,
        five_day_dates_list=five_day_dates_list,
        five_day_weather_icons = five_day_weather_icons,
    )
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
    #serve(app, host='0.0.0.0', port=3000)