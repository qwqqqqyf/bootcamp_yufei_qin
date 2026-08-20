import pandas as pd


def get_summary_stats(df):
    """
    Return summary statistics for numeric columns.
    """
    return df.describe()


def get_group_summary(df, category_col):
    """
    Group the data by a categorical column and calculate
    the mean of numeric columns.
    """
    return df.groupby(category_col).mean(numeric_only=True)