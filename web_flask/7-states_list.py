#!/usr/bin/python3
""" Graham S. Paul (7-states_list.copy)
List all states Module"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """SHows a HTML the States"""
    all_states = list(storage.all(State).values())
    return (render_template('7-states_list.html', all_states=all_states))


@app.teardown_appcontext
def teardown(self):
    """Purpose that call close methofd"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)