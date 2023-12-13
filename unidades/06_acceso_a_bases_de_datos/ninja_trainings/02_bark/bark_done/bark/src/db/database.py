from mysql.connector import connect
from datetime import datetime
from zoneinfo import ZoneInfo

from src.models.models import Comment


def get_comments() -> list[Comment]:
    result: list[Comment] = []
    zone_info: ZoneInfo = ZoneInfo("Europe/Madrid")

    try:
        with connect(
                host="db", user="dwes", password="dwes", database="dwesdb"
        ) as conn:
            with conn.cursor() as cursor:
                sql = """
                select u.id, u.username, u.comment, u.category, u.posted
                from comment c, user
                where c.user = user.id
                order by posted
                """
                for t in cursor.execute(sql):
                    result.append(
                        Comment(
                            id=t[0],
                            user=t[1],
                            comment=t[2],
                            category=t[3],
                            poted=datetime.fromisoformat(t[4]).astimezone(zone_info)
                        )
                    )
    except Exception as e:
        print("Error base de datos: " + str(e))

    return result


def insert_comment(comment: Comment) -> bool:
    return False
