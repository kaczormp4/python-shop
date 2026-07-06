from abc import ABC, abstractmethod

from shop.domain.entities import Order

class OrdersRepository(ABC):
    
    @abstractmethod
    def create() -> Order:
        pass
    
    @abstractmethod
    def get_by_id(id) -> Order:
        pass
    
    @abstractmethod
    def list() -> list[Order]:
        pass
    
    @abstractmethod
    def delete() -> None:
        pass
    
    @abstractmethod
    def update() -> None:
        pass