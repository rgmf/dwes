"""Módulos y paquetes en Python.

Este es el script principal, el que tienes que ejecutar para probar
manualmente el programa.

En este script principal se "parsea" la entrada por línea de comandos. Para
ver cómo se ejecuta el programa y las opciones de ejecución pues ejecutar el 
script así desde la terminal (desde la carpeta donde está "src", NO dentro de
"src"):

`python -m src.main --help`

Completa los comentarios TODO que ves en este fichero y en todos los demás.
"""
import argparse

from src.view.rick_and_morty import show as show_rick_and_morty
from src.view.country import show as show_country
from src.model.rick_and_morty.definitions import RICK_AND_MORTY_CHOICES
from src.model.countries.definitions import COUNTRY_CHOICES


def rick_and_morty_handler(arguments: argparse.Namespace) -> list[str]:
    """Handler for Rick and Morty options."""
    return show_rick_and_morty(arguments.rick_and_morty)


def country_handler(arguments: argparse.Namespace) -> dict[str, int | str]:
    """Handler for country options."""
    if arguments.country:
        return show_country(arguments.country)
    elif arguments.country_search_capital:
        return show_country(arguments.country_search_capital)
    else:
        return {}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DWES practice: modules and packages in Python")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--rick_and_morty", "-r",
        choices=RICK_AND_MORTY_CHOICES,
        help="Rick and Morty info"
    )
    group.add_argument(
        "--country", "-c",
        choices=COUNTRY_CHOICES,
        help="Country info"
    )
    group.add_argument(
        "--country_search_capital", "-s",
        help="Look for a capital of a country"
    )

    args = parser.parse_args()

    if args.rick_and_morty:
        rick_and_morty_handler(args)
    elif args.country or args.country_search_capital:
        country_handler(args)
