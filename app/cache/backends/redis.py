from contextlib import suppress

from redis import asyncio as aioredis
from redis.exceptions import RedisError

from app.cache.types import Backend


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
