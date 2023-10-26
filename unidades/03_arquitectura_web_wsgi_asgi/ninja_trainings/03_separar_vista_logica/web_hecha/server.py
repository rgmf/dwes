from typing import Callable, Iterator
from urllib.parse import parse_qs


def app(environ: dict, start_response: Callable) -> Iterator:
    """Aplicación de ejemplo.

    La versión más simple con respuesta en texto plano.

    :environ dict: diccionario que contiene las variables de entorno CGI así
                   como otros parámetros y metadatos.
    :start_response Callable: es una función ("Callable") que recibe dos
                              parámetros: el estado (status) y las cabeceras
                              de la respuesta (header response).

    :return: devuelve el cuerpo de la respuesta como un "Iterator" de bytes.
             Así, se devuelve el cuerpo como "byte" y no como "str".
    """

    context: dict[str, str] = {
        "lang_list": "<ul><li>Python</li><li>Java</li><li>PHP</li></ul>"
    }
    html_str: str = ""
    query_param: dict[str, list[str]] = (
        parse_qs(environ["QUERY_STRING"]) if "QUERY_STRING" in environ else []
    )
    lang: str = query_param["lang"][0] if "lang" in query_param else "es"
    template: str = "views/english.html" if lang == "en" else "views/spanish.html"

    with open(template, "r") as file_object:
        html_str = file_object.read()

    html_str = html_str.format(**context)

    html_in_bytes: bytes = html_str.encode("utf-8")

    start_response(
        "200 OK",
        [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(html_in_bytes)))
        ]
    )

    # El cuerpo de la respuesta la envío como un Iterator
    return iter([html_in_bytes])
