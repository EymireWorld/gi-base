from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER


engine = create_async_engine(
    f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}',
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
