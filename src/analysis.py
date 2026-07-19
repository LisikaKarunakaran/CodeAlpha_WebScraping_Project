import pandas as pd

df = pd.read_csv("dataset/clean_books.csv")

print("="*50)
print("BOOK DATA ANALYSIS")
print("="*50)

print("\nTotal Books:", len(df))

print("\nAverage Price")
print(df["Price"].mean())

print("\nHighest Price")
print(df["Price"].max())

print("\nLowest Price")
print(df["Price"].min())

print("\nAverage Rating")
print(df["Rating"].value_counts())

print("\nAvailability")
print(df["Availability"].value_counts())