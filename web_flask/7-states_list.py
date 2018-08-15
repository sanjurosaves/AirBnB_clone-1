#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    dic = storage.all("State")
    return render_template('7-states_list.html', dic=dic)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
