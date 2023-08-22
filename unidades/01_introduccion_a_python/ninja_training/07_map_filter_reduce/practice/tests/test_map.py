from src.map import (
    add_to_list,
    str_lengths,
    mark_descriptions,
    student_names,
    my_round,
    anonymize
)


def test_add_to_list():
    assert add_to_list([10, 100, 1000, 10000], -1) == [9, 99, 999, 9999]
    assert add_to_list([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
    assert add_to_list([1, 2, 3, 4, 5], 10) == [11, 12, 13, 14, 15]
    assert add_to_list([], 10) == []


def test_str_lengths():
    l: list[str] = ["a", "aa", "", "abcde fg"]
    e: list[int] = [1, 2, 0, 8]
    assert str_lengths(l) == e

    l: list[str] = []
    e: list[int] = []
    assert str_lengths(l) == e


def test_mark_descriptions():
    l: list[int] = [0, 4, 5, 5, 4, 6, 7, 8, 10]
    e: list[str] = [
        "Suspenso", "Suspenso", "Susprobado", "Susprobado", "Suspenso",
        "Susprobado", "Aprobado", "Aprobado", "Aprobado"
    ]
    assert mark_descriptions(l) == e


def test_student_names():
    d: dict[str, int] = {"a": 1, "b": 2, "c": 3}
    e: list[str] = ["a", "b", "c"]
    assert student_names(d) == e

    d: dict[str, int] = {}
    e: list[str] = []
    assert student_names(d) == e


def test_my_round():
    l: list[float] = [1, 1.0, 1.4, 1.5, 1.6, 1.999]
    e: list[int] = [1, 1, 1, 1, 1, 1]
    assert my_round(l) == e

    l: list[float] = []
    e: list[str] = []
    assert my_round(l) == e


def test_anonymize():
    l: list[dict[str, str | int]] = [
        {"name": "Alice", "age": 25, "weight": 50, "height": 165},
        {"name": "Bob", "age": 25, "weight": 70, "height": 175},
        {"name": "Mary", "age": 25, "weight": 60, "height": 170},
        {"name": "Jon", "age": 25, "weight": 80, "height": 190}
    ]
    e: list[dict[str, str | int]] = [
        {"age": 25, "weight": 50, "height": 165},
        {"age": 25, "weight": 70, "height": 175},
        {"age": 25, "weight": 60, "height": 170},
        {"age": 25, "weight": 80, "height": 190}
    ]
    assert anonymize(l) == e
