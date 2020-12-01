import sys
from flask import Flask, jsonify
from scraper.WPData import *

app = Flask(__name__)

d1 = WPData("test",2,3,4,5,6,7)
d2 = WPData(8,9,10,11,12,13,14)

@app.route('/')
def index():
    return 'api.py index'

@app.route('/datatoday', methods=['GET'])
def data_today():
    return d1.temp

if __name__ == "__main__":
    app.debug = True
    app.run()