from uuid import UUID

from sqlalchemy import select

from shop.domain.entities.products import Product
from shop.domain.repositories.products import ProductsRepository
from shop.infrastructure.database import UnitOfWork
from shop.infrastructure.orm.products import ProductModel


class ImplProductsRepository(ProductsRepository):
    def __init__(self, uow: UnitOfWork) -> None:
        self.session = uow.session

    def create(self, product: Product) -> Product:
        product_model = ProductModel(
            name=product.name,
            description=product.description,
            category=product.category,
            price=product.price,
            quantity_stock=product.quantity_stock,
        )

        self.session.add(product_model)
        self.session.flush()
        self.session.refresh(product_model)

        return Product(
            id=product_model.id,
            name=product_model.name,
            description=product_model.description,
            category=product_model.category,
            price=float(product_model.price),
            quantity_stock=product_model.quantity_stock,
            is_available=product_model.quantity_stock > 0,
        )

    def get_by_id(self, product_id: UUID) -> ProductModel | None:
        return self.session.get(ProductModel, product_id)

    def list(self) -> list[ProductModel]:
        statement = select(ProductModel).order_by(ProductModel.created_at.desc())

        return list(self.session.scalars(statement).all())

    def delete(self, product_id: UUID) -> bool:
        product = self.get_by_id(product_id)

        if product is None:
            return False

        self.session.delete(product)
        self.session.flush()

        return True

    def update(self, product_id: UUID, product_data: ProductModel) -> ProductModel | None:
        product = self.get_by_id(product_id)

        if product is None:
            return None

        product.name = product_data.name
        product.description = product_data.description
        product.category = product_data.category
        product.price = product_data.price
        product.quantity_stock = product_data.quantity_stock

        self.session.flush()
        self.session.refresh(product)

        return product
