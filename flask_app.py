from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>My first Flask App</p>"

@app.route("/welcome")
def welcome():
    return "<p>Welcome Page for my 1st flask app</p>"

if __name__ == '__main__':
    app.run(debug=True)  # Important for development!