from uuid import UUID

from shop.domain.entities.users import User
from shop.domain.repositories.users import UsersRepository


class UsersService:
    def __init__(
        self,
        users_repository: UsersRepository,
    ) -> None:
        self.users_repository = users_repository

    def create_user(self, user: User) -> User:
        return self.users_repository.create(user)

    def get_user_by_id(
        self,
        user_id: UUID,
    ) -> User:
        user = self.users_repository.get_by_id(user_id)

        if user is None:
            raise ValueError(f"User with id={user_id} does not exist")

        return user

    def list_users(self) -> list[User]:
        return self.users_repository.list()

    def delete_user(
        self,
        user_id: UUID,
    ) -> None:
        deleted = self.users_repository.delete(user_id)

        if not deleted:
            raise ValueError(f"User with id={user_id} does not exist")
