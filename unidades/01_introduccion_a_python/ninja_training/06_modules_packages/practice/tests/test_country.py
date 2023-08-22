import argparse

from src.main import country_handler


def test_country_currencies():
    args = argparse.Namespace(country="currencies")
    result: dict[str, int] = country_handler(args)

    assert "Euro" in result
    assert result["Euro"] == 36

    assert "United States dollar" in result
    assert result["United States dollar"] == 20


def test_country_capitals():
    args = argparse.Namespace(country="capital")
    result: dict[str, str] = country_handler(args)

    assert "Spain" in result
    assert result["Spain"] == "Madrid"

    assert "United States" in result
    assert result["United States"] == "Washington, D.C."

    assert "France" in result
    assert result["France"] == "Paris"


def test_capital_of_spain():
    args = argparse.Namespace(country_search_capital="Spain", country=None)
    result: dict[str, str] = country_handler(args)
    assert result["Spain"] == "Madrid"


def test_capital_of_mexico():
    args = argparse.Namespace(country_search_capital="Mexico", country=None)
    result: dict[str, str] = country_handler(args)
    assert result["Mexico"] == "Mexico City"


def test_country_invented_arg():
    args = argparse.Namespace(country_search_capital=None, country=None, invented="")
    result: dict[str, str] = country_handler(args)
    assert not result
