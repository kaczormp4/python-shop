from abc import ABC, abstractmethod
from uuid import UUID

from shop.domain.entities.users import User


class UsersRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, user_id: UUID) -> User | None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[User]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id: UUID) -> bool:
        raise NotImplementedError
