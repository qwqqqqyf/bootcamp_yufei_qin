# Stage 06 — Data Preprocessing

## Cleaning Strategy

The raw dataset is loaded from `data/raw/sample_data.csv` and cleaned using reusable functions in `src/cleaning.py`.

### Missing Values

Missing values in numeric columns (`age`, `income`, and `score`) are filled using the median of each column.

The median is used because it is simple and less sensitive to extreme values than the mean.

Rows with too many missing values are removed using a 50% non-missing threshold.

### Normalization

The numeric columns `age`, `income`, and `score` are normalized using min-max scaling.

The normalized values range from 0 to 1.

### Output

The cleaned dataset is saved to:

`data/processed/sample_data_cleaned.csv`

The notebook compares the original and cleaned data by checking shape, missing values, and summary statistics.

### Assumptions

- `age`, `income`, and `score` are numeric variables suitable for median imputation.
- A row should contain at least 50% non-missing values to be retained.
- Min-max normalization is appropriate for the selected numeric variables.
- The `zipcode` column is kept as a string because it represents a geographic code rather than a numeric measurement.
- The `city` column is not normalized because it is categorical data.
- `extra_data` is not used for numerical imputation because it is not a required analysis variable.