import pandas as pd


def eda_summary(df):
    """
    Return a basic EDA summary for a DataFrame.

    Includes data types, missing values, and descriptive statistics.
    """
    summary = {
        "shape": df.shape,
        "dtypes": df.dtypes,
        "missing_values": df.isna().sum(),
        "describe": df.describe(include="all"),
    }

    return summary