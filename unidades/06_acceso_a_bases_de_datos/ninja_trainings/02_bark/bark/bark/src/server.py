from typing import Callable, Iterator

from src.controllers import home, bark_form, error404


def app(environ: dict, start_response: Callable) -> Iterator:
    path: str = environ.get("PATH_INFO")
    headers: list[tuple[str, str]] = [
        ("Content-Type", "text/html")
    ]

    if path.endswith("/"):
        path = path[:-1]

    if path == "":
        data: str = home()
    elif path == "/bark":
        data: str = bark_form(environ)
    else:
        data: str = error404()

    data_in_bytes: bytes = data.encode("utf-8")
    headers.append(("Content-Length", str(len(data_in_bytes))))
    start_response("200 OK", headers)

    return iter([data_in_bytes])
