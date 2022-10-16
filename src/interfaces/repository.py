from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

Schema = TypeVar('Schema')


class RepositoryInterface(ABC, Generic[Schema]):
    db_session: AsyncSession

    def _check_rows(self, result):
        if result.rowcount == 0:
            raise ValueError("Todo not found")

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 10) -> list[Schema]:
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
