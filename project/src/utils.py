import pandas as pd


def clean_column_names(df):
    """
    Clean dataframe column names.

    Converts names to lowercase and replaces spaces
    with underscores.
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(r"\s+", "_", regex=True)
    )
    return df


def parse_date_column(df, column):
    """
    Convert a column to datetime format.
    """
    df = df.copy()
    df[column] = pd.to_datetime(df[column])
    return df
