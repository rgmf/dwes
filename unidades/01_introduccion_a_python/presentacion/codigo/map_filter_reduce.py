###############################################################################
# Función map
###############################################################################

# Vamos a necesitar algunos imports.
from typing import Iterator
from functools import reduce


# Típico ejemplo de función "map".
def square_of_number(num: int) -> int:
    return num ** 2


numbers: list[int] = [2, 5, 7, 4, 3]
squares: list[int] = map(square_of_number, numbers)

# Puedes usar funciones anónimas y no haría falta la función
# `square_of_number`.
numbers: list[int] = [2, 5, 7, 4, 3]
squares: Iterator[int] = map(lambda num: num ** 2, numbers)

# La función map devuelve un Generator (tienes en las referencias un enlace en
# el que se explica muy bien la diferencia entre Iterator, Iterable y
# Generator).
#
# Así pues, `squares` es un Generator (objeto).
print(squares)

# Puedes obtener los valores del Generator recorriéndolo en un bucle o
# convirtiéndolo en lista, por ejemplo.
list_of_squares: list[int] = list(squares)

###############################################################################
# Función filter
###############################################################################

# Dada esta lista de números.
numbers: list[int] = [3, 2, 4, 8, 11, 15]

# Queremos obtener los cuadrados de los números pares.
# 1. Obtenemos los números pares.
even_numbers: list[int] = list(filter(lambda n: n % 2 == 0, numbers))

# 2. Calculamos los cuadrados de los números pares.
even_squares: list[int] = list(map(lambda n: n ** 2, even_numbers))

# Podemos hacerlo todo en una función.
even_squares: list[int] = list(
    map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers))
)

# Un ejemplo más de filter.
things: list[int | str | bool] = ["a", 2, True, "b"]

only_str: list[str] = list(filter(lambda x: isinstance(x, str), things))

###############################################################################
# Función reduce
###############################################################################

# Tenemos, de nuevo, una lista de números.
numbers: list[int] = [1, 2, 3, 4, 5]

# Queremos multiplicarlos todos... reduce es la respuesta. Ojo, porque para
# usar reduce tienes que importar esta función del módulo `functools`.
product: int = reduce(lambda x, y: x * y, numbers)

