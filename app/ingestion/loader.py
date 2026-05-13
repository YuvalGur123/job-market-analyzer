# Loader file to load the dataset, Explore its shape and features and prepare to process the data later
# Will be utilized more when moving from csv file to online sources

import pandas as pd
from app.utils import paths

def load_data(path):
    df = pd.read_csv(path)
    return df
