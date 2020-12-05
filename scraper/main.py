import json
import time
from flask import Flask, jsonify
from wp import wp_data
from copper import copper_data
from data import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'main.py index'

@app.route('/today')
def today():
    return 'today'

@app.route('/json')
def data():
    wp = wp_data().dict()
    x = json.dumps(wp)
    return x
    
if __name__ == "__main__":
    app.debug = True
    app.run()