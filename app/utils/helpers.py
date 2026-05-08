# A file containing useful helpers functions, made to keep the main files more readable

def drop_unnamed_columns(df):
    columns_to_drop = [
        column for column in df.columns
        if "unnamed" in column.lower()
    ]
    print(columns_to_drop)
    return df.drop(columns=columns_to_drop)

def standardize_columns_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
    )
    return df
