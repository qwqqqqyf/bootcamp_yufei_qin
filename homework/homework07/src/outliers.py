import pandas as pd


def detect_outliers_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
    """
    Detect outliers using the IQR method.

    Parameters
    ----------
    series : pandas.Series
        Numeric data.
    k : float
        IQR multiplier. Must be positive.

    Returns
    -------
    pandas.Series
        Boolean mask indicating outliers.
    """
    if k <= 0:
        raise ValueError("k must be positive.")

    if series.empty:
        return pd.Series(False, index=series.index)

    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1

    lower = q1 - k * iqr
    upper = q3 + k * iqr

    return (series < lower) | (series > upper)


def detect_outliers_zscore(
    series: pd.Series,
    threshold: float = 3.0
) -> pd.Series:
    """
    Detect outliers using the Z-score method.

    Parameters
    ----------
    series : pandas.Series
        Numeric data.
    threshold : float
        Z-score threshold. Must be positive.

    Returns
    -------
    pandas.Series
        Boolean mask indicating outliers.
    """
    if threshold <= 0:
        raise ValueError("threshold must be positive.")

    if series.empty:
        return pd.Series(False, index=series.index)

    mean = series.mean()
    std = series.std(ddof=0)

    if std == 0:
        return pd.Series(False, index=series.index)

    z = (series - mean) / std

    return z.abs() > threshold


def winsorize_series(
    series: pd.Series,
    lower: float = 0.05,
    upper: float = 0.95
) -> pd.Series:
    """
    Winsorize a series by clipping values at given quantiles.

    Parameters
    ----------
    series : pandas.Series
        Numeric data.
    lower : float
        Lower quantile.
    upper : float
        Upper quantile.

    Returns
    -------
    pandas.Series
        Winsorized series.
    """
    if not 0 <= lower < upper <= 1:
        raise ValueError("lower and upper must satisfy 0 <= lower < upper <= 1.")

    if series.empty:
        return series.copy()

    low_value = series.quantile(lower)
    high_value = series.quantile(upper)

    return series.clip(lower=low_value, upper=high_value)