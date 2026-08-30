import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

import pandas as pd


SECTOR_ETFS = {
    "Communication Services": "XLC", "Consumer Discretionary": "XLY",
    "Consumer Staples": "XLP", "Energy": "XLE", "Financials": "XLF",
    "Health Care": "XLV", "Industrials": "XLI", "Information Technology": "XLK",
    "Materials": "XLB", "Real Estate": "XLRE", "Utilities": "XLU",
}


def download_yahoo_chart(ticker: str, range_: str = "5y") -> pd.DataFrame:
    """Download daily close data from Yahoo Finance's public chart endpoint."""
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range={range_}&interval=1d"
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    result = payload["chart"]["result"][0]
    closes = result["indicators"]["quote"][0]["close"]
    dates = pd.to_datetime(result["timestamp"], unit="s", utc=True).tz_convert(None)
    return pd.DataFrame({"date": dates, "close": closes}).assign(ticker=ticker)


def download_sector_data(output_path: Path, range_: str = "5y") -> pd.DataFrame:
    frames = []
    for sector, ticker in SECTOR_ETFS.items():
        frame = download_yahoo_chart(ticker, range_)
        frame["sector"] = sector
        frames.append(frame)
    data = pd.concat(frames, ignore_index=True).dropna(subset=["close"])
    data = data[["date", "ticker", "sector", "close"]].sort_values(["sector", "date"])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(output_path, index=False)
    return data

