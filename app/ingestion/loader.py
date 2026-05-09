# Loader file to load the dataset, Explore its shape and features and prepare to process the data later
# Will be used better when moving from csv file to online sources

import pandas as pd
from app.utils import paths

def load_data(path):
    df = pd.read_csv(path)

    print("First 3 rows:")
    print(df.head(3).to_string())

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)


    return df


if __name__ == "__main__":
    load_data()