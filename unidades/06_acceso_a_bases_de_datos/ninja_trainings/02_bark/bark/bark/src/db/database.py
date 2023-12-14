import logging
from src.models.models import Comment

logging.basicConfig(level=logging.DEBUG)


def get_comments() -> list[Comment]:
    """TODO

    Esta función tiene que devolver una lista de objetos de la clase Comment.

    Fíjate en la clase Comment, especialmente en los atributos que necesita
    para ser construido. Especial atención merece el hecho de que tiene un
    atributo llamado user que es del tipo User.

    Para obtener los comentarios de la base de datos y generar la lista de
    los mismos, solo necesitas una select en la que unas información de los
    comentarios y los usuarios.

    Tendrás que proyectar los atributos necesarios para poder construir los
    objetos Comment que contengan el User.

    Recuerd además que: la fecha (posted) está almacenada como varchar en
    MariaDB y con eso tienes que construir el datetime de Python. Te recuerdo
    cómo:

    zone_info: ZoneInfo = ZoneInfo("Europe/Madrid")
    posted: datetime = datetime.fromisoformat(dt_str).astimezone(zone_info)

    En última instancia, no dudes en mirar el resultado, echarle un vistazo
    y volver a tu código para completarlo.

    Te he puesto, como ves, el código básico con el try-except y el mensaje
    al sistema de logs si hay error.

    Completa el resto del código.
    """
    result: list[Comment] = []

    try:
        # TODO: aquí debe ir todo tu código.
        pass
    except Exception as e:
        logging.error("Error base de datos: " + str(e))

    return result


def insert_comment(comment: Comment) -> bool:
    """TODO

    Esta función tiene que insertar en la base de datos el comentario que se
    recibe.

    Este comentario trae consigo al usuario que lo escribió.

    En MariaDB, en la tabla comentario, user es una clave ajena donde tienes
    que almacenar el id del usuario.

    Esto significa que tendrás que verificar si el usuario que escribió el
    comentario está ya en la base de datos para coger su id (SELECT users) y si
    no está el usuario entonces tendrás que insertarlo (INSERT INTO users).

    En ambos casos te tienes que hacer con el id del usuario para poder,
    finalmente, insertar el comentario (INSERT comments).

    Recuerda crear el cursor con el parámetro buffered igual a True porque vas
    a tener que usar el mismo cursor para varias queries.

    Recuerda hacer un commit por cada insert que ejecutes.

    Echa un vistazo a la solución si lo necesitas, analízalo, vuelve a tu código
    y acábalo. En ningún caso copies y pegues.

    Esta función devolverá True o False si se pudo o no hacer el insert.

    Esta podría ser una manera de devolver True o False, comprobando si se
    insertó o no el comentario:

    return cursor.rowcount == 1

    Evidentemente, si salta al except deberá devolver False. Eso ya te lo doy
    hecho.
    """
    try:
        pass
    except Exception as e:
        logging.error("Error base de datos: " + str(e))
    return False
