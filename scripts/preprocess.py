**Need to edit**

import os
import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """Load raw dataset from the data directory."""
    print(f"[1/4] Loading raw data from: {filepath}")
    df = pd.read_csv(filepath)
    print(f"      Initial records: {len(df):,} rows, {df.shape[1]} columns")
    return df


def inspect_quality(df: pd.DataFrame) -> None:
    """Print preliminary data quality metrics."""
    print("[2/4] Inspecting data quality...")
    missing_counts = df.isnull().sum()
    print("      Missing values per column:")
    for col, count in missing_counts[missing_counts > 0].items():
        print(f"        - {col}: {count} missing")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize text formatting, handle missing fields,
    and deduplicate records.
    """
    print("[3/4] Cleaning and transforming data...")
    cleaned = df.copy()

    # 1. Strip leading/trailing whitespace and normalize column names
    cleaned.columns = [c.strip().lower().replace(" ", "_") for c in cleaned.columns]

    # 2. Standardize text fields (example: uppercase/strip text columns)
    for col in cleaned.select_dtypes(include="object").columns:
        cleaned[col] = cleaned[col].astype(str).str.strip()

    # 3. Deduplicate
    initial_len = len(cleaned)
    cleaned = cleaned.drop_duplicates()
    print(f"      Removed {initial_len - len(cleaned)} duplicate rows")

    return cleaned


def save_data(df: pd.DataFrame, output_path: str) -> None:
    """Save the preprocessed dataframe to output/."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"[4/4] Cleaned dataset saved to: {output_path} ({len(df):,} records)")


def main():
    raw_path = "data/raw_data.csv"           # Replace with your actual raw data path
    output_path = "data/cleaned_data.csv"     # Output location

    if os.path.exists(raw_path):
        raw_df = load_data(raw_path)
        inspect_quality(raw_df)
        clean_df = clean_data(raw_df)
        save_data(clean_df, output_path)
    else:
        print(f"Placeholder: Place raw dataset at {raw_path} to run the full pipeline.")


if __name__ == "__main__":
    main()
