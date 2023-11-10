from src.templates import render_template


def home() -> str:
    return render_template("src/views/index.html")


def form_contact(environ: dict[str, list[str]]) -> str:
    return render_template("src/views/form_contact.html")


def error404() -> str:
    return render_template("src/views/404.html")
