from src.models.models import Comment, BarkForm


def build_comments(http_cookies: dict) -> list[Comment]:
    """Construye una lista de Comment.

    Esta función recibe un diccionario con las cookies y de ahí construye los
    comentarios (lista de objetos Comment).

    Cada cookie tiene esta forma:
    <nombre de la cookie>=<valor de la cookie>

    A su vez, el nombre de la cookie coincide con el username del usuario que
    escribió el comentario. El valor de la cookie codifica: el comentario,
    la categoría y la fecha en que se escribió en formato ISO-8601 (string).

    Cada parte está separada por el carácter "|". Por ejemplo:

    alice=Pues%20se%20ha%20quedado%20buen%20d%C3%ADa|weather|2023-11-21T15%3A05%3A46.143220%2B00%3A00

    Donde, como ves, los valores están codificados para que no aparezcan
    espacios ni caracteres prohibidos en las cookies. En cualquier caso, una
    vez decodificado, estos serían los valores:
    - alice: nombre de la cookie que coincide con el nombre de usuario.
    - Pues se ha quedado buen día: es el comentario.
    - weather: es la categoría.
    - 2023-11-21T15:05:46.143220-00:00: es la fecha en formato ISO-8601.

    Para extraer los valores que hay en la cookie usa el método split("|") de
    los str de Python. Para decodificar cada una de las partes usa la función
    unquote de urllib.parse.

    Por último, para crear un objeto datetime a partir de un str con la fecha
    en formato ISO-8601 usa datetime.fromisoformat.
    """
    pass


def build_bark_form(form: dict[str, str]) -> BarkForm:
    """Construye un objeto de la clase BarkForm.

    Esta función recibe un diccionario con los datos del formulario HTML:
    - Las claves del diccionario son los valores del name del HTML.
    - Los valores del diccionario son los valores que el usuario ha escrito en
      ese campo.

    Si no llega alguno de los campos en este diccionario, toma la cadena
    vacía como valor por defecto.

    Te recuerdo que en el formulario hay tres campos:
    - username
    - comment
    - category
    """
    pass
