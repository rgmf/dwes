from src.templates import render_template


def home() -> str:
    return render_template("src/views/index.html")


def error404() -> str:
    return render_template("src/views/404.html")


def form_username(environ: dict[str, list[str]]) -> str:
    # TODO Controlador a completar
    return "Está por hacer"
