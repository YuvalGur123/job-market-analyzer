# A validator file for the job market domain. Should check if salaries are valid, that experience levels are reasonable and so on.

experience_levels = {'EN', 'MI', 'SE', 'EX'}

def validate_job_market(df):
    validation_results = {
        "invalid_salary_rows": (df['salary'] <= 0).sum(),
        "invalid_experience_level_rows": (~df['experience_level'].isin(experience_levels)).sum()
    }

    return validation_results