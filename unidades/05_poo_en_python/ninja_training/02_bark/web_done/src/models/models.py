from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from urllib.parse import quote


class Comment:
    def __init__(self, username: str, comment: str, category: str, posted: datetime) -> None:
        self.username: str = username
        self.comment: str = comment
        self.category: str = category
        self.posted: datetime = posted

    def to_html(self) -> str:
        zoneinfo_madrid: str = ZoneInfo("Europe/Madrid")
        dt_madrid: datetime = self.posted.astimezone(zoneinfo_madrid)
        dt_str: str = dt_madrid.strftime("%d de %B de %Y a las %H:%M:%S")
        return f"""
        <p>
        <small>Escrito por <strong>{self.username}</strong></small><br>
        <em>{self.comment}</em><br>
        <small>Publicado el {dt_str} ({self.category})</small>
        </p>
        """


class BarkForm:
    def __init__(self, username: str, comment: str, category: str) -> None:
        self.username: str = username.strip()
        self.comment: str = comment.strip()
        self.category: str = category.strip()

    def __get_username_error(self) -> str:
        if not self.username:
            return "El nombre de usuario es obligatorio"
        if " " in self.username:
            return "El nombre de usuario no puede tener espacios"
        return ""

    def __get_comment_error(self) -> str:
        if not self.username:
            return "El comentario es obligatorio"
        return ""

    def is_valid(self) -> bool:
        if not self.username or " " in self.username:
            return False
        if not self.comment:
            return False
        if not self.category:
            return False
        return True

    def get_context(self) -> dict[str, str]:
        return {
            "username": self.username,
            "username_error": self.__get_username_error(),
            "comment": self.comment,
            "comment_error": self.__get_comment_error()
        }

    def get_cookie(self) -> tuple[str, str]:
        comment_enc: str = quote(self.comment)
        category_enc: str = quote(self.category)
        dtnow_enc: str = quote(datetime.now(timezone.utc).isoformat())
        return (
            "Set-Cookie",
            f"{self.username}={comment_enc}|{category_enc}|{dtnow_enc}"
        )
