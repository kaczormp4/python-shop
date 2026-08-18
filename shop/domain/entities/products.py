from enum import Enum

from pydantic import BaseModel, Field


class ProductCategory(Enum):
    ELECTRONICS = "electronics"
    CLOTHES = "clothes"
    FOOD = "food"
    BOOKS = "books"
    OTHER = "other"


class Product(BaseModel):
    id: str
    name: str
    description: str | None = None
    category: ProductCategory
    price: float
    quantity_stock: int = Field(ge=0)
    is_available: bool = True
