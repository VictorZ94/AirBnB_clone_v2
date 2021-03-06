#!/usr/bin/python3
"""First app with flask
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(debug=True)
