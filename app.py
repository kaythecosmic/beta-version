import predict
from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import pandas as pd
import json


# answer = predict.predictAnswer(Context, question)


app = Flask(__name__)
contextFlag = False

@app.route("/", methods=["GET", "POST"])
def main():
    # if request.method=='POST':
    #     Context = request.form['Context']
    
    global contextFlag

    if not contextFlag:
        userInput = request.form.values()
        contextFlag = True

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
