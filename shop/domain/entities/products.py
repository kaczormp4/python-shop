from enum import Enum
from pydantic import BaseModel

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
    quantity: int
    is_available: bool = True