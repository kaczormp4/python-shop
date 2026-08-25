from abc import ABC, abstractmethod
from uuid import UUID

from shop.domain.entities.roles import UserRole


class RolesRepository(ABC):
    @abstractmethod
    def create(self, role: UserRole) -> UserRole:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, role_id: UUID) -> UserRole | None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[UserRole]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, role_id: UUID) -> bool:
        raise NotImplementedError
