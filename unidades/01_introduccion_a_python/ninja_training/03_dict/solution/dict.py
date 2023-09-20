"""Introducción a los diccionarios (dict)

En este "entrenamiento ninja" te vas a enfrentar a los diccionarios de Python.
Solo tienes que seguir los comentarios TODO que ves más abajo.

Cuando termines lanza los tests con `pytest` y verifica que lo tienes todo
bien.
"""

from collections import namedtuple

# TODO Crea un diccionario con las capitales de tres países.
#      El nombre del país será la clave y el nombre de la capital el valor.
capitals: dict[str, str] | None = {
    "Spain": "Madrid",
    "England": "London",
    "Francia": "Paris"
}

# TODO Crea una lista con el nombre de todos los países que hay en `capitals`.
countries: list[str] | None = list(capitals)

# TODO Asigna a la siguiente variable el nombre de la capital del segundo país
#      que haya en `capitals`. PIENSA UN POCO, ya que tiene que dar igual el
#      nombre del país, lo tienes que hacer teniendo en cuenta que no conoces
#      el nombre de los países que hay en el diccionario, no sabes qué datos
#      hay en el diccionario.
second_capital: str | None = capitals[countries[1]]

# A continuación tienes un diccionario con las temperaturas máximas y mínimas
# de la última semana (inventadas, claro está).
weather: dict[str, list[int]] = {
    "lunes": [30, 25],
    "martes": [33, 24],
    "miercoles": [29, 24],
    "jueves": [34, 23],
    "viernes": [31, 20],
    "sabado": [27, 22],
    "domingo": [34, 25]
}

# TODO Asigna a esta variable la temperatura máxima del jueves.
thursday_max: int | None = weather["jueves"][0]

# TODO Asigna a esta variable la temperatura mínima de domingo.
sunday_min: int | None = weather["domingo"][1]

# Los mismos ejercicios que antes, pero ahora, he usado un namedtuple para que
# el código sea más fácil de leer y comprender. De hecho, he llamado al
# diccionario `wheather_hf` donde "hf" significa "Human Friendly" :D.
TemperatureStats = namedtuple("TemperatureStats", ["max", "min"])
weather_hf: dict[str, TemperatureStats] = {
    "lunes": TemperatureStats(31, 24),
    "martes": TemperatureStats(34, 23),
    "miercoles": TemperatureStats(30, 23),
    "jueves": TemperatureStats(35, 22),
    "viernes": TemperatureStats(32, 19),
    "sabado": TemperatureStats(28, 21),
    "domingo": TemperatureStats(35, 24)
}

# TODO Asigna a esta variable la temperatura máxima del lunes del diccionario
# weather_hf.
monday_max: int | None = weather_hf["lunes"].max

# TODO Asigna a esta variable la temperatura mínima del viernes del diccionario
# weather_hf.
friday_min: int | None = weather_hf["viernes"].min

# Aquí tienes una lista de diccionarios en el que se tiene el alumnado con una
# nota o calificación.
students_info: list[dict[str, str | float]] = [
    {
        "name": "Alice",
        "mark": 9.75
    },
    {
        "name": "Bob",
        "mark": 6.25
    },
    {
        "name": "Lisa",
        "mark": 5.5
    }
]

# TODO Guarda en la siguiente variable la nota de "Bob".
bob_mark: float = students_info[1]["mark"]

# TODO Guarda en la siguiente variable el nombre del último alumno/a.
last_student_name: str = students_info[-1]["name"]

# TODO Cambia, aquí debajo, la nota de "Alice" por un 9.0.
students_info[0]["mark"] = 9.0

# TODO Cambia, aquí debajo, el nombre de "Bob" por "Bo Bob".
students_info[1]["name"] = "Bo Bob"

# TODO Añade un alumno/a más con el nombre de "Jon" y la nota de 8.0.
students_info.append({"name": "Jon", "mark": 8.0})
