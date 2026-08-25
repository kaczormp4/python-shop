from uuid import UUID

from shop.domain.entities.roles import UserRole
from shop.domain.repositories.roles import RolesRepository


class RolesService:
    def __init__(
        self,
        roles_repository: RolesRepository,
    ) -> None:
        self.roles_repository = roles_repository

    def create_role(
        self,
        role: UserRole,
    ) -> UserRole:
        return self.roles_repository.create(role)

    def get_role_by_id(
        self,
        role_id: UUID,
    ) -> UserRole:
        role = self.roles_repository.get_by_id(role_id)

        if role is None:
            raise ValueError(f"Role with id={role_id} does not exist")

        return role

    def list_roles(self) -> list[UserRole]:
        return self.roles_repository.list()

    def delete_role(
        self,
        role_id: UUID,
    ) -> None:
        deleted = self.roles_repository.delete(role_id)

        if not deleted:
            raise ValueError(f"Role with id={role_id} does not exist")
