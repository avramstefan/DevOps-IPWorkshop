import redis
import requests

r = redis.StrictRedis(host='redis-service', port=6379, decode_responses=True, db=1)


def run_task():
    cities = r.hgetall("weather")

    for city,_ in cities.items():
        c = str(city)
        res = requests.get(f"http://weather-location:5002/locations/{c}")
        
        new_temp = r.hget("weather", city)
        print(f"{city}: {new_temp}") 

if __name__ == "__main__":
    run_task()
