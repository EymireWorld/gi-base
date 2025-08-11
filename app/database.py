from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.settings import database_settings


engine = create_async_engine(
    f'postgresql+asyncpg://{database_settings.DB_USER}:{database_settings.DB_PASSWORD}@{database_settings.DB_HOST}/{database_settings.DB_NAME}'
)
session_factory = async_sessionmaker(
    engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


async def get_session():
    async with session_factory() as session:
        yield session
