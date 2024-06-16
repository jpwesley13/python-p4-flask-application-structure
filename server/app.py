#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'
# Anything included in the route passed to the app.route decorator with angle brackets <> surrounding it will be passed to the decorated function as a parameter. We can make sure that the username is a valid string, int, float, or path (string with slashes) by specifying this in the route:

if __name__ == '__main__':
    app.run(port=5555, debug=True)