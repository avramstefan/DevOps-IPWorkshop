from flask import Flask
import requests
import redis
import os
import json

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis-service', port=6379, db=1)

API_KEY = os.environ["OPEN_WEATHER_API_KEY"]
API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

@app.route('/locations/<city>')
def update_temperature(city):
    response = requests.get(API_URL.format(city, API_KEY))
    data = response.json()

    if 'main' in data and 'temp' in data['main']:
        temperature = round(float(data['main']['temp']) - 273.15)

        v = {
            "lon":data["coord"]["lon"],
            "lat":data["coord"]["lat"],
            "temperature":temperature
        }

        serialized_v = json.dumps(v)
        redis_client.hset('weather', city, serialized_v)
        return f"Temperature for {city}: {temperature}°C\n"
    else:
        return f"Temperature data not available for {city}\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)

