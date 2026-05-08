# Used to determine if a given dataframe is structurally acceptable,
# as in no large parts of the dataframe are empty or missing, if the dataframe even contains data and so on.

def validate_dataframe(df):
    validation_results = {
        "is_empty": df.empty,
        "duplicate_count": df.duplicated().sum(),
        "missing_values": {
            column: df[column].isnull().sum()
            for column in df.columns
            if df[column].isnull().sum() > 0},
        "dtypes": df.dtypes.astype(str).to_dict(),
    }


    return validation_results