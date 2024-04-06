import sys
sys.path.insert(1, 'C://Programming//barnardine//backend//postgres')
sys.path.insert(2, 'C://Programming//barnardine//backend//mongo')
sys.path.insert(3, 'C://Programming//barnardine//services//analysis')
from flask import Flask, jsonify 
from flask_cors import CORS
from postgres_read import *
from mongo_read import *
from gdp import *
from config import load_config
config = load_config()

app = Flask(__name__)
CORS(app)

@app.route(f'/gdp-highest/gdp_data')
def gdp_highest(): 
    data = highest_by_quarter()
    return jsonify(data)

@app.route(f'/gdp-lowest/gdp_data')
def gdp_lowest():
    data = lowest_by_quarter()
    return jsonify(data)

@app.route('/reviews/all', methods=['GET'])
def all_reviews():
    data = mongo_read_all()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)