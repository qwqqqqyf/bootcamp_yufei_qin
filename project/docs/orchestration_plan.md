# Orchestration Plan

| Step | Input | Output | Dependency | Idempotent |
|---|---|---|---|---|
| Ingest | public Yahoo chart endpoint | `data/raw/sp500_sector_data.csv` | none | yes, same request range replaces the file |
| Clean | raw sector CSV | `data/processed/sp500_sector_prices_clean.csv` | ingest | yes |
| Features | cleaned CSV | `data/processed/sp500_sector_features_stage09.csv` | clean | yes |
| Model | feature CSV | `model/model.pkl` | features | yes, deterministic fit |
| Evaluate | model predictions and test data | metrics and scenario CSV | model | yes |
| Report | evaluation outputs | `reports/project_summary.md` | evaluate | yes |

Ingestion must precede cleaning, then features, model, evaluation, and reporting. Cleaning and basic source validation can run together after ingestion; reporting waits for evaluation. Every step writes a checkpoint to a known path and logs row counts, date ranges, and exceptions. A failed network request is retried once; schema or validation failures stop the pipeline for manual review. Partial output files should be written only after successful completion.

The current automation target is the feature-building step because it is deterministic and already has a CLI wrapper. Model fitting and reporting can be scheduled later. Source credentials, sector mapping changes, and final stakeholder interpretation remain manual because they require review.
