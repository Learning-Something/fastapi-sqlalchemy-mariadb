from collections.abc import Generator

from common.enums import EnvironmentSet
from database.base_model import ORMBaseModel
from settings import DATABASE_URL, ENVIRONMENT
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session, create_async_engine
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(DATABASE_URL, pool_pre_ping=False, pool_recycle=3600, echo_pool=False)
async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


async def start_db():
    if ENVIRONMENT == EnvironmentSet.DEVELOPMENT:
        async with engine.begin() as conn:
            await conn.run_sync(ORMBaseModel.metadata.create_all)
            await conn.run_sync(ORMBaseModel.metadata.create_all)


async def session_db():
    session: AsyncSession
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception as exc:
            await session.rollback()
            raise exc
        finally:
            await session.close()
