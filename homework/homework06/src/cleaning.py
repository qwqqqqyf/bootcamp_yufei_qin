import pandas as pd


def fill_missing_median(df, columns):
    """
    Fill missing values in numeric columns with the column median.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame.
    columns : list
        Numeric columns to fill.

    Returns
    -------
    pandas.DataFrame
        DataFrame with missing values filled by median.
    """
    df = df.copy()

    for column in columns:
        df[column] = df[column].fillna(df[column].median())

    return df


def drop_missing(df, threshold=0.5):
    """
    Drop rows with too many missing values.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame.
    threshold : float
        Minimum proportion of non-missing values required.
        For example, 0.5 means a row must have at least
        50% non-missing values.

    Returns
    -------
    pandas.DataFrame
        DataFrame with rows containing too many missing values removed.
    """
    df = df.copy()

    min_non_missing = int(df.shape[1] * threshold)

    df = df.dropna(
        thresh=min_non_missing
    )

    return df


def normalize_data(df, columns):
    """
    Normalize numeric columns using min-max scaling.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame.
    columns : list
        Numeric columns to normalize.

    Returns
    -------
    pandas.DataFrame
        DataFrame with selected columns scaled to 0-1.
    """
    df = df.copy()

    for column in columns:
        minimum = df[column].min()
        maximum = df[column].max()

        if maximum != minimum:
            df[column] = (
                (df[column] - minimum)
                / (maximum - minimum)
            )

    return df