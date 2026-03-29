import requests
from dotenv import load_dotenv

import os

load_dotenv()

query = input("What type of news are you intrested in today?: ")
api_key = os.getenv("API_KEY")

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-03-28&sortBy=popularity&apiKey={api_key}"

r = requests.get(url)
data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n*******************************************************************\n")
