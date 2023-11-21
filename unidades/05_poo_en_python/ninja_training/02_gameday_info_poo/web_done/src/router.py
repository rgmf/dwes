from src.models.data import GAMEDAYS


def load_data() -> list[Gameday]:
    pass


def app(environ: dict[str, str], start_response: callable) -> iter:
    path: str = environ.get("PATH_INFO")
    gamedays: list[Gameday] = load_data()

    if path.endswith("/"):
        path = path[:-1]

    if path == "":
        data: str = gameday_list(gamedays)
    elif path == "/gameday":
        data: str = form_username(environ)
    else:
        data: str = error404()

    data: str = "TODO: todo por hacer"
    data_in_bytes: bytes = data.encode("utf-8")

    start_response(
        "200 OK",
        [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data_in_bytes)))
        ]
    )

    return iter([data_in_bytes])
