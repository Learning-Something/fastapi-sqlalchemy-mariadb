from interfaces.schemas import BaseModel
from pydantic import BaseModel as PydanticBaseModel


class TodoSchema(BaseModel):
    title: str
    description: str | None = None


class PartialTodoSchema(PydanticBaseModel):
    title: str | None = None
    description: str | None = None
