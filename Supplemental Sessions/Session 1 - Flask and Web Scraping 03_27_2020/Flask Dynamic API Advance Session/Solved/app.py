from flask import Flask, jsonify, render_template,request
app = Flask(__name__)

import plotly.express as px
import pandas as pd
import numpy as np
import json
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/line")
def test():
    data = [{
        "x": [1, 2, 3, 4, 5],
        "y": [1, 2, 4, 8, 16]}]

    return jsonify(data)

@app.route("/iris")
def plotpython():
    return render_template('index2.html')


@app.route("/getInfoENDPOINT",methods=['GET'])
def getInfo():

    #Creates dictionary of data holding all the requests.
    dataHolder = {
            'species':request.args.get("species"),
            'sepal_width':request.args.get("sepal_width"), 
            'sepal_length':request.args.get("sepal_length")
            }
    #This filterList is used later to hold all the items that you want to filter by.
    filterList=[]

    #Goes through each key value pair and check if the value exists.
    #Processing!
    for key, value in dataHolder.items(): 
        if(value!=None):
            if key in ['sepal_width','sepal_length']:
                filterList.append(df[key]==float(value))
            
            else:
                filterList.append(df[key]==value)

    #If there is nothing, it doen't get filtered.
    if(len(filterList)==0):
        filteredData=df
    else:
    #Filter the df by what was queried. np.all is the equivalent several AND statements.
    # e.g. A AND B AND C AND D.
        filteredData=df[np.all(filterList,axis=0)]
    #Creates the plotly object.
    fig = px.scatter(filteredData, x="sepal_width", y="sepal_length",color='species')    

    #Returns the fig object with the data and layout 
    return jsonify(json.loads(fig.to_json()))



@app.route("/getInfoENDPOINTPOST",methods=['POST'])
def getInfoPost():

    #Creates dictionary of data holding all the requests.
    dataHolder=request.json()
    #This filterList is used later to hold all the items that you want to filter by.
    filterList=[]

    #Goes through each key value pair and check if the value exists.
    #Processing!
    for key, value in dataHolder.items(): 
        if(value!=None):
            if key in ['sepal_width','sepal_length']:
                filterList.append(df[key]==float(value))
            
            else:
                filterList.append(df[key]==value)

    #If there is nothing, it doen't get filtered.
    if(len(filterList)==0):
        filteredData=df
    else:
    #Filter the df by what was queried. np.all is the equivalent several AND statements.
    # e.g. A AND B AND C AND D.
        filteredData=df[np.all(filterList,axis=0)]
    #Creates the plotly object.
    fig = px.scatter(filteredData, x="sepal_width", y="sepal_length",color='species')    

    #Returns the fig object with the data and layout 
    return jsonify(json.loads(fig.to_json()))


if __name__ == "__main__":
    app.run(debug=True)
