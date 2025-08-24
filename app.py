import streamlit as st
import pandas as pd
import numpy as np

st.title(body="Housing Price Dashboard")

prediction = st.Page("pages/prediction.py", title="Prediction Tool", icon="📈")
performance = st.Page("pages/performance.py", title="Model Performance", icon="⚡")
features = st.Page("pages/features.py", title="Feature Analysis", icon="📊")
document = st.Page("pages/document.py", title="Feature Documentation", icon="📑")
about = st.Page("pages/about.py", title="About", icon="ℹ️")

pg = st.navigation([prediction,performance,features,document,about])
st.set_page_config(page_title="Housing Price Prediction", page_icon="🏠")
pg.run()