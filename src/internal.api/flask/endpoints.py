import sys
sys.path.insert(1, 'C:/Programming/barnardine/src/backend/mongo')
sys.path.insert(2, 'C:/Programming/barnardine/src/services/analysis')
from flask import Flask, jsonify 
from flask_cors import CORS
from mongo_read import *
from rds_gdp import *

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