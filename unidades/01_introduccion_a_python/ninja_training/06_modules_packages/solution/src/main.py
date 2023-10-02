"""Módulos y paquetes en Python.

Este es el script principal, el que tienes que ejecutar para probar
manualmente el programa.

En este script principal se "parsea" la entrada por línea de comandos. Para
ver cómo se ejecuta el programa y las opciones de ejecución puedes ejecutar el
script así desde la terminal (desde la carpeta donde está "src", NO dentro de
"src"):

`python -m src.main --help`

Como verás en esta ayuda, puedes ver información de la serie "Rick and Morty"
y de los países de (casi) todo el mundo.

Para ver información de "Rick and Morty" usa estas opciones de ejecución:

`python -m src.main --rick_and_morty names`
`python -m src.main -r names`

        Verás los nombres de todos los personajes que salen en la serie

`python -m src.main --rick_and_morty origin`
`python -m src.main -r origin`

        Verás de dónde son todos los personajes de la serie

Para ver información de los países puedes usar estas opicones de ejecución:

`python -m src.main --country currencies`
`pythoh -m src.main -c currencies`

        Verás todas las monedas y en cuántos países se usa

`python -m src.main --country capital`
`pythoh -m src.main -c capital`

        Verás las capitales de todos los países

`python -m src.main --country_search_capital Spain`
`pythoh -m src.main -s Spain`

        Verás la capital de Spain (puedes poner cualquier país en inglés)

Evidentemente, si ejecutas los comandos anteriores no verás lo que se indica
porque el programa está por completar. A lo largo de todos los ficheros fuente
verás comentarios TODO con instrucciones para completar.

Como siempre, puedes lanzar los tests para verificar que lo que has hecho está
bien (al menos pasa las pruebas).
"""
import argparse

# TODO Aquí se está importando una función `show` con el alias
#      `show_rick_and_morty`. Crea el módulo y la función correspondiente
#      donde proceda. Esta función show realiza lo siguiente:
#      - Recibe como parámetro un string con una de las opciones que ves en
#        `RICK_AND_MORTY_CHOICES`.
#      - Si la opción es `RICK_AND_MORTY_NAME` devuelve la lista de los
#        nombres de los personajes de la serie que se encuentran en el
#        diccionario `src.model.rick_and_morty.character.CHARACTER`
#      - Si la opción es `RICK_AND_MORTY_ORIGIN` devuelve la lista de
#        todos los orígenes del diccionario anterior.
#      - En otro caso devuelve una lista vacía.
#      - Además de devolver la lista, muestra por pantalla la información.
from src.view.rick_and_morty import show as show_rick_and_morty

# TODO Aquí se está importando una función `show` con el alias
#      `show_country`. Crea el módulo y la función correspondiente donde
#      proceda. Esta función show realiza lo siguiente:
#      - Recibe como parámetro un string con una de las opciones que ves en
#        `COUNTRY_CHOICES`.
#      - Si la opción es `COUNTRY_CURRENCIES` devuelve un diccionario con el
#        nombre de cada moneda (como clave) y el número de países donde se usa
#        dicha moneda como valor. Esta información está en el diccionario
#        `src.model.countries.country.COUNTRIES`.
#      - Si la opción es `COUNTRY_CAPITAL` devuelve un diccionario con el
#        nombre de cada país (como clave) y el nombre común de la capital.
#        Esta información la tienes que sacar de:
#        `src.model.countries.country.COUNTRIES`.
#      - En otro caso buscará el país indicado en el mismo diccionario para
#        devolver un diccionario con ese país (como clave) junto a su
#        capital.
#      - Además de devolver el diccionario indicado, en todos los casos se
#        mostrará esa misma información por pantalla.
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
