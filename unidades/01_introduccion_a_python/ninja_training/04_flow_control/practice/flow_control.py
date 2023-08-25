"""Estructuras de control.

En este "entrenamiento ninja" pondrás en práctica el uso de las estructuras de
control en Python.

Sigue los comentarios TODO para completar las tareas y, no olvides, lanzar los
con `pytest` y verifica que lo tienes todo bien.
"""

from random import randint


# TODO genera 10 números aleatorios de 0 a 100 y guárdalos en la siguiente
# lista.
# Como ves al principio del fichero ya he importado la función `randint`que
# puedes usar para generar los números aleatorios.
random_nums: list[int] = []


# TODO suma los dos números más pequeños de random_nums y guarda el resultado
# de esta suma en la siguiente variable.
addition_large_nums: int = 0


# TODO suma todos los números de `random_nums` y guarda el resultado en esta
# variable.
addition: int = 0


# A continuación tienes un diccionario con información de un conjunto de
# estudiantes.
students: dict[str, float] = {
    "Alice": 6.75,
    "Bob": 7.25,
    "Mary": 8.5,
    "Jon": 3.75
}

# TODO Calcula la nota media de todo este alumnado y guarda el resultado en la
# siguiente variable.
avg_grades: float = 0.0


# TODO Guarda en la siguiente variable el nombre y la nota del estudiante con
# la nota más alta con este formato:
# f"{name} ha obtenido la nota más alta: {mark}."
info_best_student: str = ""


# A continuación tienes una LISTA de DICCIONARIOS con información de los
# personajes de la serie "Rick and Morty".
# Por cierto, ves acostumbrándote a este tipo de estructuras porque será
# así como consumiremos APIs más adelante y, también, será así como nuestras
# APIs enviarán la información a los clientes... Tiempo al tiempo.
rick_and_morty: list[dict[int, str, str, str, str]] = [
    {
        "id": 1,
        "name": "Rick Sanchez",
        "status": "Alive",
        "species": "Human",
        "gender": "Male"
    },
    {
        "id": 2,
        "name": "Morty Smith",
        "status": "Alive",
        "species": "Human",
        "gender": "Male"
    },
    {
        "id": 3,
        "name": "Summer Smith",
        "status": "Alive",
        "species": "Human",
        "gender": "Female"
    },
    {
        "id": 4,
        "name": "Beth Smith",
        "status": "Alive",
        "species": "Human",
        "gender": "Female"
    },
    {
        "id": 5,
        "name": "Abadango Cluster Princess",
        "status": "Alive",
        "species": "Alien",
        "gender": "Female",

    }
]


# TODO Guarda en esta lista el nombre de todos los personajes usando un bucle
# for y sin "list comprehension".
rick_and_morty_names: list[str] = []


# TODO Guarda en esta lista el nombre de los personajes femeninos usando un
# bucle for y sin "list comprehension".
female_characteres: list[str] = []


# TODO En la lista de diccionarios de `rick_and_morty` se tienen diccionarios
# con 5 datos: id, name, status, species y gender. Simplifícalo para que
# dichos diccionarios solo tengan: name, species y gender.
#
# No modifiques `rick_and_morty`, guarda la simplificación en `simple_ram` que
# tienes a continuación.
simple_ram: list[dict[str, str, str]] = []

