from ..list01 import random_numbers, l1, l2, l3, l4, l5
from ..list02 import a_stack, ascending_list, descending_list, last_item
from ..list03 import (
    text, first_letter, second_letter, others, two_first_letters
)


def test_list01():
    assert len(random_numbers) == 10

    assert len(l1) == 1
    assert l1[0] == random_numbers[3]

    assert len(l2) == 4
    assert l2 == random_numbers[:4]

    assert len(l3) == 3
    assert l3 == random_numbers[-3:]

    assert len(l4) == 3
    assert l4 == random_numbers[1:4]

    assert len(l5) == 5
    assert l5 == random_numbers[::2]


def test_list02():
    assert len(a_stack) == 3
    assert "".join(a_stack) == "aAá"

    assert len(ascending_list) == 4
    assert ascending_list == ["A", "a", "Á", "á"]

    assert len(descending_list) == 4
    assert descending_list == ["á", "Á", "a", "A"]

    assert last_item == "Á"


def test_list03():
    assert len(text) > 2
    sorted_text: str = sorted(text)
    assert first_letter == sorted_text[0]
    assert second_letter == sorted_text[1]
    assert others == sorted_text[2:]
    assert two_first_letters == [first_letter, second_letter]
