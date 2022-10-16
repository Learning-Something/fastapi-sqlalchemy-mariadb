from database.models.todo import Todo
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import TodoSchema


class TodoRepository:
    db_session: AsyncSession

    def __check_rows(self, result):
        if result.rowcount == 0:
            raise ValueError("Todo not found")

    async def get_all(self, skip: int = 0, limit: int = 10):
        todo_query = select(Todo).offset(skip).limit(limit).order_by(Todo.created_at.desc())
        todos = await self.db_session.execute(todo_query)
        return [TodoSchema.from_orm(todo) for todo in todos.scalars().all()]

    async def get_by_id(self, todo_id: int):
        todo_query = select(Todo).where(Todo.id == todo_id)
        todo = await self.db_session.execute(todo_query)
        try:
            return TodoSchema.from_orm(todo.scalar_one())
        except NoResultFound as ex:
            raise ValueError("Todo not found") from ex

    async def create(self, todo_schema: TodoSchema):
        todo_query = insert(Todo).values(
            **todo_schema.dict(exclude={"id", "created_at", "updated_at"})
        )
        todo = await self.db_session.execute(todo_query)
        await self.db_session.commit()
        return TodoSchema.parse_obj(
            {
                **todo_schema.dict(),
                "id": todo.inserted_primary_key[0],  # type: ignore [attr-defined]
            }
        )

    async def update(self, todo_id: int, todo_schema: TodoSchema):
        todo_query = (
            update(Todo)
            .where(Todo.id == todo_id)
            .values(**todo_schema.dict(exclude={"id", "created_at", "updated_at"}))
        )
        todo = await self.db_session.execute(todo_query)
        await self.db_session.commit()
        if self.__check_rows(todo):
            raise ValueError("Todo not found")
        return await self.get_by_id(todo_id)

    async def delete(self, todo_id: int):
        todo_query = delete(Todo).where(Todo.id == todo_id)
        result = await self.db_session.execute(todo_query)
        if self.__check_rows(result):
            raise ValueError("Todo not found")
        await self.db_session.commit()
