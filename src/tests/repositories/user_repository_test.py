import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_isabel = User('isabel', '1234')
        self.user_janika = User('Janika', 'salasana')

    def test_create_user(self):
        user_repository.create_user(self.user_isabel)
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_isabel.username)
    
    def test_find_by_username(self):
        user_repository.create_user(self.user_janika)
        user = user_repository.find_by_username(self.user_janika.username)

        self.assertEqual(user.username, self.user_janika.username)
    
    def test_find_all(self):
        user_repository.create_user(self.user_isabel)
        user_repository.create_user(self.user_janika)
        users = user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_isabel.username)
        self.assertEqual(users[1].username, self.user_janika.username)
