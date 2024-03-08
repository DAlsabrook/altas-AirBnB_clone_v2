#!/usr/bin/python3
"""
This is a module to learn how to use flask in creating a webpage
"""
from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_not_fun(text):
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    try:
        return f"{int(n)} is a number"
    except ValueError:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def number_html(n):
    try:
        num = int(n)
        return render_template('5-number.html', content=num)
    except ValueError:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
