from ..function_params import (
    look_for_numbers, generate_list_number, conditional_op, ADD, AVG, UNKNOWN_OP
)


def test_look_for_numbers():
    assert look_for_numbers(0, 100, 10, 15, 100, 200, 300) == [10, 15, 100]
    assert look_for_numbers(500, 1000, 1, 100, 1000) == [1000]
    assert look_for_numbers(30, 0, 10, 20, 30) == []
    assert look_for_numbers() == []


def test_generate_list_number():
    assert generate_list_number() == []
    assert generate_list_number(
        start=0,
        end=5,
        step=1
    ) == [0, 1, 2, 3, 4, 5]
    assert generate_list_number(
        start=0,
        end=10,
        step=2
    ) == [0, 2, 4, 6, 8, 10]

    assert generate_list_number(
        end=10,
        step=2
    ) == []
    assert generate_list_number(
        start=0,
        step=2
    ) == []
    assert generate_list_number(
        start=0,
        end=10,
    ) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert generate_list_number(
        start=0,
        end=10,
        step=20
    ) == [0]
    assert generate_list_number(
        start=0,
        end=10,
        step=3
    ) == [0, 3, 6, 9]


def test_conditional_op_add():
    assert conditional_op(
        ADD,
        10, 20.5, 30,
        two=2, three=3
    ) == 65.5

    assert conditional_op(
        ADD,
        "hola", 10, True,
        name="DWES", age=25, height=180
    ) == 215

    assert conditional_op(
        ADD,
        "hola", "", "True", False, True,
        name="DAW", lastname="DWES"
    ) == 0


def test_conditional_op_avg():
    assert conditional_op(
        AVG,
        10, 20.5, 30,
        two=2, three=3
    ) == (10 + 20.5 + 30 + 2 + 3) / 5

    assert conditional_op(
        AVG,
        "hola", 10, True,
        name="DWES", age=25, height=180
    ) == (10 + 25 + 180) / 3

    assert conditional_op(
        AVG,
        "hola", "", "True", False, True,
        name="DAW", lastname="DWES"
    ) == 0


def test_conditional_op_no_args_neither_kwargs():
    assert conditional_op(ADD) == 0


def test_conditional_op_unknown_operation():
    assert conditional_op("unknown", 10, number=10) == UNKNOWN_OP
