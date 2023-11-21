from multipart import parse_form_data

from src.templates import render_template
from src.models.builders import build_bark_form
from src.models.models import Comment, BarkForm


def home(comments: list[Comment]) -> str:
    if comments:
        context: dict[str, str] = {
            "barks": "".join([comment.to_html() for comment in comments])
        }
    else:
        context: dict[str, str] = {
            "barks": "<p>No se escuchan ladridos...</p>"
        }
    return render_template("src/views/index.html", context)


def bark_form(environ: dict[str, list[str]], headers: list[tuple[str, str]]) -> str:
    method: str = environ.get("REQUEST_METHOD", "").upper()

    if method != "POST":
        return render_template(
            "src/views/bark_form.html",
            {
                "username": "",
                "username_error": "",
                "comment": "",
                "comment_error": ""
            }
        )

    form, _ = parse_form_data(environ)
    bark_form: BarkForm = build_bark_form(form)
    if bark_form.is_valid():
        headers.append(bark_form.get_cookie())
        return render_template(
            "src/views/message.html",
            {"message": "Comentario enviado correctamente"}
        )
    else:
        return render_template(
            "src/views/bark_form.html",
            bark_form.get_context()
        )


def error404() -> str:
    return render_template("src/views/404.html")
