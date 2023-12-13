class BarkForm:
    def __init__(self, form: dict) -> None:
        self.username: str = form.get("username", "").strip()
        self.comment: str = form.get("comment", "").strip()
        self.category: str = form.get("category", "").strip()

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
