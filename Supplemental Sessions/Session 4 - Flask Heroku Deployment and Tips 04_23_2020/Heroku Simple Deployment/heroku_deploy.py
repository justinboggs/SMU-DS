from flask import Flask
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():

    return'<h1>Hello World</h1>'





if __name__ == "__main__":
    app.run(debug=True)
