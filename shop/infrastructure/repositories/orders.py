from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from shop.domain.repositories.orders import OrdersRepository
from shop.infrastructure.database import UnitOfWork
from shop.infrastructure.orm.orders import OrderModel


class ImplOrdersRepository(OrdersRepository):
    def __init__(self, uow: UnitOfWork) -> None:
        self.session = uow.session

    def create(self, order: OrderModel) -> OrderModel:
        self.session.add(order)
        self.session.flush()
        self.session.refresh(order)

        return order

    def get_by_id(self, order_id: UUID) -> OrderModel | None:
        statement = (
            select(OrderModel)
            .options(selectinload(OrderModel.items))
            .where(OrderModel.id == order_id)
        )

        return self.session.scalar(statement)

    def list(self) -> list[OrderModel]:
        statement = (
            select(OrderModel)
            .options(selectinload(OrderModel.items))
            .order_by(OrderModel.creation_date.desc())
        )

        return list(self.session.scalars(statement).all())

    def delete(self, order_id: UUID) -> bool:
        order = self.get_by_id(order_id)

        if order is None:
            return False

        self.session.delete(order)
        self.session.flush()

        return True

    def update(
        self,
        order_id: UUID,
        order_data: OrderModel,
    ) -> OrderModel | None:
        order = self.get_by_id(order_id)

        if order is None:
            return None

        order.delivery_date = order_data.delivery_date
        order.status = order_data.status
        order.total_price = order_data.total_price

        self.session.flush()
        self.session.refresh(order)

        return order
