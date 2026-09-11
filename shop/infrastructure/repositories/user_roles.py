from uuid import UUID

from sqlalchemy import delete, select

from shop.domain.entities.roles import UserRole
from shop.domain.repositories.user_roles import UserRolesRepository
from shop.infrastructure.database import UnitOfWork
from shop.infrastructure.orm.roles import RolesModel
from shop.infrastructure.orm.user_roles_mapping import (
    UserRolesMappingModel,
)
from shop.infrastructure.repositories.mappers import to_entity


class ImplUserRolesRepository(UserRolesRepository):
    def __init__(self, uow: UnitOfWork) -> None:
        self.session = uow.session

    def assign_role(
        self,
        user_id: UUID,
        role_id: UUID,
    ) -> None:
        mapping = UserRolesMappingModel(
            user_id=user_id,
            role_id=role_id,
        )

        self.session.add(mapping)
        self.session.flush()

    def remove_role(
        self,
        user_id: UUID,
        role_id: UUID,
    ) -> bool:
        statement = delete(UserRolesMappingModel).where(
            UserRolesMappingModel.user_id == user_id,
            UserRolesMappingModel.role_id == role_id,
        )

        result = self.session.execute(statement)
        self.session.flush()

        return result.rowcount > 0

    def get_user_roles(
        self,
        user_id: UUID,
    ) -> list[UserRole]:
        statement = (
            select(RolesModel)
            .join(
                UserRolesMappingModel,
                UserRolesMappingModel.role_id == RolesModel.id,
            )
            .where(UserRolesMappingModel.user_id == user_id)
        )

        role_models = self.session.scalars(statement).all()

        return [to_entity(role_model, UserRole) for role_model in role_models]
