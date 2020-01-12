# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 13:46:31 2020

@author: a_danda
"""
import numpy as np
import requests
from flask import Flask,jsonify, request, render_template
import pickle

app = Flask(__name__)
#model = pickle.load(open('model.pkl','rb'))


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        # get url that the user has entered
        try:            
            text = request.form['text']
            model = pickle.load(open('model.pkl','rb')) 
            return render_template('index.html',result = model(text))
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
    return render_template('index.html', errors=errors, results=results)

    
if __name__ == '__main__':
    app.run()       
    

    
    
