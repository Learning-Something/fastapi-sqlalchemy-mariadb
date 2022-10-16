from fastapi import FastAPI
from packages.todo.controllers import TodoControler
from packages.todo.repository import TodoRepository
from packages.todo.services import TodoService


def init_routes(app: FastAPI):
    @app.get('/')
    async def health_check():
        return {'status': 'ok'}

    app.include_router(
        TodoControler(TodoService(repository=TodoRepository())).router,
        tags=['Todos'],
        prefix='/v1/todos',
    )
