#api load for cp/wp taking too long - considerations: preloading data daily into database and calling today data

import json
import time
from flask import Flask, jsonify
from wp import wp_data
from copper import copper_data
from data import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'Copper VS Winter Park!'

#Today: WP or copper choice?
@app.route('/today')
def today():
    wp = wp_data()
    cp = copper_data()

    #compare int temp
    if(wp.temp > cp.temp):
        return 'Winter park is warmer today: ' + str(wp.temp)
    else:
        return 'Copper is warmer today: ' + str(cp.temp)

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