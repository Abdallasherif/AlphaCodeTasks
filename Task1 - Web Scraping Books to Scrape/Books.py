import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
book_data = []

# Loop through all pages (1 to 50)
for page in range(1, 51):
    url = base_url.format(page)
    response = requests.get(url)
    response.encoding = 'UTF-8'

    if response.status_code != 200:
        print(f"❌ Failed to get page {page}")
        continue

    soup = BeautifulSoup(response.text, 'lxml')
    books = soup.select("article.product_pod")

    for book in books:
        title = book.h3.a['title']
        price = book.select_one("p.price_color").text
        availability = book.select_one('p.instock.availability').text.strip()
        img_url = "http://books.toscrape.com/" + book.img["src"].replace("../", "")
        rate = book.select_one('p.star-rating')["class"][1]

        book_data.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rate": rate,
            "ImgUrl": img_url
        })

    print(f"✅ Scraped page {page}")

# Save to CSV
df = pd.DataFrame(book_data)
df.to_csv("Books.csv", index=False)
print("✅ All data saved to Books.csv")
