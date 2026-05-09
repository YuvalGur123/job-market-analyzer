# The file that will build the pipeline and return the processed data

from app.utils.paths import get_raw_data_path
from app.ingestion import loader
from app.processing import cleaner
from app.validation import generic_validator, job_market_validator



def run_pipeline():
    file_path = get_raw_data_path('ds_salaries.csv')
    df = loader.load_data(file_path)
    df = cleaner.clean_data(df)
    validation_results = {
        'generic_validation_results': generic_validator.validate_dataframe(df),
        'job_market_validation_results' : job_market_validator.validate_job_market(df)
    }

    return df, validation_results