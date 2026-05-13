# Visualisation layer, will use Streamlit to display the data in a clean way

import streamlit as st

from app.analysis import salary_analysis
from app.pipeline import run_pipeline
import pandas as pd
import matplotlib.pyplot as plt



df, validation_results = run_pipeline()

experience_levels_mapping = {
    'EN' : 'Entry Level',
    'MI' : 'Mid Level',
    'SE' : 'Senior',
    'EX' : 'Executive'
}

st.title('Job Market Analyzer')
st.markdown("Analyzing salary trends, roles, and outliers in the data science job market.")

# Adding filtering ability

st.sidebar.header("Filters")

experience_levels = sorted(df["experience_level"].unique())
work_years = sorted(df["work_year"].unique())
remote_ratios = sorted(df["remote_ratio"].unique())

# Making internal coding more readable to users

display_experience_levels = [
    experience_levels_mapping[level]
    for level in experience_levels_mapping
]

reverse_experience_labels = {
    value: key
    for key, value in experience_levels_mapping.items()
}

selected_experience = st.sidebar.selectbox(
    "Experience Level",
    options=["All"] + display_experience_levels
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
    selected_experience = reverse_experience_labels[selected_experience]
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

# Ability to Export the filtered CSV

csv_data = filtered_df.to_csv(index=False)
st.sidebar.subheader("Export Data")
st.sidebar.download_button(
    label="Download",
    data=csv_data,
    file_name="Filtered_job_market_data.csv",
    mime="text/csv")


analysis_results = {
        'salary_analysis' : salary_analysis.salary_analysis(filtered_df),
        'outlier_analysis' : salary_analysis.salary_outliers_analysis(filtered_df),
    }

st.subheader('Key Metrics')
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Average Salary",
        f"${analysis_results['salary_analysis']['overall_stats']['mean_salary']:,.0f}"
    )
with col2:
    st.metric(
        "Median Salary",
        f"${analysis_results['salary_analysis']['overall_stats']['median_salary']:,.0f}"
    )
with col3:
    st.metric(
        "Jobs Count",
        len(filtered_df)
    )
with col4:
    st.metric(
        "Upper Outliers",
        analysis_results['outlier_analysis']["upper_outliers_count"]
    )

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Average Salary by Experience Level")
    experience_df = pd.DataFrame(
        analysis_results["salary_analysis"]['salary_by_experience'].items(),
        columns=["Experience Level", "Average Salary"]
    )
    experience_df["Experience Level"] = (
        experience_df["Experience Level"]
        .map(experience_levels_mapping)
    )

    st.bar_chart(
        experience_df,
        x="Experience Level",
        y="Average Salary"
    )

with chart_col2:
    st.subheader("Salary by Remote Ratio")

    salary_by_remote = (
        analysis_results["salary_analysis"]["salary_by_remote_ratio"]
    )
    remote_df = pd.DataFrame(
        salary_by_remote.items(),
        columns=["Remote Ratio", "Average Salary"]
    )

    st.bar_chart(
        remote_df,
        x="Remote Ratio",
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

st.subheader('Salary Outlier Insights')

outlier_col1, outlier_col2 = st.columns(2)

with outlier_col1:
    st.metric(
        "Upper Outliers' bound:",
        f"${analysis_results['outlier_analysis']['upper_bound']:,.0f}"
    )
with outlier_col2:
    st.metric(
        "lower Outliers' bound:",
        f"${analysis_results['outlier_analysis']['lower_bound']:,.0f}"
    )

outliers_df = pd.DataFrame(
    analysis_results['outlier_analysis']['upper_outliers']
)
outliers_df = outliers_df.sort_values(
    by="salary_in_usd",
    ascending=False
)
outliers_df = outliers_df.head(5)

st.dataframe(outliers_df.style.format({
    'salary_in_usd': '{:,.0f}'
})
)

st.subheader("Salary Distribution")
fig, ax = plt.subplots()
ax.hist(
    filtered_df["salary_in_usd"],
    bins = 10,
    rwidth=0.8
)
ax.set_xlabel("Salary in USD")
ax.set_ylabel("Frequency")
ax.set_title("Salary Distribution")
st.pyplot(fig)