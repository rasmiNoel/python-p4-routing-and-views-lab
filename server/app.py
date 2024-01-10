#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:name>')
def print_string(name):
    return f'{name}'

@app.route('count/<int:num>')
def count(num):
    return f'{num}'

@app.route('/math/<int:num1>*<int:num2>')
def math(num1, num2):
    return f'{num1 * num2}'