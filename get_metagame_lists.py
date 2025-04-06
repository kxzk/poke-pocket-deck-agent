#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "beautifulsoup4",
#     "requests",
# ]
# ///
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    base_url = "https://play.limitlesstcg.com"
    url = f"{base_url}/decks?game=pocket"

    response = requests.get(url)
    # print(response.content)

    # table class -> meta

    # deck lists
    deck = "/decks/giratina-ex-a2b-darkrai-ex-a2?game=POCKET&amp;format=standard&amp;set=A2b"
    response = requests.get(f"{base_url}{deck}")
    print(response.content)

    # extact top 5 deck lists

    # have playwright go:
    # * copy deck list
    # * write deck list locally in deck-lists
