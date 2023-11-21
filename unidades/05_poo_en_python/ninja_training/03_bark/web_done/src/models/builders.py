from datetime import datetime
from http.cookies import SimpleCookie
from urllib.parse import unquote

from src.models.models import Comment, BarkForm


def build_comments(http_cookies: dict) -> list[Comment]:
    comments: list[Comment] = []
    cookies: SimpleCookie = SimpleCookie()
    cookies.load(http_cookies)

    for username, morsel in cookies.items():
        comment, category, posted_dt = morsel.value.split("|")
        comments.append(
            Comment(
                username=username,
                comment=unquote(comment),
                category=unquote(category),
                posted=datetime.fromisoformat(unquote(posted_dt))
            )
        )

    return comments


def build_bark_form(form: dict[str, str]) -> BarkForm:
    return BarkForm(
        username=form["username"] if "username" in form else "",
        comment=form["comment"] if "comment" in form else "",
        category=form["category"] if "category" in form else "",
    )

# # Codificar un valor de cookie con espacios
# original_cookie_value = "mi valor con espacios"
# encoded_cookie_value = quote(original_cookie_value)
# print(f"Original: {original_cookie_value}")
# print(f"Codificado: {encoded_cookie_value}")

# # Decodificar el valor de la cookie
# decoded_cookie_value = unquote(encoded_cookie_value)
# print(f"Decodificado: {decoded_cookie_value}")

# # Crear un objeto SimpleCookie
# cookie = SimpleCookie()

# # Establecer un valor con espacios
# cookie["mi_cookie"] = "mi valor con espacios"

# # Obtener el valor codificado
# encoded_value = cookie["mi_cookie"].value_encode()[1]
# print(f"Valor codificado: {encoded_value}")

# # Decodificar el valor
# decoded_value = SimpleCookie.value_decode(encoded_value)
# print(f"Valor decodificado: {decoded_value}")
