import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

books = []

print("Scraping started...\n")

# Loop through all 50 pages
for page in range(1, 51):

    url = base_url.format(page)
    print(f"Scraping Page {page}...")

    response = requests.get(url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")

    for book in soup.find_all("article", class_="product_pod"):

        # Title
        title = book.h3.a["title"]

        # Price
        price = book.find("p", class_="price_color").text

        # Availability
        availability = (
            book.find("p", class_="instock availability")
            .text.strip()
        )

        # Rating
        rating = book.p["class"][1]

        # Product Link
        link = (
            "https://books.toscrape.com/catalogue/"
            + book.h3.a["href"]
        )

        books.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating,
            "Link": link
        })

# Create DataFrame
df = pd.DataFrame(books)

# Save CSV
df.to_csv("dataset/books.csv", index=False, encoding="utf-8")

print("\n===================================")
print("Scraping Completed Successfully!")
print("===================================")
print(f"Total Books Scraped : {len(df)}")
print("Dataset saved as dataset/books.csv")