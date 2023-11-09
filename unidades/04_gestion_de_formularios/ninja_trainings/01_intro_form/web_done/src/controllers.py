from urllib.parse import parse_qs

from multipart import parse_form_data

from src.templates import render_template


def home() -> str:
    return render_template("src/views/index.html")


def form_contact(environ: dict[str, list[str]]) -> str:
    # Método por el que nos han enviado el formulario.
    method: str = environ.get("REQUEST_METHOD", "").upper()

    # Dependiendo del método se tiene que procesar de una manera u otra.
    if method == "GET":
        return compute_get_form(environ)
    elif method == "POST":
        return compute_post_form(environ)
    else:
        return render_template("src/views/404.html")


def compute_get_form(environ: dict[str, list[str]]) -> str:
    # Obtenemos el query string y lo transformamos en un dict[str, str].
    qs: dict[str, list[str]] = parse_qs(environ["QUERY_STRING"])
    form: dict[str, str] = {key: value[0] for key, value in qs.items()}

    # Si faltan campos hay que completar el diccionario con valores vacíos.
    for name in ["username", "password", "email", "birthdate", "comment"]:
        if name not in form:
            form[name] = ""

    # Volvemos al formulario pasándole los valores.
    return render_template("src/views/form_contact.html", form)


def compute_post_form(environ: dict[str, list[str]]) -> str:
    # Obtenemos el formulario (y los ficheros que vamos a ignorar) por medio de
    # la biblioteca multipart de Python.
    form, files = parse_form_data(environ)

    # Si faltan campos hay que completar el diccionario con valores vacíos.
    for name in ["username", "password", "email", "birthdate", "comment"]:
        if name not in form:
            form[name] = ""

    # Volvemos al formulario pasándole los valores.
    return render_template("src/views/form_contact.html", form)


def error404() -> str:
    return render_template("src/views/404.html")
