import pickle
from flask import jsonify
import xgboost as xgb
from flask import request

input_file = 'xgb_model_eta_depth_child_0.2_5_5'

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


with open(input_file,'rb') as model_files:
    dv, xgb_model = pickle.load(model_files)

def resign_predict(employee):
    employee = dv.transform([employee])
    features = list(dv.get_feature_names_out())
    d_employee = xgb.DMatrix(employee, feature_names=features)
    resign_prob = xgb_model.predict(d_employee)
    resign_decision = (resign_prob>=0.5).astype('int')
    result = {
        'resign_decision': bool(resign_decision),
        'resign_probability': float(resign_prob)
    }

    return result

def lambda_handler(event,context):
    employee = event['employee']
    result = resign_predict(employee)
    return result


