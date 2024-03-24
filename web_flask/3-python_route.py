#!/usr/bin/python3
""" start a flask web app """

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    """ return a string on query """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ return a string on query """
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """ return string on query """
    return "C " + text.replace("_", " ")


@app.route("/python/")
@app.route("/python/<text>")
def python_text(text="is cool"):
    """ return string on query """
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
