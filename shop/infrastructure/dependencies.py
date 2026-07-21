from shop.infrastructure.database import UnitOfWork
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


DATABASE_URL = "postgresql://postgres@localhost:5432/shopApp"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


def get_uow() -> UnitOfWork:
    return UnitOfWork(SessionLocal)