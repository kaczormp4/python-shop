from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from shop.domain.entities.users import User
from shop.domain.repositories.users import UsersRepository
from shop.infrastructure.database import UnitOfWork
from shop.infrastructure.orm.users import UsersModel


class ImplUsersRepository(UsersRepository):
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    @property
    def session(self) -> Session:
        if self.uow.session is None:
            raise RuntimeError("UnitOfWork session is not initialized")

        return self.uow.session

    def create(self, user: User) -> User:
        user_model = UsersModel(
            name=user.name,
            surname=user.surname,
            email=user.email,
        )

        self.session.add(user_model)
        self.session.flush()
        self.session.refresh(user_model)

        return self._to_entity(user_model)

    def get_by_id(
        self,
        user_id: UUID,
    ) -> User | None:
        statement = select(UsersModel).where(
            UsersModel.id == user_id,
        )

        user_model = self.session.scalar(statement)

        if user_model is None:
            return None

        return self._to_entity(user_model)

    def list(self) -> list[User]:
        statement = select(UsersModel)

        user_models = self.session.scalars(statement).all()

        return [self._to_entity(user_model) for user_model in user_models]

    def delete(self, user_id: UUID) -> bool:
        user_model = self.session.get(
            UsersModel,
            user_id,
        )

        if user_model is None:
            return False

        self.session.delete(user_model)
        self.session.flush()

        return True

    @staticmethod
    def _to_entity(user_model: UsersModel) -> User:
        return User(
            id=user_model.id,
            name=user_model.name,
            surname=user_model.surname,
            email=user_model.email,
        )
