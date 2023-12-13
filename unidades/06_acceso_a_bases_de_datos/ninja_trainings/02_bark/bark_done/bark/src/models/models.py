from datetime import datetime
from zoneinfo import ZoneInfo


class User:
    def __init__(self, username: str, id: int | None = None) -> None:
        self.__id: int | None = id
        self.__username: str = username

    @property
    def id(self) -> int | None:
        return self.__id

    @property
    def username(self) -> str:
        return self.__username

    def __str__(self) -> str:
        return f"User(id={self.__id}, username='{self.__username}')"

    def __repr__(self) -> str:
        return self.__str__()


class Comment:
    def __init__(
            self,
            user: User,
            comment: str,
            category: str,
            posted: datetime,
            id: int | None = None
    ) -> None:
        self.__id: int | None = id
        self.__user: User = user
        self.__comment: str = comment
        self.__category: str = category
        self.__posted: datetime = posted

    @property
    def id(self) -> int | None:
        return self.__id

    @property
    def user(self) -> User:
        return self.__user

    @property
    def comment(self) -> str:
        return self.__comment

    @property
    def category(self) -> str:
        return self.__category

    @property
    def posted(self) -> datetime:
        return self.__posted

    def __str__(self) -> str:
        return (
            f"Comment(id={self.__id}, user={str(self.__user)}, "
            f"comment='{self.__comment}', category='{self.__category}', "
            f"posted={self.__posted})"
        )

    def __repr__(self) -> str:
        return self.__str__()

    def to_html(self) -> str:
        zoneinfo_madrid: str = ZoneInfo("Europe/Madrid")
        dt_madrid: datetime = self.posted.astimezone(zoneinfo_madrid)
        dt_str: str = dt_madrid.strftime("%d de %B de %Y a las %H:%M:%S")
        return f"""
        <p>
        <small>Escrito por <strong>{self.user.username}</strong></small><br>
        <em>{self.comment}</em><br>
        <small>Publicado el {dt_str} ({self.category})</small>
        </p>
        """
