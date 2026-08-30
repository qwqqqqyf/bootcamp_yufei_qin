import pandas as pd


def iqr_outlier_mask(series: pd.Series, k: float = 1.5) -> pd.Series:
    """Return a boolean mask for IQR outliers; missing values are not outliers."""
    if k <= 0:
        raise ValueError("k must be positive")
    numeric = pd.to_numeric(series, errors="coerce")
    q1, q3 = numeric.quantile([0.25, 0.75])
    spread = q3 - q1
    return numeric.lt(q1 - k * spread) | numeric.gt(q3 + k * spread)


def flag_return_outliers(df: pd.DataFrame, column: str = "daily_return") -> pd.DataFrame:
    """Add an ``is_outlier`` flag without deleting genuine market events."""
    out = df.copy()
    out["is_outlier"] = iqr_outlier_mask(out[column])
    return out

