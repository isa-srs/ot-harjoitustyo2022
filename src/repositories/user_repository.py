from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute(
            'insert into users (username, password) values (?,?)',
            (user.username, user.password)
        )
        self._connection.commit()
        return user

    def find_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from users where username = ?',
            (username,)
        )
        result = cursor.fetchone()
        return get_user_by_row(result)

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from users'
        )
        result = cursor.fetchall()
        return list(map(get_user_by_row, result))


user_repository = UserRepository(get_database_connection())
