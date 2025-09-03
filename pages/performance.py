import streamlit as st 
import pandas as pd
import plotly.express as px
import cloudpickle
from mlflow.tracking import MlflowClient
import time


try:
    with open("models/baggingmodel.cloudpickle", "rb") as f:
       bagging = cloudpickle.load(f)
    with open("models/boostingmodel.cloudpickle", "rb") as f:
       boosting = cloudpickle.load(f)
    with open("models/votingmodel.cloudpickle", "rb") as f:
       voting = cloudpickle.load(f)
    with open("models/lrmodel.cloudpickle", "rb") as f:
       linear = cloudpickle.load(f)
    with open("models/basemodel.cloudpickle", "rb") as f:
       base = cloudpickle.load(f)
    print("Model Loaded Successfully!")
except Exception as e:
   print(f"Not able to load the models: {e}")

client = MlflowClient()

experiments = client.search_experiments()

exp_ids = [exp.experiment_id for exp in experiments]
exp_ids = exp_ids[:-1]

try: 
    runs = client.search_runs(experiment_ids=exp_ids,max_results=100, order_by=["attributes.start_time DESC"])
    print("Successfully loaded runs data")
except Exception as e:
   print(f"Not able to get the runs data: {e}")

run_dict = {}
for run in runs[0:5]:
   run_dict[run.info.experiment_id] = {"metrics": run.data.metrics, "params": run.data.params}

dict_r2 = {}
dict_rmse = {}
dict_crossval = {}
dict_params = {}

experiment_model_dict = {
    "428448064423756712": "Boosting",
    "374848408681755308": "Voting",
    "361855249608578602": "Bagging",
    "495584249720982550": "Linear Regression",
    "944212936157275241": "Base Model"
}

def get_model_name(model_id):
   return experiment_model_dict[model_id]


for ids in run_dict.keys():
   current_model = run_dict[ids]
   model_name = get_model_name(ids)
   if model_name != "Base Model":
      dict_r2[model_name] = current_model["metrics"]["R2 Score"]
      dict_rmse[model_name] = current_model["metrics"]["Root Mean Squared Error"]
      dict_crossval[model_name] = current_model["metrics"]["Cross Val Score"]
      dict_params[model_name] = current_model["params"]
   else:
      dict_r2[model_name] = current_model["metrics"]["R2"]
      dict_rmse[model_name] = current_model["metrics"]["rmse"]


st.title(body="Model Performance")
st.text("Model Performance Comparison By Metrics")

options_metrics = ["R2 Score", "Root Mean Squared Error", "Cross Validation Score (R2)"]

select_metrics = st.selectbox(label="Select Metrics", options=options_metrics)

if select_metrics == "Cross Validation Score (R2)":
   db_cv = pd.DataFrame(dict_crossval.values(), columns=["value"])
   db_cv["models"] = ["Boosting","Voting","Bagging","Linear Regression"]
   fig  = px.bar(db_cv, db_cv["models"], db_cv["value"])
   st.plotly_chart(fig)
elif select_metrics == "R2 Score":
   db_r2 = pd.DataFrame(dict_r2.values(), columns=["value"])
   db_r2["models"] = ["Boosting","Voting","Bagging","Linear Regression","Base Model"]
   fig  = px.bar(db_r2, db_r2["models"], db_r2["value"])
   st.plotly_chart(fig)
else:
   db_rmse = pd.DataFrame(dict_rmse.values(), columns=["value"])
   db_rmse["models"] = ["Boosting","Voting","Bagging","Linear Regression","Base Model"]
   fig  = px.bar(db_rmse, db_rmse["models"], db_rmse["value"])
   st.plotly_chart(fig)

st.text("Model Parameters Comparison")
db_params = pd.DataFrame(dict_params)
db_params = db_params.fillna("-")
st.table(db_params)