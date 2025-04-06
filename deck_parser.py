#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
from dataclasses import dataclass


@dataclass
class PokemonCard:
    name: str
    set: str
    number: int


def read_file(path: str) -> list[str]:
    with open(path, "r") as f:
        lines = f.readlines()
    return lines


def parse_cards(data: list[str]) -> list[PokemonCard]:
    cards = []

    for line in data:
        parts = line.replace("\n", "").split()

        if len(parts) < 3:  # invalid
            continue
        else:
            # NOTE: might need to check length of handle
            # when Energy type is specified
            quantity = int(parts[0])
            # when len(parts) > 3 then name is longer
            # ['Charizard', 'ex'] => ['Charizard ex']
            name = " ".join(parts[1:-2])
            card_set = parts[-2]
            card_number = parts[-1]

            for _ in range(quantity):
                cards.append(PokemonCard(name, card_set, card_number))

    print(cards)


if __name__ == "__main__":
    files = glob.glob("deck-lists/*.txt")

    for f in files:
        d = read_file(f)
        cards = parse_cards(d)
