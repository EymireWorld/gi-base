from redis import asyncio as aioredis
from redis.exceptions import RedisError

from app.cache.types import Backend


class RedisBackend(Backend):
    def __init__(self, client: aioredis.Redis):
        self.client = client

    async def get(self, key: str) -> bytes | None:
        try:
            result = await self.client.get(key)
        except RedisError:
            return None
        return result

    async def set(self, key: str, value: bytes, expire: int) -> bool:
        try:
            await self.client.set(key, value, ex=expire)
        except RedisError:
            return False
        return True

    async def clear(self, key: str) -> bool:
        try:
            await self.client.delete(key)
        except RedisError:
            return False
        return True
