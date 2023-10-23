#!/usr/bin/python3
# Graham S. Paul (0-hello_route.py)
"""Begin Flask Application must make use of  the option strict_slashes=False in your route definition
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return("Hello HBNB!")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
