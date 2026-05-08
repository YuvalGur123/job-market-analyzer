# Cleaner file to clean the data. Will handle missing values, remove duplicates and normalize names and values.

from app.ingestion.loader import load_data
from app.utils.helpers import drop_unnamed_columns

def clean_data(df):
    df = drop_unnamed_columns(df)
    df = df.drop_duplicates()
    df = df.dropna() # To be replaced with generic logic later

    return df

