from random import randint

OPTIONS = ["1", "X", "2"]


def random_bet() -> str:
    return OPTIONS[randint(0, len(OPTIONS) - 1)]


def is_valid_bet(bet: str) -> bool:
    return bet in OPTIONS


def is_a_correct_pick(bet: str, scoreboard: tuple[int, int]) -> bool:
    if bet == "1" and scoreboard[0] > scoreboard[1]:
        return True
    if bet == "X" and scoreboard[0] == scoreboard[1]:
        return True
    if bet == "2" and scoreboard[0] < scoreboard[1]:
        return True
    return False
