# Visualisation layer, will use streamlit to display the data in a clean way

import streamlit as st

from app.analysis import salary_analysis
from app.pipeline import run_pipeline
import pandas as pd

df, validation_results = run_pipeline()

st.title('Job Market Analyzer')
st.markdown("Analyzing salary trends, roles, and outliers in the data science job market.")

st.sidebar.header("Filters")

experience_levels = sorted(df["experience_level"].unique())
work_years = sorted(df["work_year"].unique())
remote_ratios = sorted(df["remote_ratio"].unique())


selected_experience = st.sidebar.selectbox(
    "Experience Level",
    options=["All"] + experience_levels
)

selected_year = st.sidebar.selectbox(
    "Work Year",
    options=["All"] + list(work_years)
)

selected_remote = st.sidebar.selectbox(
    "Remote Ratio",
    options=["All"] + list(remote_ratios)
)

filtered_df = df.copy()

if selected_experience != "All":
    filtered_df = filtered_df[
        filtered_df["experience_level"] == selected_experience
    ]

if selected_year != "All":
    filtered_df = filtered_df[
        filtered_df["work_year"] == selected_year
    ]

if selected_remote != "All":
    filtered_df = filtered_df[
        filtered_df["remote_ratio"] == selected_remote
    ]

analysis_results = {
        'salary_analysis' : salary_analysis.salary_analysis(filtered_df),
        'outlier_analysis' : salary_analysis.salary_outliers_analysis(filtered_df)
    }

st.subheader("Average Salary by Experience Level")
experience_df = pd.DataFrame(
    analysis_results["salary_analysis"]['salary_by_experience'].items(),
    columns=["Experience Level", "Average Salary"]
)

st.bar_chart(
    experience_df,
    x="Experience Level",
    y="Average Salary"
)


top_jobs = (
    analysis_results["salary_analysis"]["top_paying_jobs"]
)
top_jobs_df = pd.DataFrame(
    top_jobs.items(),
    columns=["Job Title", "Average Salary"]
)

st.subheader("Top Paying Jobs")

st.bar_chart(
    top_jobs_df,
    x="Job Title",
    y="Average Salary"
)

st.subheader("Salary by Remote Ratio")

salary_by_remote = (
    analysis_results["salary_analysis"]["salary_by_remote_ratio"]
)
remote_df = pd.DataFrame(
    salary_by_remote.items(),
    columns=["Remote Ratio", "Average Salary"]
)
st.subheader("Average Salary by Remote Ratio")

st.bar_chart(
    remote_df,
    x="Remote Ratio",
    y="Average Salary"
)