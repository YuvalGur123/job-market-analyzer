# The main file, where the application will run

from app.ingestion import loader
from app.processing import cleaner
from app.validation import generic_validator, job_market_validator

def run_pipeline():
    df = loader.load_data('../data/raw/ds_salaries.csv')
    df = cleaner.clean_data(df)
    generic_validation_results = generic_validator.validate_dataframe(df)
    job_market_validation_results = job_market_validator.validate_job_market(df)

    return df, generic_validation_results, job_market_validation_results


if __name__ == '__main__':
    df, generic_results, job_results = run_pipeline()

    print(generic_results)
    print(job_results)


