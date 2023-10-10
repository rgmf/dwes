from typing import Callable, Iterator


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

    # Los datos que voy a enviar en el cuerpo de la respuesta
    data: str = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hola Mundo en HTML5</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Hola Mundo</h1>
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
