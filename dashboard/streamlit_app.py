# Visualisation layer, will use streamlit to display the data in a clean way

import streamlit as st
from app.pipeline import run_pipeline

df, validation_results, analysis_results = run_pipeline()

st.title('Job Market Analyzer')
st.markdown("Analyzing salary trends, roles, and outliers in the data science job market.")
st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Validation Results")
st.write(validation_results)

st.subheader("Salary Analysis")
st.write(analysis_results)