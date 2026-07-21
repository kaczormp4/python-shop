from shop.domain.entities import Product
from shop.domain.repositories.products import ProductsRepository
from shop.infrastructure.orm.products import ProductModel
from shop.infrastructure.database import UnitOfWork

class ImplProductsRepository(ProductsRepository):

    def __init__(self, uow: UnitOfWork):
        self.uow = uow
         
    def create(self, product: Product) -> Product:
        return self.uow.session.add(product)

    def get_by_id(self, id: str) -> Product:
        pass

    def list(self) -> list[Product]:
        pass

    def delete(self, id: str) -> None:
        pass

    def update(self, id: str, product: Product) -> Product:
        pass