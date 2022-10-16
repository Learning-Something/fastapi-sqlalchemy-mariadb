from common.pagination import Params
from interfaces.services import RepositoryInterface, ServiceInterface

from .schemas import PartialTodoSchema, TodoSchema


class TodoService(ServiceInterface[TodoSchema]):
    def __init__(self, repository: RepositoryInterface[TodoSchema]):
        super().__init__(repository)
        self.repository = repository

    async def get_all(self, params: Params = Params(page=1, size=10)):
        return await self.repository.get_all(params)

    async def get_by_id(self, schema_id: int):
        return await self.repository.get_by_id(schema_id)

    async def create(self, schema: PartialTodoSchema):
        return await self.repository.create(schema)

    async def update(self, schema_id: int, schema: PartialTodoSchema):
        return await self.repository.update(schema_id, schema)

    async def delete(self, schema_id: int):
        return await self.repository.delete(schema_id)
