from flask import Flask
import requests
import os
import redis
import json

app = Flask(__name__)
ow_api_key = os.environ["OPEN_WEATHER_API_KEY"]
ow_target_url = 'https://api.openweathermap.org/data/2.5/weather'
r = redis.StrictRedis(host="redis-service", port=6379, decode_responses=True, db=1)

def get_request_for_coordinates(lon, lat, fkey, skey):
    params={
        "lat":lat,
        "lon":lon,
        "appid":ow_api_key
    }

    res = requests.get(ow_target_url, params=params)
    return res.json()[fkey][skey]

def get_request(city, fkey, skey):
    params = {
            "q":city,
            "appid":ow_api_key
    }

    res = requests.get(ow_target_url, params=params)
    return res.json()[fkey][skey]

@app.route("/weather/cities")
def get_cities():
    cities_data = r.hgetall("weather")
    res = ""

    for k, v in cities_data.items():
        v_dict = json.loads(v)
        lon = v_dict["lon"]
        lat = v_dict["lat"]
        temp = v_dict["temperature"]

        res += f"{lon} {lat} {k}: {temp}\n"
    return res

@app.route("/weather/temp/<string:city>")
def get_temperature(city):
    temp = round(float(get_request(city, "main", "temp")) - 273.15)
    return f"{temp} °Celsius"

@app.route("/weather/humidity/<string:city>")
def get_humidity(city):
    humidity = get_request(city, "main", "humidity")
    return f"Humidity: {humidity}"

@app.route("/weather/temp-coordinates/<float:lon>/<float:lat>")
def get_temperature_with_coordinates(lon, lat):
    temp = round(float(get_request_for_coordinates(lon, lat, "main", "temp")) - 273.15)
    return f"{temp} °Celsius"   

@app.route("/weather/humidity-coordinates/<float:lon>/<float:lat>")
def get_humidity_with_coordinates(lon, lat):
    humidity = get_request_for_coordinates(lon, lat, "main", "humidity")
    return f"Humidity: {humidity}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
