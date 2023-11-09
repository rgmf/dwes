from src.templates import render_template


def home() -> str:
    return render_template("src/views/index.html")


def form_contact(environ: dict[str, list[str]]) -> str:
    # TODO por hacer.
    return "Este controlador está por hacer."


def error404() -> str:
    return render_template("src/views/404.html")
