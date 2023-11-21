class Result:
    def __init__(self, goals1: int, goals2: int) -> None:
        self.goals1: int = goals1
        self.goals2: int = goals2

    def description(self) -> str:
        if self.goals1 > self.goals2:
            return "1"
        elif self.goals1 < self.goals2:
            return "2"
        else:
            retur "X"
