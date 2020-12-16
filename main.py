# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:17:08 2020

@author: Harsh_12
"""

import uvicorn
from fastapi import FastAPI 
from EmployeeAttrition import Employee
import numpy as np
import pandas as od
import joblib

app=FastAPI()
preprocessing=joblib.load("Employee_Attrition\\preprocess_pipeline.sav")
model=joblib.load("Employee_Attrition\\finalized_model.sav")


@app.get("/")
def index():
    return {"message":"Welcome to Employee attrition System"}

@app.post('/predict')
def predict_attrition(data:Employee):
    data=data.dict()
    print(data)
    Age=data["Age"]           
    DailyRate=data["DailyRate"]
    DistanceFromHome=data["DistanceFromHome"]
    EmployeeNumber=data["EmployeeNumber"]
    JobLevel=data["JobLevel"]
    JobRole=data["JobRole"]
    MaritalStatus=data["MaritalStatus"]
    MonthlyIncome=data["MonthlyIncome"]
    MonthlyRate=data["MonthlyRate"]
    OverTime=data["Overtime"]
    StockOptionLevel=data["StockOptionLevel"]
    TotalWorkingYears=data["TotalWorkingYears"]
    TrainingTimesLastYear=data["TrainingTimesLastYear"]
    YearsAtCompany=data["YearsAtCompany"]
    YearsInCurrentRole=data["YearsInCurrentRole"]
    YearsSinceLastPromotion=data["YearsSinceLastPromotion"]
    YearsWithCurrManager=data["YearsWithCurrManager"]
    pred=model.predict([[Age,DailyRate,DistanceFromHome,EmployeeNumber,JobLevel,JobRole,
                   MaritalStatus,MonthlyIncome,MonthlyRate,StockOptionLevel,
                   TotalWorkingYears,TrainingTimesLastYear,YearsAtCompany,YearsInCurrentRole
                   ,YearsSinceLastPromotion,YearsWithCurrManager]])
    if pred==1:
        prediction="Employee will leave"
    else:
        prediction="Employee will not leave"
    return {'prediction':f"{prediction}"}

if __name__=='__main__':
    uvicorn.run(app,host="127.0.0.1",port=8000)
