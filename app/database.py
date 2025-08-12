from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.settings import db_settings


engine = create_async_engine(
    f'postgresql+asyncpg://{db_settings.DB_USER}:{db_settings.DB_PASSWORD}@{db_settings.DB_HOST}/{db_settings.DB_NAME}',
    pool_size=10,
    max_overflow=15,
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
