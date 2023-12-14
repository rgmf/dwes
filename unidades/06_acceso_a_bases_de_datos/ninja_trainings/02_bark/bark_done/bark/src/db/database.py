import logging
from mysql.connector import connect
from datetime import datetime
from zoneinfo import ZoneInfo

from src.models.models import Comment, User

logging.basicConfig(level=logging.DEBUG)


def get_comments() -> list[Comment]:
    result: list[Comment] = []
    zone_info: ZoneInfo = ZoneInfo("Europe/Madrid")

    try:
        with connect(
                host="db", user="dwes", password="dwes", database="dwesdb"
        ) as conn:
            with conn.cursor() as cursor:
                sql = """
                select c.id, u.id, u.username, c.comment, c.category, c.posted
                from comments c, users u
                where c.user = u.id
                order by posted
                """
                cursor.execute(sql)
                for t in cursor.fetchall():
                    posted: datetime = datetime.fromisoformat(t[5]).astimezone(zone_info)
                    user: User = User(id=t[1], username=t[2])
                    comment: Comment = Comment(
                        id=t[0],
                        user=user,
                        comment=t[3],
                        category=t[4],
                        posted=posted
                    )
                    result.append(comment)
    except Exception as e:
        logging.error("Error base de datos: " + str(e))

    return result


def insert_comment(comment: Comment) -> bool:
    try:
        with connect(
                host="db", user="dwes", password="dwes", database="dwesdb"
        ) as conn:
            with conn.cursor(buffered=True) as cursor:
                sql = "select id from users where username=%s"
                values = (comment.user.username,)
                user_id = None

                cursor.execute(sql, values)
                result = cursor.fetchone()
                if not result:
                    sql = "insert into users (username) values (%s)"
                    values = (comment.user.username,)

                    cursor.execute(sql, values)
                    conn.commit()

                    user_id = cursor.lastrowid
                else:
                    user_id = result[0]

                sql = """
                insert into comments (user, comment, category, posted)
                values (%s, %s, %s, %s)
                """
                values = (
                    user_id,
                    comment.comment,
                    comment.category,
                    comment.posted.isoformat()
                )
                cursor.execute(sql, values)
                conn.commit()

                return cursor.rowcount == 1
    except Exception as e:
        logging.error("Error base de datos: " + str(e))
    return False
