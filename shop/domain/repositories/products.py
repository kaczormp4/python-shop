from abc import ABC, abstractmethod
from shop.domain.entities import Product

class ProductsRepository(ABC):

    @abstractmethod
    def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Product:
        pass

    @abstractmethod
    def list(self) -> list[Product]:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass

    @abstractmethod
    def update(self, id: str, product: Product) -> Product:
        pass