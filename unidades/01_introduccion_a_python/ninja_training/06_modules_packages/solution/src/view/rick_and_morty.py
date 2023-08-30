from src.model.rick_and_morty.character import CHARACTER
from src.model.rick_and_morty.definitions import (
    RICK_AND_MORTY_NAME,
    RICK_AND_MORTY_ORIGIN
)


def show(attribute: str = RICK_AND_MORTY_NAME) -> list[str]:
    if attribute == RICK_AND_MORTY_NAME:
        return show_names()
    elif attribute == RICK_AND_MORTY_ORIGIN:
        return show_locations()
    else:
        return []


def show_names() -> list[str]:
    names: list[str] = []

    print("Nombre de todos los personajes de la serie:")
    print("-------------------------------------------")
    for character in CHARACTER["results"]:
        if RICK_AND_MORTY_NAME in character:
            names.append(character[RICK_AND_MORTY_NAME])
            print(f"- {character[RICK_AND_MORTY_NAME]}")
    print()

    return names


def show_locations() -> list[str]:
    locations: list[str] = []

    print("Lugares de donde son todos los personajes de la serie:")
    print("-------------------------------------------------------------------------")
    print()
    print("Nombre                           | Origen")
    print("-------------------------------------------------------------------------")
    for character in CHARACTER["results"]:
        if RICK_AND_MORTY_NAME in character and RICK_AND_MORTY_ORIGIN in character:
            name = character[RICK_AND_MORTY_NAME]
            location = character[RICK_AND_MORTY_ORIGIN]["name"]
            locations.append(location)
            print(f"- {name:<30} | {location}")
    print("-------------------------------------------------------------------------")
    print()

    return locations
