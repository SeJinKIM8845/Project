from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/write", methods=["GET","POST"])
def board_write():
    return ""