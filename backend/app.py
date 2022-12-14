from flask import Flask,jsonify,request
from flask_cors import CORS
from model import DataRoute
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app,resources={r'*':{'origins':'http://localhost:3000'}},supports_credentials=True)

@app.route('/<market>',methods=['GET'])
def allSearch(market):
  data = DataRoute.markets(market)
  return jsonify(data)

@app.route('/getnames',methods=['POST'])
def getname():
  data= DataRoute.getname()
  return jsonify(data)

@app.route('/daydata/<name>',methods=['GET'])
def getday(name):
  data= DataRoute.getDay(name)
  return jsonify(data)

@app.route('/getsearch/<name>',methods=['GET'])
def getSearch(name):
  data= DataRoute.getSearch(name)
  return jsonify(data)

@app.route('/getsearchinput/<name>',methods=['GET'])
def getSearchInput(name):
  data = DataRoute.getSearchInput(name)
  return jsonify(data)