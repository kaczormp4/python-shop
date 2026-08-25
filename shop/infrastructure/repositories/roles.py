from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from shop.domain.entities.roles import UserRole
from shop.domain.repositories.roles import RolesRepository
from shop.infrastructure.database import UnitOfWork
from shop.infrastructure.orm.roles import RolesModel


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

        return self._to_entity(role_model)

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

        return self._to_entity(role_model)

    def list(self) -> list[UserRole]:
        statement = select(RolesModel)

        role_models = self.session.scalars(statement).all()

        return [self._to_entity(role_model) for role_model in role_models]

    def delete(self, role_id: UUID) -> bool:
        statement = select(RolesModel).where(
            RolesModel.id == role_id,
        )

        role_model = self.session.scalar(statement)

        if role_model is None:
            return False

        self.session.delete(role_model)
        self.session.flush()

        return True

    @staticmethod
    def _to_entity(role_model: RolesModel) -> UserRole:
        return UserRole(
            id=role_model.id,
            role=role_model.role,
        )
