from uuid import UUID

from shop.domain.repositories.orders import OrdersRepository
from shop.infrastructure.orm.orders import OrderModel


class OrdersService:
    def __init__(
        self,
        orders_repository: OrdersRepository,
    ) -> None:
        self.orders_repository = orders_repository

    def create_order(self, order: OrderModel) -> OrderModel:
        self._validate_order(order)

        return self.orders_repository.create(order)

    def get_order_by_id(self, order_id: UUID) -> OrderModel:
        order = self.orders_repository.get_by_id(order_id)

        if order is None:
            raise ValueError(
                f"Order with id={order_id} does not exist",
            )

        return order

    def list_orders(self) -> list[OrderModel]:
        return self.orders_repository.list()

    def delete_order(self, order_id: UUID) -> None:
        order = self.orders_repository.get_by_id(order_id)

        if order is None:
            raise ValueError(
                f"Order with id={order_id} does not exist",
            )

        self.orders_repository.delete(order_id)

    def update_order(
        self,
        order_id: UUID,
        order: OrderModel,
    ) -> OrderModel:
        existing_order = self.orders_repository.get_by_id(
            order_id,
        )

        if existing_order is None:
            raise ValueError(
                f"Order with id={order_id} does not exist",
            )

        self._validate_order(order)

        updated_order = self.orders_repository.update(
            order_id,
            order,
        )

        if updated_order is None:
            raise ValueError(
                f"Order with id={order_id} does not exist",
            )

        return updated_order

    @staticmethod
    def _validate_order(order: OrderModel) -> None:
        if order.total_price < 0:
            raise ValueError(
                "Order total price cannot be negative",
            )
