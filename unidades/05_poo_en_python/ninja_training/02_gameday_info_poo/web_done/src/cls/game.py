from src.cls.result import Result


class Game:
    def __init__(self, team1: str, team2: str, result: Result | None) -> None:
        self.team1: str = team1
        self.team2: str = team2
        self.result: Result | None = result

    def victory(self) -> str:
        if not self.result:
            return "Partido por jugar"
        if self.result.description() == "1":
            return self.team1
        elif self.result.description() == "2":
            return self.team2
        else:
            return "Empate"
