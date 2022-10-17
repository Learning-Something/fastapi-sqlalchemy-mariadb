from common.pagination import Params
from database.models.todo import Todo
from fastapi_pagination import Page
from fastapi_pagination.bases import BasePage
from fastapi_pagination.ext.async_sqlalchemy import paginate
from interfaces.repository import RepositoryInterface
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import NoResultFound

from .exceptions import TodoNotFound
from .schemas import PartialTodoSchema, TodoSchema


class TodoRepository(RepositoryInterface[TodoSchema]):
    async def get_all(self, params: Params = Params(page=1, size=10)):
        todo_query = select(Todo).order_by(Todo.created_at.desc())
        todos_page: BasePage[Todo] = await paginate(self.db_session, todo_query, params)
        return Page.create(
            [TodoSchema.from_orm(todo) for todo in todos_page.items],
            params=params,
            total=todos_page.total,
        )

    async def get_by_id(self, schema_id: int):
        todo_query = select(Todo).where(Todo.id == schema_id)
        todo = await self.db_session.execute(todo_query)
        try:
            todo = todo.scalar_one()
            print('todo', vars(todo))
            return TodoSchema.from_orm(todo)
        except NoResultFound as ex:
            raise TodoNotFound(schema_id) from ex

    async def create(self, schema: PartialTodoSchema):
        todo_query = insert(Todo).values(**schema.dict())
        todo_id = await self.db_session.execute(todo_query)
        await self.db_session.commit()
        return await self.get_by_id(todo_id.inserted_primary_key[0])  # type: ignore

    async def update(self, schema_id: int, schema: PartialTodoSchema):
        todo_query = (
            update(Todo).where(Todo.id == schema_id).values(**schema.dict(exclude_unset=True))
        )
        todo = await self.db_session.execute(todo_query)
        await self.db_session.commit()
        if not self._check_rows(todo):
            raise TodoNotFound(schema_id)
        return await self.get_by_id(schema_id)

    async def delete(self, schema_id: int):
        todo_query = delete(Todo).where(Todo.id == schema_id)
        result = await self.db_session.execute(todo_query)
        if not self._check_rows(result):
            raise TodoNotFound(schema_id)
        await self.db_session.commit()
