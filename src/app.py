from fastapi import FastAPI
from fastapi_pagination import add_pagination
from settings import APPLICATION_NAME, SERVERS


def create_app():
    app = FastAPI(title=APPLICATION_NAME, description='A simple todo list API', servers=SERVERS)

    # init_middlewares(app)
    # init_routes(app)
    add_pagination(app)

    return app
