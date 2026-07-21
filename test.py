from datetime import datetime, timezone
from uuid import UUID

from shop.domain.entities.orders import OrderStatus
from shop.domain.entities.products import ProductCategory
from shop.infrastructure.dependencies import get_uow
from shop.infrastructure.orm.order_items import OrderItemModel
from shop.infrastructure.orm.orders import OrderModel
from shop.infrastructure.repositories.orders import ImplOrdersRepository
from shop.infrastructure.repositories.products import ImplProductsRepository
from shop.infrastructure.orm.products import ProductModel

from decimal import Decimal
import shop.infrastructure.orm

products = [
    # ProductModel(
    #     name="iPhone 16 Pro",
    #     description="Smartfon Apple z ekranem ProMotion i aparatem klasy premium.",
    #     category=ProductCategory.ELECTRONICS,
    #     price=Decimal("5299.00"),
    #     quantity_stock=25,
    # ),
    # ProductModel(
    #     name="Mechanical Keyboard",
    #     description="Klawiatura mechaniczna z przełącznikami typu tactile.",
    #     category=ProductCategory.ELECTRONICS,
    #     price=Decimal("499.99"),
    #     quantity_stock=40,
    # ),
    # ProductModel(
    #     name="Office Chair",
    #     description="Ergonomiczne krzesło biurowe z regulacją wysokości i podparciem lędźwiowym.",
    #     category=ProductCategory.FURNITURE,
    #     price=Decimal("1299.00"),
    #     quantity_stock=8,
    # ),
    # ProductModel(
    #     name="Clean Code",
    #     description="Książka Roberta C. Martina o tworzeniu czytelnego i utrzymywalnego kodu.",
    #     category=ProductCategory.BOOKS,
    #     price=Decimal("149.90"),
    #     quantity_stock=30,
    # ),
]

product1 = ProductModel(
        name="MacBook Pro 14",
        description="Laptop Apple z procesorem M4 Pro, 18 GB RAM i dyskiem 512 GB SSD.",
        category=ProductCategory.ELECTRONICS,
        price=Decimal("9999.99"),
        quantity_stock=12,
    )


product2 = ProductModel(
        name="Mechanical Keyboard",
        description="Klawiatura mechaniczna z przełącznikami typu tactile.",
        category=ProductCategory.ELECTRONICS,
        price=Decimal("499.99"),
        quantity_stock=40,
    )


with get_uow() as uow:
    product_repository = ImplProductsRepository(uow)
    
    ## create
    # product_repository.create(product2)
    
    ## get all 
    # products = product_repository.list()
    
    # for product in products:
    #     print(product)

    ## get by id 
    # product = product_repository.get_by_id(
    #     UUID("32a621a9-87a8-4f7c-a5be-0fc1ef4cafcc")
    # )

    # print(product)
    
    ## delete
    # deleted = product_repository.delete(
    #     UUID("32a621a9-87a8-4f7c-a5be-0fc1ef4cafcc")
    # )

    # print("Usunięto:", deleted)
    
    
    ### 
    ### ORDER 
    ###
    
    order_repository = ImplOrdersRepository(uow)
    PRODUCT_ID: UUID = '78605b46-83b0-4faa-870a-5869880ed62f'
    
    ## create 
    # product = product_repository.get_by_id(PRODUCT_ID)

    # if product is None:
    #     raise ValueError(f"Product with id={PRODUCT_ID} does not exist")

    # quantity = 2

    # order = OrderModel(
    #     total_price=product.price * quantity,
    #     items=[
    #         OrderItemModel(
    #             product=product,
    #             quantity=quantity,
    #         )
    #     ],
    # )

    # created_order = order_repository.create(order)

    # print(created_order)
    # print(created_order.items)
    
    ## get by id 
    # ordered_by_id = order_repository.get_by_id("38ab386e-32aa-40ae-8887-b224915c6b9e")
    
    # print(ordered_by_id)
    
    # get list
    # order_list = order_repository.list()
    
    # print(order_list)
    
    ## delete
    # is_deleted = order_repository.delete('id')
    
    # print(is_deleted)
    
    ## update
    # updated_order = order_repository.update(
    #     UUID("38ab386e-32aa-40ae-8887-b224915c6b9e"),
    #     OrderModel(
    #         delivery_date=datetime.now(timezone.utc),
    #         status=OrderStatus.SHIPPED,
    #         total_price=Decimal("999.98"),
    #     ),
    # )
    
    # if updated_order is None:
    #     print("Nie znaleziono zamówienia")
    # else:
    #     print("Zaktualizowano:", updated_order)
    