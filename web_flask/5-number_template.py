#!/usr/bin/python3
""" Learning flask as web framework
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


@app.route('/python/<text>')
def show_python_text(text='is cool'):
    if text:
        text_split = text.split('_')
        text = ' '.join(text_split)
        return 'Python {}'.format(text)
    else:
        @app.errorhandler(404)
        def page_not_found(e):
            # we set the 404 status explicitly
            return 'Python {}'.format(text), 404


@app.route('/number/<int:n>')
def only_int(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def only_template_int(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(debug=True)
