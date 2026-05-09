# The main file, where the application will run

import pipeline
from app.analysis import salary_analysis

if __name__ == '__main__':
    df, generic_results, job_results = pipeline.run_pipeline()

    print(generic_results)
    print(job_results)
    print(salary_analysis.salary_analysis(df))
    print(salary_analysis.salary_outliers_analysis(df))


