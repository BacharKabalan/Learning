import pickle
from flask import Flask
from flask import jsonify
import xgboost as xgb
from flask import request

input_file = 'xgb_model_eta_depth_child_0.2_5_5'
app = Flask('resign')


with open(input_file,'rb') as model_files:
    dv, xgb_model = pickle.load(model_files)

@app.route('/resign_predict', methods = ['POST'])
def resign_predict():
    employee = request.get_json()
    employee = dv.transform([employee])
    features = list(dv.get_feature_names_out())
    d_employee = xgb.DMatrix(employee, feature_names=features)
    resign_prob = xgb_model.predict(d_employee)
    resign_decision = (resign_prob>=0.5).astype('int')
    result = {
        'resign_decision': bool(resign_decision),
        'resign_probability': float(resign_prob)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 9696)

