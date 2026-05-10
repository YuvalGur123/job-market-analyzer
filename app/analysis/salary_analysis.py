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

def salary_outliers_analysis(df):
    q1 = df['salary_in_usd'].quantile(0.25)
    q3 = df['salary_in_usd'].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    lower_outliers = df[df['salary_in_usd'] < lower_bound]
    upper_outliers = df[df['salary_in_usd'] > upper_bound]
    results = {
        'iqr': iqr,
        'lower_bound': lower_bound,
        'upper_bound': upper_bound,


        'lower_outliers_count':  len(lower_outliers),
        'upper_outliers_count':  len(upper_outliers),


        'lower_outliers': lower_outliers[
            ['job_title', 'salary_in_usd']
        ].to_dict(orient='records'),
        'upper_outliers': upper_outliers[
            ['job_title', 'salary_in_usd']
        ].to_dict(orient='records')
    }
    return results
