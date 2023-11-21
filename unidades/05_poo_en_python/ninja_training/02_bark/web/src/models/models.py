class Comment:
    """Clase Comment.

    Esta clase tiene 4 atributos a saber:
    - username: un str con el nombre de usuario.
    - comment: un str con el comentario.
    - category: un str con la categoría.
    - posted: un datetime UTC con la fecha y hora del comentario.

    Crea el método __init__ y un método to_html que devuelva los valores del
    objeto para ser representado en formato HTML. Por ejemplo:

    <p>
      <small>Escrito por <strong>Alice</strong></small><br>
      <em>Parece que se ha quedado buen día</em><br>
      <small>Publicado el 21 de noviembre de 2023 a las 15:50 horas (weather)</small>
    </p>

    Evidentemente los valores del HTML de arriba dependerán de los valores de
    los atributos.

    Un datos importante: recuerda que la fecha está en UTC. A la hora de
    mostrarla en el HTML deberá aparecer en Europe/Madrid. Tienes el método
    astimezone al que le puedes pasar un ZoneInfo para mostrar la fecha y hora
    en esa zona horaria.
    """
    pass


class BarkForm:
    """Clase de utilidad para el formulario.

    Los atributos de este clase serán:
    - username: un str con el nombre de usuario.
    - comment: un str con el comentario.
    - category: un str con la categoría.

    Crea el método __init__ y los siguientes métodos (a parte de todos estos
    métodos puedes crear todos los métodos auxiliares que quieras pero tendrán
    que ser privados, nombre que comiencen por __):

    - is_valid: método que no recibe nada y devuelve un booleano indicando si
                los atributos de la clase contienen valores válidos. Un
                formulario es válido si:
                - El username no es vacío y no tiene espacios.
                - El comment no es vacío.
                - La categoría no es vacía.

    - get_context: método que no recibe nada y devuelve un diccionario con el
                   contexto que se pasará a la vista src/views/bark_form.html:
                   - username: el valor del atributo username.
                   - username_error: descripción del error en el atributo
                                     username o cadena vacía si no hay error.
                   - comment: el valor del atributo comment.
                   - comment_error: descripción del error en el atributo
                                    comment o cadena vacía si no hay error.

    - get_cookie: devuelve una tupla cuyo primer elemento será "Set-Cookie" y
                  el segundo elemento el valor de la cookie en formato:
                  <comentario>|<categoría>|<fecha de ahora en UTC>

                  Estos tres valores tendrás que coficiarlos con método quote
                  de la biblioteca urllib.parse.

                  Un ejemplo de tupla devuelta (datos ficticios, con fecha
                  acortada):

                  ("Set-Cookie", "Alice|Mi%20comentario|weather|2023-11-21")

    NOTA: ojo con los espacios delante y detrás de los str. Límpialos con un
    strip, ya que estos valores llegan del formulario rellenado por el usuario.
    """
    pass
