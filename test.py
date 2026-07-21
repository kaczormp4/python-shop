from shop.domain.entities.products import ProductCategory
from shop.infrastructure.dependencies import get_uow
from shop.infrastructure.repositories.products import ImplProductsRepository
from shop.infrastructure.orm.products import ProductModel

from decimal import Decimal


products = [
    # ProductModel(
    #     name="iPhone 16 Pro",
    #     description="Smartfon Apple z ekranem ProMotion i aparatem klasy premium.",
    #     category=ProductCategory.ELECTRONICS,
    #     price=Decimal("5299.00"),
    #     quantity_stock=25,
    # ),
    # ProductModel(
    #     name="Mechanical Keyboard",
    #     description="Klawiatura mechaniczna z przełącznikami typu tactile.",
    #     category=ProductCategory.ELECTRONICS,
    #     price=Decimal("499.99"),
    #     quantity_stock=40,
    # ),
    # ProductModel(
    #     name="Office Chair",
    #     description="Ergonomiczne krzesło biurowe z regulacją wysokości i podparciem lędźwiowym.",
    #     category=ProductCategory.FURNITURE,
    #     price=Decimal("1299.00"),
    #     quantity_stock=8,
    # ),
    # ProductModel(
    #     name="Clean Code",
    #     description="Książka Roberta C. Martina o tworzeniu czytelnego i utrzymywalnego kodu.",
    #     category=ProductCategory.BOOKS,
    #     price=Decimal("149.90"),
    #     quantity_stock=30,
    # ),
]

product1 = ProductModel(
        name="MacBook Pro 14",
        description="Laptop Apple z procesorem M4 Pro, 18 GB RAM i dyskiem 512 GB SSD.",
        category=ProductCategory.ELECTRONICS,
        price=Decimal("9999.99"),
        quantity_stock=12,
    )

with get_uow() as uow:
    product_repository = ImplProductsRepository(uow)
    product_repository.create(product1)
