import pytest
from packages.todo.exceptions import TodoNotFound
from packages.todo.repository import TodoRepository
from packages.todo.schemas import PartialTodoSchema


class TestTodoRepository:
    async def test_get_all(self, todo_repository: TodoRepository):
        todos = await todo_repository.get_all()
        assert todos.total == 0

        new_todo = PartialTodoSchema(title='test', description='test')
        await todo_repository.create(new_todo)
        todos = await todo_repository.get_all()
        assert todos.total == 1
        todo = todos.items[0]
        assert todo.title == new_todo.title
        assert todo.description == new_todo.description

    async def test_get_by_id(self, todo_repository: TodoRepository):
        new_todo = PartialTodoSchema(title='test', description='test')
        todo_created = await todo_repository.create(new_todo)
        todo = await todo_repository.get_by_id(todo_created.id)
        assert todo.title == new_todo.title
        assert todo.description == new_todo.description

    async def test_get_by_id_not_found(self, todo_repository: TodoRepository):
        with pytest.raises(TodoNotFound) as ex:
            await todo_repository.get_by_id(1)
        assert ex.value.code == 404
        assert ex.value.message == 'Todo with id 1 not found'

    async def test_create(self, todo_repository: TodoRepository):
        new_todo = PartialTodoSchema(title='test', description='test')
        todo_created = await todo_repository.create(new_todo)
        assert todo_created.id is not None
        assert todo_created.title == new_todo.title
        assert todo_created.description == new_todo.description

    async def test_update(self, todo_repository: TodoRepository):
        new_todo = PartialTodoSchema(title='test', description='test')
        todo_created = await todo_repository.create(new_todo)
        todo_updated = await todo_repository.update(
            todo_created.id, PartialTodoSchema(title='test2', description='test2')
        )
        assert todo_updated.title == 'test2'
        assert todo_updated.description == 'test2'

    async def test_update_not_found(self, todo_repository: TodoRepository):
        with pytest.raises(TodoNotFound) as ex:
            await todo_repository.update(1, PartialTodoSchema(title='test2', description='test2'))
        assert ex.value.code == 404
        assert ex.value.message == 'Todo with id 1 not found'

    async def test_delete(self, todo_repository: TodoRepository):
        new_todo = PartialTodoSchema(title='test', description='test')
        todo_created = await todo_repository.create(new_todo)
        await todo_repository.delete(todo_created.id)
        todos = await todo_repository.get_all()
        assert todos.total == 0

    async def test_delete_not_found(self, todo_repository: TodoRepository):
        with pytest.raises(TodoNotFound) as ex:
            await todo_repository.delete(1)
        assert ex.value.code == 404
        assert ex.value.message == 'Todo with id 1 not found'
