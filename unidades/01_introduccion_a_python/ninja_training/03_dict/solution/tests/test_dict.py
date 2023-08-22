from ..dict import (
    capitals, second_capital, thursday_max, sunday_min, monday_max, friday_min,
    bob_mark, last_student_name, students_info
)


def test_tuple():
    assert isinstance(capitals, dict)
    assert len(capitals) == 3

    assert isinstance(second_capital, str)
    assert second_capital == capitals[list(capitals)[1]]

    assert thursday_max == 34
    assert sunday_min == 25

    assert monday_max == 31
    assert friday_min == 19

    assert bob_mark == 6.25
    assert last_student_name == "Lisa"
    assert students_info[0]["mark"] == 9.0
    assert students_info[1]["name"] == "Bo Bob"
    assert len(students_info) == 4
