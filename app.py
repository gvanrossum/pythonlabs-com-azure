import sys
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    with open("pylabs.html") as f:
        return f.read()

@app.route("/favicon.ico")
def favicon():
    with open("favicon.ico", "rb") as fb:
        return fb.read()

@app.route("/hello")
def hello():
    return "Hello, world."
