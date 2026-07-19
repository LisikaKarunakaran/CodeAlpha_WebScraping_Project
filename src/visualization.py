import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("dataset/clean_books.csv")

# -------------------------------
# Convert Rating to Numeric
# -------------------------------
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

# -------------------------------
# Chart 1: Rating Distribution
# -------------------------------
plt.figure(figsize=(8,5))
df["Rating"].value_counts().sort_index().plot(kind="bar")
plt.title("Books by Rating")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("images/books_by_rating.png")
plt.close()

# -------------------------------
# Chart 2: Price Distribution
# -------------------------------
plt.figure(figsize=(8,5))
plt.hist(df["Price"], bins=20)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("images/price_distribution.png")
plt.close()

# -------------------------------
# Chart 3: Average Price by Rating
# -------------------------------
plt.figure(figsize=(8,5))
df.groupby("Rating")["Price"].mean().plot(kind="bar")
plt.title("Average Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")
plt.tight_layout()
plt.savefig("images/average_price_rating.png")
plt.close()

# -------------------------------
# Chart 4: Top 10 Most Expensive Books
# -------------------------------
top10 = df.nlargest(10, "Price")

plt.figure(figsize=(12,6))
plt.bar(top10["Title"], top10["Price"])
plt.xticks(rotation=90)
plt.title("Top 10 Most Expensive Books")
plt.ylabel("Price (£)")
plt.tight_layout()
plt.savefig("images/top10_expensive_books.png")
plt.close()

# -------------------------------
# Chart 5: Availability
# -------------------------------
plt.figure(figsize=(6,6))
df["Availability"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Book Availability")
plt.tight_layout()
plt.savefig("images/book_availability.png")
plt.close()

print("All charts generated successfully!")