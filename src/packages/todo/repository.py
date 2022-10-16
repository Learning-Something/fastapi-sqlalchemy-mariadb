from database.models.todo import Todo
from interfaces.repository import RepositoryInterface
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import NoResultFound

from .schemas import TodoSchema


class TodoRepository(RepositoryInterface[TodoSchema]):
    async def get_all(self, skip: int = 0, limit: int = 10):
        todo_query = select(Todo).offset(skip).limit(limit).order_by(Todo.created_at.desc())
        todos = await self.db_session.execute(todo_query)
        return [TodoSchema.from_orm(todo) for todo in todos.scalars().all()]

    async def get_by_id(self, schema_id: int):
        todo_query = select(Todo).where(Todo.id == schema_id)
        todo = await self.db_session.execute(todo_query)
        try:
            return TodoSchema.from_orm(todo.scalar_one())
        except NoResultFound as ex:
            raise ValueError("Todo not found") from ex

    async def create(self, schema: TodoSchema):
        todo_query = insert(Todo).values(**schema.dict(exclude={"id", "created_at", "updated_at"}))
        todo = await self.db_session.execute(todo_query)
        await self.db_session.commit()
        return TodoSchema.parse_obj(
            {
                **schema.dict(),
                "id": todo.inserted_primary_key[0],  # type: ignore [attr-defined]
            }
        )

    async def update(self, schema_id: int, schema: TodoSchema):
        todo_query = (
            update(Todo)
            .where(Todo.id == schema_id)
            .values(**schema.dict(exclude={"id", "created_at", "updated_at"}))
        )
        todo = await self.db_session.execute(todo_query)
        await self.db_session.commit()
        if self._check_rows(todo):
            raise ValueError("Todo not found")
        return await self.get_by_id(schema_id)

    async def delete(self, schema_id: int):
        todo_query = delete(Todo).where(Todo.id == schema_id)
        result = await self.db_session.execute(todo_query)
        if self._check_rows(result):
            raise ValueError("Todo not found")
        await self.db_session.commit()
