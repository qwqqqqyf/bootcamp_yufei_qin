# Handoff Plan

- Install dependencies from `requirements.txt`.
- Run `src/run_step.py` to build processed features from the raw CSV.
- Fit or reload the model under `model/model.pkl`.
- Start `app.py` only after `/health` reports that the model is loaded.
- Use the monitoring thresholds in `docs/monitoring_plan.md`.
- Log data, model, system, and business issues in the project issue tracker.
- The platform on-call handles failed jobs and API incidents.
- The quantitative analyst approves model changes and rollbacks.
- The portfolio analyst reviews stakeholder reports and sector-level findings.
