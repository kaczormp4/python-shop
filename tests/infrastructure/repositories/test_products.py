from decimal import Decimal

import pytest
from shop.domain.entities.products import ProductCategory
from shop.infrastructure.database import UnitOfWork
from shop.infrastructure.orm.products import ProductModel
from shop.infrastructure.repositories.products import ImplProductsRepository


@pytest.fixture
def repository(
    uow: UnitOfWork,
) -> ImplProductsRepository:
    return ImplProductsRepository(uow)


@pytest.fixture
def created_product(
    repository: ImplProductsRepository,
):
    product = ProductModel(
        name="MacBook Pro",
        description="Test product",
        category=ProductCategory.ELECTRONICS,
        price=Decimal("9999.99"),
        quantity_stock=10,
    )

    created_product = repository.create(product)

    yield created_product

    repository.delete(created_product.id)


def test_create_product(
    created_product: ProductModel,
) -> None:
    assert created_product.id is not None
    assert created_product.name == "MacBook Pro"
    assert created_product.price == Decimal("9999.99")
    assert created_product.quantity_stock == 10


def test_get_product_by_id(
    repository: ImplProductsRepository, created_product: ProductModel
) -> None:
    found_product = repository.get_by_id(created_product.id)

    assert found_product is not None
    assert found_product.id == created_product.id


def test_get_list(repository: ImplProductsRepository, created_product: ProductModel) -> None:
    second_product = ProductModel(
        name="iPhone",
        category=ProductCategory.ELECTRONICS,
        price=Decimal("5000.00"),
        quantity_stock=5,
    )

    repository.create(second_product)

    found_list = repository.list()

    assert len(found_list) == 2
    assert created_product.id in [product.id for product in found_list]
    assert second_product.id in [product.id for product in found_list]


def test_delete_product(repository: ImplProductsRepository, created_product: ProductModel) -> None:
    is_item_deleted = repository.delete(created_product.id)

    assert is_item_deleted


def test_updating(repository: ImplProductsRepository, created_product: ProductModel) -> None:
    updated_data = ProductModel(
        name="Test123",
        description=created_product.description,
        category=created_product.category,
        price=created_product.price,
        quantity_stock=created_product.quantity_stock,
    )

    updated_product = repository.update(
        created_product.id,
        updated_data,
    )

    assert updated_product is not None
    assert updated_product.name == "Test123"
