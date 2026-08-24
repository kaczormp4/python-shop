from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    id: UUID | None = None
    name: str
    surname: str
    email: str
