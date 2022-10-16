from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class ORMBaseModel:
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime())
    updated_at = Column(DateTime())
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:  # pylint: disable=no-self-argument
        return cls.__name__.lower()
