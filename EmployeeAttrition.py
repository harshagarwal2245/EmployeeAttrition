# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:20:18 2020

@author: Harsh_12
"""

from pydantic import BaseModel


class Employee(BaseModel):
    Age:                         int
    DailyRate:                    int
    DistanceFromHome:             int
    EmployeeNumber:               int
    JobLevel:                     int
    JobRole:                     int
    MaritalStatus:                int
    MonthlyIncome:                int
    MonthlyRate:                  int
    Overtime:                     int
    StockOptionLevel:             int
    TotalWorkingYears:            int
    TrainingTimesLastYear:        int
    YearsAtCompany:               int
    YearsInCurrentRole:           int
    YearsSinceLastPromotion:      int
    YearsWithCurrManager:         int
    
