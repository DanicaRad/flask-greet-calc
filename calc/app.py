# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/<math>')
def do_math_query_only(math):
    math = eval(math)
    a = request.args['a']
    b = request.args['b']

    return str(math(a, b))

@app.route('/math/<math>')
def do_math(math):
    math = eval(math)
    a = request.args['a']
    b = request.args['b']

    return str(math(a, b))