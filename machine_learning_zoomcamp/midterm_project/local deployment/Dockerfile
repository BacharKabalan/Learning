FROM python:3.9.18-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile","Pipfile.lock","./"]

RUN pipenv install --system --deploy

COPY ["xgb_model_eta_depth_child_0.2_5_5", "resign_predict.py","./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "resign_predict:app"]
