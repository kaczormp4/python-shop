from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from shop.domain.entities.roles import UserRole
from shop.domain.repositories.roles import RolesRepository
from shop.infrastructure.database import UnitOfWork
from shop.infrastructure.orm.roles import RolesModel
from shop.infrastructure.repositories.mappers import to_entity


class ImplRolesRepository(RolesRepository):
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    @property
    def session(self) -> Session:
        if self.uow.session is None:
            raise RuntimeError("UnitOfWork session is not initialized")

        return self.uow.session

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
