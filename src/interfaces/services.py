from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from common.pagination import Params
from fastapi_pagination import Page
from interfaces.schemas import BaseModel

from .repository import RepositoryInterface

Schema = TypeVar('Schema', bound='BaseModel')


class ServiceInterface(Generic[Schema], ABC):
    def __init__(self, repository: RepositoryInterface[Schema]):
        self.repository = repository

    @abstractmethod
    async def get_all(self, params: Params) -> Page[Schema]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, schema_id: int) -> Schema:
        raise NotImplementedError

    @abstractmethod
    async def create(self, schema: Schema) -> Schema:
        raise NotImplementedError

    @abstractmethod
    async def update(self, schema_id: int, schema: Schema) -> Schema:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, schema_id: int) -> None:
        raise NotImplementedError
