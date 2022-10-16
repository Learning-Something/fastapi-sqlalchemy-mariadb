from database.models.todo import Todo
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import TodoSchema


class TodoRepository:
    db_session: AsyncSession

    async def get_all(self, skip: int = 0, limit: int = 10):
        todo_query = select(Todo).offset(skip).limit(limit).order_by(Todo.created_at.desc())
        todos = await self.db_session.execute(todo_query)
        return [TodoSchema.from_orm(todo) for todo in todos.scalars().all()]

    async def get_by_id(self, todo_id: int):
        todo_query = select(Todo).where(Todo.id == todo_id)
        todo = await self.db_session.execute(todo_query)
        return TodoSchema.from_orm(todo.scalar_one())

    async def create(self, todo_schema: TodoSchema):
        todo_query = insert(Todo).values(
            **todo_schema.dict(exclude={"id", "created_at", "updated_at"})
        )
        todo = await self.db_session.execute(todo_query)
        await self.db_session.commit()
        return TodoSchema.from_orm(todo.scalar_one())

    async def update(self, todo_id: int, todo: TodoSchema):
        todo_query = (
            update(Todo)
            .where(Todo.id == todo_id)
            .values(**todo.dict(exclude={"id", "created_at", "updated_at"}))
        )
        todo = await self.db_session.execute(todo_query)
        await self.db_session.commit()
        return TodoSchema.from_orm(todo.scalar_one())

    async def delete(self, todo_id: int):
        todo_query = delete(Todo).where(Todo.id == todo_id)
        await self.db_session.execute(todo_query)
        await self.db_session.commit()
