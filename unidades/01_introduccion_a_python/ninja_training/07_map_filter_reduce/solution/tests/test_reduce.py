from src.reduce import my_sum, upper_initials


def test_my_sum():
    l: list[int] = [10, 100, 1000]
    e: int = 1110
    assert my_sum(l) == e

    l: list[int] = []
    e: int = 0
    assert my_sum(l) == e


def test_upper_initials():
    l: list[str] = ["a", "b", "c", "D"]
    e: str = "ABCD"
    assert upper_initials(l) == e

    l: list[str] = ["En", "la", "clase", "de", "DWES", "IES", "La", "Encantá"]
    e: str = "ELCDDILE"
    assert upper_initials(l) == e

    l: list[str] = []
    e: str = ""
    assert upper_initials(l) == e
