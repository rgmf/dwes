"""La función reduce en Python.

En este script tienes una serie de comentarios donde se describen las funciones
que tienes que programar. En todas estas funcones usarás la función `reduce` de
Python para obtener un valor a partir de una lista.

A parte de las funciones que tienes que escribir, puedes crear todo el código
que consideres oportuno: variables, constantes, otras funciones, etc.
"""

# TODO Importa la función `reduce` del módulo `functools` de Python.
from functools import reduce


# TODO Escribe una función llamada `my_sum` que reciba una lista de números y
#      obtenga la suma de todos esos números que devolverá como resultado.
#
#      Nota: ya existe una función en Python llamada `sum` que hace lo mismo,
#      por tanto cada vez que quieras hacer la suma de una lista úsala, no la
#      crees tú.
def my_sum(numbers: list[int]) -> int:
    return reduce(lambda accum, current: accum + current, numbers, 0)


# TODO Escribe una función llamada `upper_initials` que reciba una lista de
#      strings y devuelva un strings que conste de las iniciales de todos los
#      elementos de la lista en mayúsculas.
#
#      Por ejemplo, dada esta lista:
#      ["Hola", "mundo", "esto", "es", "Python"]
#
#      Devolvería el string:
#      "HMEEP"
def upper_initials(strings: list[str]) -> str:
    return reduce(
        lambda accum, current: accum + current[0].upper(), strings, ""
    )
