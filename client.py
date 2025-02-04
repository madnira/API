from flask import Flask, jsonify, request
import requests, os

app = Flask(__name__)

serverURL = "http://127.0.0.1:5002/server"

@app.route('/client', methods=["POST"])
def client():
    payload = request.get_json()
    a = payload.get("a")
    b = payload.get("b")
    data = {"a":a, "b":b}
    result = requests.post(serverURL, json=data)
    return result.json()

    

if __name__ == '__main__':
    app.run(debug=True, port= 5001)