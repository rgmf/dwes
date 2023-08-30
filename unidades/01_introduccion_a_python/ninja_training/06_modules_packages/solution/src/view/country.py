from src.model.countries.definitions import (
    COUNTRY_CURRENCIES,
    COUNTRY_CAPITAL,
    COUNTRY_NAME,
    COUNTRY_COMMON_NAME
)
from src.model.countries.country import COUNTRIES


def show(attribute: str = COUNTRY_CURRENCIES) -> dict[str, int | str]:
    if attribute == COUNTRY_CURRENCIES:
        return show_currencies()
    elif attribute == COUNTRY_CAPITAL:
        return show_capitals()
    else:
        return show_capital_for(attribute)


def show_currencies() -> dict[str, int]:
    currencies: dict[str, int] = {}
    for country in COUNTRIES:
        if COUNTRY_CURRENCIES in country:
            country_currencies: list[str] = get_country_currencies(country[COUNTRY_CURRENCIES])
            update_currencies(currencies, country_currencies)

    print("Estadísticas de monedas")
    print("----------------------------------------------------------------")
    for name, total in currencies.items():
        print(f"- {name:<40} está en {total} países")
    print()

    return currencies


def get_country_currencies(country_currencies: dict[str, dict]) -> list[str]:
    list_of_currencies: list[str] = []
    for _, currency in country_currencies.items():
        list_of_currencies.append(currency["name"])
    return list_of_currencies


def update_currencies(currencies: dict[str, int], country_currencies: list[str]) -> None:
    for name in country_currencies:
        if name in currencies:
            currencies[name] = currencies[name] + 1
        else:
            currencies[name] = 1


def show_capitals() -> dict[str, str]:
    capitals: dict[str, str] = {}

    print("Capitales de todos los países")
    print("------------------------------------------------------------")
    for country in COUNTRIES:
        if (
            COUNTRY_CAPITAL in country and
            COUNTRY_NAME in country and
            COUNTRY_COMMON_NAME in country[COUNTRY_NAME]
        ):
            name: str = country[COUNTRY_NAME][COUNTRY_COMMON_NAME]
            capital: str = country[COUNTRY_CAPITAL][0]
            capitals[name] = capital
            print(f"- {name} ({capital})")
    print()

    return capitals


def show_capital_for(country_name: str) -> dict[str, str]:
    print(f"Capital de {country_name}")
    print("-------------------------------------------------------------")
    capital: str | None = None
    for country in COUNTRIES:
        if (
            COUNTRY_CAPITAL in country and
            COUNTRY_NAME in country and
            COUNTRY_COMMON_NAME in country[COUNTRY_NAME] and
            country_name.lower() == country[COUNTRY_NAME][COUNTRY_COMMON_NAME].lower()
        ):
            capital = country[COUNTRY_CAPITAL][0]
    if capital:
        print(capital)
    else:
        print(f"No tenemos datos para el país {country_name}")
    print()

    return {country_name: capital}
