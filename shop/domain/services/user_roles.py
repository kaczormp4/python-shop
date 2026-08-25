from uuid import UUID

from shop.domain.entities.roles import UserRole
from shop.domain.repositories.roles import RolesRepository
from shop.domain.repositories.user_roles import UserRolesRepository
from shop.domain.repositories.users import UsersRepository


class UserRolesService:
    def __init__(
        self,
        user_roles_repository: UserRolesRepository,
        users_repository: UsersRepository,
        roles_repository: RolesRepository,
    ) -> None:
        self.user_roles_repository = user_roles_repository
        self.users_repository = users_repository
        self.roles_repository = roles_repository

    def assign_role(
        self,
        user_id: UUID,
        role_id: UUID,
    ) -> None:
        user = self.users_repository.get_by_id(user_id)

        if user is None:
            raise ValueError(f"User with id={user_id} does not exist")

        role = self.roles_repository.get_by_id(role_id)

        if role is None:
            raise ValueError(f"Role with id={role_id} does not exist")

        self.user_roles_repository.assign_role(
            user_id,
            role_id,
        )

    def remove_role(
        self,
        user_id: UUID,
        role_id: UUID,
    ) -> None:
        deleted = self.user_roles_repository.remove_role(
            user_id,
            role_id,
        )

        if not deleted:
            raise ValueError("User does not have this role")

    def get_user_roles(
        self,
        user_id: UUID,
    ) -> list[UserRole]:
        user = self.users_repository.get_by_id(user_id)

        if user is None:
            raise ValueError(f"User with id={user_id} does not exist")

        return self.user_roles_repository.get_user_roles(user_id)
