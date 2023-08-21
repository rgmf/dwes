# Imagina un juego 2D en el que se va a trabajar con puntos en un espacio
# bidimensional. Se usarán constantemente puntos de coordenada (x, y).
# Podemos crear estos puntos como tuplas.
p1: tuple[int] = (3, 4)
p2: tuple[int] = (7, 9)

# Aquí surge una duda: de los dos elementos de las tuplas `p1` y `p2`, ¿cuál es
# la coordenada `x` y cuál es la coordenada `y`? El primer elemento de la
# tupla, ¿es `x`?
print(f"p1: creo que x={p1[0]}")

# En escenarios como este, la mejor opción es usar namedtuple para eliminar la
# ambigüedad.
#
# Primero, hay que importar el módulo
from collections import namedtuple

# Segundo, creamos el tipo.
Point = namedtuple("Point", ["x", "y"])

# Tercero, creamos los puntos de dicho tipo.
p1 = Point(3, 4)
p2 = Point(7, 9)

# Cuarto, usamos las variables que son objetos.
print(f"p1: ahora sí, estoy seguro que x={p1.x}")

# Mejor: si vamos a tener una lista de puntos.
points: list[Point] = [
    Point(3, 4),
    Point(7, 9),
    Point(1, 10),
    Point(4, 8)
]

print(f"Coordenada x del último punto: {points[-1].x}")
