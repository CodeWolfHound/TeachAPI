from flask import Flask, jsonify , request
import json

with open('data.json') as f:
    data = json.load(f)

app = Flask(__name__)

@app.route("/")
def myWelcome():
    return "<b>Welcome to the Teach API<b>"

@app.route("/all")
def getAll():
    return jsonify(data["districts"])

@app.route("/districts")
def getDistrict():
    name = request.args.get("name")

    for district in data["districts"]:
        if district["name"] == name:
            return jsonify(district)

    return "Please query a district name or confirm district is correct"
