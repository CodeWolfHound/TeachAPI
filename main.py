from flask import Flask

app = Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to the hardcoded API"
