"""Introducción a las listas en Python.

Escribe, aquí debajo, un programa en Python que cree un string llamado `text`
con un string a tu elección como, por ejemplo: "Introducción a Python".

A partir de aquí, tienes que hacer lo siguiente:

- Guarda en una variable llamada `first_letter` la letra más pequeña de `text`
  (en orden alfabético de menor a mayor).

- Guarda en una variable llamada `second_letter` la segunda letra más pequeña
  de `text`.

- Construye una lista llamada `letters` con las dos primeras letras.

- Construye una lista llamada `others` que contenga el resto de letras en orden
  de menor a mayor.
"""
text: str = "Introducción a Python"
sorted_text: str = sorted(text)
first_letter, second_letter, *others = sorted_text

two_first_letters: list[str] = [first_letter, second_letter]
