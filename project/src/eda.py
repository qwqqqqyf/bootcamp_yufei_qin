import pandas as pd


def eda_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return numeric summary statistics and missing-value counts."""
    numeric = df.select_dtypes(include="number")
    summary = numeric.describe().T
    summary["missing"] = numeric.isna().sum()
    summary["skewness"] = numeric.skew()
    return summary

