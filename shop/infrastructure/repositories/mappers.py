from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


def to_entity[T: BaseModel](
    model: object,
    entity_class: type[T],
) -> T:
    return entity_class.model_validate(
        model,
        from_attributes=True,
    )
