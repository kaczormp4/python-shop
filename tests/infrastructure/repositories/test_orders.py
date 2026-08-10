from datetime import datetime, timezone
from decimal import Decimal
from uuid import uuid4

from shop.domain.entities.orders import OrderStatus
from shop.infrastructure.database import UnitOfWork
from shop.infrastructure.orm.orders import OrderModel
from shop.infrastructure.repositories.orders import ImplOrdersRepository


def test_create_order(uow: UnitOfWork) -> None:
    repository = ImplOrdersRepository(uow)

    order = OrderModel(
        total_price=Decimal("100.00"),
    )

    created_order = repository.create(order)

    assert created_order.id is not None
    assert created_order.total_price == Decimal("100.00")


def test_get_order_by_id(uow: UnitOfWork) -> None:
    repository = ImplOrdersRepository(uow)

    order = OrderModel(
        total_price=Decimal("200.00"),
    )

    created_order = repository.create(order)

    found_order = repository.get_by_id(created_order.id)

    assert found_order is not None
    assert found_order.id == created_order.id
    assert found_order.total_price == Decimal("200.00")


def test_get_order_by_id_returns_none_when_order_does_not_exist(
    uow: UnitOfWork,
) -> None:
    repository = ImplOrdersRepository(uow)

    result = repository.get_by_id(uuid4())

    assert result is None


def test_list_orders(uow: UnitOfWork) -> None:
    repository = ImplOrdersRepository(uow)

    order1 = OrderModel(
        total_price=Decimal("100.00"),
    )

    order2 = OrderModel(
        total_price=Decimal("200.00"),
    )

    repository.create(order1)
    repository.create(order2)

    orders = repository.list()

    assert len(orders) == 2

    order_ids = [order.id for order in orders]

    assert order1.id in order_ids
    assert order2.id in order_ids


def test_delete_order(uow: UnitOfWork) -> None:
    repository = ImplOrdersRepository(uow)

    order = OrderModel(
        total_price=Decimal("100.00"),
    )

    created_order = repository.create(order)

    result = repository.delete(created_order.id)

    assert result is True
    assert repository.get_by_id(created_order.id) is None


def test_delete_returns_false_when_order_does_not_exist(
    uow: UnitOfWork,
) -> None:
    repository = ImplOrdersRepository(uow)

    result = repository.delete(uuid4())

    assert result is False


def test_update_order(uow: UnitOfWork) -> None:
    repository = ImplOrdersRepository(uow)

    order = OrderModel(
        total_price=Decimal("100.00"),
    )

    created_order = repository.create(order)

    delivery_date = datetime.now()

    order_data = OrderModel(
        delivery_date=delivery_date,
        status=OrderStatus.SHIPPED,
        total_price=Decimal("250.00"),
    )

    updated_order = repository.update(
        created_order.id,
        order_data,
    )

    assert updated_order is not None
    assert updated_order.status == OrderStatus.SHIPPED
    assert updated_order.total_price == Decimal("250.00")
    assert updated_order.delivery_date == delivery_date

def test_update_returns_none_when_order_does_not_exist(
    uow: UnitOfWork,
) -> None:
    repository = ImplOrdersRepository(uow)

    order_data = OrderModel(
        delivery_date=datetime.now(timezone.utc),
        status=OrderStatus.SHIPPED,
        total_price=Decimal("250.00"),
    )

    result = repository.update(
        uuid4(),
        order_data,
    )

    assert result is None