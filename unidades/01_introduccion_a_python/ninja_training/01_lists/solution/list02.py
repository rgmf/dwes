"""Colas (stack).

Toca, ahora, meterle mano a las colas en Python (stack). Recuerda que tienes
los métodos `append` y `pop` de las listas en Python para usar las listas como
si de colas se trataran.

Crea una cola vacía llamada `a_stack` y apila los strings (en este orden):
- "a".
- "A".
- "á".
- "Á".

Ahora, crea dos listas a partir de `a_stack` (`a_stack`, en ningún caso, debe
ser modificada):

- `ascending_list` con los elementos de `a_stack` en orden ascendente.

- `descending_list` con los elementos de `a_stack` en orden descendente.

Por último:

- Desapila de `a_stack` un elemento y guárdalo en `last_item`.
"""

a_stack: list[str] = []
a_stack.append("a")
a_stack.append("A")
a_stack.append("á")
a_stack.append("Á")

ascending_list: list[str] = sorted(a_stack)
descending_list: list[str] = sorted(a_stack, reverse=True)

last_item: str = a_stack.pop()
