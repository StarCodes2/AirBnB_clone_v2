#!/usr/bin/python3
""" Starts a Flask Web Application that listens on 0.0.0.0, port 5000. """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_bhnb():
    """ Display Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Displays c plus the content of text. """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """ Displays Python plus the content of text. """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Displays the content of n if it's an integer. """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
