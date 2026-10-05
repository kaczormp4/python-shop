from uuid import UUID

from sqlalchemy import delete, select

from shop.domain.entities.roles import UserRole
from shop.domain.repositories.roles import RolesRepository
from shop.infrastructure.database import UnitOfWork
from shop.infrastructure.orm.roles import RolesModel
from shop.infrastructure.orm.user_roles_mapping import (
    UserRolesMappingModel,
)
from shop.infrastructure.repositories.mappers import to_entity


class ImplRolesRepository(RolesRepository):
    def __init__(self, uow: UnitOfWork) -> None:
        self.session = uow.session

    def create(self, role: UserRole) -> UserRole:
        role_model = RolesModel(
            role=role.role,
        )

        self.session.add(role_model)
        self.session.flush()
        self.session.refresh(role_model)

        return to_entity(role_model, UserRole)

    def get_by_id(
        self,
        role_id: UUID,
    ) -> UserRole | None:
        statement = select(RolesModel).where(
            RolesModel.id == role_id,
        )

        role_model = self.session.scalar(statement)

        if role_model is None:
            return None

        return to_entity(role_model, UserRole)

    def list(self) -> list[UserRole]:
        statement = select(RolesModel)

        role_models = self.session.scalars(statement).all()

        return [to_entity(role_model, UserRole) for role_model in role_models]

    def delete(self, role_id: UUID) -> bool:
        role_model = self.session.get(
            RolesModel,
            role_id,
        )

        if role_model is None:
            return False

        self.session.delete(role_model)
        self.session.flush()

        return True

    def asign_role(
        self,
        role_id: UUID,
        user_id: UUID,
    ) -> bool:
        mapping = UserRolesMappingModel(
            role_id=role_id,
            user_id=user_id,
        )

        self.session.add(mapping)
        self.session.flush()

        return True

    def unassign_role(
        self,
        role_id: UUID,
        user_id: UUID,
    ) -> bool:
        statement = delete(UserRolesMappingModel).where(
            UserRolesMappingModel.role_id == role_id,
            UserRolesMappingModel.user_id == user_id,
        )

        result = self.session.execute(statement)
        self.session.flush()

        return result.rowcount > 0
