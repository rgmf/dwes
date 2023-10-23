from typing import Callable, Iterator
from urllib.parse import parse_qs


def app(environ: dict, start_response: Callable) -> Iterator:
    """Aplicación de ejemplo.

    La versión más simple con respuesta en formato HTML.

    :environ dict: diccionario que contiene las variables de entorno CGI así
                   como otros parámetros y metadatos.
    :start_response Callable: es una función ("Callable") que recibe dos
                              parámetros: el estado (status) y las cabeceras
                              de la respuesta (header response).

    :return: devuelve el cuerpo de la respuesta como un "Iterator" de bytes.
             Así, se devuelve el cuerpo como "byte" y no como "str".
    """

    # Parseamos el "query parameter"
    qs_dict: dict[str, list[str]] = parse_qs(environ["QUERY_STRING"])

    # Tenemos que obtener "num1" y "num2".
    # Ten en cuenta que en cada "query param" tenemos una lista, por eso cogemos el
    # primero de la lista.
    num1: int = int(qs_dict["num1"][0])
    num2: int = int(qs_dict["num2"][0])
    addition: int = num1 + num2

    # Los datos que voy a enviar en el cuerpo de la respuesta
    data: str = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sumando los Query Parameteres</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Suma de dos números</h1>
        <p>{num1} + {num2} = {addition}</p>
    </body>
    </html>
    """

    # Convertidos a bytes
    data_in_bytes: bytes = data.encode("utf-8")

    # Uso el Callable que me pasa WSGI para preparar el cuerpo de la respuesta:
    # - Código de estado 200 (HTTP)
    # - Cabeceras:
    #   - El tipo de contenido: en este caso HTML (text/html)
    #   - La longitud de los datos que vienen en el cuerpo
    start_response(
        "200 OK",
        [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data_in_bytes)))
        ]
    )

    # El cuerpo de la respuesta la envío como un Iterator
    return iter([data_in_bytes])
