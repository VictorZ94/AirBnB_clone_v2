#!/usr/bin/python3
""" Handling hbnb route
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb')
def index2():
    return "HBNB"


@app.route('/c/<text>')
def show_text(text):
    if text:
        text_split = text.split('_')
        text = ' '.join(text_split)
        return 'C {}'.format(text)
    else:
        return render_template('404.html')


@app.route('/python/<text>')
def show_python_text(text='is cool'):
    if text:
        text_split = text.split('_')
        text = ' '.join(text_split)
        return 'Python {}'.format(text)
    else:
        return text


@app.errorhandler(404)
def page_not_found(e):
    # we set the 404 status explicitly
    return 'Python is cool', 404


if __name__ == '__main__':
    app.run(debug=True)
