import pandas as pd
import numpy as np
import argparse

def check_missing_values(df):
    """Return missing value counts and rows with missing values."""
    missing_counts = df.isnull().sum()
    rows_with_missing = df[df.isnull().any(axis=1)]
    return missing_counts[missing_counts > 0], rows_with_missing

def check_duplicates(df):
    """Return duplicate rows (including all occurrences)."""
    duplicates = df[df.duplicated(keep=False)]
    return duplicates

def numeric_stats(df):
    num_df = df.select_dtypes(include=[np.number])
    return num_df.describe().round(2)

def categorical_stats(df):
    cat_df = df.select_dtypes(exclude=[np.number])
    return cat_df.describe()

def detect_outliers(df, z_thresh=3):
    """Return outlier rows using z-score method."""
    numeric_df = df.select_dtypes(include=[np.number])
    z_scores = (numeric_df - numeric_df.mean()) / numeric_df.std()
    mask = np.abs(z_scores) > z_thresh
    outlier_rows = df[mask.any(axis=1)]  # keep rows with any outlier
    return outlier_rows

def generate_report(csv_file, output_file="report.txt"):
    df = pd.read_csv(csv_file)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("📊 CSV Data Quality Report\n")
        f.write("="*40 + "\n\n")

        f.write(f"Total Rows: {df.shape[0]}\n")
        f.write(f"Total Columns: {df.shape[1]}\n\n")

        # Missing values
        missing_counts, missing_rows = check_missing_values(df)
        f.write("🔎 Missing Values:\n")
        if missing_counts.empty:
            f.write(" - No missing values found.\n\n")
        else:
            f.write(str(missing_counts) + "\n\n")
            f.write("Rows with missing values:\n")
            f.write(str(missing_rows) + "\n\n")

        # Duplicates
        duplicates = check_duplicates(df)
        f.write("🔎 Duplicates:\n")
        if duplicates.empty:
            f.write(" - No duplicate rows found.\n\n")
        else:
            f.write(f" - {len(duplicates)} duplicate rows found:\n\n")
            f.write(str(duplicates) + "\n\n")

        # Numeric stats
        f.write("📈 Numeric Column Statistics:\n")
        if not df.select_dtypes(include=[np.number]).empty:
            f.write(str(numeric_stats(df)) + "\n\n")
        else:
            f.write(" - No numeric columns.\n\n")

        # Categorical stats
        f.write("📊 Categorical Column Statistics:\n")
        if not df.select_dtypes(exclude=[np.number]).empty:
            f.write(str(categorical_stats(df)) + "\n\n")
            f.write("📊 Category Value Counts:\n")
            for col in df.select_dtypes(exclude=[np.number]).columns:
                f.write(str(df[col].value_counts(dropna=True)) + "\n\n")
        else:
            f.write(" - No categorical columns.\n\n")

        # Outliers
        outliers = detect_outliers(df)
        f.write("⚠️ Outliers Detected:\n")
        if outliers.empty:
            f.write(" - No significant outliers found.\n\n")
        else:
            f.write(f" - {len(outliers)} rows contain outliers:\n\n")
            f.write(str(outliers) + "\n\n")

    print(f"✅ Report generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV Data Quality Checker")
    parser.add_argument("csv_file", nargs="?", default="sample.csv", help="Path to CSV file")
    parser.add_argument("--output", default="report.txt", help="Output report file")

    args = parser.parse_args()
    generate_report(args.csv_file, args.output)
