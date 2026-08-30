import pandas as pd


def add_return_features(df: pd.DataFrame, windows=(5, 20)) -> pd.DataFrame:
    """Add daily returns, lagged returns, and rolling volatility by sector."""
    out = df.copy().sort_values(["sector", "date"])
    grouped = out.groupby("sector", group_keys=False)
    out["daily_return"] = grouped["close"].pct_change()
    out["cumulative_return"] = grouped["close"].transform(lambda s: s / s.iloc[0] - 1)
    for window in windows:
        out[f"rolling_volatility_{window}d"] = grouped["daily_return"].transform(
            lambda s: s.rolling(window, min_periods=window).std()
        )
    out["month"] = out["date"].dt.month
    return out


def add_modeling_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add leak-safe predictors and a five-trading-day future-return target."""
    out = add_return_features(df).sort_values(["ticker", "date"]).copy()
    out["momentum_5d"] = out.groupby("ticker")["close"].pct_change(5)
    out["rolling_mean_return_20d"] = out.groupby("ticker")["daily_return"].transform(
        lambda s: s.rolling(20, min_periods=20).mean()
    )
    out["rolling_volatility_20d"] = out.groupby("ticker")["daily_return"].transform(
        lambda s: s.rolling(20, min_periods=20).std()
    )
    out["future_return_5d"] = (
        out.groupby("ticker")["close"].shift(-5).div(out["close"]).sub(1)
    )
    return out
