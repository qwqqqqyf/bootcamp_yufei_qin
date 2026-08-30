# Lifecycle Framework Guide

| Stage | Project location | Decision or contribution |
|---|---|---|
| 01 | `README.md`, `docs/stakeholder_brief.md` | Compare historical sector risk and return for portfolio research. |
| 02 | `.gitignore`, `requirements.txt`, project folders | Establish reproducible structure and dependency tracking. |
| 03 | `notebooks/python_fundamentals_summary.ipynb`, `src/utils.py` | Practice reusable Python and pandas utilities. |
| 04 | `src/data_acquisition.py`, `data/raw/` | Download daily prices for 11 sector ETF proxies. |
| 05 | `src/config.py`, `data/processed/` | Separate raw and processed storage with project-relative paths. |
| 06 | `src/cleaning.py` | Validate dates, prices, duplicates, and required fields. |
| 07 | `src/outliers.py` | Flag IQR return outliers without silently deleting market events. |
| 08 | `src/eda.py`, `notebooks/project_pipeline.ipynb` | Profile distributions, missingness, volatility, and cumulative returns. |
| 09 | `src/features.py` | Create momentum, rolling return, volatility, and future-return fields. |
| 10 | `src/modeling.py`, `notebooks/` | Fit a chronological linear-regression baseline. |
| 11 | `src/evaluation.py`, `docs/monitoring_plan.md` | Quantify error, uncertainty, scenarios, and risks. |
| 12 | `reports/project_summary.md` | Communicate findings and limitations to a portfolio manager. |
| 13 | `app.py`, `model/model.pkl`, `docs/handoff_plan.md` | Package the model and expose a prediction endpoint. |
| 14 | `docs/monitoring_plan.md` | Define data, model, system, and business monitoring. |
| 15 | `src/run_step.py`, `docs/orchestration_plan.md` | Make feature generation repeatable and observable. |
| 16 | `docs/project_summary.md`, this guide | Make the complete lifecycle legible to a new owner. |
