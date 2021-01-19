#!/usr/bin/python3
""" Handling hbnb route
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb')
def index2():
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True)
