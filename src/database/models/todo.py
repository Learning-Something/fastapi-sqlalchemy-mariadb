from database.base_model import ORMBaseModel
from sqlalchemy import Column, String


class Todo(ORMBaseModel):
    title = Column(String, unique=False, nullable=False, index=False)
    description = Column(String, unique=False, nullable=True, index=False)
