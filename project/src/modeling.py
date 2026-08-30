from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


FEATURE_COLUMNS = [
    "daily_return", "momentum_5d", "rolling_mean_return_20d",
    "rolling_volatility_20d",
]


def fit_time_split_model(df: pd.DataFrame, test_fraction=0.2):
    """Fit a chronological linear-regression model and return model/results."""
    data = df.dropna(subset=FEATURE_COLUMNS + ["future_return_5d"]).sort_values("date")
    cut = int(len(data) * (1 - test_fraction))
    train, test = data.iloc[:cut], data.iloc[cut:]
    model = Pipeline([("scale", StandardScaler()), ("regression", LinearRegression())])
    model.fit(train[FEATURE_COLUMNS], train["future_return_5d"])
    test = test.copy()
    test["prediction"] = model.predict(test[FEATURE_COLUMNS])
    test["residual"] = test["future_return_5d"] - test["prediction"]
    return model, train, test


def save_model(model, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)

