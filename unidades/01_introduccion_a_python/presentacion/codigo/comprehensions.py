###############################################################################
# List Comprehension
###############################################################################

# Programa para construir los cuadrados de los primeros 10 números.
# VERSIÓN 1: modo tradicional.
numbers: list[int] = []
for n in range(10):
    numbers.append(n ** 2)

# VERSIÓN 2: con función map.
numbers: list[int] = list(map(lambda n: n ** 2, range(10)))

# VERSIÓN 3: Pythonic Way: List Comprehension.
numbers: list[int] = [n ** 2 for n in range(10)]

# De la siguiente lista vamos a quedarnos con los números pares.
numbers: list[int] = [3, 5, 8, 4, 0, 17, 18, 40, 42, 5]

# VERSIÓN 1: modo tradicional.
even_numbers: list[int] = []
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)

# VERSIÓN 2: con función filter.
even_numbers: list[int] = list(filter(lambda n: n % 2 == 0, numbers))

# VERSIÓN 3: Pythonic Way: List Comprehension.
even_numbers: list[int] = [n for n in numbers if n % 2 == 0]

###############################################################################
# Dict Comprehension
###############################################################################

# Necesitamos importar `randint`.
from random import randint

# A esta lista de nombre de persona, asignarles un número aleatorio.
people: list[str] = ["Alice", "Bob", "Mary", "Jon"]

# VERSIÓN 1: modo tradicional.
people_info: dict[str, int] = {}
for name in people:
    people_info[name] = randint()

# VERSIÓN 2: Pythonic Way: Dict Comprehension
people_info: dict[str, int] = {name: randint() for name in people}

# Generar un diccionario con los aprobados.
students: dict[str, int] = {
    "Alice": 6,
    "Bob": 3,
    "Mary": 4,
    "Jon": 8
}

# Vamos directos a Pythonic Way.
students_pass: dict[str, int] = {
    name: mark for name, mark in students.items() if mark >= 5
}
