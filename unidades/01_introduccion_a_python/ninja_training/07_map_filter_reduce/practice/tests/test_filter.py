from src.filter import (
    long_str,
    end_by_vowel,
    start_by,
    numbers_around,
    student_pass
)


def test_long_str():
    l: list[str] = [
        "a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "a a a", "a a a ", ""
    ]
    e: list[str] = ["aaaaaa", "a a a "]
    assert long_str(l) == e

    l: list[str] = ["aaaaa", "bbbbb", "     "]
    e: list[str] = []
    assert long_str(l) == e


def test_end_by_vowel():
    l: list[str] = ["b", "bA", "a", "A", "ba", "ce "]
    e: list[str] = ["a", "ba"]
    assert end_by_vowel(l) == e


def test_start_by():
    l: list[str] = ["b", "a", "rac", "RAB", "r", "R", "ris", "Ris"]
    c: str = "r"
    e: list[str] = ["rac", "RAB", "r", "R", "ris", "Ris"]
    assert start_by(l, c) == e

    l: list[str] = ["b", "a", "rac", "RAB", "r", "R", "ris", "Ris"]
    c: str = "R"
    e: list[str] = ["rac", "RAB", "r", "R", "ris", "Ris"]
    assert start_by(l, c) == e


def test_numbers_around():
    l: list[int] = [7, 8, 9, 10, 11, 12, 13]
    n: int = 10
    e: list[int] = [9, 10, 11]
    assert numbers_around(l, n) == e

    l: list[int] = [13, 12, 11, 10, 9, 8, 7, 6]
    n: int = 8
    e: list[int] = [9, 8, 7]
    assert numbers_around(l, n) == e

    l: list[int] = [13, 12, 11, 10, 9, 8, 7, 6, 17]
    n: int = 15
    e: list[int] = []
    assert numbers_around(l, n) == e

    l: list[int] = []
    n: int = 15
    e: list[int] = []
    assert numbers_around(l, n) == e


def test_student_pass():
    l: list[dict[str, int]] = [
        {"name": "Alice", "mark": 7},
        {"name": "Bob", "mark": 4},
        {"name": "Mary", "mark": 3},
        {"name": "Jon", "mark": 6}
    ]
    e: list[dict[str, int]] = [
        {"name": "Alice", "mark": 7},
        {"name": "Jon", "mark": 6}
    ]
    assert student_pass(l) == e

    l: list[dict[str, int]] = [
        {"name": "Alice", "mark": 5},
        {"name": "Bob", "mark": 6},
        {"name": "Mary", "mark": 6},
        {"name": "Jon", "mark": 5}
    ]
    e: list[dict[str, int]] = [
        {"name": "Alice", "mark": 5},
        {"name": "Bob", "mark": 6},
        {"name": "Mary", "mark": 6},
        {"name": "Jon", "mark": 5}
    ]
    assert student_pass(l) == e

    l: list[dict[str, int]] = [
        {"name": "Alice", "mark": 4},
        {"name": "Bob", "mark": 4},
        {"name": "Mary", "mark": 3},
        {"name": "Jon", "mark": 3}
    ]
    e: list[dict[str, int]] = []
    assert student_pass(l) == e
