#!/usr/bin/python3
"""
This is a module to start displaying things to the front end
"""
from flask import Flask, render_template, abort
from models.__init__ import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(error):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
