from common.pagination import Params
from database import session_db
from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from interfaces.services import ServiceInterface
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import PartialTodoSchema, TodoSchema


class TodoControler:
    def __init__(self, todo_service: ServiceInterface[TodoSchema]):
        self.service = todo_service
        self.router = APIRouter()
        self.router.add_api_route(
            '/', self.get_all, methods=['GET'], response_model=Page[TodoSchema]
        )
        self.router.add_api_route(
            '/{todo_id}/', self.get_one, methods=['GET'], response_model=TodoSchema
        )
        self.router.add_api_route(
            '/', self.create, methods=['POST'], response_model=TodoSchema, status_code=201
        )
        self.router.add_api_route(
            '/{todo_id}/', self.update, methods=['PUT'], response_model=TodoSchema
        )
        self.router.add_api_route('/{todo_id}/', self.delete, methods=['DELETE'], status_code=204)

    async def get_all(
        self, db_session: AsyncSession = Depends(session_db), params: Params = Depends()
    ):
        self.service.repository.db_session = db_session
        return await self.service.get_all(params)

    async def get_one(self, todo_id: int, db_session: AsyncSession = Depends(session_db)):
        self.service.repository.db_session = db_session
        return await self.service.get_by_id(todo_id)

    async def create(self, todo: PartialTodoSchema, db_session: AsyncSession = Depends(session_db)):
        self.service.repository.db_session = db_session
        return await self.service.create(todo)

    async def update(
        self, todo_id: int, todo: PartialTodoSchema, db_session: AsyncSession = Depends(session_db)
    ):
        self.service.repository.db_session = db_session
        return await self.service.update(todo_id, todo)

    async def delete(self, todo_id: int, db_session: AsyncSession = Depends(session_db)):
        self.service.repository.db_session = db_session
        await self.service.delete(todo_id)
