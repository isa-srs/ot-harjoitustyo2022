from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)


class AppService:
    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository
    
    def create_user(self, username, password):
        user = self._user_repository.create_user(User(username, password))

        return user

service = AppService()
