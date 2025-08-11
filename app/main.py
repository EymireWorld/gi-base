from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.staticfiles import StaticFiles
from redis import asyncio as aioredis

from app.cache import CacheStorage
from app.cache.backends import RedisBackend
from app.settings import redis_settings

from .api.router import router as api_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    redis = aioredis.Redis(
        host=redis_settings.REDIS_HOST,
        port=redis_settings.REDIS_PORT,
    )
    CacheStorage.init(RedisBackend(redis))
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title='gi-base',
        redoc_url=None,
        default_response_class=ORJSONResponse,
        lifespan=lifespan,
        swagger_ui_parameters={'defaultModelsExpandDepth': -1},
    )
    app.mount(
        '/static',
        StaticFiles(directory='static'),
        'static',
    )
    app.include_router(api_router)

    return app
