#!/usr/bin/python3
""" Graham S. Paul (1-hbnb_route.py)
Begin flask web application
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
