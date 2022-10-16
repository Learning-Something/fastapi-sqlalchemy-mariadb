from database import start_db
from fastapi import FastAPI
from rest import init_routes
from settings import APPLICATION_NAME, SERVERS


def create_app():
    app = FastAPI(title=APPLICATION_NAME, description='A simple todo list API', servers=SERVERS)

    # init_middlewares(app)
    init_routes(app)

    @app.on_event('startup')
    async def startup():
        await start_db()

    return app
