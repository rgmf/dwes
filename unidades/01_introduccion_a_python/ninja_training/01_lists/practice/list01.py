"""Introducción a las listas.

En este programa ya he inicializado una lista con 10 números aleatorios llamada
`random_numbers`. No te preocupes ahora mismo si no entiendes nada. Pronto
comprenderás cómo lo he hecho.

A partir de aquí, crea las siguientes listas:

- `l1` con el 4º elemento de `random_numbers`.

- `l2` con los primeros 4 números de la lista `random_numbers`.

- `l3` con los 3 últimos números de `random_numbers`.

- `l4` con los números que hay en las posiciones 2ª, 3ª y 4ª de
  `random_numbers`.

- `l5` con los números que hay en las posiciones impares de `random_numbers`.
"""
from random import randint


# Creamos una lista con 10 números aleatorios entre 0 y 100.
random_numbers: list[int] = [randint(0, 100) for _ in range(10)]
print(random_numbers)

l1: list[int] = [random_numbers[3]]

print(f"La lista l1: {l1}")