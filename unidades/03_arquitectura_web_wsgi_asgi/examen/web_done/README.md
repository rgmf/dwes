# Antes de comenzar
Estos son los requisitos generales que debes cumplir:

- Usar las PEP-8 cuando escribas tu código en Python y las anotaciones de tipo (o *type hints*).
- Los ficheros HTML no se modificarán, a menos que se diga lo contrario.
- Si en el enunciado se indica, explícitamente, que se modifique un HTML, se hará siguiendo escrupulosamente este enunciado.
- Lo que sí puedes hacer es crear todos los ficheros HTML que creas necesario.
- No dejes `print`s en tu código y asegúrate que, antes de entregar, eliminas todo código que uses a modo de depuración y prueba.
- Todo código sospechoso de haber sido copiado/pegado, "chatgpteado", etc, llevará al alumnado al procedimiento de "prueba de autenticidad".
- Si tienes que manejar *Query Parameters* tendrás que asegurarte que los valores que llegan son válidos. En otro caso envía un error o página 404.

# Descripción
En este examen vas a completar la práctica de las quinielas aleatorias añadiendo nuevos recursos o *paths* que te explico en los siguientes apartados.

Antes de que pases a dichos apartados, algo importante:
- Los HTML que tienes que generar no tienen porque seguir ningún estilo, puede ser HTML sin más, sin CSS.
- Puedes o no incluir el menú de navegación en las páginas HTML que vas a crear.
- De todos modos, si quieres añadir el menú de navegación, es muy fácil: fíjate en cómo lo he hecho en el controlador `home` que tienes en `controller.py`.

## `/about` - 2 puntos
Añade esta ruta al menú principal de navegación que está en `views/parts/nav.html`.

Cuando un usuario solicite este recurso se le entregará una página web HTML en la que aparecerá tu nombre dentro de un `<h1>`.

## `/teams` - 2 puntos
Añade esta ruta al menú principal de navegación que está en `views/parts/nav.html`.

Cuando un usuario solicite este recurso se el entregará una página web HTML en al que aparezca un listado con todos los equipos que puedes encontrar en la lista `GAMEDAYS`, dentro del fichero `models/data.py`. Tienes que averiguar, por tanto, cómo obtener los equipos que hay en esa lista.

Ten en cuenta que el número de equipos podría disminuir o crecer. Es decir, busca los equipos de forma general ya que el contenido de `GAMEDAYS` podría ser diferente aunque la estructura no cambie.

Pista: para extraer todos los equipos basta con irte a una jornada concreta y sacarlos de ahí. Aunque lo puedes hacer como quieras... siempre que funcione... estará bien.

Por último, en este listado se tendrá un enlace que te lleve al siguiente *path*.

## `/teams/?name=<nombre del equipo>` - 4 puntos
Si el usuario hace clic en uno de los equipos del apartado anterior se solicitará este recurso donde se devolverá una página web HTML con todos los partidos de la temporada (de todas las jornadas) de ese equipo concreto.

Si el equipo indicado no existe se tendrá que devolver un **Error 404** (la página `404.html` ya está escrita).

## `/scoreboard/?name=<nombre del equipo>&gameday=<número de jornada> - 2 puntos
Añade, en la lista de equipos, un enlace adicional para solicitar este recurso en el que tendrás que devolver una página web HTML que indique los puntos que tiene ese equipo en la jornada indicada.

Sabes los resultados de todas las jornadas porque los tienes en la lista `SCOREBOARDS` dentro de `models/data.py`.

Como antes, si algún *Query Parameter* no es correcto devuelve un **Error 404**.
