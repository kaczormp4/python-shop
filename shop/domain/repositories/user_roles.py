from abc import ABC, abstractmethod
from uuid import UUID

from shop.domain.entities.roles import UserRole


class UserRolesRepository(ABC):
    @abstractmethod
    def assign_role(
        self,
        user_id: UUID,
        role_id: UUID,
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_role(
        self,
        user_id: UUID,
        role_id: UUID,
    ) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_user_roles(
        self,
        user_id: UUID,
    ) -> list[UserRole]:
        raise NotImplementedError
