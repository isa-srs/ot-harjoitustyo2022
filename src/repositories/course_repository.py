from entities.course import Course
from database_connection import get_database_connection


def get_course_by_row(row):
    """Hakee kurssin.

    Args:
        row

    Returns:
        Course: Haettu kurssi Course-oliona.
    """
    return Course(row["name"], row["credit"], row["grade"], row["user"]) if row else None


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
            'insert into courses (name, credit, grade, user) values (?,?,?,?)',
            (course.name, course.credit, course.grade, course.user)
        )
        self._connection.commit()
        return course

    def get_current_course(self, course):
        """Hakee kurssin, jolle ollaan merkitsemässä arvosanaa. Arvo aina None, paitsi ollessa set_grade-näkymässä.

        Args:
            course (str): Course-oliosta poimittu kurssin nimi

        Returns:
            course.name (str): Löydetyn kurssin nimi
        """
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from courses where name=?', (course,)
        )
        course = cursor.fetchone()
        return course.name

    def set_course_completed(self, course, grade):
        """Merkitsee kurssin suoritetuksi eli muuttaa sen arvosanan joksikin muuksi kuin nollaksi (0).

        Args:
            course (str): Course-oliosta poimittu kurssin nimi
            grade (str): Käyttäjän syöttämä arvosana
        """
        cursor = self._connection.cursor()
        cursor.execute(
            'update courses set grade = ? where name=?', (grade, course,)
        )
        self._connection.commit()

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

    def find_not_completed_courses_by_user(self, user):
        """Hakee kaikki kesken olevat kurssit käyttäjänimen perusteella

        Args:
            user (str): Käyttäjänimi, jonka kurssit halutaan hakea

        Returns:
            List: Lista löydetyistä kursseista
        """
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from courses where user=? and grade=0', (user,)
        )
        courses = cursor.fetchall()
        return list(map(get_course_by_row, courses))

    def find_completed_courses_by_user(self, user):
        """Hakee kaikki suoritetut kurssit käyttäjänimen perusteella.

        Args:
            user (str): Käyttäjänimi, jonka kurssit halutaan hakea

        Returns:
            List: Lista löydetyistä kursseista
        """
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from courses where user=? and grade>0', (user,)
        )
        courses = cursor.fetchall()
        return list(map(get_course_by_row, courses))

    def delete_course(self, name):
        """Poistaa valitun kurssin tietokannasta.

        Args:
            name (str): Poistettavan kurssin nimi.
        """

        cursor = self._connection.cursor()
        cursor.execute('delete from courses where name=?', (name,)
        )
        self._connection.commit()

    def delete_all(self):
        """Tyhjentää koko kurssitietokannan.
        """

        cursor = self._connection.cursor()
        cursor.execute('delete from courses')
        self._connection.commit()

course_repository = CourseRepository(get_database_connection())
