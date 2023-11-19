def app(environ: dict[str, str], start_response: callable) -> iter:
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
