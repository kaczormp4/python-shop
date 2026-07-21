from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from shop.domain.entities import Product
from shop.domain.repositories.products import ProductsRepository
from shop.infrastructure.orm.products import ProductModel
from shop.infrastructure.database import UnitOfWork

class ImplProductsRepository(ProductsRepository):

    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow
    
    @property
    def session(self) -> Session:
        if self.uow.session is None:
            raise RuntimeError(
                "UnitOfWork session is not initialized"
            )

        return self.uow.session

    def create(self, product: ProductModel) -> ProductModel:
        self.session.add(product)
        self.session.flush()
        self.session.refresh(product)
        
        return product

    def get_by_id(self, product_id: UUID) -> ProductModel | None:
        return self.session.get(ProductModel, product_id)
        

    def list(self) -> list[ProductModel]:
        statement = (
            select(ProductModel).order_by(ProductModel.created_at.desc())
        )
        
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
        
        pass