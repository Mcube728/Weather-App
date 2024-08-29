from flask import Flask, render_template, request
from weather import getCurrentWeather
from waitress import serve
import werkzeug.serving

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
    return render_template(
        'weather.html',
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp = f"{weather_data['main']['temp']:.2f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
    )
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
    #serve(app, host='0.0.0.0', port=3000)