FROM public.ecr.aws/lambda/python:3.8

RUN pip install scikit-learn
RUN pip install xgboost
RUN pip install flask

COPY xgb_model_eta_depth_child_0.2_5_5 .

COPY lambda_function.py .


CMD ["lambda_function.lambda_handler"]

