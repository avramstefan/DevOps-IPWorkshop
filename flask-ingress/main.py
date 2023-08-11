from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/echo/<string:input_string>')
def echo(input_string):
    return input_string

@app.route('/reverse/<string:input_string>')
def reverse(input_string):
    return input_string[::-1]

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
