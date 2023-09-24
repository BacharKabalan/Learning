
import requests

url = 'http://127.0.0.1:9696/resign_predict'
employee = {
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
}

response = requests.post(url, json=employee).json()

if response['resign_decision'] == 1:
    print(f'You are likely to resign. Your resign probability is {100*response["resign_probability"]:.3f}%')
else:
    print( f'You are unlikely to resign. Your resign probability is {100*response["resign_probability"]:.3f}%')