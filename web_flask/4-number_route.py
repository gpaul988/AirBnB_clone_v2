#!/usr/bin/python3
""" Graham S. Paul (4-number_route.py)
Begins a Flask application with routes
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Shows text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Shows text"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Shows custom text given"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    '''Python route'''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def text_if_int(n):
    """Shows text only if int given"""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
