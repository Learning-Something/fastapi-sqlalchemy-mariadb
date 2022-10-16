from fastapi import FastAPI


def init_routes(app: FastAPI):
    @app.get('/')
    async def health_check():
        return {'status': 'ok'}
