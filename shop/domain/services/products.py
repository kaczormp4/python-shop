from shop.domain.entities import Product
from shop.domain.repositories.products import ProductsRepository


class ProductsService:
    def __init__(
        self,
        products_repository: ProductsRepository,
    ) -> None:
        self.products_repository = products_repository

    def create_product(self, product: Product) -> Product:
        self._validate_product(product)

        return self.products_repository.create(product)

    def get_product_by_id(self, product_id: str) -> Product:
        product = self.products_repository.get_by_id(product_id)

        if product is None:
            raise ValueError(
                f"Product with id={product_id} does not exist",
            )

        return product

    def list_products(self) -> list[Product]:
        return self.products_repository.list()

    def delete_product(self, product_id: str) -> None:
        product = self.products_repository.get_by_id(product_id)

        if product is None:
            raise ValueError(
                f"Product with id={product_id} does not exist",
            )

        self.products_repository.delete(product_id)

    def update_product(
        self,
        product_id: str,
        product: Product,
    ) -> Product:
        existing_product = self.products_repository.get_by_id(
            product_id,
        )

        if existing_product is None:
            raise ValueError(
                f"Product with id={product_id} does not exist",
            )

        self._validate_product(product)

        return self.products_repository.update(
            product_id,
            product,
        )

    @staticmethod
    def _validate_product(product: Product) -> None:
        if product.price <= 0:
            raise ValueError(
                "Product price must be greater than 0",
            )

        if product.quantity < 0:
            raise ValueError(
                "Product quantity cannot be negative",
            )
