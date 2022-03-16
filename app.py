from flask import Flask, request, jsonify
import getData
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/getdata', methods=["POST"])
def testpost():
    input_json = request.get_json(force=True) 
    ward = input_json['ward']
    return jsonify(getData.getWardData(ward))