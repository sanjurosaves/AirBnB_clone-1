#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def list_states():
    dic = storage.all("State")
    lis = []
    return render_template('9-states.html', lis=lis)


@app.route('/states/<id>')
def lookup_state(id):
    dic = storage.all("State")
    lis = []
    id_lis = []
    for key, val in dic.items():
        lis.append(val)
        id_lis.append(val.id)
    return render_template('9-states.html', lis=lis, id_lis=id_lis, id=id)


@app.teardown_appcontext
def tear(self):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
