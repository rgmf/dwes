
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


otto: Labrador = Labrador("Otto", 10)
oriol: Chihuahua = Chihuahua("Oriol", 8)

# Acceso a atributos de instancia.
# Se usa operador punto (.) seguido del nombre de instancia.
print(otto.name)
print(otto.age)

# Acceso a atributos de clase.
# Lo podemos hacer de dos maneras:
# 1.- Por medio del nombre de la clase:
print(Dog.species)

# 2.- Por medio de un objeto:
print(otto.species)
print(oriol.species)

# Acceso a métodos.
otto.description()
otto.sound(5)

oriol.description()
oriol.sound(5)
