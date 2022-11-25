import unittest
from entities.user import User
from services.service import AppService, UsernameExistsError


class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []


class TestAppService(unittest.TestCase):
    def setUp(self):
        self.service = AppService(FakeUserRepository())

        self.user_isabel = User("isabel", "123456")

    def login_user(self, user):
        self.service.create_user(user.username, user.password)

    def test_create_new_user(self):
        username = self.user_isabel.username
        password = self.user_isabel.password

        self.service.create_user(username, password)

        users = self.service.get_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)

    def test_create_existing_user(self):
        username = self.user_isabel.username
        password = self.user_isabel.password

        self.service.create_user(username, password)

        self.assertRaises(UsernameExistsError,
                          self.service.create_user(username, "123"))
