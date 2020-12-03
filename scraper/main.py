from flask import Flask, jsonify
from wp import *
from copper import *

app = Flask(__name__)

# returns winter park / copper data objects 
wp = wp_data()
#cp = copper_data()

@app.route('/')
def index():
    return 'api.py index'

@app.route('/today', methods=['GET'])
def data_today():
    return 'today'
    
if __name__ == "__main__":
    app.debug = True
    app.run()