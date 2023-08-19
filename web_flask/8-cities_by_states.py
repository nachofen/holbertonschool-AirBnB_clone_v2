#!/usr/bin/python3
"""List of states"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_session(arg=None):
    "Close the session after each request"
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """gets all of the State objects from the storage engine"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """the list of all State objects present in DBStorage
    """
    return render_template('8-cities_by_states.html',
                           states=storage.all(State))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
