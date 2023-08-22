import argparse

from src.main import rick_and_morty_handler


def test_rick_and_morty_character_names():
    args = argparse.Namespace(rick_and_morty="name")
    assert rick_and_morty_handler(args) == [
        "Rick Sanchez",
        "Morty Smith",
        "Summer Smith",
        "Beth Smith",
        "Jerry Smith",
        "Abadango Cluster Princess",
        "Abradolf Lincler",
        "Adjudicator Rick",
        "Agency Director",
        "Alan Rails",
        "Albert Einstein",
        "Alexander",
        "Alien Googah",
        "Alien Morty",
        "Alien Rick",
        "Amish Cyborg",
        "Annie",
        "Antenna Morty",
        "Antenna Rick",
        "Ants in my Eyes Johnson"
    ]


def test_rick_and_morty_character_origins():
    args = argparse.Namespace(rick_and_morty="origin")
    assert rick_and_morty_handler(args) == [
        "Earth (C-137)",
        "unknown",
        "Earth (Replacement Dimension)",
        "Earth (Replacement Dimension)",
        "Earth (Replacement Dimension)",
        "Abadango",
        "Earth (Replacement Dimension)",
        "unknown",
        "Earth (Replacement Dimension)",
        "unknown",
        "Earth (C-137)",
        "Earth (C-137)",
        "unknown",
        "unknown",
        "unknown",
        "unknown",
        "Earth (C-137)",
        "unknown",
        "unknown",
        "unknown"
    ]


def test_rick_and_morty_unknown():
    args = argparse.Namespace(rick_and_morty="unknown")
    assert rick_and_morty_handler(args) == []
