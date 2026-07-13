# shop/infrastructure/database/models/product.py

import uuid
from datetime import datetime
from decimal import Decimal
from enum import StrEnum

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Enum,
    Integer,
    Numeric,
    String,
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from shop.domain.entities.products import ProductCategory
from shop.infrastructure.orm.base import Base


# class ProductCategory(StrEnum):
#     ELECTRONICS = "electronics"
#     CLOTHING = "clothing"
#     FOOD = "food"
#     OTHER = "other"


class ProductModel(Base):
    __tablename__ = "products"

    __table_args__ = (
        CheckConstraint(
            "price >= 0",
            name="ck_products_price_non_negative",
        ),
        CheckConstraint(
            "quantity_stock >= 0",
            name="ck_products_quantity_stock_non_negative",
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    category: Mapped[ProductCategory] = mapped_column(
        Enum(
            ProductCategory,
            name="product_category",
            values_callable=lambda enum: [item.value for item in enum],
        ),
        nullable=False,
        index=True,
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    quantity_stock: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
        server_default="0",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
    
    order_items: Mapped[list["OrderItemModel"]] = relationship(
        back_populates="product",
    )
    
    def __repr__(self) -> str:
        return (
            f"ProductModel("
            f"id={self.id!r}, "
            f"name={self.name!r}, "
            f"category={self.category!r}"
            f")"
        )