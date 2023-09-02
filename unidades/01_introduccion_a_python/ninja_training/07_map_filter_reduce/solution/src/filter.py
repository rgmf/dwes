"""La función filter en Python.

En este script tienes una serie de comentarios donde se describen las funciones
que tienes que programar. En todas estas funcones usarás la función `filter` de
Python para filtrar elementos en listas creando una nueva lista.

A parte de las funciones que tienes que escribir, puedes crear todo el código
que consideres oportuno: variables, constantes, otras funciones, etc.
"""


# TODO Escribe una función llamada `long_str` que reciba como parámetro una
#      lista de strings y devuelva una lista con los strings que tengan más de
#      5 caracteres, es decir, de 6 para arriba.
def long_str(strings: list[str]) -> list[int]:
    return list(filter(lambda s: len(s) > 5, strings))


# TODO Escribe una función llamada `end_by_vowel` que reciba una lista de
#      strings y devuelva una lista con los strings que acaban por vocal
#      minúscula.
def end_by_vowel(strings: list[str]) -> list[str]:
    return list(filter(lambda s: s[-1] in ["a", "e", "i", "o", "u"], strings))


# TODO Escribe una función llamada `start_by` que reciba dos parámetros:
#      - Una lista de strings
#      - Una letra
#
#      Y devuelva una lista con los strings que comienzan por la letra,
#      ignorando minúsculas y mayúsculas.
def start_by(strings: list[str], letter: str) -> list[str]:
    return list(filter(lambda s: s[0].lower() == letter.lower(), strings))


# TODO Escribe una función llamada `numbers_around` que reciba dos parámetros:
#      una lista de números enteros y un número entero. Esta función devolverá
#      una nueva lista con los elementos que estén cerca del número. Cerca
#      puede ser:
#      - Un número por debajo
#      - El mismo número
#      - Un número por arriba
#
#      Por ejemplo, dados estos parámetros:
#      [10, 14, 20, 15, 16, 13, 17]
#      15
#
#      Devolvería:
#      [14, 15, 16]
#
#      Que son los números alrededor de 15.
def numbers_around(numbers: list[int], reference: int) -> list[int]:
    return list(filter(lambda n: reference - 1 <= n <= reference + 1, numbers))


# TODO Escribe una función llamada `students_pass` que reciba un diccionario
#      con el nombre de una serie de estudiantes y sus notas. Esta función
#      devolverá una lista de diccionarios con los estudiantes que han aprobado
#      (sus notas son superiores o iguales a 5).
#
#      Por ejemplo, si recibe esta lista:
#      [
#          {"name": "Alice", "mark": 7},
#          {"name": "Bob", "mark": 4},
#          {"name": "Mary", "mark": 3},
#          {"name": "Jon", "mark": 6}
#      ]
#
#      Devolvería esta otra lista:
#      [
#          {"name": "Alice", "mark": 7},
#          {"name": "Jon", "mark": 6}
#      ]
def student_pass(students: list[dict[str, int]]) -> list[dict[str, int]]:
    return list(filter(lambda s: s["mark"] >= 5, students))
