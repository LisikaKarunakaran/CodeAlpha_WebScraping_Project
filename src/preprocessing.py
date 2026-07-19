import pandas as pd

# ==============================
# Load Dataset
# ==============================
try:
    df = pd.read_csv("dataset/books.csv", encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv("dataset/books.csv", encoding="latin1")

print("=" * 50)
print("        BOOKS DATASET PREVIEW")
print("=" * 50)
print(df.head())

# ==============================
# Dataset Information
# ==============================
print("\n" + "=" * 50)
print("DATASET INFORMATION")
print("=" * 50)
print(df.info())

# ==============================
# Statistical Summary
# ==============================
print("\n" + "=" * 50)
print("STATISTICAL SUMMARY")
print("=" * 50)
print(df.describe(include="all"))

# ==============================
# Missing Values
# ==============================
print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())

# ==============================
# Duplicate Rows
# ==============================
print("\n" + "=" * 50)
print("DUPLICATE ROWS")
print("=" * 50)
print("Duplicate Rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# ==============================
# Clean Price Column
# ==============================
print("\nCleaning Price Column...")

df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("Â", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

# Convert Price to Numeric
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Remove rows where price is invalid
df = df.dropna(subset=["Price"])

# ==============================
# Reset Index
# ==============================
df.reset_index(drop=True, inplace=True)

# ==============================
# Cleaned Dataset Preview
# ==============================
print("\n" + "=" * 50)
print("CLEANED DATASET PREVIEW")
print("=" * 50)
print(df.head())

# ==============================
# Final Dataset Information
# ==============================
print("\n" + "=" * 50)
print("FINAL DATASET INFORMATION")
print("=" * 50)
print(df.info())

# ==============================
# Save Clean Dataset
# ==============================
output_file = "dataset/clean_books.csv"
df.to_csv(output_file, index=False, encoding="utf-8")

print("\n" + "=" * 50)
print("SUCCESS!")
print("=" * 50)
print(f"Clean dataset saved as: {output_file}")
print(f"Total Records: {len(df)}")
print(f"Total Columns: {len(df.columns)}")