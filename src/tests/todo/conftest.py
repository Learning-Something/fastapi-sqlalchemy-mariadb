import pytest
from packages.todo.repository import TodoRepository
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture(scope='function')
async def todo_repository(db_session: AsyncSession):
    _todo_repository = TodoRepository()
    _todo_repository.db_session = db_session
    return _todo_repository
