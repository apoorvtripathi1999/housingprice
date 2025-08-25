import streamlit as st 
import pandas as pd
import numpy as np
import cloudpickle

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
except Exception as e:
   print(f"Not able to load the models: {e}")

try:
   with open("data/basetemplate.csv", "rb") as f:
      basetemplate = f.read()
   with open("data/template.csv", "rb") as f:
      template = f.read()
except Exception as e:
   print(f"Data Templates not loaded correcctly: {e}")

st.title(body="Prediction Tool")
st.text("Upload a valid CSV file for batch prediction")

options = ["Base Model (Linear Regression)", "Linear Regression", "Voting (With LR, RF and KNN)", "XGboost", "Bagging Regressor"]
selection = st.selectbox(label="Select Model", options=options)
if(selection == "Base Model (Linear Regression)"):
   model = base
elif(selection == "Linear Regression"):
   model = linear
elif(selection == "Voting (With LR, RF and KNN)"):
   model = voting
elif(selection == "XGboost"):
   model = boosting
elif(selection == "Bagging Regressor"):
   model = bagging

st.download_button(
       label="Download Template for Base Model",
       data=basetemplate,
       file_name="basetemplate.csv",
       mime="text/csv")
st.download_button(
       label="Download Template for Other Models",
       data=template,
       file_name="template.csv",
       mime="text/csv")

csvfile = st.file_uploader("Upload CSV", type="csv", accept_multiple_files=False)

if csvfile is not None:
   try:
       data = pd.read_csv(csvfile)
   except Exception as e:
      st.error(f"Error while uploading file: {e}")

   y_pred = model.predict(data)
   db_y_pred = pd.DataFrame(y_pred, columns=["predictions"])
   result = db_y_pred.to_csv(index = False).encode('utf-8')
   
   st.download_button(
       label="Download Result",
       data=result,
       file_name="result.csv",
       mime="text/csv"
    )