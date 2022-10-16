from abc import ABC
from datetime import datetime

from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel, ABC):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
