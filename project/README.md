# S&P 500 Sector Performance Analysis

## Project Summary

This project analyzes the performance of major S&P 500 sectors over time. The goal is to understand how different sectors perform, how their returns vary, and whether some sectors show stronger or more stable performance than others.

The analysis can help investors and portfolio managers better understand sector-level market behavior and identify differences in return and risk across sectors.

## Stakeholder

The primary stakeholders are individual investors, portfolio managers, and investment analysts.

They care about sector performance, return differences, volatility, and changes in sector behavior over time. The results should provide a clear and practical comparison of S&P 500 sectors.

## Project Goals

1. Compare performance across S&P 500 sectors.
2. Analyze sector returns and volatility.
3. Identify differences in sector behavior over time.
4. Create useful features for later modeling and analysis.

## Lifecycle Mapping

| Goal | Lifecycle Stage | Deliverable |
|---|---|---|
| Define the problem | Problem Framing | Project README |
| Set up project | Tooling Setup | Project structure |
| Prepare Python tools | Python Fundamentals | utils.py |
| Acquire market data | Data Acquisition | Raw sector data |
| Store data | Data Storage | Raw and processed datasets |
| Clean data | Data Preprocessing | cleaning.py |
| Analyze outliers | Outlier Analysis | outliers.py |
| Understand data | EDA | eda.py and EDA notebook |
| Create useful variables | Feature Engineering | features.py |

## Data

The project uses historical S&P 500 sector performance data.

Raw data is stored in `data/raw/`.

Processed data is stored in `data/processed/`.

## Project Structure

- `data/` — raw and processed datasets
- `src/` — reusable Python functions
- `notebooks/` — analysis notebooks
- `docs/` — project documentation
- `reports/` — final reports
- `model/` — future modeling work

## Assumptions and Risks

The analysis assumes that the historical sector data is accurate and representative of past market behavior.

Historical performance does not guarantee future performance. Sector returns can also be affected by macroeconomic conditions, market events, and changes in sector composition.

The project is intended for analytical and educational purposes rather than investment advice.

## Data Storage

`data/raw/sp500_sector_data.csv` is the raw download from Yahoo Finance's public chart endpoint. It contains daily close prices for the 11 Select Sector SPDR ETFs used as sector proxies. The processed datasets are written to `data/processed/` after cleaning and feature construction. CSV is used because it is portable and easy to inspect; the pipeline uses `pathlib` paths relative to this project.

## Pipeline Notes

The pipeline proceeds from raw prices to validated prices, flags IQR-based return outliers for review, produces summary statistics and charts, and creates daily-return and rolling-volatility features. Outliers are flagged rather than silently deleted because extreme market moves may be genuine events. The Yahoo Finance endpoint, ETF mapping, download range, and validation assumptions are recorded in `src/data_acquisition.py` and the pipeline notebook.

## Feature Definitions

| Feature | Definition | Purpose |
|---|---|---|
| `daily_return` | One-day percentage price change | Measure daily performance |
| `momentum_5d` | Percentage change over five trading days | Capture short-term momentum |
| `rolling_mean_return_20d` | Mean daily return over 20 trading days | Smooth short-term noise |
| `rolling_volatility_20d` | Standard deviation of returns over 20 trading days | Measure recent risk |
| `future_return_5d` | Return during the next five trading days | Modeling target only |

## Running the Project

From the repository root, install dependencies with `pip install -r project/requirements.txt`. To rebuild features, run `cd project` followed by `python -m src.run_step --input data/raw/sp500_sector_data.csv --output data/processed/sp500_sector_features_stage09.csv`. Open `project/notebooks/project_pipeline.ipynb` for the end-to-end analysis. See `docs/handoff_plan.md` and `docs/monitoring_plan.md` for reuse and operations notes.
