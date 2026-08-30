import pandas as pd


def clean_sector_prices(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize sector-price data and remove unusable rows."""
    out = df.copy()
    out["date"] = pd.to_datetime(out["date"], errors="coerce")
    out["close"] = pd.to_numeric(out["close"], errors="coerce")
    out = out.dropna(subset=["date", "sector", "ticker", "close"])
    out = out[out["close"] > 0]
    return out.sort_values(["sector", "date"]).drop_duplicates(["sector", "date"])

