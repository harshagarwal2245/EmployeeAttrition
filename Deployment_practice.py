# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:55:22 2020

@author: Harsh_12
"""

import uvicorn
from fastapi import FastAPI 

# create the object
app=FastAPI()

#index route open automatically to http://127.0.0.1:8000
@app.get("/")
def index():
    return {'message':"Hello world"}

#route with a single parameter, returns the paramter within  a message
# located at http://127.0.0.1:8000/anynamehere
@app.get("/welcome")
def get_name(name: str):
    return {"Welcome to employee attrition site":f'{name}'}


#run api with uvicorn
if __name__=='__main__':
    uvicorn.run(app,host="127.0.0.1",port=8000)