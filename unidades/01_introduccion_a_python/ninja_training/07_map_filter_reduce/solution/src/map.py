"""La función map en Python.

En este script tienes una serie de comentarios donde se describen las funciones
que tienes que programar. En todas estas funcones usarás la función `map` de
Python para transformar listas.

A parte de las funciones que tienes que escribir, puedes crear todo el código
que consideres oportuno: variables, constantes, otras funciones, etc.
"""
from math import floor


# TODO Escribe una función llamada `add_to_list` que reciba dos parámetros: una
#      lista de números enteros y un número entero. Esta función devolverá una
#      nueva lista con la suma del número entero y los elementos de la lista.
#      Por ejemplo: si recibe como parámetro:
#      [1, 2, 3, 4, 5]
#      15
#
#      Devolvería:
#      [16, 17, 18, 19, 20]
def add_to_list(numbers: list[int], addition: int) -> list[int]:
    return list(map(lambda n: n + addition, numbers))


# TODO Escribe una función llamada `str_lengths` que reciba como parámetro una
#      lista de strings y devuelva una lista de números con las longitudes de
#      esos strings.
#
#      Por ejemplo, si la funcion recibe esta lista:
#      ["Alice", "Bob", "Mary", "Jon"]
#
#      Devolvería esta otra lista:
#      [5, 3, 4, 3]
def str_lengths(strings: list[str]) -> list[int]:
    return list(map(lambda s: len(s), strings))


# TODO Escribe una función llamada `mark_descriptions` que reciba una lista de
#      notas numéricas (números enteros) y devuelva otra lista con las
#      descripciones de esas notas siguiente estas reglas:
#      - Nota menor que 5: "Suspenso"
#      - Nota igual a 5 o 6: "Susprobado"
#      - Nota mayor que 6: "Aprobado"
def mark_descriptions(marks: list[int]) -> list[str]:
    def mark_to_desc(m: int) -> str:
        if m < 5:
            return "Suspenso"
        elif m < 7:
            return "Susprobado"
        else:
            return "Aprobado"

    return list(map(mark_to_desc, marks))


# TODO Escribe una función llamada `student_names` que reciba un diccionario
#      con el nombre de una serie de estudiantes y sus notas. Esta función
#      devolverá una lista con el nombre de los estudiantes.
#
#      Por ejemplo, si recibe este dicccionario:
#      {"Alice": 7, "Bob": 6, "Mary": 9, "Jon": 6}
#
#      Devolvería esta lista:
#      ["Alice", "Bob", "Mary", "Jon"]
def student_names(students: dict[str, int]) -> list[str]:
    return list(map(lambda student_tuple: student_tuple[0], students.items()))


# TODO Escribe una función llamada `my_round` que reciba números reales y
#      devuelva los números truncados, sin la parte decimal.
#
#      Por ejemplo: si recibe esta lista:
#      [3.8, 5.60573, 7.0, 4.25]
#
#      Devolvería:
#      [3, 5, 7, 4]
#
#      Para redondear los números hacia abajo tienes una función en la
#      biblioteca `math` de Python llamada `floor`
def my_round(numbers: list[float]) -> list[int]:
    return list(map(lambda n: floor(n), numbers))


# TODO Escribe una función llamada `anonymize` que reciba una lista de
#      diccionarios con los datos de una serie de pacientes y los anonimice
#      elimando el nombre de esta lista.
#
#      Por ejemplo, si recibe esta lista:
#      [
#          {"name": "Alice", "age": 25, "weight": 50, "height": 165},
#          {"name": "Bob", "age": 25, "weight": 70, "height": 175},
#          {"name": "Mary", "age": 25, "weight": 60, "height": 170},
#          {"name": "Jon", "age": 25, "weight": 80, "height": 190}
#      ]
#
#      Devolvería esta lista:
#      [
#          {"age": 25, "weight": 50, "height": 165},
#          {"age": 25, "weight": 70, "height": 175},
#          {"age": 25, "weight": 60, "height": 170},
#          {"age": 25, "weight": 80, "height": 190}
#      ]
#
#      MUCHO OJO AQUÍ!!! NO DEBERÍAS MODIFICAR EL DICCIONARIO ORIGINAL.
#      En Python existe el método `copy` de `dict` para hacer una copia de un
#      diccionario.
def anonymize(students: list[dict]) -> list[dict]:
    def del_name(student: dict) -> dict:
        student_copy = student.copy()
        del student_copy["name"]
        return student_copy

    return list(map(del_name, students))
