"""Comienzo del módulo.

Esto es un docstring, o texto literal, ya que comienza con una triple comilla y
termina con otra tiple comilla.
"""

# Aquí se imprime por pantalla el resultado de una suma.
n1: int = 5
n2: int = 10
print(n1 + n2)

"""
Esto es un comentario multilínea. Parece un docstring pero no lo es porque no
se encuentra al comienzo del módulo, función, clase o método.

Es, por tanto, una cuestión de contexto.

Aprovecho para imprimir un "Hola Mundo".
"""
print("Hola Mundo")


def fn():
    """Una función.

    Aunque no hemos visto funciones en Python, aquí tienes una.

    Este texto es un texto literal o docstring y no un comentario multilínea.
    ¿Por qué? Porque está al comienzo de una función.

    Olvídate de lo que no entiendas.
    """
    pass


# Como ves, los comentarios multilínea y docstring son un lío.
#
# Así pues, aquí mismo, te estoy mostrando qué hago yo y te recomiendo hacer
# cuando tengo que escribir un comentario multilínea: en realidad escribo
# varios comentarios de una línea.
#
# Aprovecho para decirte adiós, espero que haya quedado claro.
print("Hasta pronto")
