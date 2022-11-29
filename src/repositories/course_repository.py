from entities.course import Course
from database_connection import get_database_connection


def get_course_by_row(row):
    return Course(row["name"], row["credits"]) if row else None


class CourseRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_course(self, course):
        cursor = self._connection.cursor()
        cursor.execute(
            'insert into courses (name, credits) values (?,?)',
            (course.name, course.credits)
        )
        self._connection.commit()
        return course

    # def find_courses_by_user(self, user):
    #     cursor = self._connection.cursor()
    #     cursor.execute(
    #         'select * from courses where user=?', (user,)
    #     )
    #     courses = cursor.fetchall()
    #     return list(map(get_course_by_row, courses))

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from courses'
        )
        result = cursor.fetchall()
        return list(map(get_course_by_row, result))

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute('delete from courses')
        self._connection.commit()

course_repository = CourseRepository(get_database_connection())
