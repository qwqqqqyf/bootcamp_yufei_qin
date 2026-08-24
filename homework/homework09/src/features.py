import pandas as pd


def add_spend_income_ratio(df):
    """Add spending relative to income."""
    df = df.copy()
    df["spend_income_ratio"] = df["monthly_spend"] / df["income"]
    return df


def add_income_credit_ratio(df):
    """Add income relative to credit score."""
    df = df.copy()
    df["income_credit_ratio"] = df["income"] / df["credit_score"]
    return df


def add_region_frequency(df):
    """Add frequency encoding for region."""
    df = df.copy()
    frequencies = df["region"].value_counts(normalize=True)
    df["region_frequency"] = df["region"].map(frequencies)
    return df