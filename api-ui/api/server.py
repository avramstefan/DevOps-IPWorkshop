from flask import Flask
import os

app = Flask(__name__)

@app.route("/echo/<string:text>'")
def echo(text):
    return text

@app.route("/reverse/<string:text>'")
def reverse(text):
    return text[::-1]    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")