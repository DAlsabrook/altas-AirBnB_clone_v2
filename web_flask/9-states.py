#!/usr/bin/python3
"""
This is a module to start displaying things to the front end
"""
from flask import Flask, render_template, abort
from models.__init__ import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states")
@app.route("/states/<id>")
def states_id_route(id=None):
    """
    Displays an HTML formatted of cities with a given State id
    """
    states = storage.all(State)
    return render_template("9-states.html", state_list=states, id=id)


@app.teardown_appcontext
def close(error):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
