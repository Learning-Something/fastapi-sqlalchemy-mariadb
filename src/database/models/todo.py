from database.base_model import ORMBaseModel
from sqlalchemy import Column, String


class Todo(ORMBaseModel):
    title = Column(String(50), unique=False, nullable=False, index=False)
    description = Column(String(255), unique=False, nullable=True, index=False)
