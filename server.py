from flask import Flask, jsonify, request
import requests, os

app = Flask(__name__)

@app.route('/server', methods=["POST"])
def server():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    c = a+b
    return jsonify({"c":c})


if __name__ == '__main__':
    app.run(debug=True, port= 5002)