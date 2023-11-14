from typing import Callable, Iterator

from src.controllers import home, form_contact, error404


def app(environ: dict, start_response: Callable) -> Iterator:
    path: str = environ.get("PATH_INFO")

    if path.endswith("/"):
        path = path[:-1]

    if path == "" or path == "/home":
        data: str = home()
    elif path == "/contact":
        data: str = form_contact(environ)
    else:
        data: str = error404()

    data_in_bytes: bytes = data.encode("utf-8")
    start_response(
        "200 OK",
        [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data_in_bytes)))
        ]
    )

    # El cuerpo de la respuesta la envío como un Iterator
    return iter([data_in_bytes])
