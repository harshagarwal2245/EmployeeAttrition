# EmployeeAttrition
Employee attrition is an important factor for any organization with help of AI 
we can predict whether an employee will leave the company or not.  I had used the IBM 
dataset which is freely available on Kaggle.First I had cleaned the data and visualize 
it to see which columns affect the employee turnover most then I had done data preprocessing 
since data is small its good to split train and test as 70% and 30% respectively after that, 
I had tried a few promising models and I found that random-forest will work best. on testing 
on the test set we got 86% accurate which is great after that I had used various metrics to analyze
the result and finally saved the model using the joblib package. \
The next step of the project is to create an API and giving Ui for which I had used the FastApi package which is good
for data science applications. It lies between Django and flask. It also provides built-in Ui which gives me an option
to focus on code. Next, I had created a function that will take inputs and give a prediction for which I had used the model
that I saved I had used the joblib package to read the model after that send the result to API. The last part of the project is to deploy
it using Heroku, pythonaywhere  platforms.

# To download project on your system
git clone https://github.com/harshagarwal2245/EmployeeAttrition.git
2. pip install -r requirments.txt
this will create all files on your system and that it we are ready to go

# To run app
1. open command prompt
2. uvicorn main:app --reload
3. open browser and type 127.0.0.1:8000/docs
It will start swagger ui which will use to test app
4. Select predict function
5. Click on Try It out!
6. and Enter Value and click on Execute function
7. and you will get Your result
