import requests

# url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

url = 'https://var7v7pg6g.execute-api.us-east-1.amazonaws.com/test/resign_predict'

data = {"employee":{
    "Age": 37,
    "BusinessTravel": "travel_rarely",
    "DailyRate": 370,
    "Department": "research_&_development",
    "DistanceFromHome": 10,
    "Education": "master",
    "EducationField": "medical",
    "EmployeeNumber": 1809,
    "EnvironmentSatisfaction": "very_high",
    "Gender": "male",
    "HourlyRate": 58,
    "JobInvolvement": "high",
    "JobLevel": 2,
    "JobRole": "manufacturing_director",
    "JobSatisfaction": "low",
    "MaritalStatus": "single",
    "MonthlyIncome": 4213,
    "MonthlyRate": 4992,
    "NumCompaniesWorked": 1,
    "OverTime": "no",
    "PercentSalaryHike": 15,
    "PerformanceRating": "excellent",
    "RelationshipSatisfaction": "medium",
    "StockOptionLevel": 0,
    "TotalWorkingYears": 10,
    "TrainingTimesLastYear": 4,
    "WorkLifeBalance": "bad",
    "YearsAtCompany": 10,
    "YearsInCurrentRole": 3,
    "YearsSinceLastPromotion": 0,
    "YearsWithCurrManager": 8
}}

result = requests.post(url, json = data).json()
print(result)