#!/usr/bin/python3
""" fecthing data of db and display in HTML template
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def app_index():
    """ function to call all states
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ function to call all cities
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html',
                           states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ After each request remove the current SQLAlchemy Session:
    """
    storage.close()


if __name__ == '__main__':
    app.run(debug=True)
