from collections.abc import Generator

import pytest
from shop.infrastructure.database import UnitOfWork
from shop.infrastructure.orm.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

SQLALCHEMY_DATABASE_URL = "sqlite://"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestSessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


@pytest.fixture(autouse=True)
def prepare_database() -> Generator[None, None, None]:
    Base.metadata.create_all(bind=engine)

    yield

    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def uow() -> Generator[UnitOfWork, None, None]:
    unit_of_work = UnitOfWork(TestSessionLocal)

    with unit_of_work as current_uow:
        yield current_uow
