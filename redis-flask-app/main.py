from flask import Flask, render_template, request, redirect
import redis
import os

app = Flask(__name__)
r = redis.StrictRedis(host="redis-service", port=6379, decode_responses=True, db=1)

@app.post('/set')
def set_pair():
    if request.method == "POST":

        data = request.json

        key = data.get("key")
        value = data.get("value")

        r.set(key, value)

        return "Pair added successfully! 200 OK"
    return "ERR: Not a POST method! 400 Bad Request"

@app.get('/get')
def get_pair():
    if request.method == "GET":
        key = request.args.get("key")
        
        value = r.get(key)

        pair = {key:value}
        return "The pair is " + str(pair) + "  200 OK"
    return "ERR: Not a GET method! 400 Bad Request"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
