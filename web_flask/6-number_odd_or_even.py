#!/usr/bin/python3
""" start a flask web app """

from flask import Flask, render_template
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


@app.route("/number/<int:n>")
def number(n):
    """ return a number """
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def num_template(n):
    """ render a html page """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def even_or_odd(n):
    """ render a even or odd template """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
