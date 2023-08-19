#!/usr/bin/python3
"""
This module defines a simple Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def app_teardown_appcontext(self):
    """After each request this removes the current SQLAlchemy Session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():

    return render_template('8-cities_by_states.html',
                           states=storage.all(State))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
