from common.exceptions import CommonException
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
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

    @app.exception_handler(CommonException)
    async def common_exception_handler(request: Request, error: CommonException):
        return JSONResponse(error.to_dict(), status_code=error.code)
