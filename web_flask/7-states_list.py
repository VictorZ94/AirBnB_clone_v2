#!/usr/bin/python3
""" fecthing data of db and display in HTML template
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def app_index():
    list_id = []
    list_name = []
    for value in storage.all(State).values():
        list_id.append(value.id)
        list_name.append(value.name)
    return render_template('7-states_list.html',
                           len=len(list_id),
                           list_id=list_id,
                           list_name=list_name)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(debug=True)
