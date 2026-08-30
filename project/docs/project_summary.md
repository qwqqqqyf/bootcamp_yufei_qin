# Project Summary

## Purpose

This project compares the historical performance and risk of the 11 major S&P 500 sector groups. A portfolio manager can use the analysis as research input during sector-allocation review. The data uses Select Sector SPDR ETFs as investable proxies for sectors.

## What was done

Daily closing prices were downloaded from a public Yahoo Finance chart endpoint and preserved in `data/raw/`. The pipeline validates dates and prices, flags potential IQR outliers, calculates daily and cumulative returns, and creates five-day momentum and twenty-day rolling return and volatility features.

The modeling baseline predicts the return over the next five trading days using a chronological train-test split. This respects the direction of time and avoids using future observations when fitting the model. The model is packaged with a saved artifact and a small Flask API.

## Findings and interpretation

The processed dataset contains equal-length histories for 11 sectors. Sector behavior varies across time: a sector with stronger recent returns can also experience higher recent volatility. The appropriate stakeholder question is therefore not simply which sector returned the most, but how return and risk changed together.

The regression is a baseline, not a trading system. Short-horizon financial returns are noisy, and low explanatory power is expected. Residual diagnostics, rolling error, and scenario comparisons should be reviewed before using any result.

## What not to rely on

Do not treat historical rankings as guaranteed future performance. ETF fees, tracking differences, sector composition changes, missing observations, unusual market events, and data-source changes can affect results. The outlier flag is a review signal; deleting extreme observations could understate real market risk.

## Next steps

Compare performance across market regimes, add transaction-cost assumptions, test more robust time-series baselines, and monitor freshness, schema, feature null rates, rolling error, API latency, and sector-ranking stability. The quantitative analyst should approve model changes, while the platform owner maintains the scheduled pipeline and API.
