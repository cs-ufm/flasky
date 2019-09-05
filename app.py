import os

from flask import Flask
from flask import url_for

app = Flask(__name__)
app.config.from_pyfile("config.py")


var=os.getenv("VAR",None)

@app.route("/")
def hello():
    logo=url_for('static', filename='ufm_logo.png')
    print("LOGO:",logo)
    return f'<img src="{logo}" alt="Girl in a jacket" style="width:400px;height:100px;" > <br><h1> Hello, UFM {var} </h1>'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
