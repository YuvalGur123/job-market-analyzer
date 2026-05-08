# This file will analyze the trends of salaries, and produce insights from the data regarding salaries.

def salary_analysis(df):
    results = {}
    results['overall_stats'] = {
        'mean_salary': df['salary_in_usd'].mean(),
        'median_salary': df['salary_in_usd'].median(),
        'min_salary': df['salary_in_usd'].min(),
        'max_salary': df['salary_in_usd'].max()
    }
    results['salary_by_experience'] = (
        df.groupby('experience_level')['salary_in_usd']
        .mean()
        .to_dict()
    )

    results['top_paying_jobs'] = (
        df.groupby('job_title')['salary_in_usd']
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .to_dict()
    )

    results['salary_by_remote_ratio'] = (
        df.groupby('remote_ratio')['salary_in_usd']
        .mean()
        .to_dict()
    )

    return results