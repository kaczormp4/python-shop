import uuid

from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from shop.infrastructure.orm.base import Base


class UsersModel(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    surname: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )


# class User(BaseModel):
#     id: UUID | None = None
#     name: str
#     surname: str
#     email: str
