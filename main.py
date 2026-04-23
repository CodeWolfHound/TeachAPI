from flask import Flask, jsonify , request
import json

with open('data.json') as f:
    data = json.load(f)

app = Flask(__name__)

@app.route("/")
def Welcome():
    return "<b>Welcome to the Teach API<b>"

@app.route("/students")
def Students():
    return jsonify(data["students"])
