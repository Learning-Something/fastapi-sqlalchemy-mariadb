import asyncio
import sys
import traceback

import pytest
import pytest_asyncio
from app import create_app
from asgi_lifespan import LifespanManager
from database.base_model import ORMBaseModel
from httpx import AsyncClient
from settings import DATABASE_URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture(scope="session")
def event_loop():
    """
    Creates an instance of the default event loop for the test session.
    """
    if sys.platform.startswith("win") and sys.version_info[:2] >= (3, 8):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def sqla_engine():
    engine = create_async_engine(DATABASE_URL)
    try:
        async with engine.begin() as conn:
            await conn.run_sync(ORMBaseModel.metadata.create_all)
            await conn.run_sync(ORMBaseModel.metadata.create_all)
        yield engine
    finally:
        await engine.dispose()


@pytest.fixture()
async def db_session(sqla_engine):  # pylint: disable=redefined-outer-name
    """
    Fixture that returns a SQLAlchemy session with a SAVEPOINT, and the rollback to it
    after the test completes.
    """
    connection = await sqla_engine.connect()
    trans = await connection.begin()

    Session = sessionmaker(connection, expire_on_commit=False, class_=AsyncSession)
    session = Session()

    try:
        yield session
    finally:
        await session.close()
        await trans.rollback()
        await connection.close()


@pytest.fixture()
async def transaction(_engine):
    conn = await _engine.begin()
    try:
        yield conn
    finally:
        await conn.rollback()


@pytest_asyncio.fixture(scope='function', autouse=True)
async def server():
    try:
        app = create_app()
        """Async server client that handles lifespan and teardown"""
        async with LifespanManager(app):
            yield app
    except Exception:
        traceback.print_exc()
    finally:
        # await clear_database(app)
        pass


@pytest_asyncio.fixture(scope='function')
async def client(server):  # pylint: disable=redefined-outer-name
    async with AsyncClient(app=server, base_url='http://test') as _client:
        yield _client
