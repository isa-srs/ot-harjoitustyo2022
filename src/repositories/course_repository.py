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
            'insert into courses (name, credits) calues (?,?)',
            (course.name, course.credits)
        )
        self._connection.commit()
        return course
    
    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from courses'
        )
        result = cursor.fetchall()
        return list(map(get_course_by_row, result))
    
course_repository = CourseRepository(get_database_connection())
