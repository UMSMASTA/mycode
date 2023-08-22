#!/usr/bin/python3

from flask import Flask

#Flask takes name of current module as argument
app = Flask(__name__)

#route() tells the app which URL should call the function
@app.route("/")
def hello_world():
    return "Hello World"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2224)

    