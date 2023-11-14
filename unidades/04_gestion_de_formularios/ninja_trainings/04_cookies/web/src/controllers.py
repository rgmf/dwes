from multipart import parse_form_data

from src.templates import render_template


def home(environ: dict[str, list[str]]) -> str:
    context: dict[str, str] = {
        "info": render_template("src/views/parts/who_are_you_link.html")
    }
    return render_template("src/views/index.html", context)


def yourname(environ: dict[str, list[str]], headers: list[tuple[str, str]]) -> str:
    method: str = environ.get("REQUEST_METHOD", "").upper()
    context: dict[str, str] = {
        "error": ""
    }

    if method != "POST":
        return render_template("src/views/yourname.html", context)

    form, files = parse_form_data(environ)
    name: str | None = validate_form(form)

    if not name:
        context["error"] = "Campo requerido"
        return render_template("src/views/yourname.html", context)

    return render_template("src/views/message.html", {"message": "Gracias ;)"})


def validate_form(form: dict[str, str]) -> str | None:
    if "name" not in form:
        return None

    # Limpiamos y validamos los campos (solo hay uno).
    # 1. Quitamos espacios extras delante y detrás.
    name = form["name"].strip()

    # 2. comprobar que no esté vacío y que no tenga espacios.
    if not name:
        return None

    # No hay errores, devolvemos el nombre.
    return name


def error404() -> str:
    return render_template("src/views/404.html")
