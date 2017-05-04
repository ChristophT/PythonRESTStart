import json
from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)


class Response:
    name = 'as'
    tel = 23

    def __init__(self, name, tel):
        self.name = name
        self.tel = tel


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/info", methods=['POST'])
def info():
    name = "ich: " + request.json['name']
    tel = 765432
    return jsonify({"name": name, "tel": tel})

if __name__ == "__main__":
    app.run()
