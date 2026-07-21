from abc import ABC, abstractmethod
from uuid import UUID

from shop.infrastructure.orm.orders import OrderModel


class OrdersRepository(ABC):
    @abstractmethod
    def create(self, order: OrderModel) -> OrderModel:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, order_id: UUID) -> OrderModel | None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[OrderModel]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, order_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def update(
        self,
        order_id: UUID,
        order: OrderModel,
    ) -> OrderModel | None:
        raise NotImplementedError