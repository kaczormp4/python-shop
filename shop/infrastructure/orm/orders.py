# shop/infrastructure/database/models/order.py

import uuid
from datetime import datetime
from decimal import Decimal
from enum import StrEnum

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Enum,
    Numeric,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from shop.domain.entities.orders import OrderStatus
from shop.infrastructure.orm.base import Base


# class OrderStatus(StrEnum):
#     ORDERED = "ordered"
#     PAID = "paid"
#     SHIPPED = "shipped"
#     DELIVERED = "delivered"
#     CANCELLED = "cancelled"


class OrderModel(Base):
    __tablename__ = "orders"

    __table_args__ = (
        CheckConstraint(
            "total_price >= 0",
            name="ck_orders_total_price_non_negative",
        ),
        CheckConstraint(
            "delivery_date IS NULL OR delivery_date >= creation_date",
            name="ck_orders_delivery_date_after_creation_date",
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    creation_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    delivery_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    status: Mapped[OrderStatus] = mapped_column(
        Enum(
            OrderStatus,
            name="order_status",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
        default=OrderStatus.ORDERED,
        server_default=OrderStatus.ORDERED.value,
        index=True,
    )

    total_price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=Decimal("0.00"),
        server_default="0.00",
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    items: Mapped[list["OrderItemModel"]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def __repr__(self) -> str:
        return (
            f"OrderModel("
            f"id={self.id!r}, "
            f"status={self.status!r}, "
            f"total_price={self.total_price!r}"
            f")"
        )