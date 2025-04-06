#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob

import pandas as pd
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md


def get_card_data(card_id: str) -> str:
    url = f"https://pocket.limitlesstcg.com/cards/{card_id}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find("div", class_="card-text")
    texts = [d.get_text().replace("\n", "").strip() for d in data]

    return md(" ".join(texts))


def get_all_card_ids() -> list[dict[str, str]]:
    d = glob.glob("data/*.csv")[0]
    df = pd.read_csv(d)

    df["card_id"] = (
        (df.setId + "/" + df.number.astype(str)).str.replace("PROMO", "P-A").tolist()
    )

    return df[["name", "card_id"]].to_dict(orient="records")


def get_energy_mappings() -> str:
    with open("energy_mappings.txt", "r") as f:
        mappings = f.readlines()
    e_map = [m.strip() for m in mappings]
    return " ".join(e_map)
