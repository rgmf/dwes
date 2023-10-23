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

    # Recogemos el nombre si viene en los query params
    name: str | None = qs_dict["name"][0] if "name" in qs_dict else None

    if name is not None:
        # Los datos que voy a enviar en el cuerpo de la respuesta si hay nombre
        data: str = f"""
        <!DOCTYPE html>
        <html>
          <head>
            <title>Un saludo</title>
            <meta charset="utf-8">
          </head>
        <body>
          <h1>Bienvenid@ {name}</h1>
        </body>
        </html>
        """

        data_in_bytes: bytes = data.encode("utf-8")
        start_response(
            "200 OK",
            [
                ("Content-Type", "text/html"),
                ("Content-Length", str(len(data_in_bytes)))
            ]
        )
    else:
        # Bad Request (401) si no llega el nombre
        data: str = """
        <!DOCTYPE html>
        <html>
          <head>
            <title>401: Bad Request</title>
            <meta charset="utf-8">
          </head>
        <body>
          <h1>Error 401: Bad Request</h1>
          <p>Este recurso necesita el nombre como query parameter.</p>
        </body>
        </html>
        """

        data_in_bytes: bytes = data.encode("utf-8")
        start_response(
            "401 Bad Request",
            [
                ("Content-Type", "text/html"),
                ("Content-Length", str(len(data_in_bytes)))
            ]
        )

    # El cuerpo de la respuesta la envío como un Iterator
    return iter([data_in_bytes])
