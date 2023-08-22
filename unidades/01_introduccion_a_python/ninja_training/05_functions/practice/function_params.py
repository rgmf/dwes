"""Parámetros de funciones en Python.

En este ejercicio tienes una serie de funciones declaradas cuya implementarción
tienes que completar.

Todas estas funciones tienen un docstring explicando lo que tiene que hacer la
función. Fíjate, además, cómo se indican, en un docstring, los parámetros y el
valor de retorno pues lo tendrás que hacer así de aquí en adelante.

Puedes añadir todo el código que necesites.

Por último, como verás he añadido constantes que tendrás que usar en las
funciones. Las constantes ayudan a que el código sea más legible y fácil de
mantener. Tenlas siempre en mente.
"""

ADD = "add"
AVG = "avg"


def look_for_numbers(n_from: int = 0, n_to: int = 100, *args: tuple[int]) -> list[int]:
    """Buscar números en un rango.

    Esta función busca en `args` los números que están en el rango [`n_from` -
    `n_to`] y devuelve la lista de estos números.

    :param n_from: Cota inferior del rango, incluido.
    :param n_to:   Cota superior del rango, incluido.

    :return: Lista con los números que hay en `args` y que están en el rango
             [`n_from` - `n_to`].
    """
    pass


def generate_list_number(**kwargs: dict[str, int]) -> list[int]:
    """Generador de listas de números.

    Esta función genera una lista de números que devuelve como resultado.

    Para generar dicha lista se buscarán las siguientes claves en el parámetro
    `kwargs`:
    - start
    - end
    - step

    De los que solo son obligatorios "start" y "end".

    :param kwargs: Se esperan las siguientes claves:
                   - start (obligatorio): número inicial.
                   - end (obligatorio): número final.
                   - step (opcional): paso o salto (si no está este valor se
                                      usará el valor 1 como salto.

    :return: Devuelve la lista de números desde "start" hasta "end" de "step"
             en "step". Por ejemplo: si "start=0", "end=5" y "step=2" entonces
             se devuelve la lista "[0, 2, 4]".
    """
    pass


def conditional_op(operation: str, *args: tuple, **kwargs: dict) -> float:
    """Operación condicional.

    Esta función realiza la operación indicada por `operation` con los datos
    que llegan por medio de la lista de parámetros posicionales y clave-valor
    variables.

    Solo los valores numéricos (int y float) que haya en `args` y `kwargs`
    serán tenidos en cuenta.

    :param operation: Puede ser ADD o AVG para sumar o hacer la media.
    :param args:      Lista variables de valores de todo tipo.
    :param kwargs:    Conjunto de calves-valor de todo tipo.

    :return: El resultado de la operación sobre los valores de `args` y
             `kwargs` si `operation` tiene un valor válido. En otro caso
             devolverá -1.
    """
    pass
