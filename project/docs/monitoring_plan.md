# Monitoring Plan

The project predicts five-trading-day sector ETF returns. Monitoring covers four layers.

- **Data:** check daily freshness (alert if the newest date is more than two business days old), schema and ticker count (alert if the schema changes or the 11-sector count falls), and null rate in model features (alert above 2%). The data analyst investigates the source response and pauses the run if validation fails.
- **Model:** calculate rolling 20-day MAE and alert if it is more than twice the validation baseline. Track the mean prediction and residual distribution; a sustained shift in either for 20 observations triggers review. The quantitative analyst reviews features and approves retraining.
- **System:** log job success and duration. Alert the platform on-call if the scheduled job fails or p95 API latency exceeds 2 seconds. The on-call retries once, then records the incident and escalates.
- **Business:** compare sector ranking stability and the difference between predicted and realized returns. A material ranking change across two weekly runs is a review signal, not an automatic trade.

Issues are logged in the project issue tracker. Retraining is considered monthly or sooner after a feature schema change, a sustained MAE alert, or a new ETF mapping. Rollbacks are approved by the quantitative analyst; the platform on-call owns dashboards and run execution.
