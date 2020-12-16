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

#Today: WP or copper choice?
@app.route('/today')
def today():
    return 'today stats'

#Winter park stats
@app.route('/wp')
def wp():
    wp = wp_data().dict()
    x = json.dumps(wp)
    return x

#Copper stats
@app.route('/cp')
def cp():
    cp = copper_data().dict()
    x = json.dumps(cp)
    return x

if __name__ == "__main__":
    app.debug = True
    app.run()