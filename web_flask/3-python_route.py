#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    app.strict_slashes=False
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    app.strict_slashes=False
    return 'HBNB'

@app.route('/c/<text>')
def c(text):
    app.strict_slashes=False
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/<text>')
def c(text="is_cool"):
    app.strict_slashes=False
    return 'C {}'.format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
