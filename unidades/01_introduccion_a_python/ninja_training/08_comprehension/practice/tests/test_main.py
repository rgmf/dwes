from src.main import (
    initials,
    even_numbers,
    only_letters,
    random_number,
    assign_numbers,
    accum_game,
    grades,
    grades_for_pass_students
)


def test_initials():
    in_: list[str] = ["IES", "La", "Encanta", "está", "en", "Rojales"]
    out: list[str] = ["I", "L", "E", "E", "E", "R"] 
    assert initials(in_) == out


def test_even_numbers():
    assert even_numbers(1, 11) == [2, 4, 6, 8, 10]
    assert even_numbers(2, 12) == [2, 4, 6, 8, 10, 12]


def test_only_letters():
    in_: list[str] = "¡Hola Mundo, Bienvenid@!"
    out: list[str] = [
        "H", "o", "l", "a", "M", "u", "n", "d", "o", "B", "i", "e", "n", "v", "e", "n", "i", "d"
    ]
    assert only_letters(in_) == out


def test_random_number():
    in_: list[str] = ["a", "b", "c", "d", "e"]
    out: dict[str, int] = random_number(in_)
    for _, n in out.items():
        assert isinstance(n, int)


def test_assign_numbers():
    in_: list[str] = ["a", "b", "c", "d", "e"]
    out: dict[str, int] = assign_numbers(in_)
    assert out == {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}


def test_accum_game():
    in_: dict[str, int] = {"a": 10, "b": 20, "c": 30}
    assert accum_game(in_) == 60


def test_grades():
    names: list[str] = ["a", "b", "c"]
    marks: list[int] = [3, 5, 8]
    assert grades(names, marks) == {"a": 3, "b": 5, "c": 8}


def test_grades_for_pass_students():
    names: list[str] = ["a", "b", "c"]
    marks: list[int] = [3, 5, 8]
    assert grades_for_pass_students(names, marks) == {"b": 5, "c": 8}
