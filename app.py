import flask
from flask import request
import pandas as pd
from datetime import datetime as dt

data = pd.read_csv('Monarchs-of-England.csv', names=['start','end','monarch']).set_index('monarch')

series = pd.Series(index=range(data.start.min(),dt.now().year))


for monarch in data.index :
    series.loc[data.loc[m].start:data.loc[m].end] = m
app = flask.Flask(__name__)

@app.route('\', methods = ['GET'])

def home():
    year = int(request.args['year'])
    try:
        return series.loc[year]
    except KeyError:
        return f'Invalid Input ({series.index.min()-series.index.max()})'
