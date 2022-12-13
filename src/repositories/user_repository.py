from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    """Hakee käyttäjän.

    Args:
        row

    Returns:
        User: Haettu käyttäjä
    """

    return User(row["username"], row["password"]) if row else None


class UserRepository:
    """Luokka, joka vastaa käyttäjätietokannasta.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Connection-olio, joka kuvaa tietokantayhteyttä.
        """

        self._connection = connection

    def create_user(self, user):
        """Lisää uuden käyttäjän tietokantaan.

        Args:
            user (User): Tietokantaan lisättävä User-olio.

        Returns:
            User: Lisätty käyttäjä User-oliona.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'insert into users (username, password) values (?,?)',
            (user.username, user.password)
        )
        self._connection.commit()
        return user

    def find_by_username(self, username):
        """Hakee tietokannasta käyttäjän käyttäjänimen perusteella.

        Args:
            username (str): Annettu käyttäjänimi

        Returns:
            User: Haettu käyttäjä User-oliona.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'select * from users where username = ?',
            (username,)
        )
        result = cursor.fetchone()
        return get_user_by_row(result)

    def find_all(self):
        """Hakee tietokannasta kaikki käyttäjät.

        Returns:
            List: Lista kaikista käyttäjistä.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'select * from users'
        )
        result = cursor.fetchall()
        return list(map(get_user_by_row, result))

    def delete_all(self):
        """Tyhjentää koko käyttäjätietokannan.
        """

        cursor = self._connection.cursor()
        cursor.execute('delete from users')
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
