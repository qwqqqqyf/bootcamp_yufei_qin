import numpy as np
import pandas as pd


def regression_metrics(y_true, y_pred) -> dict:
    """Return MAE, RMSE, and R-squared without requiring sklearn."""
    error = np.asarray(y_true) - np.asarray(y_pred)
    mse = np.mean(error ** 2)
    total = np.sum((np.asarray(y_true) - np.mean(y_true)) ** 2)
    return {"mae": float(np.mean(np.abs(error))), "rmse": float(np.sqrt(mse)),
            "r2": float(1 - np.sum(error ** 2) / total) if total else float("nan")}


def bootstrap_metric(y_true, y_pred, metric_fn, n_boot=1000, seed=42):
    """Estimate a percentile bootstrap interval for a prediction metric."""
    rng = np.random.default_rng(seed)
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    values = [metric_fn(y_true[idx], y_pred[idx])
              for idx in (rng.integers(0, len(y_true), len(y_true)) for _ in range(n_boot))]
    return {"estimate": float(metric_fn(y_true, y_pred)),
            "lower": float(np.percentile(values, 2.5)),
            "upper": float(np.percentile(values, 97.5))}
