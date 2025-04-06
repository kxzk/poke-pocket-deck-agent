#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "beautifulsoup4",
#     "requests",
#     "markdownify",
# ]
# ///
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

if __name__ == "__main__":
    url = "https://pocket.limitlesstcg.com/cards/A1a/56"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.find_all("div", class_="card-text")

    t = [d.get_text().replace("\n", "").strip() for d in data]

    print(md(" ".join(t)))
