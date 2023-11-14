from typing import Callable, Iterator

from src.controllers import home, yourname, error404


def app(environ: dict, start_response: Callable) -> Iterator:
    path: str = environ.get("PATH_INFO")
    headers: list[tuple[str, str]] = [
        ("Content-Type", "text/html")
    ]

    if path.endswith("/"):
        path = path[:-1]

    if path == "" or path == "/home":
        data: str = home(environ)
    elif path == "/yourname":
        data: str = yourname(environ, headers)
    else:
        data: str = error404()

    data_in_bytes: bytes = data.encode("utf-8")
    headers.append(("Content-Length", str(len(data_in_bytes))))
    start_response("200 OK", headers)

    return iter([data_in_bytes])
