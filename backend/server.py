#!/usr/bin/env python
import json
import requests
from flask import Flask, jsonify, request, Response
app = Flask(__name__)


@app.route("/")
def index():
  return "Hello World!"

@app.route("/data")
def data():
	f = open('datascraper/linkedin-formatted-to-json.txt', 'r')
	ret = f.read()
	return Response(response=ret, status=200, headers=None, mimetype='application/json', content_type=None, direct_passthrough=False)

if __name__ == "__main__":
  app.run(debug=True,host='0.0.0.0',port=80)
