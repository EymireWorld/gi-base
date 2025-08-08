import abc
import hashlib
import pickle
from collections.abc import Callable
from contextlib import suppress
from functools import wraps
from inspect import iscoroutinefunction
from typing import Any

from fastapi.concurrency import run_in_threadpool
from redis import asyncio as aioredis
from redis.exceptions import RedisError

from app.settings import REDIS_HOST, REDIS_PORT


class Backend(abc.ABC):
    @abc.abstractmethod
    async def get(self, key: str) -> bytes | None: ...

    @abc.abstractmethod
    async def set(self, key: str, value: bytes, expire: int) -> None: ...

    @abc.abstractmethod
    async def clear(self, key: str) -> None: ...


class RedisBackend(Backend):
    def __init__(self, client: aioredis.Redis):
        self.client = client

    async def get(self, key: str) -> bytes | None:
        with suppress(RedisError):
            return await self.client.get(key)

    async def set(self, key: str, value: bytes, expire: int) -> None:
        with suppress(RedisError):
            await self.client.set(key, value, ex=expire)

    async def clear(self, key: str) -> None:
        with suppress(RedisError):
            await self.client.delete(key)


def key_builder(
    func: Callable[..., Any],
    namespace: str = '',
    *,
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
):
    cache_key = hashlib.md5(
        f'{func.__module__}:{func.__name__}:{args}:{kwargs}'.encode()
    ).hexdigest()

    return f'{namespace}:{cache_key}'


class CacheStorage:
    def __init__(self, backend: Backend, prefix: str = 'fastapi-cache') -> None:
        self.backend = backend
        self.prefix = prefix

    def cache(
        self,
        expire: int = 120,
        namespace: str = '',
        ignore_kwargs: list[str] | None = None,
    ):
        def wrapper(func):
            @wraps(func)
            async def inner(*args, **kwargs):
                async def run_func(*args, **kwargs):
                    if iscoroutinefunction(func):
                        return await func(*args, **kwargs)
                    else:
                        return await run_in_threadpool(func, *args, **kwargs)

                kwargs_copy = kwargs.copy()

                if ignore_kwargs:
                    for kwarg in ignore_kwargs:
                        kwargs_copy.pop(kwarg)

                cache_key = key_builder(
                    func,
                    f'{self.prefix}:{namespace}',
                    args=args,
                    kwargs=kwargs_copy,
                )

                cached = await self.backend.get(cache_key)

                if cached is None:
                    result = await run_func(*args, **kwargs)

                    await self.backend.set(cache_key, pickle.dumps(result), expire)
                else:
                    result = pickle.loads(cached)

                return result

            return inner

        return wrapper


redis = aioredis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
)
cache_storage = CacheStorage(RedisBackend(redis))
