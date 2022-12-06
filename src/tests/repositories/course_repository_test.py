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
        self.course_ohte = Course('ohte', '4', self.user_isabel.username)
        self.course_tira = Course('tira', '5', self.user_isabel.username)
        self.course_ohtu = Course('ohtu', '5', self.user_sohvi.username)
    
    def test_add_course(self):
        user_repository.create_user(self.user_isabel)
        course_repository.add_course(self.course_ohte)

        courses = course_repository.find_all()

        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0].name, self.course_ohte.name)
        self.assertEqual(courses[0].credits, self.course_ohte.credits)
        self.assertEqual(courses[0].user, self.user_isabel.username)
    
    def test_find_all(self):
        course_repository.add_course(self.course_ohte)
        course_repository.add_course(self.course_ohtu)
        course_repository.add_course(self.course_tira)

        courses = course_repository.find_all()

        self.assertEqual(len(courses), 3)
        self.assertEqual(courses[0].name, self.course_ohte.name)
        self.assertEqual(courses[2].credits, self.course_tira.credits)