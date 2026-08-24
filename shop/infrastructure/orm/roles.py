import uuid

from sqlalchemy import UUID, Enum
from sqlalchemy.orm import Mapped, mapped_column

from shop.domain.entities.roles import UserRoles
from shop.infrastructure.orm.base import Base


class RolesModel(Base):
    __tablename__ = "roles"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    role: Mapped[UserRoles] = mapped_column(
        Enum(UserRoles),
        nullable=False,
        index=True,
        default=UserRoles.USER,
    )
