"""namedtuples y bucles."""

from collections import namedtuple

Player = namedtuple("Player", ["name", "games", "points"])


# TODO A continuación tienes una lista de jugadores de baloncesto con sus
# estadísticas. De cada jugador, como ves arriba, conocemos su nombre (str),
# los partidos que ha jugado (int) y los puntos totales que ha metido (int).
#
# Escribe un programa que quite de la lista los jugadores que han metido
# menos de 20.0 puntos por partido. Como tienes los puntos totales y los
# partidos que ha jugado, para calcular los puntos por partido solo tienes
# que dividir: puntos / partidos.
#
# Por ejemplo, en la lista de abajo tiens un tal MJ que ha jugado 82 partidos
# y ha metido 2000 puntos, lo que hace un total de 2000 / 82 = 24.39 puntos por
# partido.
players: list[Player] = [
    Player("MJ", 82, 2000),
    Player("LJ", 80, 1880),
    Player("AI", 82, 2550),
    Player("KB", 82, 1500),
    Player("AE", 82, 1350),
    Player("CB", 75, 1500)
]
