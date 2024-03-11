#!/usr/bin/python3
"""
This is a module to start displaying things to the front end
"""
from flask import Flask, render_template
from models.__init__ import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters")
def states_id_route(id=None):
    """
    Displays an HTML formatted of cities with a given State id
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states_dict=states, amenities_dict=amenities)


@app.teardown_appcontext
def close(error):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
