from flask import Flask

app = Flask(__name__)

@app.route('/world')
def world():
    return "world"