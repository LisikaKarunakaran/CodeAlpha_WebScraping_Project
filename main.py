import os

print("=" * 50)
print("BOOKS WEB SCRAPING & DATA ANALYTICS PROJECT")
print("=" * 50)

print("\nStep 1: Scraping Data...")
os.system("py src/scraper.py")

print("\nStep 2: Cleaning Data...")
os.system("py src/preprocessing.py")

print("\nStep 3: Data Analysis...")
os.system("py src/analysis.py")

print("\nStep 4: Creating Visualizations...")
os.system("py src/visualization.py")

print("\nProject Completed Successfully!")