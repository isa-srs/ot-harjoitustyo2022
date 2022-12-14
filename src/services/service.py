from entities.user import User
from entities.course import Course

from repositories.user_repository import (
    user_repository as default_user_repository
)
from repositories.course_repository import (
    course_repository as default_course_repository
)


class InvalidCredentialsError(Exception):
    """Luokka, joka nostaa virheen, kun annettu käyttäjä tai salasana on väärin tai liian lyhyt.

    Args:
        Exception
    """


class UsernameExistsError(Exception):
    """Luokka, joka nostaa virheen, kun yritetään rekisteröityä varatulla käyttäjänimellä.

    Args:
        Exception
    """


class AppService:
    """Luokka, joka vastaa sovelluslogiikasta.
    """

    def __init__(self,
        user_repository=default_user_repository,
        course_repository=default_course_repository):
        """Luokan konstruktori, alustaa uuden palvelun.

        Args:
            user_repository:
                Vapaaehtoinen, oletusarvoltaan UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
            course_repository:
                Vapaaehtoinen, oletusarvoltaan CourseRepository-olio.
                Olio, jolla on CourseRepository-luokkaa vastaavat metodit.
        """

        self._user = None
        self._course = None
        self._user_repository = user_repository
        self._course_repository = course_repository

    def create_user(self, username, password):
        """Luo uuden käyttäjän.

        Args:
            username (str): Käyttäjänimi
            password (str): Salasana

        Raises:
            UsernameExistsError: Virhe, joka tulee, jos annettu käyttäjänimi on jo käytössä.

        Returns:
            User: Luotu käyttäjä User-oliona.
        """

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(
                f"Käyttäjänimi {username} on jo käytössä")

        user = self._user_repository.create_user(User(username, password))

        return user

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username (str): Käyttäjänimi
            password (str): Salasana

        Raises:
            InvalidCredentialsError: Virhe, joka tulee, jos käyttäjänimi tai salasana ei täsmää.

        Returns:
            User: Kirjautunut käyttäjä User-oliona.
        """

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError(
                "Käyttäjänimi tai salasana ei täsmää")

        self._user = user

        return user

    def logout(self):
        """Kirjaa käyttäjän ulos.
        """

        self._user = None

    def get_all_users(self):
        """Hakee tietokannasta kaikki käyttäjät.

        Returns:
            List: Lista kaikista olemassa olevista käyttäjistä.
        """

        return self._user_repository.find_all()

    def get_current_user(self):
        """Hakee tietokannasta sillä hetkellä kirjautuneen käyttäjän.

        Returns:
            User: Kirjautunut käyttäjä User-oliona.
        """

        return self._user

    def add_course(self, name, credit):
        """Lisää uuden kurssin tietokantaan.

        Args:
            name (str): Kurssin nimi
            credit (str): Kurssin opintopisteet

        Returns:
            Course: Lisätty kurssi Course-oliona.
        """

        course = self._course_repository.add_course(Course(name, credit, "0", self._user.username))
        return course

    def delete_course(self, name):
        return self._course_repository.delete_course(name)

    def get_courses_by_user(self):
        """Hakee tietokannasta annetun käyttäjän lisäämät kurssit.

        Returns:
            List: Lista käyttäjän lisäämistä kursseista.
        """

        return self._course_repository.find_courses_by_user(self._user.username)

    def set_current_course(self, course):
        """Asettaa self._coursen arvoksi kurssin, jolle ollaan sillä hetkellä merkitsemässä arvosana. Muulloin arvona on None.

        Args:
            course (None tai Course-olio): Kurssi-olio tai None, riippuen onko sillä hetkellä kurssia valittuna.
        """
        self._course = course

    def get_current_course(self):
        """Hakee kurssin, jolle ollaan sillä hetkellä merkitsemässä arvosanaa.

        Returns:
            Course: Course-olio
        """
        return self._course

    def get_not_completed_courses_by_user(self):
        """Hakee tietokannasta käyttäjän kaikki kesken olevat kurssit.

        Returns:
            List: Lista löydetyistä kursseista.
        """
        return self._course_repository.find_not_completed_courses_by_user(self._user.username)

    def get_completed_courses_by_user(self):
        """Hakee tietokannasta käyttäjän kaikki suoritetut kurssit.

        Returns:
            List: Lista löydetyistä kursseista.
        """
        return self._course_repository.find_completed_courses_by_user(self._user.username)

    def set_course_completed(self, course, grade):
        """Merkitsee annetulle kurssille arvosanan kurssirepositorion kautta.

        Args:
            course (Course): Kurssi-olio
            grade (str): Merkkijonoarvona käyttäjän syöttämä arvosana
        """
        self._course_repository.set_course_completed(course.name, grade)

    def get_credit_and_grade_average(self):
        """Hakee tietokannasta kaikki käyttäjän suorittamat kurssit sekä laskee opintopisteiden keskimäärän ja arvosanojen keskiarvon.

        Returns:
            Tuple: Opintopisteiden pistemäärä ja arvosanojen keskiarvo pyöristettynä kahteen desimaaliin.
        """
        courses = self.get_completed_courses_by_user()
        credit = 0
        grade_average = 0
        for course in courses:
            credit += int(course.credit)
            grade_average += int(course.grade)
        if len(courses) > 0:
            grade_average = grade_average/len(courses)

        return (credit, round(grade_average,2))



service = AppService()
