import streamlit as st 

st.title(body="Feature Documentation")

with open("data\data_description.txt", "r", encoding="utf-8") as f:
    data  = f.read()

st.text(data)