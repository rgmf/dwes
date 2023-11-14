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
        # Obtenemos el query string y lo transformamos en un dict[str, str].
        qs: dict[str, list[str]] = parse_qs(
            environ["QUERY_STRING"],
            keep_blank_values=True
        )
        form: dict[str, str] = {key: value[0] for key, value in qs.items()}
        return compute_form(form)
    elif method == "POST":
        # Obtenemos el formulario (y los ficheros que vamos a ignorar) por
        # medio de la biblioteca multipart de Python.
        form, files = parse_form_data(environ)
        return compute_form(form)
    else:
        return render_template("src/views/404.html")


def compute_form(form: dict[str, str]) -> str:
    all_fields: list[str] = ["username", "password", "email", "birthdate", "comment"]

    # Si faltan campos hay que enviar el formulario vacío porque "algo raro"
    # ha pasado o es la primera vez que se solcita el formulario.
    # Así pues, lo enviamos vacío.
    if len(form) < len(all_fields) or not all(key in form for key in all_fields):
        return render_template(
            "src/views/form_contact.html",
            {
                "username": "",
                "password": "",
                "email": "",
                "birthdate": "",
                "comment": "",

                "username_error": "",
                "password_error": "",
                "email_error": "",
                "birthdate_error": "",
                "comment_error": ""
            }
        )

    errors: int = 0

    # Limpiamos y validamos los campos.
    for name in all_fields:
        # 1. Quitamos espacios extras delante y detrás.
        form[name] = form[name].strip()

        # 2. comprobar que no esté vacío.
        if not form[name]:
            form[name + "_error"] = "Campo obligatorio"
            errors += 1
        else:
            form[name + "_error"] = ""

    if errors == 0:
        # Si no hay errores => se ha enviado el formulario correctamente.
        return render_template(
            "src/views/message.html",
            {"message": "Formulario enviado correctamente"}
        )
    else:
        # Si hay errores => volvemos al formulario pasándole los valores.
        return render_template("src/views/form_contact.html", form)


def error404() -> str:
    return render_template("src/views/404.html")
