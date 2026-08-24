from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class UserRoles(Enum):
    USER = "user"
    EMPLOYEE = "employee"
    ADMIN = "admin"


class UserRole(BaseModel):
    id: UUID | None = None
    role: UserRoles
