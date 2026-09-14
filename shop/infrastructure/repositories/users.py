from uuid import UUID

import bcrypt
from sqlalchemy import select

from shop.domain.entities.users import User
from shop.domain.repositories.users import UsersRepository
from shop.infrastructure.database import UnitOfWork
from shop.infrastructure.orm.users import UsersModel
from shop.infrastructure.repositories.mappers import to_entity


def hash_password(password: str) -> str:
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt(),
    ).decode("utf-8")


def verify_password(
    password: str,
    hashed_password: str,
) -> bool:
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8"),
    )


class ImplUsersRepository(UsersRepository):
    def __init__(self, uow: UnitOfWork) -> None:
        self.session = uow.session

    def create(self, user: User) -> User:
        user_from_db = self.session.scalar(
            select(UsersModel).where(
                UsersModel.email == user.email,
            )
        )
        if user_from_db is not None:
            if user.email == user_from_db.email:
                raise ValueError("user not valid")

        user_model = UsersModel(
            name=user.name,
            surname=user.surname,
            email=user.email,
            password=hash_password(user.password),
        )

        self.session.add(user_model)
        self.session.flush()
        self.session.refresh(user_model)

        return to_entity(user_model, User)

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

        return to_entity(user_model, User)

    def list(self) -> list[User]:
        statement = select(UsersModel)

        user_models = self.session.scalars(statement).all()

        return [to_entity(user_model, User) for user_model in user_models]

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
