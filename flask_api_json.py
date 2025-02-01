from flask import Flask , jsonify

app = Flask(__name__)

@app.route("/")
def userDetails():
    name = "Arin"
    age = 25+10
    user = {
        "Name" : name,
        "Age" : age,
        "Location" : "New York"
    }

    return jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)  # Important for development!
    app.host = '127.0.0.1'
    app.port = 5001
    