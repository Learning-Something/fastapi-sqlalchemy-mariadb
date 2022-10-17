from datetime import datetime

import pytest
from fastapi_pagination import Page
from httpx import AsyncClient
from packages.todo.exceptions import TodoNotFound
from packages.todo.schemas import TodoSchema
from pytest_mock import MockerFixture


class TestTodoControllers:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = '/v1/todos'
        self.todo = TodoSchema(
            id=1,
            title='title',
            description='description',
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

    async def test_get_todos(self, client: AsyncClient, mocker: MockerFixture):
        todo_page_zero = Page(items=[], total=0, page=1, size=1)
        mocker.patch(
            'packages.todo.repository.TodoRepository.get_all'
        ).return_value = todo_page_zero
        response = await client.get(f'{self.url}/')
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['items'] == []
        assert response_json['total'] == 0
        assert response_json['page'] == 1
        assert response_json['size'] == 1

        todo_page_one = Page(items=[self.todo], total=1, page=1, size=1)
        mocker.patch('packages.todo.repository.TodoRepository.get_all').return_value = todo_page_one
        response = await client.get(f'{self.url}/')
        assert response.status_code == 200
        response_json = response.json()
        assert [TodoSchema.parse_obj(todo).dict() for todo in response_json['items']] == [
            self.todo.dict()
        ]
        assert response_json['total'] == 1
        assert response_json['page'] == 1
        assert response_json['size'] == 1

    async def test_get_twenty_todos(self, client: AsyncClient, mocker: MockerFixture):
        todo_twenty = [
            TodoSchema(
                id=i + 1,
                title=f'title {i+1}',
                description=f'description {i+1}',
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            for i in range(20)
        ]
        todo_page_twenty = Page(items=todo_twenty[:10], total=20, page=1, size=2)
        mocker.patch(
            'packages.todo.repository.TodoRepository.get_all'
        ).return_value = todo_page_twenty
        response = await client.get(f'{self.url}/')
        assert response.status_code == 200
        response_json = response.json()
        assert [TodoSchema.parse_obj(todo).dict() for todo in response_json['items']] == [
            todo.dict() for todo in todo_page_twenty.items
        ]
        assert response_json['total'] == 20
        assert response_json['page'] == 1
        assert response_json['size'] == 2

        todo_page_twenty = Page(items=todo_twenty[10:], total=20, page=2, size=2)
        mocker.patch(
            'packages.todo.repository.TodoRepository.get_all'
        ).return_value = todo_page_twenty
        response = await client.get(f'{self.url}/', params={'page': 2})
        assert response.status_code == 200
        response_json = response.json()
        assert [TodoSchema.parse_obj(todo).dict() for todo in response_json['items']] == [
            todo.dict() for todo in todo_page_twenty.items
        ]
        assert response_json['total'] == 20
        assert response_json['page'] == 2
        assert response_json['size'] == 2

    async def test_get_todo_by_id(self, client: AsyncClient, mocker: MockerFixture):
        mocker.patch('packages.todo.repository.TodoRepository.get_by_id').return_value = self.todo
        response = await client.get(f'{self.url}/{self.todo.id}/')
        response_json = response.json()
        assert response.status_code == 200
        assert TodoSchema.parse_obj(response_json).dict() == self.todo.dict()

    async def test_get_todo_not_found(self, client: AsyncClient, mocker: MockerFixture):
        mocker.patch(
            'packages.todo.repository.TodoRepository.get_by_id'
        ).side_effect = TodoNotFound(self.todo.id)
        response = await client.get(f'{self.url}/{self.todo.id}/')
        assert response.status_code == 404
        response_json = response.json()
        assert response_json['message'] == f'Todo with id {self.todo.id} not found'

    async def test_create_todo(self, client: AsyncClient, mocker: MockerFixture):
        mocker.patch('packages.todo.repository.TodoRepository.create').return_value = self.todo
        response = await client.post(
            f'{self.url}/', json=self.todo.dict(exclude={'id', 'created_at', 'updated_at'})
        )
        assert response.status_code == 201
        response_json = response.json()
        assert TodoSchema.parse_obj(response_json).dict() == self.todo.dict()

    async def test_update_todo(self, client: AsyncClient, mocker: MockerFixture):
        self.todo.title = 'new title'
        mocker.patch('packages.todo.repository.TodoRepository.update').return_value = self.todo
        response = await client.put(f'{self.url}/{self.todo.id}/', json={'title': 'new title'})
        assert response.status_code == 200
        response_json = response.json()
        assert TodoSchema.parse_obj(response_json).dict() == self.todo.dict()

    async def test_update_todo_not_found(self, client: AsyncClient, mocker: MockerFixture):
        mocker.patch('packages.todo.repository.TodoRepository.update').side_effect = TodoNotFound(
            self.todo.id
        )
        response = await client.put(f'{self.url}/{self.todo.id}/', json={'title': 'new title'})
        assert response.status_code == 404
        response_json = response.json()
        assert response_json['message'] == f'Todo with id {self.todo.id} not found'

    async def test_delete_todo(self, client: AsyncClient, mocker: MockerFixture):
        mocker.patch('packages.todo.repository.TodoRepository.delete').return_value = None
        response = await client.delete(f'{self.url}/{self.todo.id}/')
        assert response.status_code == 204

    async def test_delete_todo_not_found(self, client: AsyncClient, mocker: MockerFixture):
        mocker.patch('packages.todo.repository.TodoRepository.delete').side_effect = TodoNotFound(
            self.todo.id
        )
        response = await client.delete(f'{self.url}/{self.todo.id}/')
        assert response.status_code == 404
        response_json = response.json()
        assert response_json['message'] == f'Todo with id {self.todo.id} not found'
