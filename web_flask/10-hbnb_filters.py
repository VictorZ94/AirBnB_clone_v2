#!/usr/bin/python3
""" fecthing data and display with flask
"""
from flask import Flask, render_template, request
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def app_index():
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html',
                           states=states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """ Filter states and only cities depends on the state
    """
    states = storage.all(State)
    if id:
        id = "{}.{}".format('State', id)
    return render_template('9-states.html',
                           states=states, id=id)


@app.route('/hbnb_filters', strict_slashes=False)
def dynamic_web():
    """ loading data to html files
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(debug=True)
