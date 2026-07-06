from shop.domain.entities import Product
from shop.domain.repositories.products import ProductsRepository

class ProductsService:
    def __init__(self, products_repository: ProductsRepository) -> None:
        self.products_repository = products_repository

    def create_product(self, product: Product) -> Product:
        if product.price <= 0:
            raise ValueError("Product price must be greater than 0")

        if product.quantity < 0:
            raise ValueError("Product quantity cannot be negative")

        return self.products_repository.create(product)