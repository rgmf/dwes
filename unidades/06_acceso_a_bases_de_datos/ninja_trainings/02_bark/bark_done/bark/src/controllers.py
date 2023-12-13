from multipart import parse_form_data
from datetime import datetime, timezone

from src.templates import render_template
from src.forms.bark_form import BarkForm
from src.db.database import get_comments, insert_comment
from src.models.models import Comment, User


def home() -> str:
    comments: list[Comment] = get_comments()
    if comments:
        context: dict[str, str] = {
            "barks": "".join([comment.to_html() for comment in comments])
        }
    else:
        context: dict[str, str] = {
            "barks": "<p>No se escuchan ladridos...</p>"
        }
    return render_template("src/views/index.html", context)


def bark_form(environ: dict[str, list[str]]) -> str:
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
    bark_form: BarkForm = BarkForm(form)
    if bark_form.is_valid():
        user: User = User(bark_form.username)
        comment: Comment = Comment(
            comment=bark_form.comment,
            user=user,
            category=bark_form.category,
            posted=datetime.now(timezone.utc)
        )
        insert_comment(comment)
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
