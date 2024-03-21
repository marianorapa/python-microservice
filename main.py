from flask import Flask

app = Flask(__name__)

@app.route("/process")
def hello_world():
    data = {
        "data": 10
    }
    return data
