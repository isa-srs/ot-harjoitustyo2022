from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class AppService:
    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository
    
    def create_user(self, username, password):
        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f"Käyttäjänimi {username} on jo käytössä")

        user = self._user_repository.create_user(User(username, password))

        return user
    
    def login(self, username, password):
        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Käyttäjänimi tai salasana ei täsmää")

        self._user = user

        return user

    def logout(self):
        self._user = None
    
    def get_all_users(self):
        return self._user_repository.find_all()
    
    def get_current_user(self):
        return self._user

service = AppService()
