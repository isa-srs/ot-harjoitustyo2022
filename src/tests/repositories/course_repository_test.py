import unittest
from repositories.course_repository import course_repository
from repositories.user_repository import user_repository
from entities.course import Course
from entities.user import User


class TestCourseRepository(unittest.TestCase):
    def setUp(self):
        course_repository.delete_all()
        user_repository.delete_all()

        self.user_isabel = User('isabel', '1234')
        self.user_sohvi = User('sohvi', 'pohvi')
        self.course_ohte = Course('ohte', '4', '0', self.user_isabel.username)
        self.course_tira = Course('tira', '5', '4', self.user_isabel.username)
        self.course_ohtu = Course('ohtu', '5', '5', self.user_sohvi.username)
    
    def test_add_course(self):
        isabel = user_repository.create_user(self.user_isabel)
        course_repository.add_course(self.course_ohte)

        courses = course_repository.find_courses_by_user(user=isabel.username)

        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0].name, self.course_ohte.name)
        self.assertEqual(courses[0].credit, self.course_ohte.credit)
        self.assertEqual(courses[0].user, self.user_isabel.username)
    
    def test_set_course_completed(self):
        isabel = user_repository.create_user(self.user_isabel)
        course_repository.add_course(self.course_ohte)
        grade = "5"

        course_repository.set_course_completed(self.course_ohte.name, grade)

        courses = course_repository.find_courses_by_user(user=isabel.username)

        self.assertEqual(courses[0].grade, grade)
    
    def test_find_courses_by_user(self):
        isabel = user_repository.create_user(self.user_isabel)
        sohvi = user_repository.create_user(self.user_sohvi)

        course_repository.add_course(Course('ohte', '4', '0', user=isabel.username))
        course_repository.add_course(Course('ohtu', '5', '0', user=sohvi.username))

        isabel_courses = course_repository.find_courses_by_user(
            self.user_isabel.username
        )

        self.assertEqual(len(isabel_courses), 1)
        self.assertEqual(isabel_courses[0].name, 'ohte')
        self.assertEqual(isabel_courses[0].grade, '0')

        sohvi_courses = course_repository.find_courses_by_user(
            self.user_sohvi.username
        )

        self.assertEqual(len(sohvi_courses), 1)
        self.assertEqual(sohvi_courses[0].name, 'ohtu')
        self.assertEqual(sohvi_courses[0].grade, '0')

    def test_find_not_completed_courses_by_user(self):
        isabel = user_repository.create_user(self.user_isabel)
        ohte = course_repository.add_course(self.course_ohte)

        isabel_courses = course_repository.find_not_completed_courses_by_user(user=isabel.username)

        self.assertEqual(len(isabel_courses), 1)
        self.assertEqual(isabel_courses[0].name, 'ohte')
        self.assertEqual(isabel_courses[0].grade, '0')
    
    def test_find_completed_courses_by_user(self):
        sohvi = user_repository.create_user(self.user_sohvi)
        course_repository.add_course(self.course_ohtu)

        sohvi_courses = course_repository.find_completed_courses_by_user(user=sohvi.username)

        self.assertEqual(len(sohvi_courses), 1)
        self.assertEqual(sohvi_courses[0].name, 'ohtu')
        self.assertEqual(sohvi_courses[0].grade, '5')

    def test_delete_course(self):
        isabel = user_repository.create_user(self.user_isabel)
        ohte = course_repository.add_course(self.course_ohte)
        tira = course_repository.add_course(self.course_tira)

        course_repository.delete_course(ohte.name)

        courses = course_repository.find_courses_by_user(isabel.username)

        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0].name, tira.name)
    