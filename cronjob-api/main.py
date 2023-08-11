from flask import Flask
import redis

app = Flask(__name__)
r = redis.StrictRedis(host="redis-service", port=6379, decode_responses=True, db=1)

@app.route("/guess/<int:number>")
def guess(number):
    rn = int(r.get("rn"))
    print(rn)

    if rn == number:
        return "You guessed the number"
    elif rn < number:
        return "It's bigger"
    return "It's smaller"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

