from typing import Callable, Iterator
from urllib.parse import parse_qs


def get_html(num1: int, num2: int) -> str:
    addition: int = num1 + num2

    return f"""
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


def get_401() -> str:
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Petición no aceptada</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Bad Request - petición no aceptada</h1>
        <p>Se necesitan dos números por la query param: num1 y num2.</p>
    </body>
    </html>
    """


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

    qs_dict: dict[str, list[str]] = parse_qs(environ["QUERY_STRING"])

    if (
        "num1" in qs_dict and "num2" in qs_dict and
        qs_dict["num1"][0].isdigit() and qs_dict["num2"][0].isdigit()
    ):
        data: str = get_html(int(qs_dict["num1"][0]), int(qs_dict["num2"][0]))
        response_status: str = "200 OK"
    else:
        data: str = get_401()
        response_status: str = "401 BAD REQUEST"

    data_in_bytes: bytes = data.encode("utf-8")
    start_response(
        response_status,
        [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data_in_bytes)))
        ]
    )

    return iter([data_in_bytes])
