from src.cls.game import Game


class Gameday:
    def __init__(self, gameday: int, played: bool, games: list[Game]) -> None:
        self.gameday: int = gameday
        self.played: bool = played
        self.games: list[Game] = games
