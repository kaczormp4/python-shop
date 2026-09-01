from sqlalchemy.orm import Session, sessionmaker


class UnitOfWork:
    def __init__(self, session_factory: sessionmaker[Session]):
        self._session_factory = session_factory
        self._session: Session | None = None

    @property
    def session(self) -> Session:
        if self._session is None:
            raise RuntimeError(
                "UnitOfWork session is not initialized",
            )

        return self._session

    def __enter__(self) -> "UnitOfWork":
        self._session = self._session_factory()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if self._session is None:
            return False

        try:
            if exc_type is None:
                self._session.commit()
            else:
                self._session.rollback()
        finally:
            self._session.close()
            self._session = None

        # False oznacza: nie przechwytuj wyjątku,
        # pozwól mu polecieć dalej
        return False
