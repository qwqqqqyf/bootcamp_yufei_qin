# Stage 05 — Data Storage

## Folder Structure

```text
data/
├── raw/
└── processed/
```

- `data/raw/` stores raw CSV files.
- `data/processed/` stores processed Parquet files.

## Data Formats

CSV is used for raw data because it is simple and easy to inspect.

Parquet is used for processed data because it is efficient for analytical workflows and preserves data types.

## Environment Variables

The data paths are controlled by `.env`:

```text
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed
```

The notebook uses `python-dotenv` to load these environment variables.

## Validation

The saved CSV and Parquet files are reloaded and validated.

The validation checks:

- Shape
- Column names
- Data types
- Missing values

## Storage Utilities

The notebook includes:

- `detect_format()` to detect the file format from the file extension.
- `write_df()` to save DataFrames as CSV or Parquet.
- `read_df()` to load CSV or Parquet files.

The utilities also create missing directories and provide a clear message if a Parquet engine is unavailable.