import streamlit as st
import pandas as pd
import numpy as np

st.title(body="Housing Price Dashboard")

prediction = st.Page("pages/prediction.py", title="Prediction Tool", icon="📈")
performance = st.Page("pages/performance.py", title="Model Performance", icon="⚡")
document = st.Page("pages/document.py", title="Feature Documentation", icon="📑")

pg = st.navigation([prediction,performance,document])
st.set_page_config(page_title="Housing Price Prediction", page_icon="🏠")
pg.run()