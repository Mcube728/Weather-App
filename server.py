from flask import Flask, render_template, request
from weather import getCurrentWeather
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
    )
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
    #serve(app, host='0.0.0.0', port=3000)