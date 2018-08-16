#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states_list():
    dic = storage.all("State")
    lis = []
    for key, val in dic.items():
        lis.append(val)
    return render_template('8-cities_by_states.html', lis=lis)


@app.teardown_appcontext
def tear(self):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
