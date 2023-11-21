class Dog:
    species: str = "Canis familiaris"

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def description(self) -> None:
        print(f"Soy un {self.species} llamado {self.name} de {self.age} años")

    def sound(self, times: int) -> str:
        print(", ".join(["Guau!" for _ in range(times)]))


class Labrador(Dog):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.breed: str = "Labrador"

    def sound(self, times: int) -> str:
        print(f"Me pides que ladre {times} veces, pero yo no ladro nunca")


class Chihuahua(Dog):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.breed: str = "Chihuahua"
