# Descripción del Ninja Training
En este Ninja Training tienes que hacer una aplicación web con las siguientes rutas o *paths*:

- `/`: ruta para la página principal, donde aparecerá el listado de las jornadas y, al lado, si se ha jugado o no.

- `/?gameday=<número de jornada>`: ruta en la que se mostrarán los partidos de esa jornada (y los resultados si los tiene).

Eso sí, a los controladores, le vas a pasar un objeto con la información que precisan. Así, antes de hacer nada, tendrás que convertir el famoso `GAMEDAYS` a objetos. Para ello, tendrás que crear las siguientes clases:

## `Gameday`
Representa una jornada con estos atributos:

- `gameday`: número de jornada (`int`).
- `was_played`: un booleano que indica si se ha jugado o no esa jornada.
- `games`: será una lista de objetos del tipo `Game` (ver apartado siguiente).

## `Game`
Representa un partido.

Los atributos de esa clase son:

- `team1`: equipo local (`str`).
- `team2`: equipo visitante (`str`).
- `result`: atributo de tipo `Result` (ver debajo) que podrá ser `None` si no se ha jugado este partido.

## `Result`
Representa un resultado.

- `goals1`: número de goles del equipo local (`int`).
- `goals2`: número de goles del equipo visitante (`int`).
