#!/usr/bin/python3
"""
This is a module to start displaying things to the front end
"""
from flask import Flask, render_template, abort
from models.__init__ import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close(error):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    try:
        states_dict = storage.all(State)
        #sort the states_dict by name A-Z
        sorted_dict = {k: v for k, v in sorted(states_dict.items(),
                                               key=lambda item: item[1].name)}
        return render_template('7-states_list.html', states_list=sorted_dict)
    except ValueError:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
