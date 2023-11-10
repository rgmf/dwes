from src.controller import (
    home,
    gamedays,
    random_bet_list,
    random_bet_list_checking,
    about,
    teams,
    error404
)


def app(environ: dict[str, str], start_response: callable) -> iter:
    path: str = environ.get("PATH_INFO")
    http_result: str = "200 OK"

    if path.endswith("/"):
        path = path[:-1]

    if path == "" or path == "/home":
        data: str = home()
    elif path == "/about":
        data: str = about()
    elif path == "/gamedays":
        data: str = gamedays(environ)
    elif path == "/randombetlist":
        data: str = random_bet_list(environ)
    elif path == "/randombetlist/check":
        data: str = random_bet_list_checking(environ)
    elif path == "/teams":
        data: str = teams(environ)
    else:
        http_result = "404 NOT FOUND"
        data: str = error404()

    data_in_bytes: bytes = data.encode("utf-8")

    start_response(
        http_result,
        [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data_in_bytes)))
        ]
    )

    return iter([data_in_bytes])
