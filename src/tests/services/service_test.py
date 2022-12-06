import unittest
from entities.user import User
from entities.course import Course
from services.service import (
    AppService,
    InvalidCredentialsError,
    UsernameExistsError
)


class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def create_user(self, user):
        self.users.append(user)
        return user

    def find_by_username(self, username):
        matching = filter(
            lambda user: user.username == username,
            self.users
        )

        matching_list = list(matching)

        return matching_list[0] if len(matching_list) > 0 else None
    
    def find_all(self):
        return self.users

    def delete_all(self):
        self.users = []


class TestAppService(unittest.TestCase):
    def setUp(self):
        self.service = AppService(
            FakeUserRepository()
        )
    
        self.user_isabel = User("isabel", "1234")
    
    def create_user(self, user):
        self.service.create_user(user.username, user.password)

    def login_user(self, user):
        self.service.login(user.username, user.password)

    def test_create_new_user(self):
        username = self.user_isabel.username
        password = self.user_isabel.password

        self.service.create_user(username, password)

        users = self.service.get_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)
    
    def test_create_user_with_existing_username(self):
        username = self.user_isabel.username

        self.service.create_user(username, "salasana")

        self.assertRaises(
            UsernameExistsError,
            lambda: self.service.create_user(username, "jotain")
        )

    def test_get_current_user(self):
        self.create_user(self.user_isabel)
        self.login_user(self.user_isabel)

        current_user = self.service.get_current_user()

        self.assertEqual(current_user.username, self.user_isabel.username)