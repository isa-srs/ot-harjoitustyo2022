from entities.course import Course
from database_connection import get_database_connection


def get_course_by_row(row):
    """Hakee kurssin.

    Args:
        row

    Returns:
        Course: Haettu kurssi Course-oliona.
    """
    return Course(row["name"], row["credits"], row["user"]) if row else None


class CourseRepository:
    """Luokka, joka vastaa kurssitietokannasta.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyttä kuvaava Connection-olio.
        """

        self._connection = connection

    def add_course(self, course):
        """Lisää uuden kurssin tietokantaan.

        Args:
            course (Course): Tietokantaan lisättävä Course-olio.

        Returns:
            Course: Lisätty kurssi Course-oliona.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'insert into courses (name, credits, user) values (?,?,?)',
            (course.name, course.credits, course.user)
        )
        self._connection.commit()
        return course

    def find_courses_by_user(self, user):
        """Hakee kaikki yhden käyttäjän lisäämät kurssit.

        Args:
            user (str): Käyttäjän käyttäjänimi, jonka lisäämät kurssit haetaan.

        Returns:
            List: Lista käyttäjän lisäämistä kursseista.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'select * from courses where user=?', (user,)
        )
        courses = cursor.fetchall()
        return list(map(get_course_by_row, courses))

    def find_all(self):
        """Hakee tietokannasta kaikki kurssit.

        Returns:
            List: Lista kaikista kursseista.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'select * from courses'
        )
        result = cursor.fetchall()
        return list(map(get_course_by_row, result))

    def delete_all(self):
        """Tyhjentää koko kurssitietokannan.
        """

        cursor = self._connection.cursor()
        cursor.execute('delete from courses')
        self._connection.commit()

course_repository = CourseRepository(get_database_connection())
